from machine import Pin
import time

dips = []
for i in range(6, 1, -1):
    dips.append(Pin(i, Pin.IN, Pin.PULL_DOWN))
    
while True:
    for i in range(0, len(dips)):
        if dips[i].value() == 1:
            print(f"Switch {i + 1} on")
        else:
            print(f"Switch {i + 1} OFF")
            
    print("--------------")
    print()
    
    time.sleep(5)