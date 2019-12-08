import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
# Import custom modules
sys.path.append(os.path.join('../comp_vision/helper'))
from Camera import Camera
from ThreadWorker import *

def object_tracking(it_count = 10, default_loop = True):
    # Initialize camera object
    camera = Camera('sat1')

    # Start camera
    camera.start_camera()

    # Initialize loop parameters
    circle_detected = False         # Initialize variable to break loop
    iteration = 0                   # Iterator to determine whether or not to run circle detect code
    #center = None
    s =1
    tinit = time.time()
    xpos = np.array([])
    ypos = np.array([])
    t = np.array([])
    detection = 0
    
    # Initialize worker threads to parallelize code
    circle_detect_worker = Threader(camera.circle_detect)
    read_and_write_worker = Threader(camera.read_and_write)
    
        
    if (default_loop):
        while(detection<50):
            # Read and write images from camera
            read_and_write_worker.start()
            image = read_and_write_worker.get_results()

            # Check whether or not to run circle detection code
            if (iteration > it_count):
                circle_detect_worker.start((image,))
                [output_image, circle_detected, center, dist_read] = circle_detect_worker.get_results()
                
                iteration = 0
            else:
                output_image = image

            # If circle detected, append position data to 
            if (circle_detected):
                detection = detection +1
                tcurrent = time.time() - tinit
                c1 = center[0]
                c2 = center[1]
                xcur = c1
                ycur = c2
                t = np.append(t, tcurrent)
                xpos = np.append(xpos, xcur)
                ypos = np.append(ypos, ycur)
                

            # Increment iteration
            iteration += 1
    else:
        circle_detect_worker1 = Threader(camera.circle_detect)
        read_and_write_worker1 = Threader(camera.read_and_write)
        read_and_write_worker1.start()
        image = read_and_write_worker1.get_results()
        circle_detect_worker1.start((image,))
        [output_image, circle_detected, center, dist_read] = circle_detect_worker1.get_results()
    
    camera.stop_camera()
    print(len(xpos), len(ypos), len(t))
    plt.plot(xpos,ypos)
    plt.title('X-Y Plot')
    plt.show()
    plt.figure()
    plt.plot(t,xpos)
    plt.title('X versus Time')
    plt.show()
    plt.figure()
    plt.plot(t,ypos)
    plt.title('Y versus Time')
    plt.show()
#     if circle_detected:
#         return [circle_detected, center, dist_read]
#     else:
#         return [circle_detected, center, dist_read]
object_tracking()
