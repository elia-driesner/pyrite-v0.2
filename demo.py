import pygame
import sys
import time
import os

import pyrite

class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        pyrite.init(self, '')
        
        self.player = pyrite.assign_character ('Carter', self.world.map_output[2])
                
    def render(self):
        self.window.display.blit(game.world.map_surf, (0 - self.camera.scroll[0], 0 - self.camera.scroll[1]))
        self.player.update(self.input.key_events, self.clock.dt, self.world.tile_list)
        self.camera.set_focus(self.player)
        self.player.draw(self.window.display, self.camera.scroll)
        
        self.window.update()
    
    def loop(self):
        """game loop"""
        self.camera.set_focus(self.player)
        while self.run:
            self.input.events()
            pyrite.update(self)
        
game = Game()
game.loop()