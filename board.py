from globalvars import rows, columns

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.display = []    
        self.display = [" " * (width - 1) + "\n" for i in range(height)]

Grid = Board(rows, columns)