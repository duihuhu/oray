import ray
import time
import os
import numpy as np
import time
import multiprocessing
ray.init(address='auto', _node_ip_address='192.172.200.2')

@ray.remote
def square():
  time.sleep(10)
  return np.zeros(100)

@ray.remote
def circle(ref):
  print("ccccc")
  print(ray.get(ref))
  return np.zeros(100)

d_ref = square.remote()

c_ref = circle.remote([d_ref])

print(ray.get(c_ref))
