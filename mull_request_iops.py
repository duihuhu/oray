# import ray
import time
import os
import numpy as np
import time
import multiprocessing
import ray
ray.init(address='auto', _node_ip_address='192.172.200.2')
global n = 0
#@ray.remote
#def circle():
#    return np.zeros(1000000)
process_parallel = 1
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
    return np.zeros(100000)

@ray.remote
def worker(reference):
  n = n + 1 
  print(n)
  # t1 = time.time()
  # for ref in reference:
  #   e = ray.get(ref)
  # t2 = time.time()
  # print("time: " , t1, " ", t2, " ", t2-t1)
  # print(e)



reference1 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(process_parallel) ]


reference2 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(process_parallel) ]

reference3 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(process_parallel) ]

time.sleep(30)

# for ref in reference:
worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote([reference1])

# for ref in reference:
worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote([reference2])

# for ref in reference:
worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote([reference3])

time.sleep(5)

