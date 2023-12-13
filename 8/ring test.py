from machine import Pin
from neopixel import NeoPixel
import random

ring = NeoPixel(Pin(2), 12)
        
ring.fill((0, 0, 0))
ring[random.randint(0, len(ring) - 1)] = (10, 0, 0)
ring.write()