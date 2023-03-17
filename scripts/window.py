import pygame
from scripts.text.customfont import CustomFont

class Window:
    def __init__(self, game, config):
        self.game = game

        self.wn_size = config['wn-size']
        self.fullscreen = config['fullscreen']
        self.bg_color = config['bg-color']
        self.render_offset = (0, 0)
        
        self.display = pygame.Surface(self.wn_size)
        if self.fullscreen:
            self.window = pygame.display.set_mode(self.wn_size, pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode(self.wn_size)
    
    def reset(self):
        self.display.fill(self.bg_color)
        
    def update(self):
        self.window.blit(self.display, self.render_offset)
        pygame.display.update()