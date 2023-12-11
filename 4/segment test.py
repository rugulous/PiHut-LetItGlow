from machine import Pin
import time

# Set up the LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

while True:
    # Turn on each LED at a time
    seg1.value(1)
    time.sleep(1)

    seg2.value(1)
    time.sleep(1)

    seg3.value(1)
    time.sleep(1)

    seg4.value(1)
    time.sleep(1)

    seg5.value(1)
    time.sleep(1)

    # Turn all LEDs off
    seg1.value(0)
    seg2.value(0)
    seg3.value(0)
    seg4.value(0)
    seg5.value(0)
    
    time.sleep(1)