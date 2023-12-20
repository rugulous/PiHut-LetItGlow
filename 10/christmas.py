from machine import Pin
from neopixel import NeoPixel
import time

RED = (255, 0, 0)
GREEN = (0, 255, 0)

strand = NeoPixel(Pin(2), 15)

strand.fill((0, 0, 0))
strand.write()

colours = list((RED, GREEN))

while True:
    for led in range(len(strand)):
        if led % 2 == 0:
            strand[led] = colours[0]
        else:
            strand[led] = colours[1]
        
    strand.write()
    
    c = colours.pop(0)
    colours.append(c)
    time.sleep(0.25)
