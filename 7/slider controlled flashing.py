import time
from machine import Pin, ADC
from neopixel import NeoPixel
import random

slider = ADC(Pin(28))
leds = [NeoPixel(Pin(2), 1), NeoPixel(Pin(5), 1)]
flash = 0

while True:
    flash = slider.read_u16() / 65000
    
    colour = [random.randint(0, 255) for i in range(3)]
    for led in leds:
        led.fill(colour)
        led.write()
        
    time.sleep(flash)