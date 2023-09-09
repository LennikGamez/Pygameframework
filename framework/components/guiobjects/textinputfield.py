import pygame

from framework.components.guiobjects.button import Button
from framework.vectorclass import Vector
from framework.render import Render
from framework.components.guiobjects.GuiEventHandler import GuiEventHandler

class TextInput(Button):
    def __init__(self, position: Vector, size: Vector):
        GuiEventHandler.textinput.append(self)
        super().__init__(position, size)
        self.font = Render.FONTS.get("default")
        self.focused = False
        self.cursor_index = 0
        self.text = "Hallo"

    def renderCursor(self):
        if self.focused:
            size = self.font.size(self.text)
            center = self.center()
            pos = Vector(center.x+size[0]/2, center.y-size[1]/2)
            pos2 = Vector(self.center().x+size[0]/2, center.y+size[1]/2)
            Render.line(pos, pos2)

    def render(self):
        Render.rect(self.position, self.size.x, self.size.y, width=2)
        Render.text(self.center(), self.text)
        self.renderCursor()

    def isClicked(self, click):
        if not super().isClicked(click):
            self.focused = False

    def onClick(self):
        self.focused = True

    def onKeyPress(self, event):
        if not self.focused:
            return
        if event.unicode == '\x08':
            self.text = self.text[:-1]
        elif event.unicode == '\r':
            self.send()
        else:
            self.text += event.unicode

    def send(self):
        """Overwrite"""
        print("sending",self.text)
        self.focused = False