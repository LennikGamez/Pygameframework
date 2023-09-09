from pygame import Surface
import pygame

from framework.color import Color
from ..helperfunctions import tuple2vec

from framework.render import Render
from ..vectorclass import Vector
from .position import Position2D


class Sprite(Position2D):
    def __init__(self, pos: Vector, img: Surface) -> None:
        super().__init__(pos)
        self.img = img
        self.org_img = self.img.copy()

        self.angle = 0
        self.scale = 0
        self.size = tuple2vec(self.org_img.get_size())

    def fixedUpdate(self):
        self.size = tuple2vec(self.org_img.get_size())

        return super().fixedUpdate()

    def render(self, camera=True):
        Render.image(self.position+self.size/2, self.img, layer=self.layer, camera=camera)

    def setRotation(self, angle):
        self.angle = angle
        self.img = pygame.transform.rotate(self.org_img, self.angle)
    
    def rotateBy(self, angle):
        self.angle += angle
        self.img = pygame.transform.rotate(self.org_img, self.angle)

    def setScale(self, scale):
        self.scale = scale
        self.img = pygame.transform.scale_by(self.img, self.scale)
    
    def scaleBy(self, scale):
        self.scale += scale
        self.img = pygame.transform.scale_by(self.img, self.scale)