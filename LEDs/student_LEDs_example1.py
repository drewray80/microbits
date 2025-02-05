# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
     for i in range(5):
        for j in range(5):
             display.set_pixel(j,i,9)
        sleep(75)
        display.clear()