import pygame
import random

from .particle import Particle

class ParticleManager:
    def __init__(self):
        self.particles = []
        
    def add_particle(self, particle):
        self.particles.append(particle)
    
    def random_speed(self, right, down, left, up, speed):
        random_x = random.randint((speed * left * 1000) * -1, speed * right * 1000) / 1000 -1
        random_y = random.randint((speed * up * 1000) * -1, speed * down * 1000) / 1000 -1
        
        return (random_x, random_y)
    
    
class LandParticle(ParticleManager):
    def __init__(self):
        super().__init__()
        self.spawn_delay = 0
        self.counter = self.spawn_delay
        
    def add(self, pos):
        if self.counter <= 0:
            self.add_particle(Particle(pos, self.random_speed(up=1, down=1, left=1, right=1, speed=2), 100))
            self.counter = self.spawn_delay
        self.counter -= 1
        
    def render(self, window):
        window = window
        self.add(pygame.mouse.get_pos())
        
        for particle in self.particles:
            particle.calc_pos()
            particle.duration -= 1
            pygame.draw.circle(window, (255, 255, 255), (particle.x, particle.y), 4)