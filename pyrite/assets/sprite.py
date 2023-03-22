import pygame

class Sprite:
    def __init__(self, image, size, scale, colorkey ="1"):
        self.sprite = image
        self.width = size[0]
        self.height = size[1]
        self.size = size
        self.scale = scale
        self.colorkey = colorkey
        if not colorkey == "1":
            self.colorkey = colorkey
        

    def cut(self, frame, layer, custom_size=None):
        """cuts the given sprite and returns requested frame"""
        
        if custom_size:
            width = custom_size[0]
            height = custom_size[1]
        else:
            width = self.width
            height = self.height
        
        image = pygame.Surface((width, height))
        image.blit(self.sprite, (0, 0), ((frame * width), (self.height * layer), width, height))
        image = pygame.transform.scale((image), self.scale)
        
        if not self.colorkey == "1":
            image.set_colorkey(self.colorkey)
        
        return image