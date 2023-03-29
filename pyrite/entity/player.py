import pygame

from .entity import Entity, PhysicalEntity
from ..assets.json_loader import JsonLoader
from ..assets.rect_cutter import cut_rect

class Player(PhysicalEntity):
    def __init__(self, pos, player_data):
        """
        pos = player spawn
        size = player size
        type = None ?Playable or moved
        image_info = None ?img_path, is_animated bool
        """
        self.player_data = player_data
        
        self.character_name = self.player_data['name']
        self.size = self.player_data['size']
        self.movement_data = self.player_data['movement']
        self.assets_path = self.player_data['assets_path']
        player_sprite = self.assets_path + self.player_data['animations']['main']
        animation_rules_path = self.assets_path + self.player_data['animations']['animation-rules']
        animated = self.player_data['animated']
        frame_resolution = self.player_data['animations']['frame_resolution']
         
        super().__init__(pos, self.size, self.movement_data)
        
        self.load_images(player_sprite, animation_rules_path, {'player_size': self.size, 'frame_size': frame_resolution}, animated)
        self.type = type
            
        self.animation = 'run'
        self.animation_loader.set_animation(self.animation)
        self.animation_loader.update(self)
        self.rect = self.image.get_rect()
        context_rect = cut_rect(self.image)
        
    def update(self, keys, dt, tile_list):
        self.calc_movement(self, keys, dt, tile_list)
        self.animation_loader.update(self)
    

def load_player_data(path):
    json_loader = JsonLoader()
    properties = json_loader.read_path(path)        
    return properties