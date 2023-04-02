import pygame

class PaletteSwap:
    def __init__(self):
        pass

    def swap(self, image, original_color, new_color):
        image_size = image.get_size()
        print(image_size)