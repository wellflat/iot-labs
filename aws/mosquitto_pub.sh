#!/bin/sh

mosquitto_pub \
  --cafile certs/root-CA.crt \
  --cert certs/69d2c41b2a-certificate.pem.crt \
  --key certs/69d2c41b2a-private.pem.key \
  -h a22m7207m8mvt4.iot.ap-northeast-1.amazonaws.com \
  -p 8883 -q 1 -d \
  -t topic/sns \
  -i raspberrypi \
  -m '{"message":"Raspberry Pi"}'

