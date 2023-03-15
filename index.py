import gym
from gym.utils.env_checker import check_env
from gym.utils.play import play
from gym.envs.toy_text.frozen_lake import generate_random_map

import pygame

mapped_keys = {
    (pygame.K_LEFT,): 0,
    (pygame.K_DOWN,): 1,
    (pygame.K_RIGHT,): 2,
    (pygame.K_UP,): 3,
}

play(
    gym.make(
        "FrozenLake-v1",
        render_mode="rgb_array",
        desc=generate_random_map(size=8)
    ),
    keys_to_action=mapped_keys
)

# env = gym.make("LunarLander-v2", render_mode="human")
# env.action_space.seed(42)
# check_env(env)
# observation, info = env.reset(seed=42)

# for _ in range(1000):
#     observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

#     if terminated or truncated:
#         observation, info = env.reset()

# env.close()

