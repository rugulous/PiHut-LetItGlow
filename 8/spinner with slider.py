from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

READING_MULTIPLIER = (255 / 65535)

ring = NeoPixel(Pin(2), 12)
slider = ADC(Pin(28))

ring.fill((0,0,0))
ring.write()
time.sleep(1)

while True:
    intensity = round(slider.read_u16() * READING_MULTIPLIER)
    colour = [random.randint(1, intensity) for i in range(3)]
    
    for i in range(len(ring)):
        ring[i] = colour
        ring.write()
        time.sleep(0.1)
        
    for i in range(len(ring)):
        ring[i] = (0, 0, 0)
        ring.write()
        time.sleep(0.1)
