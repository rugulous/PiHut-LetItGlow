from machine import Pin
from neopixel import NeoPixel

grb_led = NeoPixel(Pin(2), 1)

grb_led.fill((0, 0, 255))
grb_led.write()