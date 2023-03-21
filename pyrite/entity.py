import pygame
from pyrite.assets.sprite import Sprite
from pyrite.assets.animation_loader import Animation

class Entity:
    def __init__(self, pos, size):
        pygame.init()
        self.x, self.y = pos[0], pos[1]
        self.width, self.height = size[0], size[1]
        
        self.image = None
        self.rect = None
        self.mask = None
    
    def update_rect(self):
        self.rect.x, self.rect.y = self.x, self.y
    
    def update_position(self):
        self.x, self.y = self.rect.x, self.rect.y
        
    def draw(self, wn, scroll):
        """draws the entity on screen"""
        wn.blit(self.image, (self.x - scroll[0], self.y - scroll[1]))
        
    def load_animation(self, path, rules_path, image_size):
        self.animation_loader = Animation()
        self.animation_loader.get_animation(path, rules_path, image_size)
    
    def load_images(self, path, rules_path, image_size, animated=False):
        """Gets images from sprite and saves them in a array"""
        self.images = [] 
        if animated:
            self.load_animation(path=path, rules_path=rules_path, image_size=image_size)
        else:
            self.image = pygame.transform.scale(pygame.image.load(path), image_size)
            self.image.set_colorkey((0,0,0))
            self.rect = self.image.get_rect()
        