# Imports go at the top
from microbit import *
import music

#variable num = 0
num = 0

# Code in a 'while True:' loop repeats forever
while True:
    #plays music during leds
    music.play(music.PRELUDE, wait=False)
    
    #loops lights through a duo x
    for x in range(5):
        for y in range(5):
            display.set_pixel(y,x,9)
            display.set_pixel(x,y,9)
            sleep(150)
            display.clear()

    #loops lights through chase
    for x in range(5):
        for y in range(5):
            for b in range(5,10):
                display.set_pixel(x,x,b)
                display.set_pixel(y,y,b)
            sleep(150)
            display.clear()
            
    #adds 1 to num, breaks loop once num = 2
    num += 1
    if num == 2:
        #scrolls words & plays music
        display.scroll('done')
        music.play(music.POWER_DOWN)
        break

