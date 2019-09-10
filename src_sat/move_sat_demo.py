#!/usr/bin/env python
import pigpio
import time
from Solenoids import *


def init_pi():
    # Function to initialize raspberry pi
    pi = pigpio.pi()
    return pi

def move_satellite(flight_time):
    # Check if time to move is 0
    if (time != 0):
        # Initialize pi and solenoid 1
        pi = init_pi()

        sol1 = sol1(pi)
        sol2 = sol2(pi)

        # Open solenoid 1 and 2
        sol1.open()
        sol2.open()

        # Wait some time
        time.sleep(flight_time)

        # Close solenoid 1 and 2
        sol1.close()
        sol2.close()
