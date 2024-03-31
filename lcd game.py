from machine import I2C
from pico_i2c_lcd import I2cLcd
import time

# Define LCD I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

run1 =  bytearray([0x0E, 0x0E, 0x0E, 0x05, 0x0E, 0x14, 0x1A, 0x01])
run2 =  bytearray([0x0E, 0x0E, 0x0E, 0x04, 0x1F, 0x04, 0x0A, 0x11])
run3 =  bytearray([0x0E, 0x0E, 0x0E, 0x14, 0x0E, 0x05, 0x0B, 0x10])
block = bytearray([0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F])

lcd.custom_char(0, run1)
lcd.custom_char(1, run2)
lcd.custom_char(2, run3)
lcd.custom_char(3, block)

anim = 0
animation = [0, 1, 2, 1]
lcd.clear()

def build_top_row():
    return chr(3) * LCD_NUM_COLS

def build_bottom_row():
    return chr(animation[anim]) + (chr(3) * (LCD_NUM_COLS - 1))

while True:
    lcd.move_to(0, 0)
    lcd.putstr(build_top_row())
    lcd.move_to(0, 1)
    lcd.putstr(build_bottom_row())
    
    if anim == len(animation) - 1:
        anim = 0
    else:
        anim = anim + 1
        
    time.sleep(0.3)