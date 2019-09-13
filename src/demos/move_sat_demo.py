#!/usr/bin/env python
import pigpio
import time
import Solenoids


def init_pi():
    # Function to initialize raspberry pi
    pi = pigpio.pi()
    return pi

def move_satellite():
    time.sleep(30)
    # Check if time to move is 0
    if (time != 0):
        # Initialize pi and solenoid 1
        pi = init_pi()
        sol1 = Solenoids.sol1(pi)
        sol2 = Solenoids.sol2(pi)

        # Open solenoid 1 and 2
        sol1.open()
        sol2.open()

        # Wait some time
        time.sleep(2)

        # Close solenoid 1 and 2
        sol1.close()
        sol2.close()

move_satellite()
