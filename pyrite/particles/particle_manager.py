import pygame
import random

from particle import Particle

class ParticleManager:
    def __init__(self):
        self.particles = []
        
    def add_particle(self, particle):
        self.particles.append()
    
    def random_speed(self, max_x, max_y, negative=True):
        random_x = random.randint(0, max_x * 10) / 10
        random_y = random.randint(0, max_y * 10) / 10
        
        if negative:
            if random.randint(0, 1) == 0:
                random_x *= -1 
            if random.randint(0, 1) == 0:
                random_y *= -1 
        
        return (random_x, random_y)
    
    
class LandParticle(ParticleManager):
    def __init__(self):
        super().__init__()
        
    def add(self):
        self.add_particle(Particle((100, 100), self.random_speed(2, 2), 100))