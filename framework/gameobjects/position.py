
from ..vectorclass import Vector
from .dummy import Dummy


class Position2D(Dummy):
    def __init__(self, pos: Vector) -> None:
        super().__init__()
        self.position = pos
        self.last_position = self.position.copy()
        self.size = Vector()

    def fixedUpdate(self):
        self.last_position = self.position.copy()