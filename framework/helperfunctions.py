
from .vectorclass import Vector


def tuple2vec(tuple: tuple):
    """converts tuple to Vector object"""
    return Vector(tuple[0], tuple[1])


def lerp(value,start1,stop1,start2,stop2):
    """Translates a value with a specific range to another range"""
    return (value - start1) / (stop1 - start1) * (stop2-start2)+start2