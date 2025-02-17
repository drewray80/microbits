# Imports go at the top
from microbit import *
import random
import music
import time

set_volume(100)

while True:
    if pin_logo.is_touched():
        
        player_x = random.randint(0,4)
        player_y = random.randint(0,4)
        
        food_x = random.randint(0,4)
        food_y = random.randint(0,4)
        
        enemy_x = random.randint(0,4)
        enemy_y = random.randint(0,4)
        enemy_cooldown = 0
        
        score = 0
        
        while True:
        
            display.set_pixel(food_x, food_y, 5)
            
            x_strength = accelerometer.get_x()
            if player_x < 4 and x_strength > 100:
                player_x += 1
            elif player_x > 0 and x_strength < -100:
                player_x -= 1 
            
            y_strength = accelerometer.get_y()
            if player_y < 4 and y_strength > 75:
                player_y += 1
            elif player_y > 0 and y_strength < -200:
                player_y -= 1 
            display.set_pixel(player_x, player_y ,7)
        
            if (player_x, player_y) == (food_x, food_y):
                music.play(['e'])
                plus_one = Image("00005:05005:55505:05005:00005")
                display.show(plus_one, delay=200)
                score +=1
                food_x = random.randint(0,4)
                food_y = random.randint(0,4)
            
            if (player_x, player_y) == (enemy_x, enemy_y):
                    display.clear()
                    break

            if score < 2:
                enemy_cooldown += 0.5
            elif score >=2:
                enemy_cooldown += 1
            elif score > 3:
                enemy_cooldown += 2
            if enemy_cooldown >=3:
                
                if player_x > enemy_x:
                    enemy_x += 1
                elif player_x < enemy_x:
                    enemy_x -= 1
                if player_y > enemy_y:
                    enemy_y += 1
                elif player_y < enemy_y:
                    enemy_y -= 1
                enemy_cooldown = 0

            for i in range(2):
                display.set_pixel(enemy_x, enemy_y, 0)
                time.sleep(.01)
                display.set_pixel(enemy_x, enemy_y, 4)
            
            time.sleep(.5)
        
            display.clear()
        
        audio.play(Sound.YAWN)
        display.scroll('GAME OVER SCORE:', delay=75)
        display.scroll(str(score))
    if button_a.is_pressed() and button_b.is_pressed():
        break

    
    
    