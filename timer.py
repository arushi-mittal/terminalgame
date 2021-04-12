class Timer: 
    def __init__ (self):
        self.xpos = 154
        self.ypos = 3
        self.timeValue = str(0)
    def setTime (self, timeValue):
        self.timeValue = timeValue
    def display (self, arr) :
        ypos = self.ypos
        xpos = self.xpos
        timeValue = str(self.timeValue * 10)
        arr[ypos] = arr[ypos][:xpos] + timeValue[:min(4, len(timeValue))] + arr[ypos][xpos + 1:]
        return arr

timer = Timer()