
from framework.vectorclass import Vector
from .dummy import Dummy


class Position2D(Dummy):
    def __init__(self, pos: Vector, offset: Vector = Vector()) -> None:
        super().__init__()
        self.offset = offset
        self.position = pos + self.offset
        self.last_position = self.position.copy()
        self.size = Vector()

    def fixedUpdate(self):
        self.last_position = self.position.copy()
        return super().fixedUpdate()


    def setCenterToPosition(self, pos):
        self.position = pos - self.size/2

    def getCenterToPositionOffset(self, pos):
        return (pos-self.size/2) - self.position

    def oldRight(self):
        return self.last_position.x + self.size.x

    def oldLeft(self):
        return self.last_position.x

    def oldTop(self):
        return self.last_position.y

    def oldBottom(self):
        return self.last_position.y + self.size.y

    def oldCenter(self):
        return self.last_position + self.size / 2

    def right(self):
        return self.position.x + self.size.x

    def left(self):
        return self.position.x

    def top(self):
        return self.position.y

    def bottom(self):
        return self.position.y + self.size.y

    def center(self):
        return self.position + self.size / 2