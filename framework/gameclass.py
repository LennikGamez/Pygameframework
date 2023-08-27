import pygame

from .color import Color
from .helperfunctions import tuple2vec
from .vectorclass import Vector
from .scene import Scene

class Game:
    DELTA = 0
    DISPLAY = None
    def __init__(self, width=500, height=500) -> None:
        self.running = True
        pygame.init()
        self.CLOCK = pygame.time.Clock()

        self.setActiveScene(Scene())

        Game.DISPLAY = pygame.display.set_mode((width,height))
        self.background_color = Color.BLACK


    @staticmethod
    def getSize(index=None):
        """returns the window dimensions"""
        if index is None:
            return tuple2vec(Game.DISPLAY.get_size())
        return Game.DISPLAY.get_size()[index]
    @staticmethod
    def center():
        """returns the center Vector of the window"""
        return tuple2vec(Game.getSize()/2)
    @staticmethod
    def display(obj, pos: Vector):
        """Displays an Pygame Surface to the Screen"""
        Game.DISPLAY.blit(obj, pos.to_tuple())

    def drawBackground(self):
        """
        Overwrite function to change the apperance of the background
        """
        Game.DISPLAY.fill(self.background_color)

    def __onExit(self):
        pass

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
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        self.running = False
                        exit()

                self.activeScene.update()
                self.loop()

                pygame.display.flip()
                Game.DELTA = self.CLOCK.tick(framerate) / 1000
        finally:
            self.__onExit()
            self.onExit()
