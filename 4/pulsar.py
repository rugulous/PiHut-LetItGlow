from machine import Pin
import time

SLEEP_TIME = 0.08

def pulse(led):
    led.value(1)
    time.sleep(SLEEP_TIME)
    led.value(0)

# Set up the LED pins
segments = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(11, Pin.OUT), Pin(10, Pin.OUT), Pin(9, Pin.OUT)]

#make sure all off
for led in segments:
    led.value(0)
    
pulse(segments[0])

while True:

    # For loop to turn each LED on then off in order of the list
    for led in segments[1:]:
        pulse(led)
        
    # For loop in reverse, running backwards through the list
    for led in reversed(segments[:-1]):
        pulse(led)