#import cudf
import ray
import time
ray.init()
@ray.remote(num_gpus=0.5)
def worker():
    import cudf
    import time
    t1 = time.time()
    tips_df = cudf.read_csv("/home/hucc/cuda/cudf/tips.csv")
    tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
    t2 = time.time()
    print(t2, t2-t1)
    print(type(tips_df))
    return tips_df

@ray.remote(num_gpus=0.5)
def worker1(ref):
    import cudf
    import time
    tips_df = ray.get(ref)
    tips_df_data =  tips_df[0]
    t1 = time.time()
    res = tips_df_data.groupby('size').tip_percentage.mean()
    t2 = time.time()
    print("groupby", t2-t1)
    print("t2:", t2)
    return tips_df[0].groupby('size').tip_percentage.mean()
t1=time.time()
ref = worker.remote()
print(ref)
ref1 = worker1.remote([ref])
ray.get(ref1)
t2=time.time()
print("total time", t2-t1, t2, t1)
#t5=time.time()
#print(t5)
time.sleep(10)
