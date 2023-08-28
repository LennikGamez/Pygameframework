

class GroupManager:
    __groups = {

    }

    @staticmethod
    def getGroup(name):
        return GroupManager.__groups.get(name)

    @staticmethod
    def addToGroup(name, *objs):
        if name in GroupManager.__groups.keys():
            GroupManager.__groups[name].extend(objs)
        else:
            GroupManager.__groups[name] = [*objs]

    @staticmethod
    def removeFromGroup(name, *objs):
        list(map(lambda obj: GroupManager.__groups[name].remove(obj), objs))

    @staticmethod
    def objInGroup(obj, name):
        return obj in GroupManager.__groups[name]
