class Sity():
    def __init__(self, size:tuple, type:int, name:str='New Sity'):
        self.name = name
        if type in [1,2]:
            self.type = type
        # else:
        #     raise ValueError('Invalid sity type. Type must be 1 for city or 2 for village.')
        self.matrix = self.createMatrixSity(size)
    def createMatrixSity(self, size:tuple):
        matrix = []
        for i in range(size[0]):
            for o in range(size[1]):
                matrix.append([(i, o)])
        return matrix
        # self.buildings = []
        # self.population = 0
    def __str__(self):
        return f'Sity: {self.name}, Type: {self.type}, Size: {self.matrix}'