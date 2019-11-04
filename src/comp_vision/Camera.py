# Import native modules
import numpy as np
import cv2
import imutils
import argparse
import threading
import time

class Camera:
    # Contructor
    def __init__(self, id):
        self._id = id

    # Open camera
    def read_distance(self):
        # Capture video from camera
        cap = cv2.VideoCapture(0)

        # Create threads for circle detect and reading/writing images
        start = time.time()
        circle_detect_worker = ThreadWorker(self.circle_detect)
        read_and_write_worker = ThreadWorker(self.read_and_write)
        iteration = 0
        post_frame = None

        while(1):
            # Read and write each image from camera
            read_and_write_worker.start((cap,))
            image = read_and_write_worker.get_results()

            # Detect circle from image
            circle_detect_worker.start((image,))
            #post_frame = self.circle_detect(image)
            if (iteration > 50):
                post_frame = circle_detect_worker.get_results()
                iteration = 0
                circle_det_ran = 1
            else:
                circle_det_ran = 0



            # cv2.putText(image, '%.2fft' % (inches/12),
            # (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
            # 2.0, (0, 255, 0), 3)
            if (post_frame is not None) and (circle_det_ran):
                cv2.imshow('image', post_frame)
            else:
                cv2.imshow('image', image)
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
        circles_thread = ThreadWorker(cv2.HoughCircles)
        circles_thread.start((gray,cv2.HOUGH_GRADIENT, 1.2, 150,))
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
                if (r < 100):
                    print(r)
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

        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv2.imwrite('frame.jpg', frame)
        image = cv2.imread('frame.jpg')
        return image


class ThreadWorker():
    '''
    The basic idea is given a function create an object.
    The object can then run the function in a thread.
    It provides a wrapper to start it,check its status,and get data out the function.
    '''
    def __init__(self,func):
        self.thread = None
        self.data = None
        self.func = self.save_data(func)

    def save_data(self,func):
        '''modify function to save its returned data'''
        def new_func(*args, **kwargs):
            self.data=func(*args, **kwargs)

        return new_func

    def start(self,params = None):
        self.data = None
        if self.thread is not None:
            if self.thread.isAlive():
                return 'running' #could raise exception here

        #unless thread exists and is alive start or restart it
        if params is not None:
            self.thread = threading.Thread(target=self.func,args=params)
        else:
            self.thread = threading.Thread(target=self.func)
        self.thread.start()
        return 'started'

    def status(self):
        if self.thread is None:
            return 'not_started'
        else:
            if self.thread.isAlive():
                return 'running'
            else:
                return 'finished'

    def get_results(self):
        if self.thread is None:
            return 'not_started' #could return exception
        else:
            if self.thread.isAlive():
                self.thread.join()
                return self.data
            else:
                return self.data


camera = Camera('sat1')
camera.read_distance()
