import pygame.transform
from pygame import Surface
from pygame.mask import from_surface

from framework.helperfunctions import tuple2vec
from framework.components.gameobjects.position import Position2D
from framework.render import Render

class Maskcollider(Position2D):
    def __init__(self, position, surface: Surface):
        super().__init__(position)
        self.debug = False
        self.surface = surface
        self.mask = from_surface(self.surface)
        self.mask_img = self.mask.to_surface()

    def render(self, camera=True):
        if not self.debug:
            return
        Render.image(self.position+tuple2vec(self.surface.get_size())/2, self.mask_img, camera=camera)