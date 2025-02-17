# Imports go at the top
from microbit import *
import sphero

# Code in a 'while True:' loop repeats forever
while True:
    if display.read_light_level() < 20:
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.RIGHT_HEADLIGHT,255,255,255)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.LEFT_HEADLIGHT,255,255,255)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.RIGHT_BRAKELIGHT,255,0,0)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.LEFT_BRAKELIGHT,255,0,0)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.LEFT_STATUS,134,1,175)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.RIGHT_STATUS,134,1,175)
    else:
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.RIGHT_HEADLIGHT,0,0,0)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.LEFT_HEADLIGHT,0,0,0)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.RIGHT_BRAKELIGHT,0,0,0)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.LEFT_BRAKELIGHT,0,0,0)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.LEFT_STATUS,134,1,175)
        sphero.RVRLed.set_rgb_led_by_index(sphero.LEDs.RIGHT_STATUS,134,1,175)
