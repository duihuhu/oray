from ray.rllib.algorithms.ddppo import DDPPOConfig
config = DDPPOConfig().training(lr=0.003, keep_local_weights_in_sync=True)
#config = config.resources(num_gpus=0.5)
config = config.resources(num_gpus_per_worker=0.5)
config = config.rollouts(num_rollout_workers=2)
print(config.to_dict())
# Build a Algorithm object from the config and run 1 training iteration.
algo = config.build(env="CartPole-v1")
algo.train()
