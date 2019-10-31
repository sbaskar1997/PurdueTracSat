# Import native modules
import numpy as np
import cv2
import imutils
import argparse

class Camera:
    # Contructor
    def __init__(self, id):
        self._id = id

    # Open camera
    def read_distance(self):
        # Capture video from camera
        cap = cv2.VideoCapture(0)

        while(1):
            # Capture frame by frame
            ret, frame = cap.read()

            #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv2.imwrite('frame.jpg', frame)
            image = cv2.imread('frame.jpg')
            post_frame = self.circle_detect(image)



            # cv2.putText(image, '%.2fft' % (inches/12),
            # (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
            # 2.0, (0, 255, 0), 3)
            cv2.imshow('image', post_frame)

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
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 400)

        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")

            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                # only draw circle if it is small enough to be considered an actual object
                if (r < 70):
                    eta = 11.875/54;                # actual_distance/r_assoc (use one test case to calibrate correction factor)
                    offset = r * eta - 11.875;      # offset for moving object closer or greater
                    dist_act = 11.875 - offset      # subtract offset to reference distance
                    cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                    cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            # show the output image
            return output
        else:
            return image



camera = Camera('sat1')
camera.read_distance()
