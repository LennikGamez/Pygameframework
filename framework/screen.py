import pygame
from framework.helperfunctions import tuple2vec


class Screen:
    DISPLAY = None
    layers = []

    @staticmethod
    def initScreen(width=500, height=500, layers=1):
        Screen.setupScreen(width, height)
        Screen.layers = [pygame.Surface((width, height), flags=pygame.SRCALPHA) for _ in range(layers)]

    @staticmethod
    def setupScreen(width, height):
        Screen.DISPLAY = pygame.display.set_mode([width, height])
    @staticmethod
    def getLayer(index):
        return Screen.layers[index]


    @staticmethod
    def getSize(index=None):
        """returns the window dimensions"""
        if index is None:
            return tuple2vec(Screen.DISPLAY.get_size())
        return Screen.DISPLAY.get_size()[index]

    @staticmethod
    def center():
        """returns the center Vector of the window"""
        return Screen.getSize() / 2
