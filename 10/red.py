from machine import Pin
from neopixel import NeoPixel

strand = NeoPixel(Pin(2), 15)

strand.fill((50, 0, 0))
strand.write()

print("Red!")