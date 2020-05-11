import sys
import os

# Import custom modules
sys.path.append(os.path.join('../comp_vision/helper'))
from Camera import Camera
from ThreadWorker import *


def detection_demo(it_count = 10, infinite_loop = 1):
    # Initialize camera object
    camera = Camera('sat1')

    # Start camera
    camera.start_camera()

    # Initialize loop parameters
    circle_detected = False         # Initialize variable to break loop
    iteration = 0                   # Iterator to determine whether or not to run circle detect code

    # Initialize worker threads to parallelize code
    circle_detect_worker = Threader(camera.circle_detect)
    read_and_write_worker = Threader(camera.read_and_write)
    
        
    if infinite_loop:
        while(1):
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

            # If circle detected break loop
            if (circle_detected):
                break

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
    if circle_detected:
        return [circle_detected, center, dist_read]
    else:
        return [circle_detected, center, dist_read]

