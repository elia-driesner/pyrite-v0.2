import pygame
import math
from pyrite.assets.rect_cutter import *
from pyrite.assets.json_loader import *

class Weapon:
    def __init__(self, name, image, config, ent):
        self.name = name
        self.image = image
        self.config = config
        self.carrier = ent
        pos = (self.carrier.rect.x, self.carrier.rect.y)
        
        self.angle = 0
        self.display_img = self.image
        self.rect = cut_rect(self.image)
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.mouse_pos = [0, 0]
        
    def draw(self, wn, scroll):
        wn.blit(self.display_img, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
            
    def update(self, mouse_pos, ent, scroll):
        self.mouse_pos = mouse_pos
        self.carrier = ent
        self.rect.x = self.carrier.rect.center[0]
        self.rect.y = self.carrier.rect.y - self.carrier.rect.h / 2
        self.calc_angle(scroll)
    
    def calc_angle(self, scroll):
        self.mouse_pos = pygame.Vector2(self.mouse_pos)
        self.p_screen_pos = pygame.Vector2((self.carrier.rect.x - scroll[0], self.carrier.rect.y - scroll[1]))
        
        angle = math.atan2(self.mouse_pos[1] - self.carrier.rect.y, self.mouse_pos[0] - self.carrier.rect.x)
        self.display_img = pygame.transform.rotate(self.image, angle)

class Shotgun(Weapon):
    def __init__(self, ent, path):
        self.path = path
        self.config = read_path(path + '/config.json')
        self.name = self.config['name']
        self.image = pygame.image.load(path + '/' + self.config['image_path'])
        
        super().__init__(self.name, self.image, self.config, ent)