import pygame
import sys
import time

from pyrite.world.window import Window
from pyrite.world.world import World
from pyrite.world.camera import Camera
from pyrite.clock import Clock
from pyrite.assets.config import Config


class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        
        self.config = Config()
        self.settings = self.config.load_settings()
        self.frame_length = time.time()
        
        self.clock = Clock(self.settings['clock'])
        self.window = Window(self, self.settings['window'])
        self.camera = Camera(self, self.settings['camera'])
        self.world = World(self, self.settings['world'])
        
    def update(self):
        """updates the game"""
        self.frame_length = time.time()
        self.clock.p_clock.tick(self.clock.max_fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        self.world.update()
        self.render()
        self.clock.calculate_dt(self.frame_length)
                
    def render(self):
        self.window.reset()
        self.world.bg.render()
        self.world.map_surf.set_colorkey((0, 0, 0))
        self.window.display.blit(self.world.map_surf, (0, 0))
        
        self.window.update()
    
    def loop(self):
        """game loop"""
        while self.run:
            self.update()
        
game = Game()
game.loop()