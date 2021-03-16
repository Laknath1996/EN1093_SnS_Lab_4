from gym.envs.registration import register

register(
    id='CartPoleAcc-v0',
    entry_point='gym_sns.envs:CartPoleAccEnv',
)
