#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Adafruit_CharLCD import Adafruit_CharLCD
import sys
from subprocess import *
from time import sleep, strftime
from datetime import datetime

# Raspberry Pi pin configuration:
lcd_rs        = 7  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                       lcd_columns, lcd_rows, lcd_backlight)
try:
    lcd.clear()
    lcd.message('hello, world')
    sleep(10)
    lcd.clear()
except KeyboardInterrupt as e:
    lcd.message('good bye')
    lcd.clear()
    sleep(1)


# cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

# def run_cmd(cmd):
#     p = Popen(cmd, shell=True, stdout=PIPE)
#     output = p.communicate()[0]
#     return output

# while True:
#     lcd.clear()
#     ipaddr = run_cmd(cmd)
#     message = datetime.now().strftime('%b %d %H:%M:%S\n')
#     print(message)
#     lcd.message(message)
#     lcd.message('IP %s' % (ipaddr,))
#     sleep(2)
