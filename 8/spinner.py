from machine import Pin
from neopixel import NeoPixel
import time

ring = NeoPixel(Pin(2), 12)

ring.fill((0,0,0))
ring.write()
time.sleep(1)

while True:
    
    for i in range(len(ring)):
        ring[i] = (0,0,30)
        ring.write()
        
        time.sleep(0.1)
        
        ring.fill((0,0,0))
        ring.write()
