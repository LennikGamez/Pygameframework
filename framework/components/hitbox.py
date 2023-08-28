import pygame
from framework.helperfunctions import tuple2vec
from framework.render import Render
from .. import Color
from ..vectorclass import Vector
from .position import Position2D


class HitBox(Position2D):
    def __init__(self, pos: Vector, size: Vector) -> None:
        super().__init__(pos)
        self.size = size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.old_rect = self.rect.copy()

    def render(self):
        """Overwrite"""
        #Render.rect(self.position, self.size.x, self.size.y, color=Color.BLUE)
