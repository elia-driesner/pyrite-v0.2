import pygame

import time

def update(game):
    # Game clock
    game.clock.frame_lenght = time.time()
    game.clock.p_clock.tick(game.clock.max_fps)