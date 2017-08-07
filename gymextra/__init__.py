from gym.envs.registration import register

register(
    id='MountainCarContinuousExtra-v2',
    entry_point='gymextra.envs.classic_control:ContinuousMountainCarEnv',
    max_episode_steps=999,
    reward_threshold=90.0
)
