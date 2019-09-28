import csv
import sys
import pandas as pd
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

data = str(data)

for i in range(len(data)):
    if data[i] == 'binary' or data[i] == '*':
        print("space")
        GPIO.output(4,False)
    elif data[i] == '1':
        print("flash")
        GPIO.output(4,True)
    elif data[i] == '0':
        GPIO.output(4,False)
        print("no flash")
    time.sleep(.1)




