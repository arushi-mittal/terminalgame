# **TERMINAL BRICK BREAKER**

## **Overview**

Terminal brickbreaker is a terminal version of the popular brick breaker arcade game which involves using Python3 and basic libraries to implenent it.

## **Concepts**

It uses various concepts from Object Oriented Programming such as:

Polymorphism: Some of the methods perform different functions for different classes and some functions are overwritten by subclasses. Eg: Display, move and damage.

Abstraction: All the methods for each object define the function but the exact functionality is hidden from the users and can be used as the user wants as long as the correct parameters are supplied.

Encapsulation: Class and object based approach for every element. Every element such as ball, paddle, brick, board, etc. is a class and has the required objects to implement the functionality.

Inheritance: Classes that import from other super classes because they have some common attributes. Eg: Bricks, powerups.

## **Running Instructions**

```bash
$ pip3 install -r requirements.txt
$ python3 main.py
```

## **Controls**

Use a to move paddle left and d to move paddle right. Use space to launch ball and q to quit game. Ball can be launched only during the paddle attach powerup and during the start of each game or when a life is lost.

## **Scoring**

Scoring is assigned differently for each type of brick depending on the present strength of that brick. Low Level bricks are worth 10 points, medium level bricks give 10 X strength + 5 points for each hit and high level bricks give 10 X strength + 5 points for each hit.

## **Lives**

There are three lives at the beginning of each game and whenever a life is lost the game resets.
