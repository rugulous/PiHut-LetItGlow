from machine import Pin
from neopixel import NeoPixel
import time
import math

TARGET_DUR = 2

def adjust(curr, target):
    if(curr == target):
        return curr
    
    if(curr > target):
        return curr - 1
    else:
        return curr + 1

def fade(target_colour):
    steps = [x - y for x, y in zip(target_colour, curr_colour)]
    total_steps_needed = max([abs(s) for s in steps])
    sleep_period = TARGET_DUR / total_steps_needed
    print(f"Sleeping for {sleep_period}")
    raw_val = [float(x) for x in curr_colour]
    
    while target_colour != curr_colour:
        for i in range(3):
            if(curr_colour[i] != target_colour[i]):
                raw_val[i] = raw_val[i] + (steps[i] / total_steps_needed)
                curr_colour[i] = int(raw_val[i])
            
        grb_led.fill(curr_colour)
        grb_led.write()
        time.sleep(sleep_period)

grb_led = NeoPixel(Pin(2), 1)
curr_colour = list((0, 0, 0))

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

grb_led.fill(curr_colour)
grb_led.write()

while True:
    for colour in colours:
        print(f"Changing to {colour}")
        fade(list(colours[colour]))
        #time.sleep(1)