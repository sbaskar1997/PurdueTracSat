#!usr/bin/env python
# Import native modules
import numpy as np
import time

# Import custom modules
from Camera import Camera
from easygopigo3 import EasyGoPiGo3
from detection_demo import detection_demo
from ThreadWorker import *

def obstacle():
    
    # Initialize testbed motors
    gpg = EasyGoPiGo3()
    gpg.forward()
    [circle_detected, center, obj_distance] = detection_demo()
    gpg.stop()
    if (center[0] > 320):
        direction = 'right'
        rotate_dir = -1
    else:
        direction = 'left'
        rotate_dir = 1
 
    # Rotate camera gradually until object is no longer detected
    angle_rotated = 0
    
    while (circle_detected):
        gpg.turn_degrees(rotate_dir * 10)
        [circle_detected, center, obj_distance] = detection_demo(infinite_loop = False)
        angle_rotated += 10

    # Final turn to avoid grazing object after circle no longer in view
    gpg.turn_degrees(rotate_dir * 20)        
    gpg.forward()
    time.sleep(5)
    gpg.stop()
    

        
obstacle()
        
        


