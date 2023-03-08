import ray
import time
import os
import numpy as np
import time
ray.init(address='auto', _node_ip_address='192.172.200.2')

#@ray.remote
#def circle():
#    return np.zeros(1000000)

@ray.remote
def dircle():
    return np.zeros(100000)

head_id = ray.get_runtime_context().node_id.hex()
# print(ray.state.node_ids())
remote_node_id = ""
nodes = ray.nodes()
for node in nodes:
    n_id = node['NodeID']
    if n_id != head_id:
        remote_node_id = n_id

#print(remote_node_id)
# node_id = 'b0ef226853852bde98e2c1874425e0a361dace6a5fa180e19841eee4'
remote_node_bytes = bytes.fromhex(remote_node_id)
# # print(node_bytes)
# futures = 1
#c = circle.options(
#    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
#        #node_id = ray.get_runtime_context().node_id,
#        node_id = remote_node_bytes,
#        soft = False
#    )
#).remote()

#time.sleep(1000000)

d = dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote()

time.sleep(10)
t1 = time.time()
e = ray.get(d)
t2=time.time()
print(t2-t1)
print(e)
#print(ray.get(c))
#t3=time.time()
#print(ray.get(d))
#t4=time.time()
#print(t4-t3)
#print(c.__sizeof__())

