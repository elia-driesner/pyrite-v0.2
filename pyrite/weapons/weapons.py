import pygame
from ..assets.rect_cutter import *

class Weapon:
    def __init__(self, name, image, config, pos):
        self.name = name
        self.image = image
        self.config = config
        
        self.angle = 0
        self.rect = cut_rect(self.image)
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.mouse_pos = [0, 0]
        
    def update(self, mouse_pos, player, scroll):
        self.mouse_pos = mouse_pos
        self.player = player
    
    def calc_angle(self, scroll):
        self.mouse_pos = pygame.Vector2(self.mouse_pos)
        self.p_screen_pos = pygame.Vector2((self.player.rect.x - scroll[0], self.player.rect.y - scroll[1]))
        
        angle = self.p_screen_pos.angle_to(self.mouse_pos)
        print(angle)