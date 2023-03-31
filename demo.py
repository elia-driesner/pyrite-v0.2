import pygame
import sys
import time
import os

from pyrite.particles.particle_manager import LandParticles

import pyrite

class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        pyrite.init(self, '')
        
        self.player = pyrite.Player(self.world.map_output[2], pyrite.load_player_data('data/assets/player/LightMcSpeed/properties.json'))       
                
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