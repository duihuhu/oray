import numpy as np
arr = []
with open("log.txt", 'r') as fd:
  for line in fd.readlines():
    if "circle pid=" in line:
      content = line.split(" ")
      arr.append(float(content[-1]))

print(np.median(arr))