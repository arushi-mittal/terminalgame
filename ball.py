from globalvars import score, clock
from paddle import paddle
from powerup import powerups

class Ball:
    def __init__(self):
        self.symbol = u'\u2B24'
        self.xpos = paddle.xpos + paddle.length//2 - 1
        self.ypos = 43
        self.xvelocity = 0
        self.yvelocity = 0
    def display (self, arr) :
        ypos = self.ypos
        xpos = self.xpos
        symbol = self.symbol
        arr[ypos] = arr[ypos][:xpos] + symbol + arr[ypos][xpos + 1:]
        return arr
    def moveWithPaddle (self, paddle):
        self.xpos = paddle.xpos + (paddle.length//2) - 1
    def paddleCollision (self, paddle) :
        xpos = self.xpos
        ypos = self.ypos
        if (ypos == paddle.ypos - 1) :
            if xpos == paddle.xpos + (paddle.length/2) - 1:
                self.xvelocity = self.xvelocity
                self.yvelocity = -1
            elif (xpos >= paddle.xpos and xpos <= paddle.xpos + (paddle.length / 2) ) :
                self.xvelocity = self.xvelocity - 1
                self.yvelocity = -1
            elif (xpos <= (paddle.xpos + paddle.length) and xpos >= paddle.xpos + (paddle.length / 2) ) :
                self.xvelocity = self.xvelocity + 1
                self.yvelocity = -1
            
    def move (self) :
        if self.ypos > 43:
            return 0
        elif self.ypos <= 5:
            self.yvelocity = 1
        if self.xpos <= 1:
            self.xvelocity = -1 * self.xvelocity
        elif self.xpos >= 164:
            self.xvelocity = -1 * self.xvelocity
        self.ypos = self.ypos + self.yvelocity
        self.xpos = self.xpos + self.xvelocity
        return 1
    
    def brickCollision (self, bricks, scoreboard):
        xpos = self.xpos
        ypos = self.ypos
        for brick in bricks:
            if brick.strength != 0:

                if brick.ypos == ypos + 1:
                    if brick.xpos <= xpos and brick.xpos + brick.length >= xpos:
                        self.yvelocity = -1 * self.yvelocity
                        brick.damage(1)
                        if brick.type == 0:
                            scoreboard.setScore(scoreboard.score + 10)
                        elif brick.type == 1:
                            scoreboard.setScore(scoreboard.score + 10 * brick.strength + 5)
                        elif brick.type == 2:
                            scoreboard.setScore(scoreboard.score + 15 * brick.strength + 5)
                        if brick.powerups != "" and brick.strength == 0:
                            powerups[brick.powerups].active = True
                            powerups[brick.powerups].move(self)
                            powerups[brick.powerups].startTime = clock
                            powerups[brick.powerups].endTime = clock + 100
                            powerups[brick.powerups].currentTime = clock
                        
                            
                elif brick.ypos == ypos - 1:
                    if brick.xpos <= xpos and brick.xpos + brick.length >= xpos:
                        self.yvelocity = -1 * self.yvelocity
                        brick.damage(1)
                        if brick.type == 0:
                            scoreboard.setScore(scoreboard.score + 10)
                        elif brick.type == 1:
                            scoreboard.setScore(scoreboard.score + 10 * brick.strength + 5)
                        elif brick.type == 2:
                            scoreboard.setScore(scoreboard.score + 15 * brick.strength + 5)
                        if brick.powerups != "" and brick.strength == 0:
                            powerups[brick.powerups].active = True
                            powerups[brick.powerups].move(self)
                            powerups[brick.powerups].startTime = clock
                            powerups[brick.powerups].endTime = clock + 100
                            powerups[brick.powerups].currentTime = clock
                if brick.ypos == ypos:
                    if xpos + 1 == brick.xpos:
                        self.xvelocity = -1 * self.xvelocity
                        if self.xvelocity == 0:
                            self.xvelocity = -1
                        brick.damage(1)
                        if brick.type == 0:
                            scoreboard.setScore(scoreboard.score + 10)
                        elif brick.type == 1:
                            scoreboard.setScore(scoreboard.score + 10 * brick.strength + 5)
                        elif brick.type == 2:
                            scoreboard.setScore(scoreboard.score + 15 * brick.strength + 5)
                        if brick.powerups != "" and brick.strength == 0:
                            powerups[brick.powerups].active = True
                            powerups[brick.powerups].move(self)
                            powerups[brick.powerups].startTime = clock
                            powerups[brick.powerups].endTime = clock + 100
                            powerups[brick.powerups].currentTime = clock
                    elif  xpos == brick.xpos + brick.length:
                        self.xvelocity = -1 * self.xvelocity
                        if self.xvelocity == 0:
                            self.xvelocity = 1
                        brick.damage(1)
                        if brick.type == 0:
                            scoreboard.setScore(scoreboard.score + 10)
                        elif brick.type == 1:
                            scoreboard.setScore(scoreboard.score + 10 * brick.strength + 5)
                        elif brick.type == 2:
                            scoreboard.setScore(scoreboard.score + 15 * brick.strength + 5)
                        if brick.powerups != "" and brick.strength == 0:
                            powerups[brick.powerups].active = True
                            powerups[brick.powerups].move(self)
                            powerups[brick.powerups].startTime = clock
                            powerups[brick.powerups].endTime = clock + 100
                            powerups[brick.powerups].currentTime = clock


    def fast (self):
        self.yvelocity = self.yvelocity * 2

    # def collide ():

        


ball = Ball()