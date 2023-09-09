import pygame

from .color import Color
from .eventhandler import Eventhandler
from .vectorclass import Vector
from .scene import Scene
from .timer.timermanager import TimerManager as TM

from .screen import Screen


class Game:
    DELTA = 0

    def __init__(self, width=500, height=500, layers=1) -> None:
        self.running = True
        pygame.init()
        self.CLOCK = pygame.time.Clock()
        Screen.initScreen(width, height, layers=layers)

        self.setActiveScene(Scene())

        self.background_color = Color.BLACK


    @staticmethod
    def display(obj, pos: Vector, special_flags=0, layer=-1):
        """Displays a Pygame Surface to the Screen"""
        if layer == -1:
            Screen.DISPLAY.blit(obj, pos.to_tuple(), special_flags=special_flags)
        else:
            Screen.getLayer(layer).blit(obj, pos.to_tuple(), special_flags=special_flags)

    def drawBackground(self):
        """
        Overwrite function to change the apperance of the background
        """
        Screen.DISPLAY.fill(self.background_color)

    def drawLayers(self):
        for layer in Screen.layers:
            Screen.DISPLAY.blit(layer, (0, 0))
            layer.fill((0, 0, 0, 0))  # clear each layer

    def __onExit(self):
        if len(TM.activeTimers) > 0:
            TM.stopTimers()

    def onExit(self):
        """Overwrite and insert your code that executes after you close the game"""

    def loop(self):
        """OVERWRITE--gets executed every frame"""

    def setActiveScene(self, newscene: Scene):
        self.activeScene = newscene

    def addToScene(self, *objs):
        self.activeScene.addObjects(objs)

    def run(self, framerate: float = 60.0):
        try:
            while self.running:
                self.drawBackground()
                self.drawLayers()

                Eventhandler.handleEvents(self)

                self.activeScene.update()
                self.loop()

                pygame.display.flip()
                Game.DELTA = self.CLOCK.tick(framerate) / 1000
        finally:
            self.__onExit()
            self.onExit()
