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
        
        self.player = pyrite.Player(self.world.map_output[2], pyrite.load_player_data('data/assets/player/LightMcSpeed/properties.json'))        
                
    def render(self):
        self.player.update(self.input.key_events, self.clock.dt, self.world.tile_list)
        self.player.draw(self.window.display, (0, 0))
        
        self.window.update()
    
    def loop(self):
        """game loop"""
        while self.run:
            self.input.events()
            pyrite.update(self)
        
game = Game()
game.loop()