import sys
import time
import RPi.GPIO as GPIO

INTERVAL = .05

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
threshold = .2
endTransmission = True
binaryArray = []
end = 0

while endTransmission:
    if GPIO.input(17) > threshold:
        #print("start")
        time.sleep(INTERVAL+.001)
        while endTransmission:
            binary = ""
            end = 0
            #print("word start")
            for i in range(7):
                if GPIO.input(17) > threshold:
                    end+=1
                    binary += "1"
                    #print("flash")
                    time.sleep(INTERVAL)
                elif GPIO.input(17) <= threshold:
                    binary += "0"
                    #print("no flash")
                    time.sleep(INTERVAL)
            #(binary)     
            binaryArray.append(binary)
            time.sleep(INTERVAL)
            if end == 7:
                endTransmission = False
                break
            
            
            
#print(binaryArray)
binaryString = ""
for j in range(len(binaryArray)-1):
    binaryString = binaryString + "0" + binaryArray[j]
n = int(binaryString, 2)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

