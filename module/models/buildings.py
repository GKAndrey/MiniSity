from .room import *

class Building():
    def __init__(self, size:tuple, floor:int):
        self.size = size
        self.floor = floor
        self.rooms = []
    def roomsMove(self,):
        pass
    # TODO: Create script: create rooms, wall and standart

class Home(Building):
    pass