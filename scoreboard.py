class Scoreboard: 
    def __init__ (self):
        self.xpos = 74
        self.ypos = 3
        self.score = 0
    def setScore (self, score):
        self.score =  score
    def display (self, arr) :
        ypos = self.ypos
        xpos = self.xpos
        arr[ypos] = arr[ypos][:xpos] + str(self.score) + arr[ypos][xpos + 1:]
        return arr

scoreboard = Scoreboard()