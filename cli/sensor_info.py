#!/usr/bin/env python

import sys
import json

sys.path.append("../components")
import air_temp
import battery
import curtain
import ec_sensor
import fans
import humidity
import lights
import ph_sensor
import pumps
import rotation
import water_temp

def batt_level():
    percent, p, charging, b = battery.take_reading()
    return percent, p

def batt_charging():
    percent, p, charging, b = battery.take_reading()
    return charging, b


SENSORS = {"air_temp": air_temp.take_reading,
           "battery_level": batt_level,
           "battery_charging": batt_charging,
           "ec": ec_sensor.take_reading,
           "fan_status": fans.status,
           "humidity": humidity.take_reading,
           "lights": lights.status,
           "ph": ph_sensor.take_reading,
           "pumps": pumps.status,
           "rotation": rotation.status,
           "water_temp": water_temp.take_reading}

def get_sensor_info(sensor):
    func = SENSORS.get(sensor, lambda s: (None, None))
    value,units = func()
    return json.dumps({"value":value, "units":units})

def usage():
    print "Usage: %s <sensor>" % sys.argv[0]
    print "Available sensors are:"
    for sensor in sorted(SENSORS.keys()):
        print "\t", sensor

def main():
    if len(sys.argv) == 2:
        print get_sensor_info(sys.argv[1])
        return 0
    else:
        usage()
        return 1

if __name__ == "__main__":main()

