# Imports go at the top
from microbit import *
import music
import random 
#The reason that my code is creative is because it uses a plethora of other topics
#that we used in class to make more flashy light patterns then what ould be created 
#with what we just learned in that lesson the first part using if statments
#the bottom part using random commands



# Code in a 'while True:' loop repeats forever
funky = 0
while True:
    #causes this set of lights to loop twice
    for a in range(2):
       for b in range(10):
           if not b  % 5 == 0:
                continue
           else:     
               music.play(music.CHASE, wait=False)
               for x in range(5) :
                   for y in range(5):
                       display.set_pixel(y,x,b)
                       display.set_pixel(x,y,9)
                       sleep(50)
                       #makes the part that was bright in the first part a lower brightness
                       if funky == 1:
                           funky = 0
                           continue
                       else:
                           funky += 1
               display.clear()
               sleep(10)
       display.clear()
       #makes lines go across the screen
       for x in range(5):
           for y in range(5):
               display.set_pixel(y,x,9)
               sleep(60)
               display.clear
        #darkens the lines
       for x in range(5):
           for y in range(5):
               display.set_pixel(x,y,6)
               display.clear
               sleep(50)
    display.clear()
    #creates a pattern i dont know how to explain
    for x in range(5):
       for y in range(5):
           c=random.randint(0,9)
           display.set_pixel(y,x,c)
           display.set_pixel(x,y,c)
           display.set_pixel(x,1,c)
           display.set_pixel(y,1,c)
           sleep(60)
       display.clear()
        #sets up so that the dissolve is easier to see
    for x in range(5):
        for y in range(5):
            display.set_pixel(x,y,9)
            sleep(50)
            #saposed to make a a pattern where it kind of dissolves
    for x in range(100):
        e=random.randint(0,4)
        y=random.randint(0,4)
        display.set_pixel(e,y,0)
        sleep(20)
            
            

           
            