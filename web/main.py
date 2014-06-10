#!/usr/bin/env python
from flask import Flask, request
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
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(air_temp.historical(start, stop))
    else:
        value, units = air_temp.take_reading()
        return json.dumps({"value":value, "units":units})


@app.route("/sensors/battery_level")
def r_battery_level():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(battery.historical_levels(start, stop))
    else:
        percent, p, charging, c = battery.take_reading()
        return json.dumps({"value":percent, "units":p})

@app.route("/sensors/battery_charging")
def r_battery_charging():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(battery.historical_charging(start, stop))
    else:
        percent, p, charging, c = battery.take_reading()
        return json.dumps({"value":charging, "units":c})

@app.route("/sensors/curtain")
def r_curtain():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(curtain.historical(start, stop))
    else:
        value, units = curtain.status()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/ec")
def r_ec():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(ec_sensor.historical(start, stop))
    else:
        value, units = ec_sensor.take_reading()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/fans")
def r_fans():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(fans.historical(start, stop))
    else:
        value, units = fans.status()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/humidity")
def r_humidity():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(humidity.historical(start, stop))
    else:
        value, units = humidity.take_reading()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/lights")
def r_lights():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(lights.historical(start, stop))
    else:
        value, units = lights.status()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/ph")
def r_ph():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(ph_sensor.historical(start, stop))
    else:
        value, units = ph_sensor.take_reading()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/pumps")
def r_pumps():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(pumps.historical(start, stop))
    else:
        value, units = pumps.status()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/rotation")
def r_rotation():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(rotation.historical(start, stop))
    else:
        value, units = rotation.status()
        return json.dumps({"value":value, "units":units})

@app.route("/sensors/water_temp")
def r_water_temp():
    start = request.args.get("start_time")
    stop = request.args.get("stop_time")
    if start and stop:
        start = float(start)
        stop = float(stop)
        return json.dumps(water_temp.historical(start, stop))
    else:
        value, units = water_temp.take_reading()
        return json.dumps({"value":value, "units":units})

if __name__ == "__main__":
    app.debug = True
    app.run()
