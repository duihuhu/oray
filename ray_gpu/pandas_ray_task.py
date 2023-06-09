#import cudf
import ray
import time
ray.init()
@ray.remote
def worker(): 
    t1 = time.time()
    import pandas  
    t2 = time.time()
    tips_df = pandas.read_csv("/home/hucc/cuda/cudf/tips.csv")
    tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
    t3=time.time()
    print("cudf: " ,t3-t2, t2-t1, t3)
    return tips_df


@ray.remote
def worker1(ref):
    import pandas
    tips_df = ray.get(ref)
    tips_df_data = tips_df[0]
    t1=time.time()
    print("worker1 t1: ", t1)
    res = tips_df_data.groupby('size').tip_percentage.mean()
    t2=time.time()
    print("groupby: ", t2-t1, t2)
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
