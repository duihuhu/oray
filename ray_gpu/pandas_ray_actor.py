import pandas
import ray
import time
ray.init()

@ray.remote(num_gpus=1)
class Counter:
    def __init__(self):
        import cudf
        
    def worker(self):
        t0 = time.time()
        tips_df = pandas.read_csv("/home/hucc/cuda/cudf/tips.csv")
        tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
        t1 = time.time()
        print("read: ", t1-t0)
        return tips_df

    def worker1(self, ref):
        # t1 = time.time()
        # print("t1: ", t1)
        tips_df = ray.get(ref)
        # t2 = time.time()
        # print("t2: ", t2)
        # tips_df_data =  tips_df[0]
        res = tips_df[0].groupby('size').tip_percentage.mean()
        # t3 = time.time()
        # print("t3: ", t3)
        return res

# Create an actor from this class.
counter = Counter.remote()
# t_start = time.time()
# print("start: ", t_start)
ref = counter.worker.remote()
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
# t4 = time.time()
# print("t4:", t4)
print(res)

# print("aaaa")
t_start = time.time()
# print("start: ", t_start)
ref = counter.worker.remote()
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t4 = time.time()
print("total: ", t4-t_start)
print(res)

# print("aaaa")
t_start = time.time()
# print("start: ", t_start)
ref = counter.worker.remote()
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t4 = time.time()
print("total: ", t4-t_start)
print(res)


# print("aaaa")
t_start = time.time()
# print("start: ", t_start)
ref = counter.worker.remote()
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t4 = time.time()
print("total: ", t4-t_start)
print(res)


# print("aaaa")
t_start = time.time()
# print("start: ", t_start)
ref = counter.worker.remote()
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t4 = time.time()
print("total: ", t4-t_start)
print(res)


# print("aaaa")
t_start = time.time()
# print("start: ", t_start)
ref = counter.worker.remote()
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t4 = time.time()
print("total: ", t4-t_start)
print(res)

