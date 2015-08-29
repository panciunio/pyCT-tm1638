#!/usr/bin/env python

# CPU Temp and Load Average
# displays the current CPU temp and 1 minute load average, cycled every 2 seconds

import SUNXI_GPIO as GPIO
import TM1638
import time
import os

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = GPIO.PG0
CLK = GPIO.PG1
STB = GPIO.PG2

display = TM1638.TM1638(DIO, CLK, STB)
display.enable(1)

while True:
    # CPU temp
    res = os.popen('cat /sys/devices/platform/sunxi-i2c.0/i2c-0/0-0034/temp1_input').readline()
    res = res.replace('\n', '')
    display.set_text("CPU %0.1fc" % (float(res)/1000))
    time.sleep(2)

    # Load Average
    res = os.popen('uptime').readline()
    res = res.replace('\n', '')
    pos = res.index('age:')
    load = res[pos+5:pos+9]
    display.set_text("load %s" % (load))
    time.sleep(2)
