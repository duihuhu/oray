import time
#url = "https://github.com/plotly/datasets/raw/master/tips.csv"
#content = requests.get(url).content.decode('utf-8')
t1=time.time()
import pandas as pd

t2=time.time()
tips_df = pd.read_csv("/home/hucc/cuda/cudf/tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
t4=time.time()
result = tips_df.groupby('size').tip_percentage.mean()
t3=time.time()
print(t2-t1,t3-t2, t3-t4)
