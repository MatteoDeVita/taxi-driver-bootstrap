import gym
from gym.utils.env_checker import check_env
from gym.utils.play import play
from gym.envs.toy_text.frozen_lake import generate_random_map
import numpy as np
import pygame
import time

mapped_keys = {
    (pygame.K_LEFT,): 0,
    (pygame.K_DOWN,): 1,
    (pygame.K_RIGHT,): 2,
    (pygame.K_UP,): 3,
}

# gym.make() returns a class gymnasium.Env, this is the main Gym class for implementing Reinforcement Learning Agents env
# The class encapsulates an environment with arbitrary behind-the-scenes dynamics through the step() and reset() functions
# An env can be partially or fully observed by single agents.
# The main API methods are :
# - step() - Updates an env with actions returning the next agent observation :
#   - the reward for taking that actions.
#   - if the env has terminaded or truncated due to the last actions
#   - informations from the env about the step : metrics, debug info
# - reset() - Reset the env to the initial state : REQUIRED BEFORE CALLING STEP().
# Returns the first agent observation for an episode and information : metrics, debug info
# - render() - Renders the env to help visualize what the agent see, examples modes are :
# "human", "rgb_array", "ansi" (for text)
# - close() : Close env. important when external software is used : pygame, databases etc...
#
# Env hade additional attributes for users to understand the implementation :
# - action_space : The Space object corresponding to valid actions, all valid actions should be contained within the space
# - observation_space : The space object corresponding to valid observations, all valid observations should be contained within the space
# - reward_range : Tuple correspoonding to min and max possible rewards for an agent on an episode. Default range [-inf, +inf]
# - spec : env spec containing info used to initialze the env from gymnasium.make()
# - metadata : medatadata of the env : render modes, render fps, etc...
# - np_random : The random nb generator for the env. Automatically assigned during super().reset(seed=seed) i.e when calling env.reset() and
# when assessing self.np_random


def get_random_actions(n):
    return np.random.randint(4, size=n) # Generate an array of 16 elements with int between 0 and 3 included

# Run the episode and return the reward
def run_episode(env, actions, render=False):
    reward = 0
    # 1 - Reset env before running episode and getting the initial state
    initial_state = env.reset()
    # 2 - Rendering the env to see what is happening if render == True
    if render == True: env.render()
    # 3 - Actually playing the game with the given actions
    for i in range(len(actions)):
        state, reward, done, truncated, info = env.step(actions[i])
        if done or i >= len(actions):
            break
    # 4 - Return the reward
    return reward


# Create the env
env = gym.make(
    'FrozenLake-v1',
    desc=generate_random_map(size=8),
    # render_mode="human"
)
reward = 0
n_game = 0
start = time.time()
while reward < 1:
    random_actions = get_random_actions(100) #Pre generate random actions, the length of a frozen lake episode for 4*4 map is 100, 200 for 8*8 map
    reward = run_episode(env, random_actions)
    n_game = n_game + 1
end = time.time()
env.close()
print(f"Sucess in {n_game} episodes. Time taken = {end - start} seconds")


