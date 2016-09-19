#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    topic = 'topic/test:raspi'
    client.subscribe(topic)

def on_message(client, userdata, message):
    print('[' + message.topic + '] ' + str(message.payload))

if __name__ == '__main__':
    try:
        client = mqtt.Client(protocol=mqtt.MQTTv311)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("test.mosquitto.org", 1883)
        client.loop_forever()
    except KeyboardInterrupt as e:
        print('good bye')
        sys.exit(0)
