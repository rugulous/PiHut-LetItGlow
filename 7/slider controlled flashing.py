import time
from machine import Pin, ADC
from neopixel import NeoPixel
import random

slider = ADC(Pin(28))
leds = [NeoPixel(Pin(2), 1), NeoPixel(Pin(5), 1)]
flash = 0
first = True

while True:
    flash = slider.read_u16() / 65000
    
    colour = [random.randint(0, 255) for i in range(3)]
    led = leds[0 if first else 1]
    led.fill(colour)
    led.write()
    first = not first
        
    time.sleep(flash)
