# Imports
import time
from machine import Pin
from neopixel import NeoPixel

grb_led_1 = NeoPixel(Pin(2), 1)
grb_led_2 = NeoPixel(Pin(5), 1)
black = (0,0,0)

grb_led_1.fill(black)
grb_led_1.write()

grb_led_2.fill(black)
grb_led_2.write()

while True:
    for i in range(255):
        grb_led_1.fill((i,0,0))
        grb_led_1.write()
        time.sleep(0.005)
    
    grb_led_1.fill(black)
    grb_led_1.write()
    
    for i in reversed (range(255)): 
        grb_led_2.fill((i,0,0))
        grb_led_2.write()
        time.sleep(0.005)