import random

from .vectorclass import Vector
from .screen import Screen


class Camera:
    off_set = Vector(0, 0)
    target = None
    screen_shake_duration = 0
    screen_shake_intensity = 0

    @staticmethod
    def shakeScreen(intensity=8, durration=20):
        Camera.screen_shake_intensity = intensity
        Camera.screen_shake_duration = durration



    @staticmethod
    def applyCamera(pos):
        return (pos - Camera.off_set) + Screen.getSize()/2 - Camera.target.size/2 if Camera.target is not None else pos

    @staticmethod
    def update_offset():
        if Camera.target is None:
            return
        Camera.off_set = Camera.target.position

        if Camera.screen_shake_duration > 0:
            Camera.screen_shake_duration -= 1

        if Camera.screen_shake_duration:
            offset_x = random.randint(0, Camera.screen_shake_intensity) - Camera.screen_shake_intensity/2
            offset_y = random.randint(0, Camera.screen_shake_intensity) - Camera.screen_shake_intensity/2
            Camera.off_set += Vector(offset_x, offset_y)

    @staticmethod
    def set_target(target):
        Camera.target = target