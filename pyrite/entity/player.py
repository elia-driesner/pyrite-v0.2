import pygame

from ..entity.entity import Entity

class Player(Entity):
    def __init__(self, pos, size, type=None):
        super().__init__(pos, size)