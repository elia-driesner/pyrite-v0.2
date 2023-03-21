import pygame

import time

def update(game):
    game.clock.set_timepoint()
    game.clock.p_clock.tick(game.clock.max_fps)
    game.input.events()
    
    game.world.update()
    game.window.reset()
    game.world.bg.render()
    game.world.map_surf.set_colorkey((0, 0, 0))
    game.window.display.blit(game.world.map_surf, (0, 0))
    game.render()
    
    game.clock.calculate_dt()