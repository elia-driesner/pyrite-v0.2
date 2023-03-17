import pygame

class Camera:
    def __init__(self, game, config):
        self.game = game
        self.scroll = [0 ,0]
        self.scroll_smoothing = config['scroll-smoothing']
        
    def calc_scroll(self):
        
        self.scroll = [0, 0]
