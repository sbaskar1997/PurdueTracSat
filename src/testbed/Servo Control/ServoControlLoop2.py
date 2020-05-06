
#This code is meant to test the control system with manually inputted laser locations
#It is not integrated with actual laser sensors
#Location 0 is off of the laser array
import time
from easygopigo3 import EasyGoPiGo3
import RPi.GPIO as GPIO
#Defining objects

gpg =EasyGoPiGo3()

servo = gpg.init_servo("SERVO2")
servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
keepWorking = True
GPIO.setmode(GPIO.BOARD)
#setup gpio pins
#Sensor Numbers are Connected to the Numbered Pins as follows
sensor1 = 37 #need to be replaced
sensor2= 35
sensor3 = 33
sensor4 = 31
sensor5 = 36
sensorlist = [sensor1,sensor2,sensor3,sensor4,sensor5]
GPIO.setup(sensorlist,GPIO.IN)
CLoc = 0
PLoc = 0
while keepWorking:
    a = GPIO.input(sensor1)
    b = GPIO.input(sensor2)
    c = GPIO.input(sensor3)
    d = GPIO.input(sensor4)
    e = GPIO.input(sensor5)
    if (CLoc != 0):
       PLoc = CLoc

    if (a==True):
        CLoc= 1
    elif (b==True):
        CLoc = 2
    elif (c==True):
        CLoc = 3
    elif (d==True):
        CLoc = 4
    elif (e==True):
        CLoc = 5
    else:
        CLoc = 0
    
    if CLoc == 3: #if Laser is hitting center detector, don't move
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
        time.sleep(2)
        print("Laser on 3, no adjustment needed!")
    elif CLoc == 1 or CLoc == 2: #if Laser is hitting left detectors
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1300))
        print("Laser on detector ",CLoc)
        
    elif CLoc == 4 or CLoc == 5: #if Laser is hitting right detectors
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1700))
        print("Laser on detector ",CLoc)
        
    elif CLoc == 0: #If laser is not hitting any detectors
        if PLoc == 1 or PLoc == 2 or PLoc == 3: #If last detector with laser communications was 1,2,3
            servo.gpg.set_servo(servo.gpg.SERVO_2,int(1300))
            print("Laser off. It last was on detector ",PLoc)
            
        elif PLoc == 5 or PLoc ==4: #If laser exited the right side of the laser array
            servo.gpg.set_servo(servo.gpg.SERVO_2,int(1700))
            print("Laser off. It last was on detector",PLoc)
            
        elif PLoc == 0: #Initial Lock Code
            servo.gpg.set_servo(servo.gpg.SERVO_2,int(1700))
            print("Initial Lock")
            print("Moving CounterClockwise")
        else:
            print("PLoc Error")
            keepWorking= False
            servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
    elif CLoc == 7:
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
        keepWorking = False
    else:
        print("CLoc Error")
        keepWorking = False
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
        
print("Code Done")
