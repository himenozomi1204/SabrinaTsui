"""
File: Steeplechase.py
Name: Sabrina Tsui
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()



def jump():
    """
    Pre-condition: Karel is on the left, facing east.
    Post-condition: Karel is on the right.
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition: Karel is on the left, facing east.
    Post-condition: Karel is on the upper left, facing north.
    """
    turn_left()
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """
    Pre-condition: Karel is on the upper left, facing north.
    Post-condition: Karel is on the upper right, facing south.
    """
    turn_right()
    move()
    turn_right()


def down():
    while front_is_clear():
        move()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
