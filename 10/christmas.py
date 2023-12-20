from machine import Pin
from neopixel import NeoPixel

RED = (255, 0, 0)
GREEN = (0, 255, 0)

strand = NeoPixel(Pin(2), 15)

strand.fill((0, 0, 0))
strand.write()

for led in range(len(strand)):
    if led % 2 == 0:
        strand[led] = GREEN
    else:
        strand[led] = RED
        
strand.write()
