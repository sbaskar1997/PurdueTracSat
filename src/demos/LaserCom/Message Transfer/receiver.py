import sys
import time
import RPi.GPIO as GPIO

#Flash receival interval
INTERVAL = .05

#Setup Raspberry Pi pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
threshold = .2
endTransmission = True
binaryArray = []
end = 0

#Loop until laser begins flashing
while endTransmission:
    if GPIO.input(17) > threshold:
        time.sleep(INTERVAL+.001) #Phase shift interval

        #Loop until message ends
        while endTransmission:
            binary = ""
            end = 0

            #Begin letter.
            for i in range(7):
                if GPIO.input(17) > threshold:
                    end+=1
                    binary += "1"
                    time.sleep(INTERVAL)
                elif GPIO.input(17) <= threshold:
                    binary += "0"
                    time.sleep(INTERVAL)
            #print(binary)     
            binaryArray.append(binary)
            time.sleep(INTERVAL)
            if end == 7:
                endTransmission = False
                break
            
            
#Convert binary array back into text.           
#print(binaryArray)
binaryString = ""
for j in range(len(binaryArray)-1):
    binaryString = binaryString + "0" + binaryArray[j]
n = int(binaryString, 2)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

