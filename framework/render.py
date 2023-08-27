
import pygame

from framework.helperfunctions import tuple2vec
from .gameclass import Game
from .color import Color
from .vectorclass import Vector


class Render:

    @staticmethod
    def line(pos1: Vector, pos2: Vector, color=Color.WHITE, width=1):
        return pygame.draw.line(Game.DISPLAY,color,pos1.to_tuple(),pos2.to_tuple(),width)

    @staticmethod
    def rect(pos: Vector, w, h, width=0, color=Color.WHITE,border_radius=-1, bottom_left_radius=-1, bottom_right_radius=-1, top_left_radius=-1, top_right_radius=-1):
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
    def circle(pos: Vector, r, color=Color.WHITE, width=0):
        pygame.draw.circle(Game.DISPLAY,color,pos.to_tuple(),r, width=width)


    @staticmethod
    def image(pos: Vector, img):
        pos -= tuple2vec(img.get_size())/2

        Game.DISPLAY.blit(img, pos.to_tuple())