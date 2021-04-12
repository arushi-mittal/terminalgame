from colorama import Back, Fore
from powerup import powerups

class Brick:
    def __init__(self, xpos, ypos, strength, color, powerups, length, brickType):
        self.xpos = xpos
        self.ypos = ypos
        self.strength = strength
        self.color = color
        self.powerups = powerups
        self.symbol = " "
        self.length = length
        self.type = brickType

    def display (self, arr): 
        xpos = self.xpos
        ypos = self.ypos
        color = self.color
        symbol = self.symbol
        length = self.length

        if self.strength == 1:
            color = Back.YELLOW
        elif self.strength == 2:
            color = Back.GREEN
        elif self.strength == 3:
            color = Back.RED
        elif self.strength > 3:
            color = Back.MAGENTA

        arr[ypos] = arr[ypos][:xpos] + color + symbol*length + Back.RESET + arr[ypos][xpos + length:]
        return arr

    
    def damage (self, damageval):
        self.strength = self.strength - 1

        # if self.strength == 1:
        #     self.color = Back.YELLOW
        # elif self.strength == 2:
        #     self.color = Back.GREEN
        # elif self.strength == 3:
        #     self.color = Back.RED

class lowBrick (Brick):
    def __init__(self, xpos, ypos, powerups=""):
        self.xpos = xpos
        self.ypos = ypos
        self.powerups = powerups
        self.points = 10
        self.strength = 1
        self.color = Back.YELLOW
        super(lowBrick, self).__init__(xpos, ypos, self.strength, self.color, powerups, 10, 0)
    


class medBrick (Brick):
    def __init__(self, xpos, ypos, powerups=""):
        self.xpos = xpos
        self.ypos = ypos
        self.powerups = powerups
        self.points = 20
        self.strength = 2
        self.color = Back.GREEN
        super(medBrick, self).__init__(self.xpos, self.ypos, self.strength, self.color, powerups, 8, 1)
    

class highBrick (Brick):
    def __init__(self, xpos, ypos, powerups=""):
        self.xpos = xpos
        self.ypos = ypos
        self.powerups = powerups
        self.points = 50
        self.strength = 3
        self.color = Back.RED
        super(highBrick, self).__init__(self.xpos, self.ypos, self.strength, self.color, powerups, 6, 2)
    
class unbreakableBrick (Brick):
    def __init__(self, xpos, ypos, powerups=""):
        self.xpos = xpos
        self.ypos = ypos
        self.powerups = powerups
        self.strength = 1000
        self.color = Back.MAGENTA
        super(unbreakableBrick, self).__init__(self.xpos, self.ypos, self.strength, self.color, powerups, 12, 3)  

    def damage (self, damageval):
        self.strength = 1000
    
def setBricks ():
    bricks = []
    i = 150
    while (i > 0):
        bricks.append(lowBrick(i, 7))
        i = i - 12

    i = 154
    while (i > 0):
        bricks.append(medBrick(i, 9))
        i = i - 10

    i = 156
    while (i > 0):
        bricks.append(highBrick(i, 11))
        i = i - 8

    i = 150
    while (i > 0):
        bricks.append(lowBrick(i, 15))
        i = i - 12
    
    i = 148
    while (i > 100):
        bricks.append(unbreakableBrick(i, 17))
        i = i - 14

    i = 44
    while (i > 0):
        bricks.append(unbreakableBrick(i, 17))
        i = i - 14

    return bricks

bricksSet = setBricks()

for brick in bricksSet:
    xpos = brick.xpos
    ypos = brick.ypos
    for i in range(len(powerups)):
        if powerups[i].xpos >= xpos and powerups[i].xpos <= xpos + brick.length and powerups[i].ypos == ypos:
            brick.powerups = i


bricks = tuple(bricksSet)  