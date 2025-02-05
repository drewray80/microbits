# Imports go at the top
from microbit import *
import random
import music

pattern = []

# Code in a 'while True:' loop repeats forever
while True:
        
    letter = random.choice(['A','B'])
    pattern.append(letter)
    display.scroll("".join(pattern))
    sleep(1000)
    print(pattern)
    
    guess = []    
    while len(guess) != len(pattern):
        if button_a.was_pressed():
            guess.append('A')
            music.play('a:1')
        if button_b.was_pressed():
            guess.append('B')
            music.play('b:1')

    print(guess)
    
    if guess != pattern:
        display.show(Image.SKULL)
        sleep(400)
        music.play(music.DADADADUM)
        break




        