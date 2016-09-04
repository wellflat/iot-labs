#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import json
import yaml
import pycurl
from pprint import pprint
import Adafruit_BMP.BMP085 as BMP

## cURL python client(pycurl) sample
if __name__ == '__main__':
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cur_dir)
    
    sensor = BMP.BMP085() ## you can access BMP180 sensor
    temp = sensor.read_temperature()

    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    print('Temp = {0:0.2f} *C'.format(sensor.read_raw_temp()))
    print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))

    with open('m2x.yml', 'r') as f:
        conf = yaml.load(f)
        api_key = conf['api_key']
        url = conf['base_url'] + '/' + conf['stream'][0] + '/value'

    timestamp = datetime.datetime.now().isoformat()
    data = {'value': temp}  ## required 'value', 'timestamp' keys
    field_data = json.dumps(data)
    
    ch = pycurl.Curl()
    ch.setopt(pycurl.CUSTOMREQUEST, 'PUT')
    ch.setopt(pycurl.URL, url)
    ch.setopt(pycurl.VERBOSE, True)
    headers = ('X-M2X-KEY: ' + api_key, "Content-Type: application/json")
    ch.setopt(pycurl.HTTPHEADER, headers)
    print(field_data)
    ch.setopt(pycurl.POSTFIELDS, field_data)
    ch.perform()
    print('M2X Status: %d' % ch.getinfo(pycurl.RESPONSE_CODE))
