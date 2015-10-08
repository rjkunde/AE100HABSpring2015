#!/usr/bin/python

# Author: RJ Kunde
# 4/9/2015
# Aerospace Engineering 
# University of Illinois - Urbana Champaign

import time
import datetime
import SI1145.SI1145 as SI1145
import sqlite3
import os
import glob

# Initialize Sensor
sensor = SI1145.SI1145()

# Connect to Database
connection = sqlite3.connect('/home/pi/Desktop/Python_SI1145-master/production/SensorData.db')
cursor = connection.cursor()

# Loooooop
print 'Press Ctrl + Z to cancel'
cycles = 0
while True:
	# Grab Sensor Data
	vis = sensor.readVisible()
	IR = sensor.readIR()
	UV = sensor.readUV()
	uvIndex = UV / 100.0

	# Get timestamp yyyy-mm-dd 00:00:00
	# So about this... raspi doesn't have a cmos battery
	# Either we power it on and bring it live to launch
	# or we keep track of start time and modify data later with actual launch
	currentTime = datetime.datetime.now()
	currentTime = currentTime.strftime("%Y-%m-%d-%H-%M-%S")

	# Take photo with Rasp Pi Camera
	#pictureString = '/home/pi/Desktop/Python_SI1145-master/production/pictures/'
	#picturePath = pictureString + currentTime + '.jpg' 
	cmd = "raspistill -n -q 100 -awb sun -ex antishake -w 1920 -h 1080 -o /home/pi/Desktop/Python_SI1145-master/production/pictures/" +currentTime +".jpg"
	#print cmd
	os.system(cmd)

	# Place values into database
	cursor.execute("INSERT INTO sensors values(?,?,?,?,?);",(currentTime, vis, IR, UV,uvIndex))
	connection.commit()
	
	# Cycle Counter
	cycles = cycles + 1
	
	print 'Program has run ' + str(cycles) + ' times!'
	print
	print 'Record entered into database! S-U-C-C-E-S-S!'
	print
	print 'SMILE at the birdie! PHOTO TAKEN!'
	print
		
	# shhhh, POWERNAP
	#print 'powernap'
	#time.sleep(0)
# TODO
# 1. need a while loop
# 2. inside loop, get timestamp, query sensors
# 4. snap photo at same time, save to a folder (reduce image size)
# 5. repeat for set time interval

