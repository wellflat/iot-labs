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


    pwm = GPIO.PWM(GPIO_OUT, 75)
    pwm.start(50)
    time.sleep(2.0)
    pwm.ChangeDutyCycle(10)
    time.sleep(2.0)
    pwm.stop()

    GPIO.cleanup()


        
    
