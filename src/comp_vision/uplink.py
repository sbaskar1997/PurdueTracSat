from easygopigo3 import EasyGoPiGo3
from time import time, sleep
from serial import Serial
import Camera


ser = Serial('/dev/ttyACM0', 9600)
dataArray = []
i = -1
correct = 0
while (correct <= 3):
    if (ser.inWaiting()>0):
        dataArray.append(ser.readline())
        i = i + 1
    if i >= 2 and dataArray[i] == dataArray[i-1]:
        inputVectorString = dataArray[i]
        correct = correct + 1

inputVectorString = inputVectorString[:-4]
inputVectorString = inputVectorString.decode('utf-8')
inputVector = inputVectorString.split(",")
print(inputVector)

inputVector = list(map(int,inputVector))

gpg = EasyGoPiGo3()
#inputVector = [1, 100, 90, 50]
#arr = [option,vertical distance, angle, horizontal distance]
if inputVector[0] == 1:
    gpg.drive_cm(inputVector[1])
    gpg.turn_degrees(inputVector[2])
    gpg.drive_cm(inputVector[3])
    gpg.turn_degrees(-1*inputVector[2])
elif inputVector[0] == 2:
    gpg.turn_degrees(inputVector[2])
    gpg.drive_cm(inputVector[3])
    gpg.turn_degrees(-1*inputVector[2])
    gpg.drive_cm(inputVector[1])

print('dante done')
cam = Camera.Camera('oh god')
cam.read_distance()

