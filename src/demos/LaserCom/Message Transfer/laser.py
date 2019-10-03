import csv
import sys
import pandas as pd
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)
with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))



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
    time.sleep(1.3)



GPIO.output(4,True)
time.sleep(4)
GPIO.output(4,False)





