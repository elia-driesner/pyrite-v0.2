import pygame

from ..entity.entity import Entity

class Player(Entity):
    def __init__(self, pos, size, type=None, **kw):
        super().__init__()