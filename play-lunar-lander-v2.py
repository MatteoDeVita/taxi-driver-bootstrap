import gym
from gym.utils.env_checker import check_env
from gym.utils.play import play
import pygame

mapped_keys = {
    (pygame.K_RIGHT,): 1,
    (pygame.K_DOWN,): 2,
    (pygame.K_LEFT,): 3,
}

play(
    gym.make("LunarLander-v2", render_mode="rgb_array"),
    keys_to_action=mapped_keys
)