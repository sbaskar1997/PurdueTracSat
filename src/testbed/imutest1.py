import time
from easygopigo3 import EasyGoPiGo3
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

imu = InertialMeasurementUnit(bus= "GPG3_AD1")
print("Hello!")

while True:

	gyro = imu.read_gyroscope()
	accel = imu.read_accelerometer()

	string_to_print = "Gyro: X: {:.1f} Y: {:.1f} Z: {:.1f} " \
			 "Accel: X: {:.1f} Y: {:.1f} Z: {:.1f} " .format(gyro[0], gyro[1], gyro[2],
									accel[0],accel[1],accel[2])
	print(string_to_print)
	time.sleep(.1)


