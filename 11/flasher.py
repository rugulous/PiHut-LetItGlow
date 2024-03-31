from machine import Pin
import time

key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

led = Pin(6, Pin.OUT)

def flash_led(dur):
    led.value(1)
    time.sleep(dur)
    led.value(0)
    time.sleep(dur)
    
while True:
    while key1.value() == 1:
        flash_led(1)
        
    while key2.value() == 1:
        flash_led(0.5)
        
    while key3.value() == 1:
        flash_led(0.1)
        
    while key4.value() == 1:
        flash_led(0.05)