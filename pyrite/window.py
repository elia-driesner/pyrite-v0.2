import pygame
from .assets.customfont import CustomFont

class Window:
    def __init__(self, game, config):
        self.game = game

        self.wn_size = config['wn-size']
        self.wn_scale = config['wn-scale']
        self.fullscreen = config['fullscreen']
        self.bg_color = config['bg-color']
        self.show_fps = config['show-fps']
        self.render_offset = (0, 0)
        
        self.font = CustomFont(self.game.settings['font'])
        
        self.display = pygame.Surface(self.wn_size)
        if self.fullscreen:
            self.window = pygame.display.set_mode(self.wn_scale, pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode(self.wn_scale)
        pygame.display.set_caption(config['title'])
    
    def reset(self):
        self.display.fill(self.bg_color)
        
    def update(self):
        if self.show_fps:
            self.display.blit(self.font.write(f'FPS: {self.game.clock.fps}', 1), (5, 5))
        self.window.blit(pygame.transform.scale(self.display, self.wn_scale), self.render_offset)
        pygame.display.update()