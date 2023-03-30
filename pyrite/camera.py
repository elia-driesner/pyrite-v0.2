import pygame

class Camera:
    def __init__(self, game, config):
        self.game = game
        self.scroll = [0 ,0]
        self.scroll_smoothing = config['scroll-smoothing']
        self.focus = None
        
    def calc_scroll(self):
        self.scroll[0] += int((self.focus.rect.x  - self.scroll[0] - (self.game.window.wn_size[0] / 2)) / self.scroll_smoothing)
        self.scroll[1] += int((self.focus.rect.y - self.scroll[1] - (self.game.window.wn_size[1] / 2)) / self.scroll_smoothing)
    
    def set_focus(self, entity):
        self.focus = entity
    
    def remove_focus(self):
        self.focus = None
        