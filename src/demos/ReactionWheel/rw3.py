import time
import sys
import pigpio

#Connect
pi = pigpio.pi()

#Initialize
#time.sleep(2)
#print("Start init")
#pi.set_servo_pulsewidth(17,1900)
#time.sleep(3)
#pi.set_servo_pulsewidth(17,1100)
#time.sleep(3)
#print("init done")
#time.sleep(3)

time.sleep(2)
pi.set_servo_pulsewidth(17,1100)
time.sleep(2)

#Forward
print("for")

pi.set_servo_pulsewidth(17,1800)
time.sleep(8)

#Stop
print("stop")
pi.set_servo_pulsewidth(17,1100)
time.sleep(4)

#Turn off

pi.set_servo_pulsewidth(17,1100)

pi.stop()
