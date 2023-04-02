import pygame

class PaletteSwap:
    def __init__(self):
        pass

    def swap(self, input_image, colors):
        image = input_image
        image_size = image.get_size()
        img_mask = pygame.mask.from_surface(image)
        temp_surf = pygame.Surface(image_size)
        
        temp_surf.blit(img_mask.to_surface(setcolor=(colors[1]), unsetcolor=[0, 0, 0]), (0, 0))
        image.set_colorkey(colors[0])
        temp_surf.blit(image, (0, 0))
        
        temp_surf.set_colorkey((0, 0, 0))
        return temp_surf