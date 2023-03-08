import ray
import time
import os
import numpy as np
import time
import multiprocessing
# ray.init(address='auto', _node_ip_address='192.172.200.2')

#@ray.remote
#def circle():
#    return np.zeros(1000000)

# @ray.remote
# def dircle():
#     return np.zeros(100000)

def worker(barrier, lock):
  # head_id = ray.get_runtime_context().node_id.hex()
  # # print(ray.state.node_ids())
  # remote_node_id = ""
  # nodes = ray.nodes()
  # for node in nodes:
  #     n_id = node['NodeID']
  #     if n_id != head_id:
  #         remote_node_id = n_id

  # remote_node_bytes = bytes.fromhex(remote_node_id)


  # d = dircle.options(
  #     scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
  #         #node_id = ray.get_runtime_context().node_id,
  #         node_id = remote_node_bytes,
  #         soft = False
  #     )
  # ).remote()
  barrier.wait()
  with lock():
      print(multiprocessing.current_process().name+str(time.time()))

  # time.sleep(10)
  # t1 = time.time()
  # e = ray.get(d)
  # t2=time.time()
  # print(t2-t1)
  # print(e)
      
if __name__ == "__main__":
    barrier = multiprocessing.Barrier(2)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=worker, args=(barrier, lock))
    p2 = multiprocessing.Process(target=worker, args=(barrier, lock))
    p1.start()
    p2.start()