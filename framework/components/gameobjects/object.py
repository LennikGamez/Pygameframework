from .position import Position2D
from .dummy import Dummy
from .hitbox import HitBox
from .sprite import Sprite
from framework import Vector


class Object(Position2D):
    def __init__(self, position):
        super().__init__(position)

        self.components: list = []
    def addComponent(self, component, position_offset: Vector = Vector(), layer=-1):
        # match component:
        #     case HitBox():
        #         self.components["Hitboxes"].append(component)
        #     case Position2D():
        #         self.components["Positions"].append(component)
        #     case Sprite():
        #         self.components["Sprites"].append(component)
        #     case Dummy():
        #         self.components["Dummies"].append(component)
        #
        if component.offset != position_offset and position_offset != Vector(0,0):
            component.offset = position_offset
        if layer == -1:
            component.layer = self.layer
        else:
            component.layer = layer

        if component.right() > self.right():
            self.size.x = component.size.x
        if component.bottom() > self.bottom():
            self.size.y = component.size.y
        self.components.append(component)

    def removeComponent(self, component):
        self.components.remove(component)
        # match component:
        #     case HitBox():
        #         self.components["Hitboxes"].remove(component)
        #     case Position2D():
        #         self.components["Positions"].remove(component)
        #     case Sprite():
        #         self.components["Sprites"].remove(component)
        #     case Dummy():
        #         self.components["Dummies"].remove(component)

    def updatePositions(self):
        for component in self.components:
            component.position = self.position + component.offset

    def fixedUpdate(self):
        super().fixedUpdate()

        for component in self.components:
            if not isinstance(component, Dummy):
                continue
            component.position = self.position + component.offset
            component.fixedUpdate()

    def render(self, camera=True):
        super().render()
        for component in self.components:
            if not isinstance(component, Dummy):
                continue
            if not component.isVisible():
                continue
            component.render(camera)

    def activate(self):
        super().activate()
        for comp in self.components:
            comp.activate()

    def deactivate(self):
        super().deactivate()
        for comp in self.components:
            comp.deactivate()

    def hide(self):
        super().hide()
        for comp in self.components:
            comp.hide()

    def show(self):
        super().show()
        for comp in self.components:
            comp.show()