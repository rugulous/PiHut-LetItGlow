from machine import Pin
import time

MAX_VAL = 31
MIN_VAL = 0

green_button = Pin(3, Pin.IN, Pin.PULL_DOWN)
red_button = Pin(2, Pin.IN, Pin.PULL_DOWN)
segments = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(11, Pin.OUT), Pin(10, Pin.OUT), Pin(9, Pin.OUT)]
count = MIN_VAL
format_str = '{0:0' + str(len(segments)) + 'b}'

def updateLights():
    binary = list(format_str.format(count))
    for i in range(len(segments)):
        segments[i].value(1 if binary[i] == '1' else 0)

#make sure all off
for led in segments:
    led.value(0)

while True:
    time.sleep(0.1)
    
    if green_button.value() == 1:
        if count < MAX_VAL:
            count = count + 1
        else:
            count = MIN_VAL
        updateLights()
        
    elif red_button.value() == 1:
        if count > MIN_VAL:
            count = count - 1
        else:
            count = MAX_VAL
        updateLights()
            