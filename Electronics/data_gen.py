import csv
import random
import time
from gpiozero import LightSensor, Buzzer
from time import sleep

x_value = 0
total_1 = 0


fieldnames = ["x_value", "total_1", "total_2"]

ldr = LightSensor(4)

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
        }

        csv_writer.writerow(info)
        print(x_value, total_1)

        x_value += 1
        #total_1 = (random.randint(0,100)) / 100
        total_1 = ldr.value

    time.sleep(.1)