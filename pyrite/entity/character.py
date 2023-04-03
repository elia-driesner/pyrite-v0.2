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
        
class Donald(Player):
    def __init__(self, player_data, pos):
        super().__init__(pos, player_data)
        
class Carter(Player):
    def __init__(self, player_data, pos):
        super().__init__(pos, player_data)