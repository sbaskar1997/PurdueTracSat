#This code is meant to test the control system with manually inputted laser locations
#It is not integrated with actual laser sensors
#Location 0 is off of the laser array
import time
from easygopigo3 import EasyGoPiGo3
#Defining objects

gpg =EasyGoPiGo3()

servo = gpg.init_servo("SERVO2")
servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
keepWorking = True


while keepWorking:
    CLoc= int(input("Type in which detector the laser is on")) #Current laser detector the system is on
    PLoc = int(input("Type in which detector the laser was last on")) #Last laser detector the system was on
    if CLoc == 3: #if Laser is hitting center detector, don't move
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
        time.sleep(2)
        print("Laser on 3, no adjustment needed!")
    elif CLoc == 1 or CLoc == 2: #if Laser is hitting left detectors
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1700))
        print("Laser on detector ",CLoc)
        print("Moving CounterClockwise")
        time.sleep(2)
        #servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
    elif CLoc == 4 or CLoc == 5: #if Laser is hitting right detectors
        servo.gpg.set_servo(servo.gpg.SERVO_2,int(1300))
        print("Laser on detector ",CLoc)
        print("Moving Clockwise")
        time.sleep(2)
        #servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
    elif CLoc == 0: #If laser is not hitting any detectors
        if PLoc == 1 or PLoc == 2 or PLoc == 3: #If last detector with laser communications was 1,2,3
            servo.gpg.set_servo(servo.gpg.SERVO_2,int(1700))
            print("Laser off. It last was on detector ",PLoc)
            print("Moving CounterClockwise")
            time.sleep(2)
            #servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
        elif PLoc == 5 or PLoc ==4: #If laser exited the right side of the laser array
            servo.gpg.set_servo(servo.gpg.SERVO_2,int(1300))
            print("Laser off. It last was on detector",PLoc)
            print("Moving Clockwise")
            time.sleep(2)
            #servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
        elif PLoc == 0: #Initial Lock Code
            servo.gpg.set_servo(servo.gpg.SERVO_2,int(1700))
            print("Initial Lock")
            print("Moving CounterClockwise")
            time.sleep(2)
            #servo.gpg.set_servo(servo.gpg.SERVO_2,int(1490))
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
