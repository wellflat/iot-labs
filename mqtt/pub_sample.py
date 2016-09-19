#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    topic = 'topic/test:raspi'
    message = "test message from publisher " + time.ctime()
    client.publish(topic, message)

def on_message(client, userdata, message):
    print('[' + message.topic + '] ' + str(message.payload))

def on_publish(client, userdata, mid):
    print('message id: %d' % mid)
    client.disconnect()


if __name__ == '__main__':
    try:
        client = mqtt.Client(protocol=mqtt.MQTTv311)
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_publish = on_publish
        client.connect("test.mosquitto.org", port=1883, keepalive=60)
        client.loop_forever()

    except KeyboardInterrupt as e:
        print('good bye')
        sys.exit(0)
