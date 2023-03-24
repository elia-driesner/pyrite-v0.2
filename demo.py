import pygame
import sys
import time

import pyrite


class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        pyrite.init(self, '')
        
        self.player = pyrite.Player((100, 200), (16, 32), image_info=('data/assets/player/player_sprite.png' ,'data/assets/player/animation.json' ,True), movement={'speed': 5, 'gravity': 0.9, 'friction': -.3, 'jump_heigth': 17})        
                
    def render(self):
        self.player.update(self.input.key_events, self.clock.dt, self.world.tile_list)
        self.player.draw(self.window.display, (0, 0))
        
        self.window.update()
    
    def loop(self):
        """game loop"""
        while self.run:
            pyrite.update(self)
        
game = Game()
game.loop()