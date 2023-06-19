import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy as np
import ray
import time
ray.init()
@ray.remote(num_gpus=0.5)
def worker():
  import pycuda.driver as cuda
  import pycuda.autoinit
  from pycuda.compiler import SourceModule
  a = np.random.randn(4,4)
  a = a.astype(np.float32)

  a_gpu = cuda.mem_alloc(a.nbytes)

  cuda.memcpy_htod(a_gpu, a)

  mod = SourceModule("""
  __global__ void doublify(float *a)
  {
  int idx = threadIdx.x + threadIdx.y*4;
  a[idx] *= 2;
  }
  """)

  func = mod.get_function("doublify")
  func(a_gpu, block=(4,4,1))

  a_doubled = np.empty_like(a)
  cuda.memcpy_dtoh(a_doubled, a_gpu)
  print(a_doubled)
  print(a)
  return a
  
ref = worker.remote()
print(ray.get(ref))
