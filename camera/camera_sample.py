#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import picamera

def set_parameters(camera):
    camera.hflip = True
    camera.vflip = True
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
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
    
# todo: implement
if __name__ == '__main__':
    camera = picamera.PiCamera()
    camera.capture('image.jpg')
    set_parameters(camera)
    # capturing camera preview
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()
    # recording video
    camera.start_recording('video.h264')
    sleep(5)
    camera.stop_recording()
