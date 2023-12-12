from machine import ADC, Pin
import time
from neopixel import NeoPixel

slide = ADC(Pin(28))
leds = [NeoPixel(Pin(2), 1), NeoPixel(Pin(5), 1)]

def change_colour(new_colour):
    for led in leds:
        led.fill(new_colour)
        led.write()

red = (0, 255, 0)
amber = (255, 175, 150)
green = (255, 0, 0)

while True:
    reading = slide.read_u16()
    
    if reading <= 20000:
        change_colour(red)
    elif reading < 40000:
        change_colour(amber)
    else:
        change_colour(green)
    
    time.sleep(0.1)
    
    time.sleep(0.1)