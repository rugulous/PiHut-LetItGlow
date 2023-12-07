from machine import Pin
import time

red = Pin(14, Pin.OUT)
green = Pin(25, Pin.OUT)

def flash(val):
    red.value(val)
    green.value(val)

while True:
    flash(1)
    time.sleep(0.5)
    
    flash(0)
    time.sleep(0.5)