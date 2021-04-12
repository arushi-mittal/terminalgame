class Life:
    def __init__(self):
        self.xpos = 3
        self.ypos = 3
        self.value = 3
        self.symbol = u'\u2764'
    def decrease(self):
        self.value = self.value - 1
    def display (self, arr):
        ypos = self.ypos
        xpos = self.xpos
        symbol = self.symbol
        arr[ypos] = arr[ypos][:xpos] + (symbol + " ") * self.value + arr[ypos][xpos + 2*self.value:]
        return arr

life = Life()