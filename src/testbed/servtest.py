import time
from easygopigo3 import EasyGoPiGo3

gpg =EasyGoPiGo3()

servo = gpg.init_servo("SERVO2")

servo.gpg.set_servo(servo.gpg.SERVO_2,int(1700))

time.sleep(2)

servo.gpg.set_servo(servo.gpg.SERVO_2,int(1485))
