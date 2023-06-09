import cudf
import ray
import time
ray.init()

@ray.remote(num_gpus=1)
class Counter:
    def __init__(self):
        import cudf
        
    def worker(self):
        t3 = time.time()
        print("t3: ", t3)
        tips_df = cudf.read_csv("/home/hucc/cuda/cudf/tips.csv")
        tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
        return tips_df

    def worker1(self, ref):
        tips_df = ray.get(ref)
        tips_df_data =  tips_df[0]
        return tips_df[0].groupby('size').tip_percentage.mean()

# Create an actor from this class.
counter = Counter.remote()
t1 = time.time()
ref = counter.worker.remote()
ref1 = counter.worker1.remote([ref])
res = ray.get(ref1)
t2 = time.time()
print("total:", t2-t1)
print(res)