import time
import numpy as np
from easygopigo3 import EasyGoPiGo3
from di_sensors.easy_inertial_measurement_unit import EasyIMUSensor
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

print("This is the calibration function")
imu = EasyIMUSensor("AD1")

imu.safe_calibrate()

