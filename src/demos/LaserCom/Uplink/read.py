from serial import Serial

ser = Serial('/dev/tty.usbmodem14301', 9600)
dataArray = []
i = -1;
correct = 0;
while (correct <= 3):
    if (ser.inWaiting()>0):
        dataArray.append(ser.readline().decode())
        i = i + 1
    if i >= 2 and dataArray[i] == dataArray[i-1]:
        inputVectorString = dataArray[i]
        correct = correct + 1
    

inputVectorString = inputVectorString[:-3]
inputVector = inputVectorString.split(",")
print(inputVector)