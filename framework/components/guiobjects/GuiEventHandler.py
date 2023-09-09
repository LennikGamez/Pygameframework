from framework.eventhandler import onMouseButtonDown, onMouseButtonUp, onKeyDown
from framework.helperfunctions import tuple2vec



class GuiEventHandler:
    objects = []
    textinput = []




@onKeyDown
def __guikeydown__(event):
    for obj in GuiEventHandler.textinput:
        obj.onKeyPress(event)


@onMouseButtonDown
def __guiclick__(event):
    for obj in GuiEventHandler.objects:
        obj.isClicked(tuple2vec(event.pos))

@onMouseButtonUp
def __guirelease__(event):
    for obj in GuiEventHandler.objects:
        obj.isReleased(tuple2vec(event.pos))