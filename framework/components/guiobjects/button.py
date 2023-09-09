from ..gameobjects.position import Position2D
from framework.vectorclass import Vector
from framework.render import Render
from framework.color import Color
from framework.components.guiobjects.GuiEventHandler import GuiEventHandler

class Button(Position2D):

    def __init__(self, position: Vector, size: Vector):
        super().__init__(position)
        self.size = size
        GuiEventHandler.objects.append(self)

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
            return True
        return False

    def isReleased(self, release):
        if not self.isActive():
            return
        if self.position.x < release.x < self.right() and self.position.y < release.y < self.bottom():
            self.onRelease()
            return True
        return False

    def render(self, camera=False):
        Render.rect(self.position,self.size.x, self.size.y, color=Color.RGB(125,125,125), camera=camera)
