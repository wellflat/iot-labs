#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from time import sleep
import picamera
from fractions import Fraction

def set_parameters(camera):
    camera.resolution = (1920, 1080)
    camera.brightness = 50
    camera.contrast = 0
    camera.saturation = 0
    camera.sharpness = 0
    camera.iso = 0
    camera.framerate = Fraction(30, 1)
    camera.video_stabilization = False
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


def preview(camera, seconds):
    camera.start_preview()
    sleep(seconds)
    camera.stop_preview()

if __name__ == '__main__':
    try:
        camera = picamera.PiCamera()
        set_parameters(camera)
        #preview(camera, 10)
        
        print('recording video')
        camera.start_recording('html/video.h264')
        sleep(10)
        camera.stop_recording()
    
    finally:
        camera.close()
