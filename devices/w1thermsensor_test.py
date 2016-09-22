#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from w1thermsensor import W1ThermSensor, NoSensorFoundError

if __name__ == '__main__':
    try:
        sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20)
        temperature = sensor.get_temperature()
        print(temperature)
        print(sensor.sensorpath)
        print(sensor.id)
    except NoSensorFoundError as e:
        print(e)
    
