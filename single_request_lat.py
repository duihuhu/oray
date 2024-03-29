# import ray
import time
import os
import numpy as np
import time
import multiprocessing
import ray
ray.init(address='auto', _node_ip_address='192.172.200.2')
#@ray.remote
#def circle():
#    return np.zeros(1000000)
task_parallel = 1000
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
    return np.zeros(14300)

reference = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

time.sleep(60)

t1 = time.time()
for ref in reference:
    ray.get(ref)
t2 = time.time()
print("time: " , t1, " ", t2, " ", t2-t1)

