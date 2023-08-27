import pygame
from framework.helperfunctions import tuple2vec
from framework.render import Render
from ..vectorclass import Vector
from .position import Position2D


class HitBox(Position2D):
    def __init__(self, pos: Vector, size: Vector) -> None:
        super().__init__(pos)
        self.size = size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.old_rect = self.rect.copy()

    def fixedUpdate(self):
        self.updateRects()

        return super().fixedUpdate()

    def render(self):
        Render.rect(self.position, self.size.x, self.size.y)

    def updateOldRect(self):
        self.old_rect = self.rect.copy()

    def updateCurrentRect(self):
        self.rect.topleft = self.position.to_tuple()
        self.rect.width = self.size.x
        self.rect.height = self.size.y

    def updateRects(self):
        self.updateOldRect()
        self.updateCurrentRect()

    def oldRight(self):
        return self.old_rect.right

    def oldLeft(self):
        return self.old_rect.left
    
    def oldTop(self):
        return self.old_rect.top
    
    def oldBottom(self):
        return self.old_rect.bottom
    
    def oldCenter(self):
        return tuple2vec(self.old_rect.center)


    def right(self):
        return self.rect.right

    def left(self):
        return self.rect.left
    
    def top(self):
        return self.rect.top
    
    def bottom(self):
        return self.rect.bottom
    
    def center(self):
        return tuple2vec(self.rect.center)