#!/usr/bin/env python

import generic_sensor as gs
import spot_common as sc

def take_reading():
    value = 7.0
    units = "pH"
    gs.insert_reading("ph_sensor", value, units)
    return value, units

def historical(start, stop):
    return gs.historical("ph_sensor", start, stop)

if __name__ == "__main__":
    try:
        take_reading()
    except Exception as e:
        sc.log_exception(e)
