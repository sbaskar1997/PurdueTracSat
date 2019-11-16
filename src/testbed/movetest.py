import time
from easygopigo3 import EasyGoPiGo3

gpg =EasyGoPiGo3()

gpg.forward()
time.sleep(1)
gpg.stop()


