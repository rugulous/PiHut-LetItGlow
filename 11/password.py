from machine import Pin
from neopixel import NeoPixel
import time

keys = [
    Pin(11, Pin.IN, Pin.PULL_DOWN),
    Pin(10, Pin.IN, Pin.PULL_DOWN),
    Pin(13, Pin.IN, Pin.PULL_DOWN),
    Pin(12, Pin.IN, Pin.PULL_DOWN)
]

led = Pin(6, Pin.OUT)

gpio_pin = 2
num_leds = 15

strand = NeoPixel(Pin(gpio_pin), num_leds)

password_guess = []
pressed = False

def wait_for_release():
    while True:
        pressed = False
        for key in keys:
            if(key.value() == 1):
                pressed = True
                led.value(1)
                break
            
        if pressed == False:
            led.value(0)
            return
        
        time.sleep(0.1)
    
def add_key(key):
    password_guess.append(key)
    print("*", end="")
    
def check_guess():
    pwd = "4441"
    for i in range(len(pwd)):
        if password_guess[i] != pwd[i]:
            print(password_guess[i], "!=", pwd[i])
            return False
        
    return True

print("Enter passcode to continue")

while True:
    wait_for_release()
    
    for i in range(len(keys)):
        if keys[i].value() == 1:
            add_key(str(i + 1))
    
    if len(password_guess) == 4:
        if check_guess():
            print()
            print("PASSWORD CORRECT!")
            break
        else:
            print()
            print("INCORRECT PASSWORD")
            print("Please try again")
            password_guess = []
        