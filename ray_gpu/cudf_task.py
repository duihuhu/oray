import time
t1=time.time()
import cudf
t2=time.time()
#url = "https://github.com/plotly/datasets/raw/master/tips.csv"
#content = requests.get(url).content.decode('utf-8')
tips_df = cudf.read_csv("tips.csv")
tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
t4 = time.time()
result = tips_df.groupby('size').tip_percentage.mean()
t3=time.time()
print(t2-t1, t3-t2, t3-t1, t3-t4)
