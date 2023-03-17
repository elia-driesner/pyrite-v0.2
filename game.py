import pygame
import sys

from scripts.window import Window
from scripts.world.world import World
from scripts.json_loader import JsonLoader

class Game:
    def __init__(self):
        pygame.init()
        
        self.wn_size = [960, 540]
        self.fullscreen = False
        
        self.json = JsonLoader()
        self.window = Window(self)
        self.world = World(self)
        
game = Game()