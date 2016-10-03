#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import picamera
from fractions import Fraction

if __name__ == '__main__':
    try:
        camera = picamera.PiCamera()
        print('check camera parameters')
        print(dir(camera))
        print('')
        print(camera.AWB_MODES)
        print(camera.CAMERA_CAPTURE_PORT)
        print(camera.CAMERA_PREVIEW_PORT)
        print(camera.CAMERA_VIDEO_PORT)
        print(camera.CAPTURE_TIMEOUT)
        print(camera.CLOCK_MODES)
        print(camera.DEFAULT_ANNOTATE_SIZE)
        print(camera.DRC_STRENGTHS)
        print(camera.EXPOSURE_MODES)
        print(camera.FLASH_MODES)
        print(camera.IMAGE_EFFECTS)
        print(camera.ISO)
        print(camera.MAX_FRAMERATE)
        print(camera.MAX_RESOLUTION)
        print(camera.METER_MODES)
        print(camera.RAW_FORMATS)
        print(camera.STEREO_MODES)
        
    
    finally:
        camera.close()
