#Code for porting testbed object avoidance demo to CubeSat+Base
#!usr/bin/env python
# Import native modules
import numpy as np
import time
import sys
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
def move_forward(sol1,sol2):    
        #Initialize Solenoids 1-2
        #sol1 = Solenoids.sol1() #solenoid to move forward force
        #sol2 = Solenoids.sol2() #solenoid to provide backward force
        #start with Solenoids closed
    sol1.close()
    sol2.close()
    time.sleep(.5)
    #Open solenoid 1
    trun = 1.5
    sol1.open()
    time.sleep(trun)
    sol1.close()
        #
   #return(tstop)
def stop(sol1,sol2)
   #tbrake = time.time()
   
   sol1.close()
   sol2.open()
   time.sleep(1.5)
   sol2.close()

#def turnright()
  #  time.sleep(.5)
#    pi.set_servo_pulsewidth(17,1800)
 #   time.sleep(2)
  #  pi.set_servo_pulsewidth(17,1100)
def obstaclesat():
    pi = init_pi()
    purge_pi(pi)
    sol1 = Solenoids.sol1() #solenoid to move forward force
    sol2 = Solenoids.sol2() #solenoid to provide backward force
    pi.set_servo_pulsewidth(17,1100)  
    move_forward(sol1,sol2)  
    [circle_detected, center, obj_distance] = detection_demo()
    
    
    #if (center[0] > 320):
      #  direction = 'right'
     #   rotate_dir = -1
    #else:
        #direction = 'left'
        #rotate_dir = 1
    first_iteration= True
    while(circle_detected):
        #tnow = tstart - time.time() #find time to keep braking solenoid on
        
        [circle_detected, center, obj_distance] = detection_demo(infinite_loop = False)
        if first_iteration:
            stop(sol1,sol2) #use stop function
            first_iteration = False
        else:
            pi.set_servo_pulsewidth(17,1800)
            time.sleep(2)
            pi.set_servo_pulsewidth(17,1100)
    #Close all solenoids after ten seconds
    pi.set_servo_pulsewidth(17,1100)
    time.sleep(5)
    sol1.close()
    sol2.close()

 
obstaclesat()
        
        


