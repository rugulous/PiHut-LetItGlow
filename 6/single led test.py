from machine import Pin
from neopixel import NeoPixel
import time

grb_led = NeoPixel(Pin(2), 1)

colours = {
    "white": (240, 140, 255),
    "red": (0, 255, 0),
    "green": (255, 0, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 175, 150),
    "orange": (238, 223, 105),
    "pink": (150, 150, 200),
    "purple": (40, 100, 255),
    "ice_blue": (150, 25, 200),
    "unicorn": (175, 150, 255),
    "bogey": (215, 100, 0)
}

for colour in colours:
    print(f"Changing to {colour}")
    grb_led.fill(colours[colour])
    grb_led.write()
    time.sleep(1)