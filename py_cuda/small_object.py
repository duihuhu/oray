#import cudf
import ray
import time
ray.init()
@ray.remote
def worker(): 
    return 1

ref = worker.remote()
print(ray.get(ref))