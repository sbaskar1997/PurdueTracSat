from serial import Serial

class lasercom():
    def uplink(self, port):
        ser = Serial(port, 9600)
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

        inputVectorString = inputVectorString[:-3]
        inputVectorString = inputVectorString.decode('utf-8')
        inputVector = inputVectorString.split(",")
        print("Received data:")
        print(inputVector)
        #inputVector = list(map(int,inputVector))
        return inputVector

    def downlink(self, port):
        return 1