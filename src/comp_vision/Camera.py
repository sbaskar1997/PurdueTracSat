# Import native modules
import numpy as np
import cv2
import sys
import os

# Import custom modules
sys.path.append(os.path.join('../comp_vision/helper'))
from ThreadWorker import *


class Camera:
    # Contructor
    def __init__(self, id):
        self._id = id

    # Open camera
    def read_distance(self):
        # Capture video from camera
        cap = cv2.VideoCapture(0)

        # Create threads for circle detect and reading/writing images
        circle_detect_worker = Threader(self.circle_detect)
        read_and_write_worker = Threader(self.read_and_write)
        iteration = 0
        post_frame = None

        while(1):
            # Read and write each image from camera
            read_and_write_worker.start((cap,))
            image = read_and_write_worker.get_results()

            # Detect circle from image at every 25 frames
            circle_detect_worker.start((image,))

            #post_frame = self.circle_detect(image)
            if (iteration > 50) and not circle_det_ran:
                post_frame = circle_detect_worker.get_results()
                iteration = 0
                circle_det_ran = 1
            else:
                circle_det_ran = 0

            # If circle detection code ran, show image, if not do not show image
            if (post_frame is not None) and (circle_det_ran):
                cv2.imshow('image', post_frame)
            else:
                cv2.imshow('image', image)

            # Update frame count
            iteration = iteration + 1

            # Quit if prompted to quit (press q)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release and destroy everything when the simulation is over
        cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def circle_detect(image):
        # load the image, clone it for output, and then convert it to grayscale
        output = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect circles in the image
        circles_thread = Threader(cv2.HoughCircles)
        circles_thread.start((gray,cv2.HOUGH_GRADIENT, 1.2, 200,))
        circles = circles_thread.get_results()
        #circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 400)


        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")

            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                # only draw circle if it is small enough to be considered an actual object
                if (r < 200):
                    eta = 11.875/54;                # actual_distance/r_assoc (use one test case to calibrate correction factor)
                    offset = r * eta - 11.875;      # offset for moving object closer or greater
                    dist_act = 11.875 - offset      # subtract offset to reference distance
                    cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                    cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            # show the output image
            return output
        else:
            return image

    @staticmethod
    def read_and_write(cap):
        ret, frame = cap.read()
        cv2.imwrite('frame.jpg', frame)
        image = cv2.imread('frame.jpg')
        return image

camera = Camera('sat1')
camera.read_distance()
