import math
from typing import Any, Iterable


class Vector:

    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    # Vector operator overloads
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, Iterable) and len(other) == 2:
            return Vector(self.x + other[0], self.y + other[1])
        return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        if isinstance(other, Iterable) and len(other) == 2:
            return Vector(self.x - other[0], self.y-other[1])
        return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x * other.x, self.y * other.y)
        if isinstance(other, Iterable) and len(other) == 2:
            return Vector(self.x * other[0], self.y * other[1])
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x / other.x, self.y / other.y)
        if isinstance(other, Iterable) and len(other) == 2:
            return Vector(self.x / other[0], self.y / other[1])
        return Vector(self.x / other, self.y / other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        if isinstance(other, Iterable) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return self.x == other and self.y == other

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))

    def copy(self):
        return Vector(self.x, self.y)

    def __repr__(self):
        return f'{self.x}, {self.y}'

    def to_tuple(self):
        return (self.x, self.y)

    # vector Functions
    def normalized(self):
        return normalize(self)

    def magnitude(self):
        return length(self)
    
    def ZERO(self):
        self.x = 0
        self.y = 0

    def directionTo(self, position):
        d = position-self
        return d.normalized()
    
    def distanceTo(self,position):
        difference = position-self
        distance = math.sqrt(pow(difference.x,2)+pow(difference.y,2))
        return distance
    
    def angleTo(self, position):
        difference = position-self
        angle = math.degrees(math.atan2(difference.y, difference.x))
        return angle
    
    @staticmethod
    def dotproduct(vector1, vector2):
        return dot(vector1, vector2)
    
def dot(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y


def length_sqr(vec):
    return vec.x ** 2 + vec.y ** 2


def length(vec):
    return math.sqrt(length_sqr(vec))


def normalize(vec):
    vec_len = length(vec)

    if vec_len < 0.00001:
        return Vector(0, 1)
    return Vector(vec.x / vec_len, vec.y / vec_len)
