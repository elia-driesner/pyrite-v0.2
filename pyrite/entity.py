import pygame
from pyrite.assets.sprite import Sprite
from pyrite.assets.animation_loader import Animation

class Entity:
    def __init__(self, pos, size, movement=None):
        pygame.init()
        self.x, self.y = pos[0], pos[1]
        self.width, self.height = size[0], size[1]
        
        self.image = None
        self.rect = None
        self.mask = None
        
        self.direction = 'right'
        
        if movement:
            self.speed = movement['speed']
            self.gravity, self.friction = movement['gravity'], movement['friction']
            self.position, self.velocity = pygame.math.Vector2(self.x, self.y), pygame.math.Vector2(0, 0)
            self.acceleration = pygame.math.Vector2(0, self.gravity)
    
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
    
    def limit_velocity(self, max_vel):
        """limits the velocity of the player"""
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0
        
    def move(self, ent, keys, dt):
        self.acceleration.x = 0
        if keys['move_left']:
            ent.animation = 'run'
            self.direction = 'left'
            self.acceleration.x -= self.speed
        elif keys['move_right']:
            ent.animation = 'run'
            self.direction = 'right'
            self.acceleration.x += self.speed
            
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(7)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.x = self.position.x
        self.update_rect()
        
        