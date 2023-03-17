import pygame
from scripts.world.map import Map

class World:
    def __init__(self, game, config):
        self.map = Map(config['tile-size'], self.settings['window']['wn-size'], config['map-path'], config['sprite-path'])
