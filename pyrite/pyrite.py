import pygame

import time

def update(game):
    game.clock.set_timepoint()
    game.clock.p_clock.tick(game.clock.max_fps)
    game.input.events()
    game.world.update()
    game.render()
    game.clock.calculate_dt()