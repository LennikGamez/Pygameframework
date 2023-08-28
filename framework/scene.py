class Scene:
    def __init__(self, *objs) -> None:
        self.game_objects = []
        self.game_objects += (list(objs))

    def update(self):
        new_game_objects = []
        for obj in self.game_objects:
            if obj.delete_request:
                self.deleteObject(obj)
                continue
            if obj.isVisible():
                obj.render()
            if obj.isActive():
                obj.fixedUpdate()
                obj.update()
            new_game_objects.append(obj)
        self.game_objects = new_game_objects

    def addObject(self, obj):
        self.game_objects.append(obj)

    def addObjects(self, *objs):
        self.game_objects.extend(*objs)

    def forceRemoveObject(self, obj):
        self.game_objects.remove(obj)

    def forcePopObject(self, index):
        return self.game_objects.pop(index)
    def popObject(self, index):
        obj = self.game_objects[index]
        obj.delete()
        return obj

    def selectObject(self, index):
        try:
            return self.game_objects[index]
        except IndexError:
            raise Exception(f"This index is out of range! INDEX: {index}; MAXINDEX: {len(self.game_objects) - 1}")

    def deleteObject(self, obj):
        obj.deactivate()
        obj.hide()
        obj.delete_request = False
