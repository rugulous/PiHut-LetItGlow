from machine import Pin
from neopixel import NeoPixel
import time

key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

gpio_pin = 2
num_leds = 15

strand = NeoPixel(Pin(gpio_pin), num_leds)

def alternate(colour1, colour2 = None):
    if(colour2 == None):
        colour2 = colour1
    
    for led in range(num_leds):
        if led % 2 == 0:
            strand[led] = (colour1)
        else:
            strand[led] = (colour2)
            
    strand.write()
    
alternate((0, 0, 0))
    
while True:
    time.sleep(0.1)
    
    if key1.value() == 1:
        alternate((0, 255, 255), (0, 255, 0))
    elif key2.value() == 1:
        alternate((255, 255, 255), (0, 0, 255))
    elif key3.value() == 1:
        alternate((255, 255, 0), (255, 0, 255))
    elif key4.value() == 1:
        alternate((0, 0, 0))
        