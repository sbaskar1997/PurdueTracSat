import time
import numpy as np
from easygopigo3 import EasyGoPiGo3
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

imu = InertialMeasurementUnit(bus= "GPG3_AD1")
print("This is the test")
gpg = EasyGoPiGo3()
go = True 

tstart = time.time()
n = 0
fdist = 1
tvec = []
tvec.append(0)
xddotvec =[]
xddotvec.append(0)
xdotvec =[]
xdotvec.append(0)
xvec  =[]
xvec.append(0)
while go == True:
	n = n +1
	#print(t)
	gpg.forward()
	gyro = imu.read_gyroscope()
	accel = imu.read_linear_acceleration()
	accelx = accel[0]
	xddotvec.append(accelx)
	t =time.time()-tstart
	tvec.append(t)
	vel = np.trapz(xddotvec,x=tvec)
	xdotvec.append(vel)
	dist = np.trapz(xdotvec,x=tvec)
	xvec.append(dist)
	if(dist>fdist):
		go = False
		print("Distance Stop")
	if(t>15):
		go =False 
		print("Time Stop")

gpg.stop()
print(dist)

