#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import json
import time
import yaml
from pprint import pprint
import paho.mqtt.client as mqtt
import Adafruit_BMP.BMP085 as BMP


## MQTT python client sample
## notice: doesn't work yet
if __name__ == '__main__':
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cur_dir)

    sensor = BMP.BMP085() ## you can access BMP180 sensor
    temp = sensor.read_temperature()
    pres = sensor.read_pressure()
    print('Temperature: %lf' % temp)
    print('Pressure: %lf' % pres)
    
    with open('m2x.yml', 'r') as f:
        conf = yaml.load(f)
        api_key = conf['api_key']
        device_id = conf['device_id']
        stream_ids = conf['stream']
        mqtt_host = conf['mqtt_host']
        mqtt_port = conf['mqtt_port']
        mqtt_keepalive = conf['mqtt_keepalive']
        topic = 'm2x/' + api_key + '/requests'

    
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe('m2x/' + api_key + '/responses')

    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_host, port=mqtt_port, keepalive=mqtt_keepalive)
    client.loop_forever()

    timestamp = datetime.datetime.now().isoformat()

    data = {
        "id": "random id is here",
        "method": "PUT",
        "resource": "/v2/devices/" + device_id + "/streams/temperature/value",
        "agent": "M2X-Demo-Client/0.0.1",
        "body": {
            "value": temp
        }
    }
    request_data = json.dumps(data)


    ## todo implement
    # for i in range(3):
    #     print(client.publish(topic, request_data))
    #     time.sleep(0.2)

    client.disconnect()
        

