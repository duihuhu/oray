#import cudf
import ray
import time
ray.init()
@ray.remote(num_gpus=0.5)
def worker():
    import cudf
    import time
    tips_df = cudf.read_csv("/home/hucc/cuda/cudf/tips.csv")
    tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
    print(type(tips_df))
    return tips_df

ref = worker.remote()
print(ray.get(ref))