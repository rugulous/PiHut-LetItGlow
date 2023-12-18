from machine import Pin, I2C
import time
from dht20 import DHT20

i2c1_sda = Pin(14)
i2c1_scl = Pin(15)
i2c1 = I2C(1, sda=i2c1_sda, scl=i2c1_scl)
dht20 = DHT20(0x38, i2c1)

while True:
    measurements = dht20.measurements

    # Print the data
    print("-- Environment ---------")
    print(f"Temperature:      {round(measurements['t'],1)}°C")
    print(f"Humidity:         {round(measurements['rh'],1)}%")
    print("------------------------")
    print("")
    
    time.sleep(5)