#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
from pprint import pprint
import Adafruit_BMP.BMP085 as BMP
from m2x.client import M2XClient

## M2X python client library sample
if __name__ == '__main__':
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cur_dir)
    
    with open('m2x.yml', 'r') as f:
        conf = yaml.load(f)
        api_key = conf['api_key']
        device_id = conf['device_id']
        stream_ids = conf['stream']
        
    client = M2XClient(key=api_key)
    device = client.device(device_id)
    #pprint(device.data)
    stream_temp = device.stream(stream_ids[0])
    stream_pres = device.stream(stream_ids[1])
    sensor = BMP.BMP085()
    temp = sensor.read_temperature()
    pres = sensor.read_pressure()
    print('Temperature: %lf' % temp)
    print('Pressure: %lf' % pres)
    stream_temp.add_value(temp)
    print('Status: %d' % client.last_response.status)
    stream_pres.add_value(pres)
    print('Status: %d' % client.last_response.status)
    print(client.last_response.raw)
