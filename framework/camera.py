from .vectorclass import Vector


class Camera:
    off_set = Vector(0, 0)
    target = None

    @staticmethod
    def update_offset():
        if Camera.target is None:
            return
        Camera.off_set = Camera.target.position

    @staticmethod
    def set_target(target):
        Camera.target = target