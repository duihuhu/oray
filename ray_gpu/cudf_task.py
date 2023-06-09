import time
import cudf
t1=time.time()
tips_df = cudf.read_csv("/home/hucc/cuda/cudf/tips.csv").groupby('size').tip_percentage.mean()
# tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
# result = tips_df.groupby('size').tip_percentage.mean()
t2=time.time()
print(t2-t1)