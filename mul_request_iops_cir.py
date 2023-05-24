# import ray
import time
import os
import numpy as np
import time
import multiprocessing
import ray
import sys
ray.init(address='auto', _node_ip_address='192.172.200.2')

#@ray.remote
#def circle():
#    return np.zeros(1000000)
task_parallel = 1000
process_parallel = sys.argv[1]
s_time = 30
if sys.argv[1] == 16:
  s_time = 60
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
head_node_bytes = bytes.fromhex(head_id)

@ray.remote
def dircle():
    return np.zeros(14300*10)

@ray.remote
def worker(reference):
  with open("record.txt", "a+") as fd:
      fd.write("1")
  while 1:
    with open("record.txt", 'r') as fd:
        content = fd.read()
        if len(content) == process_parallel:
          break
  t1 = time.time()
  for ref in reference:
    e = ray.get(ref)
  t2 = time.time()
  print("time: " , t1, " ", t2, " ", t2-t1,)
  return 1

referenc_list = []
for j in range(0, process_parallel):
  reference = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
  ).remote() for i in range(task_parallel) ]
  referenc_list.append(reference)

# time.sleep(60)

for ref in referenc_list:
  result = worker.options(
  scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
      #node_id = ray.get_runtime_context().node_id,
      node_id = head_node_bytes,
      soft = False
  )).remote(ref)

time.sleep(s_time)

