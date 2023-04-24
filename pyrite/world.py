import pygame
from .map import CsvMap, LDTKMap
from .background import Background

class World:
    def __init__(self, game, config):
        self.game = game
        self.config = config
        self.map = LDTKMap('data/map/vulcanic', self.game.settings['window']['wn-size'])
        self.map.load()
        
        self.bg = Background(self.game, self.config)

        self.map_output = self.map.draw_map(self.game.camera.scroll)
        self.tile_list = self.map_output[1]
        self.map_surf = self.map_output[0]
        
    def update(self, scroll):
        self.map_surf = self.map.update(scroll)
        # self.map_surf = pygame.transform.scale(self.map_surf, self.game.window.wn_size)
        self.bg.update()
    
        
