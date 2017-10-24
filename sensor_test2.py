import random, time, grovepi
from statistics import mean
from terminaltables import AsciiTable

timeout = time.time() + 60*2 # Set to run for 2 minutes

sensorLoudness = 1
sensorMQ5 = 2

arrayTimestamp = []
arrayTemperature = []
arrayHumidity = []
arrayLoudness = []
arrayMQ5 = []

def readingsSensors():
    #th = grove_i2c_temp_hum_mini.th02()
    theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #theTemperature = th.getTemperature()
    #theHumidity = th.getHumidity()
    theLoudness = grovepi.analogRead(sensorLoudness)
    theMQ5 = grovepi.analogRead(sensorMQ5)
    arrayTimestamp.append(theTime)
    #arrayTemperature.append(theTemperature)
    #arrayHumidity.append(theHumidity)
    arrayLoudness.append(theLoudness)
    arrayMQ5.append(theMQ5)
    timeRemaining = str(int(timeout - time.time() + .5))
    timeMessage = "Reading taken. " + timeRemaining + " seconds remaining."
    print timeMessage
    time.sleep(0.5)

while True:
    if time.time() > timeout:
        break

    readingsSensors()

#with open("output.csv", "w") as f:
#    writer = csv.writer(f)
#    writer.writerows(dataArray)

print "Readings complete."
matrixData = []
for i in range(len(arrayTimestamp)):
    matrixData.append([arrayTimestamp[i], arrayLoudness[i], arrayMQ5[i]]) #, arrayTemperature[i], arrayHumidity[i], )

print " "
print "======="
print "REPORT:"
print "======="
print " "

meanMQ5 = mean(arrayMQ5)
minMQ5 = min(arrayMQ5)
maxMQ5 = max(arrayMQ5)
densityMQ5 = round(meanMQ5/1024, 6)
mindMQ5 = round(minMQ5/1024), 6)
maxdMQ5 = round(maxMQ5/1024), 6)

#print "RAW DATA TABLE:"
#print " "
#matrixRaw = matrixData
#matrixRaw.insert(0,["Time", "Temp", "Humidity", "Loudness", "MQ5"])
#table = AsciiTable(matrixRaw)
#print table.table
#print " "
#print "STATISTICS TABLE:"
#print " "
#round(mean(arrayMQ5),3)

tableStats = [["READING", "MIN", "MEAN", "MAX"], ["Loudness", min(arrayLoudness), round(mean(arrayLoudness),3), max(arrayLoudness)], ["MQ5", mindMQ5, densityMQ5, maxdMQ5]]
table = AsciiTable(tableStats) #["Temperature", min(arrayTemperature), round(mean(arrayTemperature),3), max(arrayTemperature)], ["Humidity", min(arrayHumidity), round(mean(arrayHumidity),3), max(arrayHumidity)], 
print table.table
