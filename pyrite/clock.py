import pygame
import time

class Clock:
    def __init__(self, config):
        pygame.init()
        self.max_fps = config['max-fps']
        self.p_clock = pygame.time.Clock()
        self.fps = self.max_fps
        self.dt = 0
        self.frame_length = 0
        
    def calculate_dt(self, frame_length):
        """Calculates the deltatime between each frame"""
        self.dt = time.time() - frame_length
        self.dt *= 60
        self.fps = str(int(self.p_clock.get_fps()))
    