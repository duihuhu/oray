import ray
import numpy as np
from collections import defaultdict
import wikipedia
from collections import Counter

ray.init()
        # include_webui=False,
        # ignore_reinit_error=True

class Stream(object):
    def __init__(self, elements):
        self.elements = elements

    def next(self):
        i = np.random.randint(0, len(self.elements))
        return self.elements[i]
        
@ray.remote
class Mapper(object):
    def __init__(self, title_stream):
        self.title_stream = title_stream
        self.num_articles_processed = 0
        self.articles = []
        self.word_counts = []

    def get_new_article(self):
        # 获取文章内容
        article = wikipedia.page(self.title_stream.next()).content
        # 分词&统计词频
        self.word_counts.append(Counter(re.split(r" |\n", article)))
        print(self.word_counts)
        self.num_articles_processed += 1

    def get_range(self, article_index, keys):
        # Process more articles if this Mapper hasn't processed enough yet.
        while self.num_articles_processed < article_index + 1:
            self.get_new_article()
        # Return the word counts from within a given character range.
        return [(k, v) for k, v in self.word_counts[article_index].items()
                if len(k) >= 1 and k[0] >= keys[0] and k[0] <= keys[1]]

@ray.remote
class Reducer(object):
    def __init__(self, keys, *mappers):
        self.mappers = mappers
        self.keys = keys

    def next_reduce_result(self, article_index):
        word_count_sum = defaultdict(lambda: 0)

        # 调用mapper的get_range方法获取结果
        # (注意ray的远程函数需要通过remote来调用和传参)
        count_ids = [mapper.get_range.remote(article_index, self.keys)
                     for mapper in self.mappers]

        # TODO(rkn): We should process these out of order using ray.wait.
        for count_id in count_ids:
            for k, v in ray.get(count_id):
                word_count_sum[k] += v
        return word_count_sum


# Create 3 streams
kw_list = ["SenseTime", "AI", "MapReduce"]
streams = [Stream(kw_list) for _ in range(3)]

# Partition the keys among the reducers.
chunks = np.array_split([chr(i) for i in range(ord("a"), ord("z") + 1)], 4)
keys = [[chunk[0], chunk[-1]] for chunk in chunks]

# Create a number of mappers.
mappers = [Mapper.remote(stream) for stream in streams]

# Create a number of reduces, each responsible for a different range of
# keys. This gives each Reducer actor a handle to each Mapper actor.
reducers = [Reducer.remote(key, *mappers) for key in keys]

# Map & Reduce
for article_index in range(10):
    print("article index = {}".format(article_index))
    wordcounts = {}
    counts = ray.get([reducer.next_reduce_result.remote(article_index)
                      for reducer in reducers])
    for count in counts:
        wordcounts.update(count)
        
    # get most 10 frequent words
    most_frequent_words = heapq.nlargest(10, wordcounts,
                                         key=wordcounts.get)
    for word in most_frequent_words:
        print("  ", word, wordcounts[word])