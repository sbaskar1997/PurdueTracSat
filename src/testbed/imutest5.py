import time
import numpy as np
from easygopigo3 import EasyGoPiGo3
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

imu = InertialMeasurementUnit(bus="GPG3_AD1")
gpg = EasyGoPiGo3()
a = True
tinit = time.time()
xddotvec = []
xdotvec =[]
xvec = []
tvec =[]
while a ==True:
	gpg.forward()
	t=time.time() - tinit
	accel = imu.read_linear_acceleration()
	accelx = accel[0]
	xddotvec.append(accelx)
	tvec.append(t)
	vel = np.trapz(xddotvec,tvec)
	xdotvec.append(vel)
	dist = np.trapz(xdotvec,tvec)
	print(accelx,vel,dist)
	if(t>10):
		a=False
		gpg.stop()
	if(dist>1):
		a=False
		gpg.stop()
