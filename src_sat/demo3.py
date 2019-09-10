#!/usr/bin/env python
import rospy
from  std_msgs.msg import Float32MultiArray
import pigpio
import time

pi = pigpio.pi()
pi.write(18,0) #SOL1 Open
pi.write(23,0) #SOL1 Close
pi.write(24,0) #SOL2 Open
pi.write(25,0) #SOL2 Close
pi.write(12,0) #SOL3 Open
pi.write(16,0) #SOL3 Close
pi.write(20,0) #SOL4 Open
pi.write(21,0) #SOL4 Close

init = False

def stop():
        print('stop')
        pi.write(12,1)
	pi.write(20,1)
	time.sleep(.02)
	pi.write(12,0)
	pi.write(20,0)

	time.sleep(2)

	pi.write(16,1)
	pi.write(21,1)
	time.sleep(.02)
	pi.write(16,0)
	pi.write(21,0)
	pi.stop()
	ros.shutdown()

def process(data):
        n = 0
        j = 0
        for i in data.data:
                if i < .5 and i != 0:
                        n = n + 1
                        if n > 10:
                                j = j + 1
                                n = 0
                else:
                        n = 0
        if j > 5:
                stop()

def initMove():
	print("Moving forward")
	pi.write(18,1)
	pi.write(24,1)
	time.sleep(.02)
	pi.write(18,0)
	pi.write(24,0)

	time.sleep(2)

	pi.write(23,1)
	pi.write(25,1)
	time.sleep(.02)
	pi.write(23,0)
	pi.write(25,0)
	
	init = True

if __name__=='__main__':
	if init == False:
		initMove()

	print("Starting LIDAR")

        rospy.init_node('demo3')

        sub=rospy.Subscriber('arr', Float32MultiArray, process)

        rospy.spin()
