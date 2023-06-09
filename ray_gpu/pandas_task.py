import time
#url = "https://github.com/plotly/datasets/raw/master/tips.csv"
#content = requests.get(url).content.decode('utf-8')
import pandas as pd
t1=time.time()
tips_df = pd.read_csv("/home/hucc/cuda/cudf/tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
result = tips_df.groupby('size').tip_percentage.mean()
t2=time.time()
print(t2-t1)


t1=time.time()
tips_df = pd.read_csv("/home/hucc/cuda/cudf/tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
result = tips_df.groupby('size').tip_percentage.mean()
t2=time.time()
print(t2-t1)

t1=time.time()
tips_df = pd.read_csv("/home/hucc/cuda/cudf/tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
result = tips_df.groupby('size').tip_percentage.mean()
t2=time.time()
print(t2-t1)

t1=time.time()
tips_df = pd.read_csv("/home/hucc/cuda/cudf/tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
result = tips_df.groupby('size').tip_percentage.mean()
t2=time.time()
print(t2-t1)

t1=time.time()
tips_df = pd.read_csv("/home/hucc/cuda/cudf/tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
result = tips_df.groupby('size').tip_percentage.mean()
t2=time.time()
print(t2-t1)

t1=time.time()
tips_df = pd.read_csv("/home/hucc/cuda/cudf/tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
result = tips_df.groupby('size').tip_percentage.mean()
t2=time.time()
print(t2-t1)
