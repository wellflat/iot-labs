#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
    GPIO_OUT = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_OUT, GPIO.OUT)

    LED_UP = True
    for i in range(6):
        GPIO.output(GPIO_OUT, LED_UP)
        LED_UP = not LED_UP
        time.sleep(0.2)


    print('using Pulse-Width Modulation')
    pwm = GPIO.PWM(GPIO_OUT, 50) # 50Hz
    pwm.start(0)
    while True:
        try:
            for i in range(100):
                pwm.ChangeDutyCycle(i) # 0 - 100
                time.sleep(0.02)

            for i in range(100):
                pwm.ChangeDutyCycle(100 - i)
                time.sleep(0.02)

        except KeyboardInterrupt as e:
            pwm.stop()
            break
    
    GPIO.cleanup()
    print('exit')
    
    


        
    
