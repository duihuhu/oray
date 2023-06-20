#import cudf
import ray
import time
ray.init()
@ray.remote
def worker(): 
    return np.zeros(1024000)

ref = worker.remote()
print(ray.get(ref))