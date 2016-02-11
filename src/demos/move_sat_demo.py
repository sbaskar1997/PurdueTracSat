#!/usr/bin/env python
import pigpio
import time
import Solenoids


def init_pi():
    # Function to initialize raspberry pi
    pi = pigpio.pi()
    return pi

def purge_pi(pi):
    pi.write(18,0)
    pi.write(23,0)
    pi.write(24,0)
    pi.write(25,0)
    pi.write(12,0)
    pi.write(16,0)
    pi.write(20,0)
    pi.write(21,0)

def move_satellite(time_flight  = 1):
    # Check if time to move is 0
    if (time_flight != 0):
        # Initialize pi and solenoid 1
        pi = init_pi()
	
	# Purge pi
	purge_pi(pi)
	
	# Initialize solenoids 1-4
        sol1 = Solenoids.sol1(pi)
        sol2 = Solenoids.sol2(pi)
	sol3 = Solenoids.sol3(pi)
	sol4 = Solenoids.sol4(pi)

	# Initialize time delay to physically move satellite
	# time.sleep(2)

        # Close solenoid 2 and 4
        sol1.close()
	sol2.close()
	sol3.close()
        sol4.close()

        # Open solenoid 2 and 4
        sol1.open()
	sol2.open()
	sol3.open()
        sol4.open()

	# Wait some time
	time.sleep(1.0)

	# Close Solenoids 2 and 4
	sol1.close()
	sol2.close()
	sol3.close()
	sol4.close()
	

move_satellite()
