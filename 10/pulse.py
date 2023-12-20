from machine import Pin
from neopixel import NeoPixel
import time

strand = NeoPixel(Pin(2), 15)

strand.fill((10,0,0))
strand.write()
time.sleep(1)

while True:
    for led in range(len(strand)):
        for i in range(255, 10, -1):
            strand[led] = (i, 0, 0)
            strand.write()
            time.sleep(0.001)