#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
    GPIO_OUT = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_OUT, GPIO.OUT)

    for i in range(10):
        if i%2 == 0:
            print('%d: ON' % (i,))
            GPIO.output(GPIO_OUT, True)
        else:
            print('%d: OFF' % (i,))
            GPIO.output(GPIO_OUT, False)

        time.sleep(0.2)


    ## using Pulse-Width Modulation
    pwm = GPIO.PWM(GPIO_OUT, 50) # 50Hz
    pwm.start(0)
    for i in range(100):
        pwm.ChangeDutyCycle(i) # 0 - 100
        time.sleep(0.02)

    for i in range(100):
        pwm.ChangeDutyCycle(100 - i)
        time.sleep(0.02)
    
    pwm.stop()
    GPIO.cleanup()


        
    
