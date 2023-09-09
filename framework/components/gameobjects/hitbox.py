import pygame
from framework.helperfunctions import tuple2vec
from framework.render import Render
from framework import Color
from framework.vectorclass import Vector
from .position import Position2D


class HitBox(Position2D):
    def __init__(self, pos: Vector, size: Vector, debug=False) -> None:
        super().__init__(pos)
        self.size = size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.old_rect = self.rect.copy()
        self.debug = debug

    def render(self, camera=True):
        """Overwrite"""
        if not self.debug:
            return
        Render.rect(self.position, self.size.x, self.size.y, color=Color.RED, layer=self.layer, camera=camera)
