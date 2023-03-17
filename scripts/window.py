import pygame

class Window:
    def __init__(self, game, config):
        self.game = game

        self.wn_size = config['wn-size']
        self.fullscreen = config['fullscreen']
        self.bg_color = config['bg-color']
        
        self.display = pygame.Surface(self.wn_size)
        if self.fullscreen:
            self.display = pygame.display.set_mode(self.wn_size, pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode(self.wn_size)
    
    def reset(self):
        self.display.fill((0, 0, 0))