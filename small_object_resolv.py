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
  print(ref)
  return np.zeros(1000)

d_ref = square.remote()

c_ref = circle(d_ref)

print(c_ref)
