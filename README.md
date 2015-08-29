# pyCT-tm1638

Python library for Cubietruck/Cubieboard and TM1638 7 segment display with 16 buttons.

This module is commonly sold on deal extreme, aliexpress or eBay, but differs from the version that has 8 LEDs and 8 buttons. The 8 button version is common cathode, the 16 button version is common anode. This library based on https://github.com/johnblackmore/py-tm1638 - John's Blackmore library for Raspberry Pi.

#Prerequisites:
- pySUNXI library - http://dl.cubieboard.org/software/libs/pySUNXI-0.1.12.tar.gz
- script.fex (script.bin) modyfication in order to use another GPIO like PG0-PG3

