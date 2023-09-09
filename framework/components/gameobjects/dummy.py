from framework.groupmanager import GroupManager as gm
class Dummy:
    def __init__(self) -> None:
        self._active = False
        self._visible = False
        self.delete_request = False
        self.layer = 0

    def inGroup(self, groupname):
        return gm.objInGroup(self, groupname)

    def isActive(self):
        return self._active

    def isVisible(self):
        return self._visible

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def show(self):
        self._visible = True

    def hide(self):
        self._visible = False

    def render(self):
        pass

    def update(self):
        pass

    def fixedUpdate(self):
        pass

    def delete(self):
        self.delete_request = True
