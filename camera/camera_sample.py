#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from time import sleep
import picamera
from fractions import Fraction

def set_parameters(camera):
    #camera.resolution = (3280, 2464)
    camera.resolution = (1920, 1080)
    camera.brightness = 50
    camera.contrast = 0
    camera.saturation = 0
    camera.sharpness = 0
    camera.framerate = Fraction(10, 1)
    camera.iso = 100  ## 0:auto
    #camera.iso = 0
    camera.shutter_speed = int(1 / 10 * 1000 * 1000)  ## microseconds, 0:auto
    #camera.shutter_speed = 0
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0, 0.0, 1.0, 1.0)
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    camera.annotate_text = now
    print(dir(camera))


if __name__ == '__main__':
    try:
        camera = picamera.PiCamera()
        set_parameters(camera)
        print('capturing still')
        camera.capture('html/image.jpg')
    
    finally:
        camera.close()
    
