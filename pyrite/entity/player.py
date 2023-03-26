import pygame

from .entity import Entity, PhysicalEntity

class Player(PhysicalEntity):
    def __init__(self, pos, size, movement, image_info, type):
        """
        pos = player spawn
        size = player size
        type = None ?Playable or moved
        image_info = None ?img_path, is_animated bool
        """
        super().__init__(pos, size, movement)
        
        self.load_images(image_info[0], image_info[1], (self.width, self.height), image_info[2])
        self.type = type
            
        self.animation = 'idle'
        self.animation_loader.set_animation(self.animation)
        self.animation_loader.update(self)
        self.rect = self.image.get_rect()
        
    def update(self, keys, dt, tile_list):
        self.calc_movement(self, keys, dt, tile_list)
        self.animation_loader.update(self)
    

def load_player_data(path):
    pass
        