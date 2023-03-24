import pygame

def tile_collision(rect, tiles):
    collision_list = []
    for tile in tiles:
        if rect.colliderect(tile[1]):
            collision_list.append(tile)
    return collision_list

def move(entity, x_movement, y_movement):
    pass