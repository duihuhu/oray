import cudf
import ray
import time
ray.init()

@ray.remote(num_gpus=1)
class Counter:
    def __init__(self):
        import cudf
        import time
    def worker(self, filename):
        t0 = time.time()
        tips_df = cudf.read_csv(filename)
        tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
        t1 = time.time()
        print("read: ", t1-t0)
        return tips_df

    def worker1(self, ref):
        tips_df = ray.get(ref)
        # tips_df_data =  tips_df[0]
        res = tips_df[0].groupby('size').tip_percentage.mean()
        # t3 = time.time()
        # print("t3: ", t3)
        return res

# Create an actor from this class.
counter = Counter.remote()
# t_start = time.time()
# print("start: ", t_start)
ref = counter.worker.remote("/home/hucc/cuda/cudf/tips.csv")
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
# t4 = time.time()
# print("t4:", t4)
print(res)


t0 = time.time()
# print("start: ", t_start)
ref = counter.worker.remote("/home/hucc/cuda/cudf/tips.csv")
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t1 = time.time()
print("t1:", t1-t0)
print(res)

t0 = time.time()
# print("start: ", t_start)
ref = counter.worker.remote("/home/hucc/cuda/cudf/tips.csv")
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t1 = time.time()
print("t1:", t1-t0)
print(res)

t0 = time.time()
# print("start: ", t_start)
ref = counter.worker.remote("/home/hucc/cuda/cudf/tips.csv")
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t1 = time.time()
print("t1:", t1-t0)
print(res)

t0 = time.time()
# print("start: ", t_start)
ref = counter.worker.remote("/home/hucc/cuda/cudf/tips.csv")
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t1 = time.time()
print("t1:", t1-t0)
print(res)

t0 = time.time()
# print("start: ", t_start)
ref = counter.worker.remote("/home/hucc/cuda/cudf/tips.csv")
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t1 = time.time()
print("t1:", t1-t0)
print(res)

t0 = time.time()
# print("start: ", t_start)
ref = counter.worker.remote("/home/hucc/cuda/cudf/tips.csv")
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t1 = time.time()
print("t1:", t1-t0)
print(res)