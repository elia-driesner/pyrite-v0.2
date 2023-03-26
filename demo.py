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
        
        self.player = pyrite.Player(self.world.map_output[2], (16, 32), {'speed': 5, 'gravity': 0.9, 'friction': -.3, 'jump_heigth': 17}, ('data/assets/player/player_sprite.png' ,'data/assets/player/animation.json' ,True), 'playable')        
                
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