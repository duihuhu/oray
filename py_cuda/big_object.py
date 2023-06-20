import ray
import time
import numpy as np
ray.init()
@ray.remote
def worker(): 
    return np.zeros(1024000)

ref = worker.remote()
print(ray.get(ref))