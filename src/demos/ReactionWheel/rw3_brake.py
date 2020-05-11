import time
import sys
import pigpio

#Connect
pi = pigpio.pi()

#Initialize

pi.set_servo_pulsewidth(17,1900)

text = raw_input("Enter go when ready:")

if text == "go":
	pi.set_servo_pulsewidth(17,1100)

text = raw_input("Enter stop when ready:")
