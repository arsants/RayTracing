class Geometry:
    def __init__(self, material, objectId=0):
        self.objectId = objectId
        self.material = material
        self.type = "Geometry"

    def getObjectId(self):
        return self.objectId

    def getType(self):
        return self.type
