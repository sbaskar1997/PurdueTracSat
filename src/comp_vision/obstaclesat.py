#Code for porting testbed object avoidance demo to CubeSat+Base
#!usr/bin/env python
# Import native modules
import numpy as np
import time

# Import custom modules
from Camera import Camera
#from easygopigo3 import EasyGoPiGo3
from detection_demo import detection_demo
from ThreadWorker import *
import pigpio 
import Solenoids

def init_pi():
    pi = pigpio.pi()
    return(pi)

def purge_pi(pi):
    ports =[18,23,24,25,12,16,20,21]
    for n in ports:
         pi.write(n,0)
def move_forward(time_flight = 1):
    tstart = time.time()
    if (time_flight != 0):
        pi = init_pi()
        purge_pi(pi)
        #Initialize Solenoids 1-2
        sol1 = Solenoids.sol1() #solenoid to move forward force
        sol2 = Solenoids.sol2() #solenoid to provide backward force
        #start with Solenoids closed
        sol1.close()
        sol2.close()
    #Open solenoid 1
        sol1.open()
   return(tstart)
def stop(tnow)
   tbrake = time.time()
   sol1.close()
   while ((time.time()-tbrake)<tnow):
    #sol1.close()
    sol2.open()
    
   sol2.close()

def obstaclesat():
 
    tstart = move_forward()  
    [circle_detected, center, obj_distance] = detection_demo()
 
    #if (center[0] > 320):
      #  direction = 'right'
     #   rotate_dir = -1
    #else:
        #direction = 'left'
        #rotate_dir = 1
    
    while (circle_detected):
        tnow = tstart - time.time() #find time to keep braking solenoid on
        [circle_detected, center, obj_distance] = detection_demo(infinite_loop = False)
        stop(tnow) #use stop function

    #Close all solenoids after ten seconds
    time.sleep(10)
    sol1.close()
    sol2.close()

 
obstaclesat()
        
        


