import numpy as np
import os
pre_name = 'log'
for i in [1,2,4,8,16]:
  time_list = []
  for j in range(1,6):
    start_time = 1884927212
    end_time = -1
    filename = "data/"+pre_name+"_"+str(i)+"_"+str(j)+".txt"
    if(os.path.exists(filename)):
      with open(filename, 'r') as fd:
        for line in fd.readlines():
          if 'time:' in line:
            content = line.split(" ")
            if start_time > float(content[-7]):
              start_time = float(content[-7])
            if end_time < float(content[-4]):
              end_time = float(content[-4])
      time_list.append(end_time-start_time)
    # print(end_time, start_time, end_time-start_time)
  print(i, (i*3000*1144000)/(np.median(time_list)*1024*1024))

