import pygame
from scene import Scene

class Game:
    DELTA = 0
    def __init__(self) -> None:
        self.running = True
        pygame.init()
        self.CLOCK = pygame.time.Clock()

        self.setActiveScene(Scene())

        pygame.display.set_mode((500,500))

    def drawBackground(self):
        """
        Overwrite function to change the apperance of the background
        """

    def __onExit(self):
        pass

    def onExit(self):
        """Overwrite and insert your code that executes after you close the game"""

    def loop(self):
        """OVERWRITE--gets executed every frame"""

    def setActiveScene(self, newscene: Scene):
        self.activeScene = newscene

    def addToScene(self, *objs):
        self.activeScene.addObjects(*objs)

    def run(self, framerate: float = 60.0):
        try:
            while self.running:
                self.drawBackground()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        self.running = False
                        exit()

                self.loop()

                pygame.display.flip()
                Game.DELTA = self.CLOCK.tick(framerate) / 1000
        finally:
            self.__onExit()
            self.onExit()

g=Game()

g.run()