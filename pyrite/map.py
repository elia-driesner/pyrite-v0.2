import pygame, os, math
from csv import reader
from .assets.sprite import Sprite
from .assets.json_loader import JsonLoader
from .assets.rect_cutter import cut_rect

class CsvMap():
    def __init__(self, tile_size, wn_size, map_path, sprite_path):
        self.tarrain = str(map_path)
        self.tile_size = tile_size
        self.sprite = Sprite(pygame.image.load(str(sprite_path)), (16, 16), (self.tile_size, self.tile_size))
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
    
    def load(self):
        self.load_csv_data()
        self.load_images()
    
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
                            img = self.images[int(tile)]
                            img_rect = img.get_rect()
                            img_rect.x, img_rect.y = x, y
                            self.tile_list.append([img, img_rect])
                    if tile == '39':
                        player_spawn = (x, y - 30)
                    if tile == '40':
                        enemy_spawn = (x, y - 30)
        
        return [self.surface, self.tile_list, player_spawn, enemy_spawn]


class LDTKMap:
    def __init__(self, folder_path, wn_size):
        self.folder_path = folder_path
        self.wn_size = wn_size
        
        self.json_loader = JsonLoader()
        self.map_info = self.json_loader.read_path(folder_path + '/map_info.json')
        self.map = self.json_loader.read_path(folder_path + '/' + self.map_info['map_path'])
        self.collision_objects = []
        
    def load_map(self):
        tileset_path = self.map['defs']['tilesets'][0]['relPath']
        self.tileset = pygame.image.load(self.folder_path + '/' + tileset_path)
        self.tile_size = self.map['defs']['tilesets'][0]['tileGridSize']
        self.sprite = Sprite(self.tileset, (16, 16), (self.tile_size, self.tile_size))
        self.tile_data = self.map['levels'][0]['layerInstances'][0]['gridTiles']
        self.map_w = self.map['levels'][0]['pxWid']
        self.map_h = self.map['levels'][0]['pxHei']
        self.map_size = (self.map_w, self.map_h)
        
    def draw_map(self, scroll):
        self.surface = pygame.Surface(self.map_size)
        self.surface.set_colorkey((0,0,0))
        
        for gridTile in self.tile_data:
            x, y = gridTile['px'][0], gridTile['px'][1]
            t_x, t_y = gridTile['src'][0], gridTile['src'][1]
            frame, layer = t_x / self.tile_size, t_y / self.tile_size
            image = self.sprite.cut(frame, layer)
            self.surface.blit(image, (x - scroll[0], y - scroll[1]))
            rect = cut_rect(image)
            rect.x, rect.y = x, y
            self.collision_objects.append([image, rect])
        print(self.collision_objects)
        
        return [self.surface, self.collision_objects, [100, 100], [100, 100]]
        
                
    def load(self):
        self.load_map()
        
        
        