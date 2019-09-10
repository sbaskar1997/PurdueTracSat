#!/usr/bin/env python
import pigpio
import time
from Solenoids import *


def init_pi():
    # Function to initialize raspberry pi
    pi = pigpio.pi()
    return pi

def move_satellite_sol1(flight_time):
    # Check if time to move is 0
    if (time != 0):
        # Initialize pi and solenoid 1
        pi = init_pi()
        sol1 = sol1(pi)

        # Open solenoid 1
        sol1.open()

        # Wait some time
        time.sleep(flight_time)

        # Close solenoid 1
        sol1.close()
