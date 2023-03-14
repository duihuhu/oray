# import ray
import time
import os
import numpy as np
import time
import multiprocessing
import ray
ray.init(address='auto', _node_ip_address='192.172.200.2')
if os.path.exists("record.txt"):
  os.remove("record.txt")
#@ray.remote
#def circle():
#    return np.zeros(1000000)
task_parallel = 1000
process_parallel = 4
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
  print("worker time: " , t1, " ", t2, " ", t2-t1,)
  print(e)
  return e




reference1 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference2 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference3 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference4 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference5 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference6 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference7 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference8 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]


'''
reference9 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference10 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference11 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference12 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference13 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference14 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference15 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]

reference16 = [ dircle.options(
    scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
        #node_id = ray.get_runtime_context().node_id,
        node_id = remote_node_bytes,
        soft = False
    )
).remote() for i in range(task_parallel) ]
'''
time.sleep(150)

# for ref in reference:
result1 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference1)


# for ref in reference:
result2 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference2)

# for ref in reference:
result3 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference3)

result4 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference4)

# for ref in reference:
result5 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference5)

# for ref in reference:
result6 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference6)

# for ref in reference:
result7 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference7)

result8 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference8)

'''
# for ref in reference:
result9 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference9)

# for ref in reference:
result10 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference10)

# for ref in reference:
result11 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference11)

result12 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference12)

# for ref in reference:
result13 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference13)

# for ref in reference:
result14 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference14)

# for ref in reference:
result15 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference15)

result16 = worker.options(
scheduling_strategy=ray.util.scheduling_strategies.NodeAffinitySchedulingStrategy(
    #node_id = ray.get_runtime_context().node_id,
    node_id = head_node_bytes,
    soft = False
)).remote(reference16)
'''
time.sleep(300)
# print(ray.get(result1))
# print(ray.get(result2))
# print(ray.get(result3))
