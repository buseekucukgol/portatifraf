import RPi_I2C_driver
import RPi.GPIO as gpio
from time import *


DT=27
SCK=17

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(SC, gpio.OUT)


mylcd=RPi_I2C_driver.lcd()
mylcd._display_string("    MERHABA", 1)
sleep(2)
mylcd.lcd_clear()

def readCount():
    i=0
    Count=0
    gpio.setup(DT,gpio.OUT)
    gpio.output(DT,1)
    gpio.output(SCK,0)
    gpio.setup(DT, gpio.IN)


    while gpio.input(DT)==1:
        i=0

    for i in range(24):
        gpio.output(SCK,1)
        Count=Count<<1

        gpio.output()SCK,0
        sleep(0.001)
        if gpio.input(DT)==0:
            Count=Count+1

gpio.output(SCK,1)
Count=Count^0x800000
gpio.output(SCK,0)
return Count

while 1:
    Count=readCount()
    print(Count)

    if Count < 8290000:
        mylcd.lcd_display_string("Tabak Dolu",1)
    elif Count > 8230000:
        mylcd.lcd_display_string("Tabak Bos !",1)
        mylcd.backlight(0)
        sleep(1)
        mylcd.backlight(1)
        sleep(1)

              
