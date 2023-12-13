from machine import Pin
from neopixel import NeoPixel
import time
import random

ring = NeoPixel(Pin(2), 12)

ring.fill((0,0,0))
ring.write()
time.sleep(1)

while True:
    colour = [random.randint(0, 255) for i in range(3)]
    
    for i in range(len(ring)):
        ring[i] = colour
        ring.write()
        
        time.sleep(0.1)
        
        ring.fill((0,0,0))
        ring.write()