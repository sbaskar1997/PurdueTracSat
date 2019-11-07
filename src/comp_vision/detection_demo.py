# Import native modules
from easygopigo3 import EasyGoPiGo3
import time

gpg = EasyGoPiGo3()

gpg.forward()
time.sleep(5)
gpg.stop()
