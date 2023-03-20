import pygame
import sys
import time

import pyrite


class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        pyrite.init(self, '')
                
    def render(self):
        self.window.reset()
        self.world.bg.render()
        self.world.map_surf.set_colorkey((0, 0, 0))
        self.window.display.blit(self.world.map_surf, (0, 0))
        
        self.window.update()
    
    def loop(self):
        """game loop"""
        while self.run:
            pyrite.update(self)
        
game = Game()
game.loop()