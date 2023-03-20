import pygame

import time

def update(game):
    game.clock.frame_lenght = time.time()
    game.clock.p_clock.tick(game.clock.max_fps)
    game.input.events()
    game.world.update()
    game.render()
    game.clock.calculate_dt()