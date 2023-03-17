import pygame
import sys

from scripts.window import Window
from scripts.world.world import World
from scripts.world.camera import Camera
from data.settings.config import Config


class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        
        self.config = Config()
        self.settings = self.config.load_settings()
        
        self.window = Window(self, self.settings['window'])
        self.camera = Camera(self, self.settings['camera'])
        self.world = World(self, self.settings['world'])
        
    def update(self):
        """updates the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        self.render()
                
    def render(self):
        self.window.reset()
        self.window.display.blit(self.world.map_surf, (0, 0))
        
        self.window.update()
    
    def loop(self):
        """game loop"""
        while self.run:
            self.update()
        
game = Game()
game.loop()