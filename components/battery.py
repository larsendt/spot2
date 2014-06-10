#!/usr/bin/env python

import spot_common as sc
import time

DB = "battery_status.sqlite"
CREATE_SQL = "CREATE TABLE IF NOT EXISTS battery_status (percent REAL, charging INTEGER, time REAL)"
INSERT_SQL = "INSERT INTO battery_status VALUES (?,?,?)"

def take_reading():
    sc.init_db(DB, CREATE_SQL)
    percent = 65.0
    charging = True
    sc.insert(DB, INSERT_SQL, (percent, charging, time.time()))
    return (percent, "percent", charging, "bool")

if __name__ == "__main__":
    try:
        take_reading()
    except Exception as e:
        sc.log_exception(e)
