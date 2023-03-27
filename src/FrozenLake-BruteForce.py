import gym
from gym.envs.toy_text.frozen_lake import generate_random_map
import numpy as np
import random
from IPython.display import clear_output
import time
import itertools
import numpy as np


# 0: LEFT
# 1: DOWN
# 2: RIGHT
# 3: UP

MAP_SIZE = 4

def create_frozen_lake_env(map_name, is_slippery=False):
    return gym.make(
        "FrozenLake-v1",
        desc=[
            "SFFF",
            "HHFH",
            "FFFF",
            "FHFG",
        ],
        # desc=generate_random_map(size=MAP_SIZE),
        map_name=map_name,
        is_slippery=is_slippery,
        render_mode="ansi"
    )


def reset_history():
    history = np.empty((MAP_SIZE, MAP_SIZE), dtype=object)
    for i in np.ndindex(history.shape): history[i] = []
    return history

def get_next_pos(current_pos, action):
    return [
        (current_pos[0] - 1, current_pos[1]),
        (current_pos[0], current_pos[1] + 1),
        (current_pos[0] + 1, current_pos[1]),
        (current_pos[0], current_pos[1] - 1),
    ][action]

def is_out_of_map(pos):
    return pos[0] < 0 or pos[0] >= MAP_SIZE or pos[1] < 0 or pos[1] >= MAP_SIZE

def display(env, sleep_time=1, clear=True):
    print(env.render())
    time.sleep(sleep_time)
    if clear: clear_output(wait=True)

def get_backward_action(current_pos, wanted_pos):
    if current_pos[0] == wanted_pos[0] + 1 and current_pos[1] == wanted_pos[1]:
        return 0
    elif current_pos[0] == wanted_pos[0] and current_pos[1] == wanted_pos[1] - 1:
        return 1
    elif current_pos[0] == wanted_pos[0] - 1 and current_pos[1] == wanted_pos[1]:
        return 2
    return 3

def generate_action_list(action_range, size):
    action_list = [0] * size
    while True:
        yield np.asarray(tuple(action_list))
        index = size - 1
        while index >= 0:
            if action_list[index] < action_range[1]:
                action_list[index] += 1
                break
            else:
                action_list[index] = action_range[0]
                index -= 1
        if index < 0:
            break

action_list = generate_action_list((0, 2), 16)

env = create_frozen_lake_env("brute_force")
n_episode = 0
for action in action_list:
    n_episode += 1
    done = False     
    state = env.reset()[0]

    for step in action:
        state, reward, done, trucaded, info = env.step(step)
        if done == True:
            if reward == 0:
                continue
            elif reward == 1:
                print(f"Solution found : {action} in {n_episode} episodes\n")
                exit(0)
        # clear_output(wait=True)
        # print(env.render())
        # time.sleep(0.25)
# action_list = generate_action_list((0, 2), 8)
# print(action_list)