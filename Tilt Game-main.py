# Imports go at the top
from microbit import *
import random
import music
import time

set_volume(100)

# Game Loop
while True:
    # Touching the logo button starts a round of play.
    if pin_logo.is_touched():
        # The player, food and enemy are randomly placed on the led board.
        player_x = random.randint(0,4)
        player_y = random.randint(0,4)
        
        food_x = random.randint(0,4)
        food_y = random.randint(0,4)
        
        enemy_x = random.randint(0,4)
        enemy_y = random.randint(0,4)
        enemy_cooldown = 0
        
        score = 0

        # Round Loop
        while True:
            # The food is displayed as a constant light at half brightness.  
            display.set_pixel(food_x, food_y, 5)

            # This moves the player on the board using the accelerometer sensor. 
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
                
            # This displays the player at 7 brightness. It is the brightest light.
            display.set_pixel(player_x, player_y ,7)

            # These detects if the player collided with the food.
            # Then it adds a point and moves the food to a new random location.
            if (player_x, player_y) == (food_x, food_y):
                music.play(['e'])
                plus_one = Image("00005:05005:55505:05005:00005")
                display.show(plus_one, delay=200)
                score +=1
                food_x = random.randint(0,4)
                food_y = random.randint(0,4)

            # This detects enemy collitions that ends the game.
            if (player_x, player_y) == (enemy_x, enemy_y):
                    display.clear()
                    break

            # This lets the enemy move faster as the player's score increases.
            if score < 2:
                enemy_cooldown += 0.5
            elif score >=2:
                enemy_cooldown += 1
            elif score > 3:
                enemy_cooldown += 2
            if enemy_cooldown >=3:

                # This moves the enemy closer to the player and restarts the cool down.
                if player_x > enemy_x:
                    enemy_x += 1
                elif player_x < enemy_x:
                    enemy_x -= 1
                if player_y > enemy_y:
                    enemy_y += 1
                elif player_y < enemy_y:
                    enemy_y -= 1
                enemy_cooldown = 0

            # This loop makes the enemy blink, so the player can identify it. 
            for i in range(2):
                display.set_pixel(enemy_x, enemy_y, 0)
                time.sleep(.01)
                display.set_pixel(enemy_x, enemy_y, 4)
            
            time.sleep(.5)
        
            display.clear()
        
        audio.play(Sound.YAWN)
        display.scroll('GAME OVER SCORE:', delay=75)
        display.scroll(str(score))
        
    # Pressing A and B together ends the game.
    if button_a.is_pressed() and button_b.is_pressed():
        break

    
    
    
