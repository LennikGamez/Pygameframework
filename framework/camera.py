from .vectorclass import Vector
from .gameclass import Game


class Camera:
    off_set = Vector(0, 0)
    target = None

    @staticmethod
    def applyOffset(position: Vector):
        if Camera.target is None:
            return position
        return ((position - Camera.off_set) + Game.getSize()/2) - Camera.target.size/2

    @staticmethod
    def update_offset():
        if Camera.target is None:
            return
        Camera.off_set = Camera.target.position

    @staticmethod
    def set_target(target):
        Camera.target = target