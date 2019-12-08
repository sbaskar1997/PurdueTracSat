import time
import numpy as np
from easygopigo3 import EasyGoPiGo3
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

imu = InertialMeasurementUnit(bus="GPG3_AD1")
gpg = EasyGoPiGo3()
a = True
told = time.time()
rotratevec = np.array([])
avec = np.array([])
tvec = np.array([])
gyroold = 0
speed = 90
goal = 360
gpg.set_speed(speed)
while a ==True:
    gpg.left()
    t=time.time() - told
    gyro = imu.read_gyroscope()
    rotationy = gyro[2]
    if rotationy == gyroold:
       gyroold = rotationy
       angle = 0
       #told = time.time()
    else:
       #rotationy = gyro[1] #Rotation in y direction (vertical)
       t = time.time() - told
       rotratevec=np.append(rotratevec,rotationy)
       tvec=np.append(tvec,t)
       angle = np.trapz(rotratevec,tvec)
       #avec=np.append(avec,angle)
       print(rotationy,angle)
       gyroold = rotationy
       #told = time.time()
    if(t>15):
        a=False
        gpg.stop()
    if(angle>goal):
        a=False
        gpg.stop()
