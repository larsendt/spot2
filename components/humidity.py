#!/usr/bin/env python

import generic_sensor as gs
import spot_common as sc

def take_reading():
    value = 45.0
    units = "humidity_units"
    gs.insert_reading("humidity_sensor", value, units)
    return value, units

def historical(start, stop):
    return gs.historical("humidity_sensor", start, stop)

if __name__ == "__main__":
    try:
        take_reading()
    except Exception as e:
        sc.log_exception(e)
