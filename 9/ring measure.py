from machine import Pin, I2C
import time
from dht20 import DHT20
from neopixel import NeoPixel

RING_SIZE = 12

i2c1_sda = Pin(14)
i2c1_scl = Pin(15)
i2c1 = I2C(1, sda=i2c1_sda, scl=i2c1_scl)
dht20 = DHT20(0x38, i2c1)
ring = NeoPixel(Pin(2), RING_SIZE)

def clear_ring():
    for i in range(RING_SIZE):
        ring.fill((0, 0, 0))
    ring.write()

def light_ring(temp):
    clear_ring()
    num = max(temp - 14, 0)
    
    for i in range(min(num, RING_SIZE)):
        ring[i] = (10, 10, 10)
    ring.write()

while True:
    measurements = dht20.measurements
    temperature = round(measurements['t'])

    # Print the data
    print("-- Environment ---------")
    print(f"Temperature:      {round(measurements['t'],1)}°C")
    print(f"Humidity:         {round(measurements['rh'],1)}%")
    print("------------------------")
    print("")
    
    light_ring(temperature)
    
    time.sleep(5)
