#!/usr/bin/env python

import generic_sensor as gs
import spot_common as sc

def take_reading():
    value = 1337.5
    units = "ec_units"
    gs.insert_reading("ec_sensor", value, units)
    return value, units

def historical(start, stop):
    return gs.historical("ec_sensor", start, stop)

if __name__ == "__main__":
    try:
        take_reading()
    except Exception as e:
        sc.log_exception(e)
