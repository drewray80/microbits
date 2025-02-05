# Imports go at the top
from microbit import *
import random
import music

pattern = []

# Code in a 'while True:' loop repeats forever
while True:
    sleep(500)
    letter = random.choice(['A','B'])
    pattern.append(letter)
    
    for i in pattern:
        sleep(200)
        if i == 'A':
            
            display.show(Image('99900:'
                               '99900:'
                               '99900:'
                               '99900:'
                               '99900'))
            music.play('a:1')
            sleep(200)
            display.clear()
        if i == 'B':
            display.show(Image('00999:'
                               '00999:'
                               '00999:'
                               '00999:'
                               '00999'))
            music.play('b:1')
            sleep(200)
            display.clear()
            
    
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




        