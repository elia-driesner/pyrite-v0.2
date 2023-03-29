import pygame

import time

def update(game):
    game.clock.set_timepoint()
    game.clock.p_clock.tick(game.clock.max_fps)
    
    game.world.update()
    game.window.reset()
    game.world.bg.render()
    game.world.map_surf.set_colorkey((0, 0, 0))
    game.camera.calc_scroll()
    game.render()
    
    game.clock.calculate_dt()