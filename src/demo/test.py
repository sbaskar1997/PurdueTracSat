#!/usr/bin/env python
import rospy
from  std_msgs.msg import Float32MultiArray
import pigpio
import time

pi = pigpio.pi()
pi.write(17,0)

def stop():
	#print('stop')
	pi.write(17,1)
	time.sleep(.01)
	pi.write(17,0)

def process(data):
	#print(len(data.data))
	n = 0
	j = 0
	for i in data.data:
		if i < .1 and i != 0:
			n = n + 1
			if n > 10:
				j = j + 1
				n = 0
		else:
			n = 0
	if j > 5:
		stop()

if __name__=='__main__':
	rospy.init_node('test')

	sub=rospy.Subscriber('arr', Float32MultiArray, process)

	rospy.spin()



