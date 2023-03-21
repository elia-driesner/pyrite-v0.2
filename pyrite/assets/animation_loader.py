import pygame
from .sprite import Sprite

class Animation:
    def __init__(self):
        pass

    def get_animation(self, img_path, sprite_size):
        image = pygame.image.load(img_path)
        sprite = Sprite(image, sprite_size, sprite_size, (0, 0, 0))
        
        image_size = image.get_size()
        image_cols = image_size[0] // sprite_size[0]
        image_rows = image_size[1] // sprite_size[1]
        
        frames = []
        
        frame = None
        for row in range(0, image_rows):
            temp_row = []
            for col in range(0, image_cols):
                frame = sprite.cut(col, row)
                frame_mask = pygame.mask.from_surface(frame)
                frame_pixels = frame_mask.count()
                if frame_pixels != 0:
                    temp_row.append(frame)
            if len(temp_row) != 0:
                frames.append(temp_row)
        print(frames)