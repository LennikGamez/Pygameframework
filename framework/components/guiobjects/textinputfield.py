import pygame

from framework.components.guiobjects.button import Button
from framework.vectorclass import Vector
from framework.render import Render
from framework.components.guiobjects.GuiEventHandler import GuiEventHandler

from framework.timer.timer import RepeatTimer

class TextInput(Button):
    def __init__(self, position: Vector, size: Vector):
        GuiEventHandler.textinput.append(self)
        super().__init__(position, size)
        self.font = Render.FONTS.get("default")
        self.focused = False
        self.showCursor = False
        self.text = "Hallo"
        self.cursor_blink = RepeatTimer(.3, self.toggleCursor)

    def toggleCursor(self):
        if self.showCursor == False:
            self.showCursor = True
        else:
            self.showCursor = False


    def renderCursor(self):
        if self.focused and self.showCursor:
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
            self.cursor_blink.stopTimer()

    def onClick(self):
        self.cursor_blink.startTimer()
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