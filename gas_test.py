#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
sys.path.append('home/GrovePi/Software/Python/')
import os
import time
import math
import decimal
import grovepi
from grovepi import *
import random

# Connections
MQ9_gas_sensor = 0

# Initializing variables
grovepi.pinMode(MQ9_gas_sensor,"INPUT")

count = 0
while True:
    try:
        #Get a average data by testing 100 times
        while(count < 100):
            sensor_value = grovepi.analogRead(MQ9_gas_sensor)
            count = count +1
            print ("Calibrating..."), count,("%"), ("  Sensor Value ="), sensor_value
        
        sensor_value=(float)(sensor_value/100.0)
        sensor_volt=(float)(sensor_value/1024.0)*5.0
        RS_air=(float)(5.0-sensor_volt)/sensor_volt #omit *RL
        R0 = (float)(RS_air/9.9)
        print("sensor volt ="), sensor_volt,("V")
        print("R0 ="), R0
        time.sleep(1)
    except (IOError,TypeError) as e:
        print "Error" + str(e)
    except KeyboardInterrupt:
        break
exit()