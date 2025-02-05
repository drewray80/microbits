# Imports go at the top
from microbit import *
import random

# Code in a 'while True:' loop repeats forever
while True:
    answer = random.randint(0,6)
    if accelerometer.was_gesture('shake'):
        if answer == 0:
            display.scroll('yes')
        elif answer == 1:
            display.scroll('no')
        elif answer == 2:
            display.scroll('maybe')
        elif answer == 3:
            display.scroll('outcome uncertain')
        elif answer == 4:
            display.scroll('probably not')
        elif answer == 5:
            display.scroll('ask lucas')
  