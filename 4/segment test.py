from machine import Pin
import time

# Set up the LED pins
segments = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(11, Pin.OUT), Pin(10, Pin.OUT), Pin(9, Pin.OUT)]

while True:
    for led in segments:
        led.value(1)
        time.sleep(1)

    for led in segments:
        led.value(0)
        
    time.sleep(1)