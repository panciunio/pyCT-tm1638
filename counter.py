#!/usr/bin/env python

# TM1638 playground

import SUNXI_GPIO as GPIO
import TM1638
import time


# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = GPIO.PG0
CLK = GPIO.PG1
STB = GPIO.PG2

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)

count = 0
while True:
    display.set_text(str(count))
    count += 100
    time.sleep(0.02)

