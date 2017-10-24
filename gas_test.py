#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
sys.path.append(GrovePi/Software/Python/)
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
grovepi.pinMode(MQ9_gas_sensor,&quot;INPUT&quot;)

count = 0
while True:
    try:
        #Get a average data by testing 100 times
        while(count &lt; 100):
            sensor_value = grovepi.analogRead(MQ9_gas_sensor)
            count = count +1
            print (&quot;Calibrating...&quot;), count,(&quot;%&quot;), (&quot;  Sensor Value =&quot;), sensor_value
        
        sensor_value=(float)(sensor_value/100.0)
        sensor_volt=(float)(sensor_value/1024.0)*5.0
        RS_air=(float)(5.0-sensor_volt)/sensor_volt #omit *RL
        R0 = (float)(RS_air/9.9)
        print(&quot;sensor volt =&quot;), sensor_volt,(&quot;V&quot;)
        print(&quot;R0 =&quot;), R0
        time.sleep(1)
    except (IOError,TypeError) as e:
        print &quot;Error&quot; + str(e)
    except KeyboardInterrupt:
        break
exit()