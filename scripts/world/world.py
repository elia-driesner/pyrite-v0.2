import pygame
from scripts.world.map import Map

class World:
    def __init__(self, game, config):
        self.game = game
        self.map = Map(config['tile-size'], self.game.settings['window']['wn-size'], config['map-path'], config['tileset-path'])
        self.map.load_csv_data()
        self.map.load_images()

        self.map_output = self.map.draw_map(self.game.camera.scroll)
        self.map_surf = self.map_output[0]
        
