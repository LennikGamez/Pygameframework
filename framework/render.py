
import pygame

from framework.helperfunctions import tuple2vec
from .gameclass import Game
from .color import Color
from .vectorclass import Vector
from .camera import Camera


class Render:
    pygame.font.init()
    FONTS = {
        "default": pygame.font.SysFont("Comic Sans MS", 30)
    }

    @staticmethod
    def line(pos1: Vector, pos2: Vector, color=Color.WHITE, width=1, camera=True):
        if camera:
            pos1 = Camera.applyOffset(pos1)
            pos2 = Camera.applyOffset(pos2)
        return pygame.draw.line(Game.DISPLAY,color,pos1.to_tuple(),pos2.to_tuple(),width)

    @staticmethod
    def rect(pos: Vector, w, h, width=0, color=Color.WHITE,\
             border_radius=-1, bottom_left_radius=-1, bottom_right_radius=-1,\
             top_left_radius=-1, top_right_radius=-1, camera=True):
        if camera:
            pos = Camera.applyOffset(pos)
        return pygame.draw.rect(Game.DISPLAY,color,pygame.Rect(
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
    def circle(pos: Vector, r, color=Color.WHITE, width=0, camera=True):
        if camera:
            pos = Camera.applyOffset(pos)
        pygame.draw.circle(Game.DISPLAY,color,pos.to_tuple(),r, width=width)


    @staticmethod
    def image(pos: Vector, img, camera=True):
        if camera:
            pos = Camera.applyOffset(pos)
        pos -= tuple2vec(img.get_size())/2

        Game.DISPLAY.blit(img, pos.to_tuple())

    @staticmethod
    def text(pos: Vector, text, antialiasing=False, font=FONTS.get("default"), color=Color.WHITE, bgcolor=None, camera=True):
        surf = font.render(str(text), antialiasing, color, bgcolor)
        rect = surf.get_rect()
        if camera:
            pos = Camera.applyOffset(pos)
        rect.center = pos.to_tuple()
        Game.DISPLAY.blit(surf, rect)
