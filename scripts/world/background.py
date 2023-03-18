import pygame
import math

class Background:
    def __init__(self, game, config):
        self.config = config
        self.game = game
        self.angle = math.radians(self.config['bg-line-angle'])
        self.thickness = self.config['bg-line-thickness']
        self.pos = 0
        
        self.speed = self.config['bg-line-speed']
        
    def update(self):
        self.pos = (self.pos + self.speed * self.game.clock.dt) % (self.thickness * 2)

    def render(self):
        angle = math.sin(self.angle) / math.cos(self.angle)
        offset = angle * self.game.window.wn_size[1]
        for i in range(int((self.thickness * 4 + abs(offset) + self.game.window.wn_size[1]) // (self.thickness * 2))):
                base_y = i * self.thickness * 2 + self.pos
                if offset > 0:
                    base_y -= offset
                pygame.draw.line(self.game.window.display, (9, 10, 20), (0, base_y), (self.game.window.display.get_width(), base_y + offset), self.thickness - 4)