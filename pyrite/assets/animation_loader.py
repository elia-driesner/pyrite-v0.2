import pygame
from ..assets.sprite import Sprite

class Animation:
    def __init__(self):
        pass

    def get_animation(self, img_path, sprite_size):
        image = pygame.load_image(img_path)
        sprite = Sprite(image, sprite_size, sprite_size, (0, 0, 0))