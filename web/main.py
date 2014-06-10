#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

import json
import sys
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


@app.route("/sensors")
def sensors():
    sensors = ["air_temp", "battery_level", "battery_charging", "ec",
            "fan_status", "humidity", "lights", "ph", "pumps", "rotation",
            "water_temp"]
    return json.dumps(sensors)


@app.route("/sensors/air_temp")
def r_air_temp():
    value, units = air_temp.take_reading()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/battery_level")
def r_battery_level():
    percent, p, charging, c = battery.take_reading()
    return json.dumps({"value":percent, "units":p})

@app.route("/sensors/battery_charging")
def r_battery_charging():
    percent, p, charging, c = battery.take_reading()
    return json.dumps({"value":charging, "units":c})

@app.route("/sensors/curtain")
def r_curtain():
    value, units = curtain.status()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/ec")
def r_ec():
    value, units = ec_sensor.take_reading()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/fans")
def r_fans():
    value, units = fans.status()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/humidity")
def r_humidity():
    value, units = humidity.take_reading()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/lights")
def r_lights():
    value, units = lights.status()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/ph")
def r_ph():
    value, units = ph_sensor.take_reading()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/pumps")
def r_pumps():
    value, units = pumps.status()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/rotation")
def r_rotation():
    value, units = rotation.status()
    return json.dumps({"value":value, "units":units})

@app.route("/sensors/water_temp")
def r_water_temp():
    value, units = water_temp.take_reading()
    return json.dumps({"value":value, "units":units})

if __name__ == "__main__":
    app.debug = True
    app.run()
