#!/usr/bin/python

# Author: RJ Kunde
# 4/9/2015
# Aerospace Engineering 
# University of Illinois - Urbana Champaign

import time
import SI1145.SI1145 as SI1145
import sqlite3
import os
import glob

# Initialize Sensor
sensor = SI1145.SI1145()

# Grab Sensor Data
vis = sensor.readVisible()
IR = sensor.readIR()
UV = sensor.readUV()
uvIndex = UV / 100.0

# Connect to Database
connection = sqlite3.connect('/home/pi/Desktop/Python_SI1145-master/production/SensorData.db')
cursor = connection.cursor()

# Place values into database
cursor.execute("INSERT INTO sensors values('Dank',5000,7000,6000,3470.0)")
connection.commit()
print 'Rock on - Script Complete'