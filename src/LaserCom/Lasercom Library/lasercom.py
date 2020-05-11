from serial import Serial
import time 

class lasercom():

    #The uplink function is used to read an array of data received by the lasercom system
    def receiveCommand(self, port):
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

    # Stream of live data from serial buffer. 
    def receiveData(self,port):
        ser = Serial(port, 9600)
        #ser.flushInput()
        time.sleep(1)
        while True:
            bytesToRead = ser.inWaiting()
            print(ser.readline(bytesToRead).strip())
            time.sleep(.1)
            

    # the Downlink function sends an array of data into the lasercom system
    def sendData(self, port, data):
        ser = Serial(port, 9600)
        #ser.flushInput()
        data = "<" + data + ">"
        print(ser.readline())
        ser.write(data.encode())
        print(ser.readline())
        ser.close()

    # Resets the lasercom system and turns off the laser.
    def resetArduino(self, port):
        ser = Serial(port, 9600)
        #ser.flushInput()
        ser.write(b'0')



# Required for reading live data.
class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

