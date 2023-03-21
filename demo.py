import pygame
import sys
import time

import pyrite


class Game:
    def __init__(self):
        pygame.init()
        self.run = True
        pyrite.init(self, '')
        
        self.player = pyrite.Player((100, 100), (16, 32), image_info=('data/assets/player/player_sprite.png' ,'data/assets/player/animation.json' ,True))
                
    def render(self):
        self.player.update()
        self.window.display.blit(self.player.image, (110, 110))
        
        self.window.update()
    
    def loop(self):
        """game loop"""
        while self.run:
            pyrite.update(self)
        
game = Game()
game.loop()