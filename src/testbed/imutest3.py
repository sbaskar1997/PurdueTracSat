import time
import numpy as np
from easygopigo3 import EasyGoPiGo3
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

imu = InertialMeasurementUnit(bus= "GPG3_AD1")
print("This is the second test")
gpg = EasyGoPiGo3()
go = True 

tstart = time.time()
n = 0
fdist = 1
tvec = []
tvec.append(0)
xddotvec =[]
inac = imu.read_linear_acceleration()
inacx = inac[0]
#oldacx = inacx
xddotvec.append(inacx)
xdotvec =[]
tvvec=[]
tvvec.append(0)
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
	#if (accelx<0):
	#	accelx = abs(accelx)
	#print(accelx)
	xddotvec.append(accelx)
	t =time.time()-tstart
	tvec.append(t)
	vel = np.trapz(xddotvec,x=tvec)
	tv = time.time() -tstart
	xdotvec.append(vel)
	tvvec.append(tv)
	dist = np.trapz(xdotvec,x=tvvec)
	print(dist)
	xvec.append(dist)
	time.sleep(.25)
	if(dist>fdist):
		go = False
		print("Distance Stop")
	if(t>8):
		go =False 
		print("Time Stop")

gpg.stop()
print(dist)

