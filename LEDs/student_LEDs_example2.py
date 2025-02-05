# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    for y in range(5):
        for x in range(5):
            for b in range(9):
                display.set_pixel(x,y,b)
                sleep(50)
    for y in range(5):
        for x in range(5):
             for b in range(9):
                display.set_pixel(y,x,b)
                sleep(50)
    ...