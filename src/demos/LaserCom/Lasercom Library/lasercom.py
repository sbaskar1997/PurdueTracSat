from serial import Serial

class lasercom():

    #The uplink function is used to read an array of data received by the lasercom system
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

    # the Downlink function sends an array of data into the lasercom system
    def downlink(self, port, data):
        ser = Serial(port, 9600)
        data = "<" + data + "#>"
        print(ser.readline())
        ser.write(data.encode())
        print(ser.readline())
        ser.close()

    # Resets the lasercom system and turns off the laser.
    def resetArduino(self, port):
        ser = Serial(port, 9600)
        ser.write(b'0')