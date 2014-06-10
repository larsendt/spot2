#!/usr/bin/env python

import spot_common as sc
import time

DB = "%s.sqlite"
CREATE_SQL = "CREATE TABLE IF NOT EXISTS %s (reading TEXT, units TEXT, time REAL)"
INSERT_SQL = "INSERT INTO %s VALUES (?,?,?)"
SELECT_SQL = "SELECT * FROM %s ORDER BY time DESC LIMIT 1"

def insert_reading(sensor_name, value, units):
    sc.init_db(DB % sensor_name, CREATE_SQL % sensor_name)
    sc.insert(DB % sensor_name, INSERT_SQL % sensor_name, (value, units, time.time()))

def latest_reading(sensor_name):
    sc.init_db(DB % sensor_name, CREATE_SQL % sensor_name)
    v = sc.select(DB % sensor_name, SELECT_SQL % sensor_name, [])
    if len(v) > 0:
        return v[0]
    else:
        return None
