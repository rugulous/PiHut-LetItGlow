from machine import ADC, Pin
import time
from neopixel import NeoPixel

READING_MULTIPLIER = (255 / 65535)

slide = ADC(Pin(28))
leds = [NeoPixel(Pin(2), 1), NeoPixel(Pin(5), 1)]

def change_colour(new_colour):
    print(new_colour)
    target = [new_colour, round(new_colour * 0.7), new_colour]
    for led in leds:
        led.fill(target)
        led.write()

red = (0, 255, 0)
amber = (255, 175, 150)
green = (255, 0, 0)

while True:
    reading = slide.read_u16()
    change_colour(round(reading * READING_MULTIPLIER))
    
    time.sleep(0.01)