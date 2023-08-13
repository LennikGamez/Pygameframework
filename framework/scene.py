
class Scene:
    def __init__(self, *objs) -> None:
        self.game_objects = []
        self.game_objects += (list(objs))
        
    def update(self):
        for obj in self.game_objects:
            if obj.visible:
                obj.render()
            if obj.active():
                obj.fix_update()
                obj.update()
        self.checkCollisions()

    def addObject(self, obj):
        self.game_objects.append(obj)

    def addObjects(self, *objs):
        self.game_objects.append(*objs)

    def removeObject(self, obj):
        self.game_objects.remove(obj)

    def popObject(self, index):
        return self.game_objects.pop(index)

    def selectObject(self, index):
        try:
            return self.game_objects[index]
        except IndexError:
            raise Exception(f"This index is out of range! INDEX: {index}; MAXINDEX: {len(self.game_objects)-1}")
        
    def checkCollisions(self):
        pass