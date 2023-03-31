import pygame

class Particle:
    def __init__(self, pos, velocity, duration):
        self.x = pos[0]
        self.y = pos[1]
        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]
        self.duration = duration
        
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
    
    def calc_pos(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.x = self.rect.x
        self.y = self.rect.y
        