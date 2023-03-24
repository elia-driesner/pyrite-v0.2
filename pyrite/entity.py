import pygame
from pyrite.assets.sprite import Sprite
from pyrite.assets.animation_loader import Animation
from pyrite.collision import * 
import time

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
            self.jump_height = movement['jump_heigth'] *-1
            self.gravity, self.friction = movement['gravity'], movement['friction']
            self.position, self.velocity = pygame.math.Vector2(self.x, self.y), pygame.math.Vector2(0, 0)
            self.acceleration = pygame.math.Vector2(0, self.gravity)
            self.on_ground = False                      
            self.is_falling = False
            self.is_jumping = False
            self.double_jump = True
            self.last_jump = time.time()
    
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
        
    def jump(self):
        """checks if player is able to jump and sets the velocity"""
        print('jump')
        if self.on_ground:
            self.last_jump = time.time()
            self.double_jump = True
            self.is_jumping = True
            self.is_falling = False
            self.velocity.y -= 17
            self.rect.y = self.y
            self.on_ground = False
        elif self.double_jump and self.on_ground == False and time.time() - self.last_jump > 0.3:
            self.double_jump = False
            self.is_jumping = True
            self.is_falling = False
            self.velocity.y -= 17
            self.on_ground = False
        if self.velocity.y <= -32.5:
            self.velocity.y = -32
        
    def calc_movement(self, ent, keys, dt, tile_list):
        movement_x = 0
        movement_y = 0
        
        self.position.x = self.x
        self.position.y = self.y
        
        # x movement
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
        movement_x = self.position.x - self.x

        # y movement
        # print(keys)
        if keys['jump']:
            self.jump()
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 16: self.velocity.y = 16
        if self.on_ground:                          
            self.is_falling = False
            self.is_jumping = False
            self.velocity.y = 0
        else:
            self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        if self.y - self.position.y < 0:
            self.is_falling = True
            self.is_jumping = False
        movement_y = self.position.y - self.y

        move(self, movement_x, movement_y, tile_list)
        self.update_rect()
    
        
        