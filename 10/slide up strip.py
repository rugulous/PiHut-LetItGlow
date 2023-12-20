from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

LED_COUNT = 15
MAX_VAL = 65535
DIVISION = MAX_VAL / LED_COUNT
STEP = (LED_COUNT - 1) / 255

strand = NeoPixel(Pin(2), LED_COUNT)
slider = ADC(28)

colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

while True:
    reading = round(slider.read_u16() / DIVISION)
    print(reading)
    colour = colours[random.randint(0, len(colours) - 1)]
    
    for i in range(reading):
        mult = STEP * (i + 1)
        strand[i] = (round(colour[0] * mult), round(colour[1] * mult), round(colour[2] * mult))
        
    print()
    
    for i in range(reading, LED_COUNT):
        strand[i] = (0, 0, 0)
    strand.write()
        
    time.sleep(0.1)