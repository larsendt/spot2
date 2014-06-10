#!/usr/bin/env python

import spot_common as sc
import time

DB = "lights_data.sqlite"
CREATE_SQL = "CREATE TABLE IF NOT EXISTS lights_data (lights_status INTEGER, time REAL)"
INSERT_SQL = "INSERT INTO lights_data VALUES (?,?)"
LATEST_SQL = "SELECT lights_status FROM lights_data ORDER BY time DESC LIMIT 1"

def lights_on():
    v = sc.select(DB, LATEST_SQL, [])
    if v is None:
        return False
    else:
        return v == 1


def on_time():
    v = sc.get_config("lights.on_time")
    try:
        on = float(v)
    except:
        sc.log_error("Lights controller failed to get 'lights on' time, setting to 8:00am UTC")
        on = 60 * 60 * 8
        sc.set_config("lights.on_time", on)
    return on


def off_time():
    v = sc.get_config("lights.off_time")
    try:
        off = float(v)
    except:
        sc.log_error("Lights controller failed to get 'lights off' time, setting to 8:00pm UTC")
        off = 60 * 60 * 20
        sc.set_config("lights.off_time", off)
    return off


def set_lights(on):
    val = int(on)
    t = time.time()
    sc.insert(DB, INSERT_SQL, (val, t))


def maybe_set_lights():
    t = sc.tod_seconds()
    if lights_on() and (t >= off_time() or t <= on_time()):
        set_lights(True)
    elif not lights_on() and (t >= on_time() or t <= off_time()):
        set_lights(False)


if __name__ == "__main__":
    sc.init_db(DB, CREATE_SQL)
    #try:
    maybe_set_lights()
    #except Exception as e:
    #    sc.log_exception(e)

