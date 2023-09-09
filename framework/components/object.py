from .position import Position2D
from .dummy import Dummy
from .hitbox import HitBox
from .sprite import Sprite
from .. import Vector


class Object(Position2D):
    def __init__(self, position):
        super().__init__(position)

        self.components: list = []
    def addComponent(self, component, position_offset = Vector()):
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
        component.offset = position_offset
        print(component.right(), self.right())
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
            component.render(camera)

    def deactivate(self):
        super().deactivate()
        for component in self.components:
            component.deactivate()

    def activate(self):
        super().activate()
        for component in self.components:
            component.activate()

    def show(self):
        super().show()
        for component in self.components:
            component.show()

    def hide(self):
        super().hide()
        for component in self.components:
            component.hide()