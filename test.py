#!/usr/bin/env python

# TM1638 playground

import TM1638
import time
import SUNXI_GPIO as GPIO

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = GPIO.PG0
CLK = GPIO.PG1
STB = GPIO.PG2

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)


count = 0
while True:
    count += 1
    for i in range(8):
        display.send_char(i, count)
#        for i in range(len(count)):
#            display.set_digit(8-len(text)+i, int(text[i]), i==dotpos)
    time.sleep(1)

