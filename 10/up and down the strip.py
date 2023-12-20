from machine import Pin
from neopixel import NeoPixel
import time
import random

strip = NeoPixel(Pin(2), 15)

strip.fill((0,0,0))
strip.write()
time.sleep(1)

while True:
    colour = [random.randint(0, 255) for i in range(3)]
    
    for i in range(len(strip)):
        strip[i] = colour
        strip.write()
        time.sleep(0.1)
        
    time.sleep(0.2)
        
    for i in range(len(strip) - 1, 0, -1):
        strip[i] = (0, 0, 0)
        strip.write()
        time.sleep(0.1)
