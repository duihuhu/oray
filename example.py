import ray
import time
import os
ray.init()

@ray.remote
def circle(x):
    return x*x
node_id = 'f2c09c50dae154540c47d9c78d6f38b7a6c2f1af003676e3fa140c77'
node_bytes = bytes.fromhex(node_id)
print(node_bytes)
futures = 1
c = circle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = node_bytes,
        soft = False
    )
).remote(futures)

print(ray.get(c))