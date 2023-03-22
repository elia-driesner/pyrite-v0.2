import pygame

from .entity import Entity

class Player(Entity):
    def __init__(self, pos, size, type=None, image_info=None):
        """
        pos = player spawn
        size = player size
        type = None ?Playable or moved
        image_info = None ?img_path, is_animated bool
        """
        super().__init__(pos, size)
        
        if image_info:
            self.load_images(image_info[0], image_info[1], (self.width, self.height), image_info[2])
            
        self.animation = 'run'
        self.animation_loader.set_animation(self.animation)
        self.animation_loader.append_animation('data/assets/player/player_wide.png', (32, 32), 20, 'wide_run')
        
    def update(self):
        self.animation_loader.update(self)