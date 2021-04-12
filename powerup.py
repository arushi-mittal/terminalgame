from colorama import Back, Fore
from input import input_to
# from util import reset

class Powerup:
    def __init__ (self, ptype, color, symbol, xpos, ypos) :
        self.xpos = xpos
        self.ypos = ypos
        self.ptype = ptype
        self.color = color
        self.symbol = symbol
        self.active = False
        self.used = False
        self.startTime = None
        self.endTime = None
        self.currentTime = None
    def display (self, arr):
        arr[self.ypos] = arr[self.ypos][:self.xpos] + self.color + self.symbol + Fore.RESET + Back.RESET + arr[self.ypos][self.xpos + 1:]
        return arr
    def move (self, ball):
        self.ypos = self.ypos + 1
        if self.xpos <= ball.xpos:
            self.xpos = self.xpos + 1
        else:
            self.xpos = self.xpos - 1   
        if self.ypos > 43:
            self.used = True
            self.active = False
        if self.xpos <= 1:
            self.xvelocity = -1 * self.xvelocity
        elif self.xpos >= 164:
            self.xvelocity = -1 * self.xvelocity


class Fast (Powerup):
    def __init__(self, xpos, ypos):
        super(Fast, self).__init__(0, Back.BLACK + Fore.RED, "$", xpos, ypos)

    def use (self, ball):
        ball.fast()

class Expand (Powerup):
    def __init__(self, xpos, ypos):
        super(Expand, self).__init__(1, Back.BLACK + Fore.RED, "@", xpos, ypos)
    def use (self,paddle):
        paddle.expand()
class Shrink (Powerup):
    def __init__(self, xpos, ypos):
        super(Shrink, self).__init__(2, Back.BLACK + Fore.RED, "&", xpos, ypos)
    def use (self, paddle):
        paddle.shrink()

class Thru (Powerup):
    def __init__(self, xpos, ypos):
        super(Thru, self).__init__(3, Back.BLACK + Fore.RED, "%", xpos, ypos)
    def use (self, ball):
        ball.collide()
class Multi (Powerup):
    def __init__(self, xpos, ypos):
        super(Multi, self).__init__(4, Back.BLACK + Fore.RED, "#", xpos, ypos)

class Attach (Powerup):
    def __init__(self, xpos, ypos):
        super(Attach, self).__init__(5, Back.BLACK + Fore.RED, "=", xpos, ypos)



def setPowerups ():
    powerups = []
    powerups.append(Fast(116, 7))
    powerups.append(Expand(80, 7))

    powerups.append(Shrink(38, 9))
    powerups.append(Thru(108, 9))

    powerups.append(Multi(78, 11))
    powerups.append(Attach(134,11))

    return tuple(powerups)
powerups = setPowerups()



# def setBricks ():
#     bricks = []
#     i = 150
#     while (i > 0):
#         bricks.append(lowBrick(i, 7))
#         i = i - 12

#     i = 154
#     while (i > 0):
#         bricks.append(medBrick(i, 9))
#         i = i - 10

#     i = 156
#     while (i > 0):
#         bricks.append(highBrick(i, 11))
#         i = i - 8

#     i = 150
#     while (i > 0):
#         bricks.append(lowBrick(i, 15))
#         i = i - 12

#     return bricks

# bricksSet = setBricks()

# bricks = tuple(bricksSet)  

powerups = setPowerups()
