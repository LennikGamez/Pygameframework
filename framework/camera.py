from .vectorclass import Vector
from .screen import Screen


class Camera:
    off_set = Vector(0, 0)
    target = None

    @staticmethod
    def applyCamera(pos):
        return (pos - Camera.off_set) + Screen.getSize()/2 - Camera.target.size/2 if Camera.target is not None else pos

    @staticmethod
    def update_offset():
        if Camera.target is None:
            return
        Camera.off_set = Camera.target.position

    @staticmethod
    def set_target(target):
        Camera.target = target