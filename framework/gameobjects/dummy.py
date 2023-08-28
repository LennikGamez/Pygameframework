class Dummy:
    def __init__(self) -> None:
        self._active = True
        self._visible = True
        self.delete_request = False

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
