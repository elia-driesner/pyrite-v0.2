from .world.window import Window
from .world.world import World
from .world.camera import Camera
from .clock import Clock
from .assets.config import Config
from .input.inputs import Input
from .entity.player import Player
from .pyrite import *

def init(game, config_path):
    game.config = Config()
    game.settings = game.config.load_settings(config_path)
    
    game.clock = Clock(game.settings['clock'])
    game.window = Window(game, game.settings['window'])
    game.camera = Camera(game, game.settings['camera'])
    game.world = World(game, game.settings['world'])
    game.input = Input(game, game.settings['input'])
    
def player_init(game, player, img_path):
    player.load_images()