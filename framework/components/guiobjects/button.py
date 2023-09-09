from ..gameobjects.position import Position2D
from framework.eventhandler import onMouseButtonDown, onMouseButtonUp
from framework.vectorclass import Vector
from framework.render import Render
from framework.color import Color
from framework.helperfunctions import tuple2vec

class Button(Position2D):
    buttons = []
    def __init__(self, position: Vector, size: Vector):
        super().__init__(position)
        self.size = size
        Button.buttons.append(self)

    def onClick(self):
        """Overwrite"""
        print("pressed")

    def onRelease(self):
        """Overwrite"""
        print("released")

    def isClicked(self, click):
        if not self.isActive():
            return
        if self.position.x < click.x < self.right() and self.position.y < click.y < self.bottom():
            self.onClick()

    def isReleased(self, release):
        if not self.isActive():
            return
        if self.position.x < release.x < self.right() and self.position.y < release.y < self.bottom():
            self.onRelease()

    def render(self, camera=False):
        Render.rect(self.position,self.size.x, self.size.y, color=Color.RGB(125,125,125), camera=camera)

@onMouseButtonDown
def __onButtonDown__(event):
    for btn in Button.buttons:
        btn.isClicked(tuple2vec(event.pos))

@onMouseButtonUp
def __onButtonUp__(event):
    for btn in Button.buttons:
        btn.isReleased(tuple2vec(event.pos))