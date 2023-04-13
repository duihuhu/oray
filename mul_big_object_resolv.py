import ray
import time
import os
import numpy as np
import time
import multiprocessing
ray.init(address='auto', _node_ip_address='192.172.200.2')
ref_number = 2
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
def square():
  # time.sleep(10)
  return np.zeros(1024000)

@ray.remote
def circle(reference):
  time.sleep(2)
  for ref in reference:
    t1 = time.time()
    e = ray.get(ref)
    t2 = time.time()
    print("time", t2-t1)
    print(e)
  return np.zeros(100)

# d_ref = square.options(
#     scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
#         #node_id = ray.get_runtime_context().node_id,
#         node_id = head_node_bytes,
#         soft = False
#     )
# ).remote()


reference = [ square.options(
  scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
      #node_id = ray.get_runtime_context().node_id,
      node_id = head_node_bytes,
      soft = False
  )
).remote() for i in range(ref_number) ]


c_ref = circle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote([reference])

print(ray.get(c_ref))
