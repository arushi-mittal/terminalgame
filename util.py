import time, copy, colorama
from colorama import Fore, Back, Style
from ball import ball
from paddle import paddle
from board import Grid
from bricks import bricks
from input import input_to
from timer import timer
from globalvars import clock, score
from life import life
from scoreboard import scoreboard
from powerup import powerups
colorama.init()


def gameOver ():
    if life.value <= 0:
        return 1
    checkBricks = []
    for brick in bricks:
        if brick.type != 4 and brick.strength > 0:
            checkBricks.append(brick)
    if len(checkBricks) == 0:
        return 1

    return 0

def display () :
    display_array = copy.deepcopy(Grid.display)
    print("\033[H\033[J", end="")
    display_array = paddle.display(display_array)
    ball_array = ball.display(display_array)
    brick_array = []
    for brick in bricks:
        if brick.strength == 0:
            continue
        brick_array.append(brick.display(display_array))
    powerup_array = []
    for powerup in powerups:
        if powerup.active == True and powerup.used == False and powerup.currentTime < powerup.endTime:
            powerup.currentTime = powerup.currentTime + 0.01
            powerup.move(ball)
            powerup_array.append(powerup.display(display_array))
    life_array = life.display(display_array)
    time_array = timer.display(display_array)
    score_array = scoreboard.display(display_array)
    display_array = ''.join(display_array)
    display_array = ''.join(ball_array)

    if powerup_array != None:
        for powerup in powerup_array:
            display_array = ''.join(powerup)
    if brick_array != None:
        for brick in brick_array:
            display_array = ''.join(brick)
    display_array = ''.join(life_array)
    display_array = ''.join(time_array)
    display_array = ''.join(score_array)
    return display_array

def reset (ball, paddle, bricks) :
    time.sleep(3)
    global clock
    clock = clock + 0.01
    paddle.xpos = 75
    paddle.ypos = 44
    ball.ypos = paddle.ypos - 1
    ball.moveWithPaddle(paddle)
    while True:
        display_array = display()
        print(display_array)
        time.sleep(0.01)
        inputvalue = input_to()
        if (inputvalue == "a") :
            paddle.move(-1)
            ball.moveWithPaddle(paddle)
        elif (inputvalue == "d") :
            paddle.move(1)
            ball.moveWithPaddle(paddle)
        elif (inputvalue == "q") :
            break
        elif (inputvalue == " ") :
            ball.paddleCollision(paddle)
            gameLoop()
            break



def gameLoop ():
    while (True) :
        if gameOver():
            break
        global clock
        display_array = display()

        print(display_array)
        time.sleep(0.01)
        clock = clock + 0.01
        timer.setTime(clock)
        ball.paddleCollision(paddle)
        ball.brickCollision(bricks, scoreboard)
        if not ball.move() :
            life.decrease()
            if life.value <= 0:
                break
            reset(ball, paddle, bricks)
        inputvalue = input_to()
        if (inputvalue == "a") :
            paddle.move(-2)
        elif (inputvalue == "d") :
            paddle.move(2)
        elif (inputvalue == "q") :
            break

def gameStart ():
    while True:
        display_array = display()
        print(display_array)
        time.sleep(0.01)
        inputvalue = input_to()
        if (inputvalue == "a") :
            paddle.move(-1)
            ball.moveWithPaddle(paddle)
        elif (inputvalue == "d") :
            paddle.move(1)
            ball.moveWithPaddle(paddle)
        elif (inputvalue == "q") :
            break
        elif (inputvalue == " ") :
            ball.paddleCollision(paddle)
            gameLoop()
            break


#Iterate through all powerups whenever there is a collision of ball and brick and if powerup exists release

#Pass powerups as parameter to brick and trigger release 