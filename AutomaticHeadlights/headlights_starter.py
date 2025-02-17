# Imports go at the top
from microbit import *
import sphero

# Code in a 'while True:' loop repeats forever
while True:
    sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.RIGHT_HEADLIGHT,255,0,0)

# I also show students that we can explicitly import the classes that we need. 
# This lets us call the classes directly without needing sphero. in fromt of all of our functions. 

# from microbit import *
# from sphero import RVRLed, LEDs

# # Code in a 'while True:' loop repeats forever
# while True:
#     RVRLed.set_rgb_led_by_index(LEDs.RIGHT_HEADLIGHT,255,0,0)
