class Area():
    sizeType = ((2, 8), (2, 3))
    def __init__(self, size:tuple, ):
        if size[0] in range(self.sizeType[0]):
            if size[1] in range(self.sizeType[1]):
                self.size = size
        elif size[1] in range(self.sizeType[0]):
            if size[0] in range(self.sizeType[1]):
                self.size = size
        if not self.size:
            raise ValueError("Invalid size")