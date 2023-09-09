
import pygame

from framework.helperfunctions import tuple2vec
from .color import Color
from .vectorclass import Vector
from .screen import Screen
from .camera import Camera


class Render:
    pygame.font.init()
    FONTS = {
        "default": pygame.font.SysFont("Comic Sans MS", 30)
    }

    @staticmethod
    def line(pos1: Vector, pos2: Vector, color=Color.WHITE, width=1, layer=0, camera=False):
        if camera:
            pos1 = Camera.applyCamera(pos1)
            pos2 = Camera.applyCamera(pos2)
        return pygame.draw.line(Screen.getLayer(layer),color,pos1.to_tuple(),pos2.to_tuple(),width)

    @staticmethod
    def rect(pos: Vector, w, h, width=0, color=Color.WHITE,\
             border_radius=-1, bottom_left_radius=-1, bottom_right_radius=-1,\
             top_left_radius=-1, top_right_radius=-1, layer=0, camera=False):
        if camera:
            pos = Camera.applyCamera(pos)
        return pygame.draw.rect(Screen.getLayer(layer),color,pygame.Rect(
            pos.x, pos.y,
            w, h
        ), width=width,
        border_radius=border_radius,
        border_bottom_left_radius=bottom_left_radius,
        border_bottom_right_radius= bottom_right_radius,
        border_top_left_radius= top_left_radius,
        border_top_right_radius= top_right_radius
        )
    
    @staticmethod
    def circle(pos: Vector, r, color=Color.WHITE, width=0, layer=0, camera=False):
        if camera:
            pos = Camera.applyCamera(pos)
        pygame.draw.circle(Screen.getLayer(layer),color,pos.to_tuple(),r, width=width)


    @staticmethod
    def image(pos: Vector, img, layer=0, camera=False):
        if camera:
            pos = Camera.applyCamera(pos)
        pos -= tuple2vec(img.get_size())/2

        Screen.getLayer(layer).blit(img, pos.to_tuple())

    @staticmethod
    def text(pos: Vector, text, antialiasing=False, font=FONTS.get("default"), color=Color.WHITE, bgcolor=None, layer=0, camera=False):
        if camera:
            pos = Camera.applyCamera(pos)
        surf = font.render(str(text), antialiasing, color, bgcolor)
        rect = surf.get_rect()
        rect.center = pos.to_tuple()
        Screen.getLayer(layer).blit(surf, rect)
