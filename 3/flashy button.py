from machine import Pin
import time

def toggle(pin, value):
    value = 0 if value == 1 else 1
    pin.value(value)
    return value

redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)
redLed = Pin(14, Pin.OUT)
greenLed = Pin(25, Pin.OUT)

while True:
    time.sleep(0.1)
    
    if redButton.value() == 1:
        redLed.toggle()
        
    if greenButton.value() == 1:
        greenLed.toggle()
    
    