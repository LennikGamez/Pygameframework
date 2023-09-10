from enum import Enum, auto
from framework.components.gameobjects.maskcollider import Maskcollider

import keyboard


class CollisionTypes(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()
    NONE = auto()


class CollisionType:
    def __init__(self, type: CollisionTypes) -> None:
        self.type = type

    def is_left(self):
        if self.type == CollisionTypes.LEFT:
            return True
        return False

    def is_right(self):
        if self.type == CollisionTypes.RIGHT:
            return True
        return False

    def is_top(self):
        if self.type == CollisionTypes.TOP:
            return True
        return False

    def is_bottom(self):
        if self.type == CollisionTypes.BOTTOM:
            return True
        return False

    def is_none(self):
        if self.type == CollisionTypes.NONE:
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.type}"


class CollisionHandler:


    @staticmethod
    def maskcollision(m1: Maskcollider, m2: Maskcollider):
        from framework.render import Render
        offset = (m2.position) - (m1.position)
        return m1.mask.overlap(m2.mask, offset.to_tuple())



    @staticmethod
    def snapbackCollision(h1, h2, parent=None):
        """Returns CollisionType and sets the position of the Hitbox to seperate it from the collider"""

        object1 = h1
        if parent is not None:
            object1 = parent
            parent.updatePositions()    # calculates the current position for each component since the position could have changed due to other parts of the script
        collision = CollisionHandler.isCollision(h1, h2)

        if collision.is_none():
            return collision


        if collision.is_left():
            object1.position.x = h2.right() - h1.offset.x
        elif collision.is_right():
            object1.position.x = h2.position.x - h1.size.x - h1.offset.x
        elif collision.is_bottom():
            object1.position.y = h2.top() - h1.size.y - h1.offset.y
        elif collision.is_top():
            object1.position.y = h2.bottom() - h1.offset.y
        if parent is not None:
            parent.updatePositions()    # prevents jittering

        return collision

    @staticmethod
    def isCollision(h1, h2):
        """Return a CollisonType object which holds information about the place of collision for example the collision happend on the left of the object"""

        if not h1.isActive() or not h2.isActive():
            return CollisionType(CollisionTypes.NONE)

        # CollisionType is from the perspective of first hitbox
        if left_right_jump(h1, h2) and CollisionHandler.y_overlap(h1, h2):
            return CollisionType(CollisionTypes.RIGHT)
        if right_left_jump(h1, h2) and CollisionHandler.y_overlap(h1, h2):
            return CollisionType(CollisionTypes.LEFT)
        if top_bottom_jump(h1, h2) and CollisionHandler.x_overlap(h1, h2):
            return CollisionType(CollisionTypes.BOTTOM)
        if bottom_top_jump(h1, h2) and CollisionHandler.x_overlap(h1, h2):
            return CollisionType(CollisionTypes.TOP)
        return CollisionType(CollisionTypes.NONE)

    @staticmethod
    def isOverlap(h1, h2):
        if CollisionHandler.x_overlap(h1, h2) and CollisionHandler.y_overlap(h1, h2):
            return True
        return False

    @staticmethod
    def x_overlap(h1, h2):
        """Returns True if h1 and h2 overlap on the x-axis"""
        # h1 colliding from right
        if h1.right() >= h2.left() and h1.right() <= h2.right() or \
                h1.left() <= h2.right() and h1.left() >= h2.left() or \
                h1.left() <= h2.left() and h1.right() >= h2.right():  # h2 inside h1
            return True
        return False

    @staticmethod
    def y_overlap(h1, h2):
        """Returns True if h1 and h2 overlap on the y-axis"""
        # h1 colliding from right
        if h1.top() <= h2.bottom() and h1.top() >= h2.top() or \
                h1.bottom() >= h2.top() and h1.bottom() <= h2.bottom() or \
                h1.bottom() >= h2.bottom() and h1.top() <= h2.top():  # h2 inside h1
            return True
        return False


def left_right_jump(h1, h2):
    if h1.oldRight() <= h2.left() and h1.right() >= h2.left():
        return True


def top_bottom_jump(h1, h2):
    if h1.oldBottom() <= h2.top() and h1.bottom() >= h2.top():
        return True


def right_left_jump(h1, h2):
    if h1.oldLeft() >= h2.right() and h1.left() <= h2.right():
        return True


def bottom_top_jump(h1, h2):
    if h1.oldTop() >= h2.bottom() and h1.top() <= h2.bottom():
        return True
