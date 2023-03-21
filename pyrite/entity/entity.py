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
        
    def load_animation(self):
        self.animation_loader = Animation()
        self.animation_loader.get_animation()
    
    def load_images(self, path, image_size, sprite_rows, spite_cols):
        """Gets images from sprite and saves them in a array"""
        self.images = [] 
        self.sprite = Sprite(pygame.image.load(str(path)), image_size, (self.width, self.height))
        for i in range(0, sprite_rows):
            row = []
            for j in range(0, spite_cols):
                row.append(self.sprite.cut(j, i))
            self.images.append(row)
        self.image = self.images[0][0]
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()