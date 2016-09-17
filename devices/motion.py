#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO_IN = 17
GPIO_OUT = 22

## using HC-SR501 Infrared PIR Motion Sensor
def detectmotion(IN):
    print('detect motion')
    GPIO.output(GPIO_OUT, True)
    time.sleep(0.2)
    GPIO.output(GPIO_OUT, False)
    

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_IN, GPIO.IN)
    GPIO.setup(GPIO_OUT, GPIO.OUT)

    try:
        GPIO.add_event_detect(GPIO_IN, GPIO.RISING, callback=detectmotion)
        while True:
            time.sleep(100)
    except KeyboardInterrupt as e:
        print('quit')
        GPIO.cleanup()


    
