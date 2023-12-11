from machine import Pin
import time

dips = []
segments = []
for i in range(6, 1, -1):
    dips.append(Pin(i, Pin.IN, Pin.PULL_DOWN))
    segments.append(Pin(i + 7, Pin.OUT))
    
while True:
    for i in range(0, len(dips)):
        segments[i].value(dips[i].value())
        if dips[i].value() == 1:
            print(f"Switch {i + 1} on")
        else:
            print(f"Switch {i + 1} OFF")
            
    print("--------------")
    print()
    
    time.sleep(5)