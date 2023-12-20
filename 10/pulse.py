from machine import Pin
from neopixel import NeoPixel
import time

strand = NeoPixel(Pin(2), 15)

strand.fill((10,0,0))
strand.write()
time.sleep(1)

while True:
    for i in range(3):
        colour = list()
        for n in range(3):
            if n == i:
                colour.append(10)
            else:
                colour.append(0)
        
    
        for led in range(len(strand)):
            for c in range(255, 10, -1):
                colour[i] = c
                strand[led] = colour
                strand.write()
                time.sleep(0.001)
