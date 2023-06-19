import pycuda.autoinit
import pycuda.driver as cuda
print(pycuda.driver.mem_get_info())
for i in range(10):
    d_A = cuda.mem_alloc(100)
    print(pycuda.driver.mem_get_ipc_handle(d_A))
    print (int(d_A))