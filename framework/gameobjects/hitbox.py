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

    def render(self):
        Render.rect(self.position, self.size.x, self.size.y)


    def oldRight(self):
        return self.last_position.x + self.size.x

    def oldLeft(self):
        return self.last_position.x
    
    def oldTop(self):
        return self.last_position.y
    
    def oldBottom(self):
        return self.last_position.y + self.size.y
    
    def oldCenter(self):
        return self.last_position + self.size/2


    def right(self):
        return self.position.x + self.size.x

    def left(self):
        return self.position.x
    
    def top(self):
        return self.position.y
    
    def bottom(self):
        return self.position.y + self.size.y
    
    def center(self):
        return self.position+self.size/2