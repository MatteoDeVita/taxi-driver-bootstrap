import gym
from gym.utils.play import play
import pygame

mapped_keys = {
    (pygame.K_DOWN,): 0,
    (pygame.K_UP,): 1,
    (pygame.K_RIGHT,): 2,
    (pygame.K_LEFT,): 3,
    (pygame.K_SPACE,): 4,
    (pygame.K_LCTRL,): 5,
}

play(
    gym.make("Taxi-v3", render_mode="rgb_array"),
    keys_to_action=mapped_keys
)