import ray
import time
import os
import numpy as np
import time
import multiprocessing
ray.init(address='auto')

@ray.remote
def square():
  time.sleep(10)
  return np.zeros(100)

@ray.remote()
def circle(ref):
  printf("ccccc")
  printf(ref)
  return np.zeros(1000)

d_ref = square.remote()

c_ref = circle(d_ref)

printf(c_ref)
