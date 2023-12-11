from machine import Pin
import time

green_button = Pin(3, Pin.IN, Pin.PULL_DOWN)
red_button = Pin(2, Pin.IN, Pin.PULL_DOWN)
segments = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(11, Pin.OUT), Pin(10, Pin.OUT), Pin(9, Pin.OUT)]
count = -1

#make sure all off
for led in segments:
    led.value(0)

while True:
    time.sleep(0.1)
    
    if green_button.value() == 1 and count < 4:
        count = count + 1
        segments[count].value(1)
        
    elif red_button.value() == 1:
        segments[count].value(0)
        if count >= 0:
            count = count - 1