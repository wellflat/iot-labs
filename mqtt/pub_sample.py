#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, message):
    print('[' + message.topic + '] ' + str(message.payload))


if __name__ == '__main__':
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("test.mosquitto.org", 1883)
        topic = 'topic/test'

        while client.loop() == 0:
            message = "test message from publisher " + time.ctime()
            client.publish(topic, message, 0, True)
            print('[' + topic + '] message published')
            time.sleep(1.5)

    except KeyboardInterrupt as e:
        print('good bye')
        sys.exit(0)
