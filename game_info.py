import gym
from gym.envs.toy_text.frozen_lake import generate_random_map
import numpy as np

MAP_SIZE = 8

env = gym.make(
    "FrozenLake-v1",
    desc=generate_random_map(size=MAP_SIZE),
    # render_mode="human"
)
reward = 0
while reward < 1:
    actions = np.random.randint(4, size=100)

    initial_state = env.reset()
    print(initial_state)
    for action in actions:
        state, reward, done, truncated, info = env.step(action)
        print(state)
        print(reward)
        print(done)
        print(truncated)
        print(info)
        print("-----------")
        if done:
            break;
print(f"Game states = int representing current_row * nrow + current_col")
print(f"Game actions = 0: Move left, 1: Move down, 2: Move right, 3: Move up")
print(f"Game rewards = Reach goal: +1, Reach hole: 0, Reach frozen: 0")
