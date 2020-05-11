import time
import numpy as np
from easygopigo3 import EasyGoPiGo3
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

imu = InertialMeasurementUnit(bus="GPG3_AD1")
gpg = EasyGoPiGo3()
a = True
tinit = time.time()
xddotvec = np.array([])

xdotvec = np.array([])
xvec = np.array([])
tvec = np.array([])
speed = 150
gpg.set_speed(speed)
aold = 0
dist = 0
while a ==True:
    gpg.forward()
    t=time.time() - tinit
    accel = imu.read_linear_acceleration()
    accelx = accel[1]
    if accelx == aold:
       aold = accelx
    else:
       t = time.time() - tinit
       xddotvec=np.append(xddotvec,accelx)
       tvec=np.append(tvec,t)
       vel = np.trapz(xddotvec,tvec)
       xdotvec=np.append(xdotvec,vel)
       dist = np.trapz(xdotvec,tvec)
       print(accelx,vel,dist)
       aold = accelx
    if(t>10):
        a=False
        gpg.stop()
    if(dist>1):
        a=False
        gpg.stop()
