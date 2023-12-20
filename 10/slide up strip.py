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

while True:
    reading = round(slider.read_u16() / DIVISION)
    print(reading)
    colour = [random.randint(100, 255) for i in range(3)]
    
    for i in range(reading):
        mult = STEP * (i + 1)
        print(mult)
        strand[i] = (round(colour[0] * mult), round(colour[1] * mult), round(colour[2] * mult))
        print(strand[i])
        
    print()
    
    for i in range(LED_COUNT - 1, reading, -1):
        strand[i] = (0, 0, 0)
    strand.write()
        
    time.sleep(1)