#!/usr/bin/env python

import spot_common as sc
import time

DB = "%s.sqlite"
CREATE_SQL = "CREATE TABLE IF NOT EXISTS %s (reading TEXT, units TEXT, time REAL)"
INSERT_SQL = "INSERT INTO %s VALUES (?,?,?)"

def insert_reading(sensor_name, value, units):
    sc.init_db(DB % sensor_name, CREATE_SQL % sensor_name)
    sc.insert(DB % sensor_name, INSERT_SQL % sensor_name, (value, units, time.time()))
