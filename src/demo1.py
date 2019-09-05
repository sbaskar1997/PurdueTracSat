#!/usr/bin/env python
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

#Forward
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

#Wait
time.sleep(5)

#Stop
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
