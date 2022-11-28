import ray
import time
import os
import numpy as np
ray.init()

@ray.remote
def circle():
    return np.zeros(10000)

head_id = ray.get_runtime_context().node_id.hex()

# print(ray.state.node_ids())
remote_node_id = ""
nodes = ray.nodes()
for node in nodes:
    n_id = node['NodeID']
    if n_id != head_id:
        remote_node_id = n_id


# node_id = 'b0ef226853852bde98e2c1874425e0a361dace6a5fa180e19841eee4'
remote_node_bytes = bytes.fromhex(remote_node_id)
# # print(node_bytes)
# futures = 1
c = circle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote()

print(ray.get(c))

print(c.__sizeof__())

