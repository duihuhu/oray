import pycuda.autoinit
import pycuda.driver as cuda
for i in range(10):
    d_A = cuda.mem_alloc(100)
    print(d_A, " " , id(d_A), " ", int(d_A))