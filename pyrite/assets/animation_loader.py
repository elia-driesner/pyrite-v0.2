import pygame
from .json_loader import JsonLoader
from .sprite import Sprite

class Animation:
    def __init__(self):
        self.aniamtion_frame = 0
        self.animation = 'idle'
        self.frames = {}


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
                "custom_length": rules[animation]["custom_length"],
                "size": rules[animation]["size"]
            }
        
        
        image_size = image.get_size()
        image_cols = image_size[0] // sprite_size[0]
        image_rows = image_size[1] // sprite_size[1]
        
        frames = {
            "unnamed_frames": []
        }
        frame = None
        y = 0
        
        for row in range(0, image_rows):
            temp_row = []
            x = 0
            for col in range(0, image_cols):
                frame = sprite.cut(col, row)
                frame_mask = pygame.mask.from_surface(frame)
                frame_pixels = frame_mask.count()
                if frame_pixels != 0:
                    if row in animation_rules:
                        width, heigth = animation_rules[row]['size'][0], animation_rules[row]['size'][1]
                        print(x, y)
                        image = pygame.Surface((width, heigth))
                        image.blit(image, (0, 0), ((x * width), (heigth * y), width, heigth))
                        frame = image
                        temp_row.append({'frame':frame, 'frame_length': animation_rules[row]['frame_duration']})
                    x += width
            y += heigth
            if len(temp_row) != 0:
                if row in animation_rules:
                    custom_length = animation_rules[row]["custom_length"]
                    if len(custom_length) != 0:
                        for custom_rule in custom_length:
                            if temp_row[custom_rule[0]]:
                                temp_row[custom_rule[0]]['frame_length'] = custom_rule[1]
                
                        
                    frames[animation_rules[row]["name"]] = temp_row
                else:
                    frames["unnamed_frames"].append(temp_row)
        print(frames)
        self.frames = frames
    
    def update(self, animation, player):
        self.animation = animation
        self.player = player
        
        total_frames = 0
        frame_steps = {}
        
        frame_list = self.frames[animation]
        
        for frame in frame_list:
            total_frames += frame['frame_length']
            frame_steps[total_frames] = frame
        
        for frame in reversed(frame_steps):
            if self.aniamtion_frame <= frame :
                self.player.image = frame_steps[frame]['frame']
                
                
        if self.aniamtion_frame > total_frames:
                self.aniamtion_frame = 0
        self.aniamtion_frame += 1
