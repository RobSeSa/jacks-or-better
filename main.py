import gym
from jacks_or_better_env import JacksOrBetterEnvironment
from numpy import random

env = JacksOrBetterEnvironment()

i = 0
while i < 10:
    print("#"*30, "\nStep:", i)
    env.reset()
    env.render()
    
    action = random.randint(52)
    env.step(action)
    env.render()

    i += 1