import sys
import time
import RPi.GPIO as GPIO
from gpiozero import LightSensor
ldr = LightSensor(17)


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,False)
threshold = .2
endTransmission = True
binaryArray = []
end = 0

while endTransmission:
    if ldr.value > threshold:
        #print("start")
        time.sleep(1.5)
        while endTransmission:
            binary = ""
            end = 0
            #print("word start")
            for i in range(7):
                if ldr.value > threshold:
                    end+=1
                    binary += "1"
                    #print("flash")
                    time.sleep(1.3)
                elif ldr.value <= threshold:
                    binary += "0"
                    #print("no flash")
                    time.sleep(1.3)
            print(binary)     
            binaryArray.append(binary)
            time.sleep(1.3)
            if end == 7:
                endTransmission = False
                break
            
            
            
#print(binaryArray)
binaryString = ""
for j in range(len(binaryArray)-1):
    binaryString = binaryString + "0" + binaryArray[j]
n = int(binaryString, 2)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

