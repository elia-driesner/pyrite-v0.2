import pygame, os, math
from csv import reader
from .assets.sprite import Sprite

class Map():
    def __init__(self, tile_size, wn_size, map_path, sprite_path):
        self.tarrain = str(map_path)
        self.tile_size = tile_size
        self.sprite = Sprite(pygame.image.load(str(sprite_path)), (32, 32), (self.tile_size, self.tile_size))
        self.sprite_rows, self.sprite_col = 7, 7
        self.surface = pygame.Surface((1920 * 3, 1080 * 3))
        self.surface.set_colorkey((0,0,0))
        self.wn_size = wn_size
        
        self.images = []
        
    def load_csv_data(self):
        """loads the map from csv file"""
        self.rows = 0
        self.colums = 0
        self.map_list = []
        with open (self.tarrain) as map:
            level = reader(map, delimiter = ",")
            for row in level:
                self.map_list.append(list(row))
            
    def load_images(self):
        """loads the tile images and saves them in an array"""
        for i in range(0, self.sprite_rows):
            for j in range(0, self.sprite_col):
                self.images.append(self.sprite.cut(j, i))
    
    def draw_map(self, scroll):
        """draws the map once on a reusable surface"""
        self.tile_list = []
        player_spawn = (0, 0)
        enemy_spawn = (0, 0)
        y = 0
        for row in self.map_list:
                self.colums = 0
                self.rows += 1
                y += self.tile_size
                x = 0
                for tile in row:
                    x += self.tile_size
                    self.colums += 1
                    if tile != '-1' and tile != '39' and tile != '40':
                            self.surface.blit(self.images[int(tile)], (x - scroll[0], y - scroll[1]))
                            self.tile_list.append([self.images[int(tile)], (x - scroll[0], y - scroll[1])])
                    if tile == '39':
                        player_spawn = (x, y - 30)
                    if tile == '40':
                        enemy_spawn = (x, y - 30)
        
        return [self.surface, self.tile_list, player_spawn, enemy_spawn]
