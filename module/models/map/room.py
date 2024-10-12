import json, os

class Room( ):
    def __init__(self, type:str, itemIdList:list, sizeMatrix:tuple, furniture:list=None, passivePersone:list=None):
        self.matrix = [[sizeMatrix[1]]]
        self.type = type
        self.furniture = furniture
        self.passivePersone = passivePersone
        self.itemIdList = itemIdList
        self.activePerson = []
        for i in range(sizeMatrix[0]):
            self.matrix.append()
        self.saveMatrix()

    def wallMatrixCreare(self, wallSize:tuple):
        self.wallMatrix = [wallSize[1]]
        for i in range(wallSize[0]):
            self.wallMatrix.append()
        # TODO Finalize wall Matrix

    def moveFurniture(self):
        pass
    # TODO MORE FINALIZE WORK!!!

class OldRoom(Room):
    def furnitureMatrix(self):
        pass
    # TODO Write this
    # Old room auto move in create.