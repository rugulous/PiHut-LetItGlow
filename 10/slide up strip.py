from machine import Pin, ADC
from neopixel import NeoPixel
import time

LED_COUNT = 15
MAX_VAL = 65535
DIVISION = MAX_VAL / LED_COUNT
STEP = round(255 / LED_COUNT)

print(STEP)

strand = NeoPixel(Pin(2), LED_COUNT)
slider = ADC(28)

while True:
    reading = round(slider.read_u16() / DIVISION)
    
    for i in range(reading):
        val = round(STEP * (i + 1))
        print(val)
        strand[i] = (val, 0, 0)
        
    for i in range(LED_COUNT - 1, reading, -1):
        strand[i] = (0, 0, 0)
    strand.write()
        
    time.sleep(0.1)