#!/usr/bin/env python

import generic_sensor as gs
import spot_common as sc

def take_reading():
    value = 78.0
    units = "deg F"
    gs.insert_reading("air_temp_sensor", value, units)

if __name__ == "__main__":
    try:
        take_reading()
    except Exception as e:
        sc.log_exception(e)
