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
        
    def glide(self):
        if self.animation_loader.animation == 'fall' and self.keys['glide']:
            if self.velocity.y > 5:
                self.velocity.y -= (self.velocity.y - 5) / 2
            
    def character_update(self):
        self.glide()
            