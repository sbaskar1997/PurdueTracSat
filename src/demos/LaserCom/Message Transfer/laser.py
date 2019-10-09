import csv
import sys
import pandas as pd
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)

if len(sys.argv) < 2:
    print("Usage: python data_to_binary.py [MESSAGE]")
    sys.exit(1)

INTERVAL = .05

messageArray = sys.argv[1:]
message = ' '.join(messageArray)
print("Message: " + message)
messageStringBinary = ' '.join(format(ord(x), 'b') for x in message)
messageArrayBinary = messageStringBinary.split(" ")
print(messageArrayBinary)
data = ["binary"]
for i in range(len(messageArrayBinary)):
    messageArrayBinary[i] = str(messageArrayBinary[i]).zfill(7)
    for j in range(len(list(messageArrayBinary[i]))):
        if j == len(list(messageArrayBinary[i])) - 1 and i != len(messageArrayBinary) - 1:
            digit = list(messageArrayBinary[i])[j]
            data.append(digit)
            data.append('*')
        else:
            digit = list(messageArrayBinary[i])[j]
            data.append(digit)
            


for i in range(len(data)):
    #print(data[i])
    if "binary" in data[i]:
        #print("start" + str(i))
        GPIO.output(4,True)
    elif "1" in data[i]:
        #print("flash"+ str(i))
        GPIO.output(4,True)
    elif "0" in data[i]:
        GPIO.output(4,False)
        #print("no flash"+ str(i))
    else:
        #print("space"+ str(i))
        GPIO.output(4,False)
    time.sleep(INTERVAL)



GPIO.output(4,True)
time.sleep(4)
GPIO.output(4,False)





