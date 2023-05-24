import numpy as np
pre_name = 'log'
for i in [1,2,4,8,16]:
  start_time = 1884927212
  end_time = -1
  time_list = []
  for j in range(1,6):
    filename = "data/"+pre_name+"_"+str(i)+"_"+str(j)+".txt"
    with open(filename, 'r') as fd:
      for line in fd.readlines():
        if 'time:' in line:
          content = line.split(" ")
          if start_time > float(content[-7]):
            start_time = float(content[-7])
          if end_time < float(content[-4]):
            end_time = float(content[-4])
    time_list.append(end_time-start_time)
    print(end_time, start_time, end_time-start_time)
  # print(i, np.median(time_list))

