import time
from easygopigo3 import EasyGoPiGo3
gpg = EasyGoPiGo3()
print("This code has the robot make a half circle")
time.sleep(5)
gpg.drive_cm(100)
gpg.stop()
time.sleep(1)
gpg.orbit(-180,50)
gpg.stop()
gpg.turn_degrees(180)
time.sleep(1)
gpg.orbit(180,50)
time.sleep(1)
gpg.drive_cm(100)
gpg.stop()
gpg.turn_degrees(180)

