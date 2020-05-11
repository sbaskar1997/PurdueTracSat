import time
from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()

print("This is the second test code")

time.sleep(5)
gpg.forward()
time.sleep(3)
gpg.stop()
time.sleep(.5)
gpg.backward()
time.sleep(3)
gpg.stop()
