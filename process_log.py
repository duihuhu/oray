import numpy as np
pre_name = 'log'
for i in [1,2,4,8,16]:
  start_time = 10000
  end_time = -1
  time_list = []
  for j in range(1,6):
    filename = "data/"+pre_name+"_"+str(i)+"_"+str(j)+".txt"
    with open(filename, 'r') as fd:
      for line in fd.readlines():
        if 'time:' in line:
          content = line.split(" ")
          start_time = content[-3]
          end_time = content[-2]
          print(content)
          if start_time > float(content[-3]):
            start_time = float(content[-3])
          if end_time < float(content[-2]):
            end_time = float(content[-2])
    time_list.append(end_time-start_time)
  print(i, j, np.median(time_list), time_list)

