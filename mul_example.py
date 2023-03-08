# import ray
import time
import os
import numpy as np
import time
import multiprocessing
# ray.init(address='auto', _node_ip_address='192.172.200.2')

#@ray.remote
#def circle():
#    return np.zeros(1000000)


def worker(barrier):
  import ray
  ray.init(address='auto', _node_ip_address='192.172.200.2')

  @ray.remote
  def dircle():
    return np.zeros(100000)


  # print("a")
  # ray.init(address='auto', _node_ip_address='192.172.200.2')
  head_id = ray.get_runtime_context().node_id.hex()
  # print("head_id", head_id)
  # print(ray.state.node_ids())
  remote_node_id = ""
  nodes = ray.nodes()
  for node in nodes:
      n_id = node['NodeID']
      if n_id != head_id:
          remote_node_id = n_id

  remote_node_bytes = bytes.fromhex(remote_node_id)
  # print("c")
  d = dircle.options(
      scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
          #node_id = ray.get_runtime_context().node_id,
          node_id = remote_node_bytes,
          soft = False
      )
  ).remote()
  barrier.wait()
  time.sleep(10)
  # with lock:
  # print(multiprocessing.current_process().name + " " +str(time.time()))

  # time.sleep(10)
  t1 = time.time()
  e = ray.get(d)
  t2=time.time()
  print("time: " , t1, " ", t2, " ", t2-t1)
  print(e)
      
if __name__ == "__main__":
  process_parallel = 10
  barrier = multiprocessing.Barrier(process_parallel)
  # lock = multiprocessing.Lock()
  pslist = [multiprocessing.Process(target=worker,args=(barrier,)) for i in range(process_parallel) ]
  for ps in pslist:
    ps.start()
    ps.join(timeout=3)

