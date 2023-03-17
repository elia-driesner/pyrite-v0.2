import pygame
import sys

from scripts.window import Window
from scripts.world.world import World
from scripts.json_loader import JsonLoader

class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        
        self.json = JsonLoader()
        self.dest = self.json.read_path('data/settings/dest.json')
        
        self.window = Window(self, self.json.read(self.dest['window']))
        self.world = World(self, self.json.read(self.dest['world']))
        
    def update(self):
        pass
    
    def loop(self):
        while self.run:
            self.update()
        
game = Game()
game.loop()