import time
from easygopigo3 import EasyGoPiGo3

gpg =EasyGoPiGo3()

gpg.drive_cm(30,True)
time.sleep(1)
gpg.stop()


