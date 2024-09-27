import json, os

class Room():
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

    def saveMatrix(self):
        with open(os.path.abspath(), 'w', encoding='utf-8') as file:
            json.dump(self.matrix, file, ensure_ascii=False, indent=4)

class OldRoom(Room):
    def furnitureMatrix(self):
        pass
    # TODO Write this