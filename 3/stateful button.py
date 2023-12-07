#red button toggles between blinking and always on
#green button toggles between on and off

from machine import Pin
import time

redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)
redLed = Pin(14, Pin.OUT)
greenLed = Pin(25, Pin.OUT)

on = False
changeState = False
blinking = True
blinkCounter = 0

redLed.value(0)
greenLed.value(0)

def blink():
    redLed.toggle()
    greenLed.toggle()

while True:
    time.sleep(0.2)
    
    #process input
    if greenButton.value() == 1:
        on = not on
        changeState = True
        print("GREEN!")
        
        if on and blinking:
            blinkCount = 5
        
    if redButton.value() == 1:
        changeState = True
        blinking = not blinking
        blinkCounter = 0
        print("RED!")
    
    if not on:
        if changeState:
            redLed.value(0)
            greenLed.value(0)
            changeState = False
        continue
    
    if blinking:
        blinkCounter = blinkCounter + 1
        
        if blinkCounter >= 5:
            blink()
            blinkCounter = 0
            
    else:
        if changeState:
            redLed.value(1)
            greenLed.value(1)
            changeState = False