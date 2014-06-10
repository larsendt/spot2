#!/usr/bin/env python

import sqlite3
import json
import time
import traceback

DB_PREFIX = "../db/"

# time of day in seconds
def tod_seconds():
    t = int(time.time())
    seconds_per_day = 60 * 60 * 24
    return t % seconds_per_day


def init_db(db, create_sql):
    conn = sqlite3.connect(DB_PREFIX + db)
    c = conn.cursor()
    c.execute(create_sql)
    conn.commit()
    conn.close()


def insert(db, insert_sql, values):
    conn = sqlite3.connect(DB_PREFIX + db)
    c = conn.cursor()
    c.execute(insert_sql, values)
    conn.commit()
    conn.close()
    print "[%s] Inserted: %s" % (db, values)


def select(db, select_sql, values):
    conn = sqlite3.connect(DB_PREFIX + db)
    c = conn.cursor()
    c.execute(select_sql, values)
    r = c.fetchall()
    conn.close()
    return r


def get_config(key):
    init_db("config.sqlite", "CREATE TABLE IF NOT EXISTS config (key TEXT UNIQUE, value TEXT)")
    value = select("config.sqlite", "SELECT * FROM config WHERE key=?", (key,))
    if len(value) > 0:
        return value[0][1]
    else:
        return None


def set_config(key, value):
    init_db("config.sqlite", "CREATE TABLE IF NOT EXISTS config (key TEXT, value TEXT)")
    insert("config.sqlite", "INSERT OR REPLACE INTO config VALUES (?,?)", (key, value))


def log_error(*args):
    s = " ".join(map(str, args))
    init_db("errors.sqlite", "CREATE TABLE IF NOT EXISTS errors (msg TEXT, time REAL, seen INTEGER)")
    insert("errors.sqlite", "INSERT INTO errors VALUES (?,?,?)", (s, time.time(), 0))
    print s


def log_warning(*args):
    s = " ".join(map(str, args))
    init_db("warnings.sqlite", "CREATE TABLE IF NOT EXISTS warnings (msg TEXT, time REAL, seen INTEGER)")
    insert("warnings.sqlite", "INSERT INTO warnings VALUES (?,?,?)", (s, time.time(), 0))
    print s


def log_exception(exc):
    s = traceback.format_exc(exc)
    init_db("exceptions.sqlite", "CREATE TABLE IF NOT EXISTS exceptions (msg TEXT, time REAL, seen INTEGER)")
    insert("exceptions.sqlite", "INSERT INTO exceptions VALUES (?,?,?)", (s, time.time(), 0))
    print s
