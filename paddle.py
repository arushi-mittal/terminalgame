from colorama import Fore, Back, Style
from globalvars import rows, columns


class Paddle:
    def __init__(self):
        self.xpos = 75
        self.ypos = 44
        self.color = Back.BLUE
        self.symbol = " "
        self.length = 10
        self.velocityx = 0
        self.velocityy = 0

    def display (self, arr):
        ypos = self.ypos
        xpos = self.xpos
        length = self.length
        color = self.color
        symbol = self.symbol
        arr[ypos] = arr[ypos][:xpos] + color + symbol*length + Fore.RESET + Back.RESET + arr[ypos][xpos + length:]
        return arr

    def move (self, xvelocity):
        if (self.xpos + xvelocity >= (columns - self.length)) :
            self.xpos = columns - self.length

        elif (self.xpos + xvelocity <= 0) :
            self.xpos = 0
        else:
            self.xpos = self.xpos + xvelocity

    def expand (self):
        paddle.length = 20
    def shrink (self):
        paddle.length = 6

    def reset (self):
        paddle.length = 10

paddle = Paddle()