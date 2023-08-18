
from framework import *


class App(Game):
    def __init__(self, width=500, height=500) -> None:
        super().__init__(width, height)

        self.position = Vector()


    def loop(self):
        self.position += Vector(3,3)
        Render.rect(self.position,10,10, color=Color.GREEN)


g = App()
g.run(60)