import gym
from jacks_or_better_env import JacksOrBetterEnvironment

env = JacksOrBetterEnvironment()

obs = env.reset()
env.render()
i = 0
while i < 10:
    print("#"*30, "\nStep:", i)
    env.render()
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    env.render()

    if done:
        obs = env.reset()

    i += 1

env.close()