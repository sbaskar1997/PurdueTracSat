import time
from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()

print("Move the motors forward freely for 1 second.")


gpg.forward()
time.sleep(1)
gpg.stop()
