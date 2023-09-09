import pygame

from framework.components.guiobjects.button import Button
from framework.vectorclass import Vector
from framework.render import Render
from framework.components.guiobjects.GuiEventHandler import GuiEventHandler

from framework.timer.timer import RepeatTimer

class TextInput(Button):
    def __init__(self, position: Vector, size: Vector, orientation="l", valign="c"):
        GuiEventHandler.textinput.append(self)
        super().__init__(position, size)
        self.font = Render.FONTS.get("default")
        self.focused = False
        self.showCursor = False
        self.text = "Hallo"
        self.orientation = orientation
        self.valgin = valign
        self.text_origin = self.position.copy()

        match orientation:
            case "l":
                pass
            case "c":
                self.text_origin.x = self.center().x    # the center point of the text is text_origin
            case "r":
                self.text_origin = Vector(self.right(),self.position.y)

        match valign:
            case "c":
                self.text_origin.y = self.center().y
                if self.orientation in "lr":
                    self.text_origin.y -= self.font.get_height()/2  # apply offset to compensate the position change by changing the orientation
            case "t":
                self.text_origin.y = self.center().y - self.font.get_height()
                if self.orientation == "c":
                    self.text_origin.y = self.center().y - self.font.get_height()/2
            case "b":
                self.text_origin.y = self.center().y
                if self.orientation == "c":
                    self.text_origin.y += self.font.get_height() / 2

        self.cursor_blink = RepeatTimer(.3, self.toggleCursor)

    def toggleCursor(self):
        if self.showCursor == False:
            self.showCursor = True
        else:
            self.showCursor = False


    def renderCursor(self):
        if self.focused and self.showCursor:
            size = self.font.size(self.text)
            x = 0
            y1, y2 = 0, 0

            match self.valgin:
                case "t" | "b":
                    if self.orientation == "c": # origin center
                        y1 = self.text_origin.y - size[1] / 2
                        y2 = self.text_origin.y + size[1] / 2
                    else:
                        y1 = self.text_origin.y # origin top right
                        y2 = self.text_origin.y + size[1]
                case "c":
                    if self.orientation == "c": # origin center
                        y1 = self.text_origin.y - size[1]/2
                        y2 = self.text_origin.y + size[1]/2
                    else:
                        y1 = self.text_origin.y # origin top right
                        y2 = self.text_origin.y + size[1]

            match self.orientation:
                case "l"|"r":
                    x = self.text_origin.x + size[0]
                case "c":
                    x = self.text_origin.x + size[0]/2

            pos = Vector(x, y1)
            pos2 = Vector(x, y2)

            Render.line(pos, pos2)

    def render(self):
        Render.rect(self.position, self.size.x, self.size.y, width=2)
        Render.text(self.text_origin, self.text, orientation=self.orientation)
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