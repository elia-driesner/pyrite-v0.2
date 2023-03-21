import pygame
from .json_loader import JsonLoader
from .sprite import Sprite

class Animation:
    def __init__(self):
        pass

    def get_animation(self, img_path, rules_path, sprite_size):
        """loads the animation from spritesheet and saves infos given in json file with the frames"""
        image = pygame.image.load(img_path)
        sprite = Sprite(image, sprite_size, sprite_size, (0, 0, 0))
        
        json_loader = JsonLoader()
        rules = json_loader.read_path(rules_path)
        animation_rules = {}
        
        for animation in rules:
            animation_rules[rules[animation]["row"]] = {
                "name": animation,
                "frame_duration": rules[animation]["frame_duration"],
                "custom_length": rules[animation]["custom_length"]
            }
        
        
        image_size = image.get_size()
        image_cols = image_size[0] // sprite_size[0]
        image_rows = image_size[1] // sprite_size[1]
        
        frames = []
        frame = None
        custon_length = None
        
        for row in range(0, image_rows):
            temp_row = []
            for col in range(0, image_cols):
                frame = sprite.cut(col, row)
                frame_mask = pygame.mask.from_surface(frame)
                frame_pixels = frame_mask.count()
                if frame_pixels != 0:
                    if row in animation_rules:
                        temp_row.append({'frame':frame, 'frame_length': animation_rules[row]['frame_duration']})
                    else:
                        temp_row.append({'frame':frame, 'frame_length': 5})
            if len(temp_row) != 0:
                if row in animation_rules:
                    custom_length = animation_rules[row]["custom_length"]
                    if len(custom_length) != 0:
                        for custom_rule in custom_length:
                            if temp_row[custom_rule[0]]:
                                temp_row[custom_rule[0]]['frame_length'] = custom_rule[1]
                
                        
                    frames.append({"animations": temp_row, "settings": animation_rules[row]})
                else:
                    frames.append({"animations": temp_row, "settings": {}})
        print(frames)