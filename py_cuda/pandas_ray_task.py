#import cudf
import ray
import time
ray.init()
@ray.remote
def worker(): 
    import pandas  
    tips_df = pandas.read_csv("/home/hucc/cuda/cudf/tips.csv")
    tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
    print(type(tips_df))
    return tips_df, tips_df['tip_percentage']


ref = worker.remote()
print(ray.get(ref))