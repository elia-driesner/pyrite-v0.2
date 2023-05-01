from pyrite.entity.player import *

class CustomPlayer(Player):
    def __init__(self, player_data, pos):
        super().__init__(pos, player_data)
        
        self.weapon = None
    
    def give_weapon(self, weapon):
        self.weapon = weapon
        
    def update(self, keys, dt, tile_list):
        self.update_player(keys, dt, tile_list)