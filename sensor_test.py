import random, time, grovepi, grove_i2c_temp_hum_mini
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
    th = grove_i2c_temp_hum_mini.th02()
    theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    theTemperature = th.getTemperature()
    theHumidity = th.getHumidity()
    theLoudness = grovepi.analogRead(sensorLoudness)
    theMQ5 = grovepi.analogRead(sensorMQ5)
    arrayTimestamp.append(theTime)
    arrayTemperature.append(theTemperature)
    arrayHumidity.append(theHumidity)
    arrayLoudness.append(theLoudness)
    arrayMQ5.append(theMQ5)
    timeRemaining = str(int(timeout - time.time() + .5))
    timeMessage = "Reading taken. " + timeRemaining + " seconds remaining."
    print timeMessage
    time.sleep(5)

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
    matrixData.append([arrayTimestamp[i], arrayTemperature[i], arrayHumidity[i], arrayLoudness[i], arrayMQ5[i]])

print " "
print "======="
print "REPORT:"
print "======="
print " "

#print "RAW DATA TABLE:"
#print " "
#matrixRaw = matrixData
#matrixRaw.insert(0,["Time", "Temp", "Humidity", "Loudness", "MQ5"])
#table = AsciiTable(matrixRaw)
#print table.table
#print " "
#print "STATISTICS TABLE:"
#print " "

tableStats = [["READING", "MIN", "MEAN", "MAX"], ["Temperature", min(arrayTemperature), round(mean(arrayTemperature),3), max(arrayTemperature)], ["Humidity", min(arrayHumidity), round(mean(arrayHumidity),3), max(arrayHumidity)], ["Loudness", min(arrayLoudness), round(mean(arrayLoudness),3), max(arrayLoudness)], ["MQ5", min(arrayMQ5), round(mean(arrayMQ5),3), max(arrayMQ5)]]
table = AsciiTable(tableStats)
print table.table
