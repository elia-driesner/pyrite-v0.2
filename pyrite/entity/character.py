import pygame 

from .player import *

def assign_character(name, pos):
    char = None
    basic_path = 'data/assets/player/'
    file_name = '/properties.json'
    combined_path = basic_path + name.lower() + file_name
    if name == 'LightMcSpeed':
        char = LightMcSpeed(load_player_data(combined_path), pos)
    elif name == 'Donald':
        char = LightMcSpeed(load_player_data(combined_path), pos)
    elif name == 'Carter':
        char = Carter(load_player_data(combined_path), pos)
    
    return char
        
class LightMcSpeed(Player):
    def __init__(self, player_data, pos):
        super().__init__(pos, player_data)
    
    def character_update(self):
        pass
        
class Donald(Player):
    def __init__(self, player_data, pos):
        super().__init__(pos, player_data)
    
    def character_update(self):
        pass
        
class Carter(Player):
    def __init__(self, player_data, pos):
        super().__init__(pos, player_data)
        self.is_flying = False
        
    def glide(self):
        if self.animation_loader.animation == 'fall' and self.keys['glide']:
            if self.velocity.y > 5:
                self.velocity.y -= (self.velocity.y - 5) / 2
            
    def fly(self):
        if self.keys['ability_1']:
            self.is_flying = True
            
        if self.is_flying:
            self.custom_movement = True
            self.custom_animation = True
            self.animation_loader.set_animation('fly')
            self.acceleration.x = 0
            self.acceleration.y = 0
            if self.keys['move_left']:
                self.direction = 'left'
                self.acceleration.x -= self.speed
            elif self.keys['move_right']:
                self.direction = 'right'
                self.acceleration.x += self.speed
            if self.keys['move_up']:
                self.direction = 'up'
                self.acceleration.y -= self.speed
            elif self.keys['move_down']:
                self.direction = 'down'
                self.acceleration.y += self.speed
            
    def character_update(self):
        self.glide()
        self.fly()
            