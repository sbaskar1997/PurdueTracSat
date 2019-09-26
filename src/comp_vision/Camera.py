# Import native modules
import numpy as np
import cv2 as cv
import imutils

class Camera:
    # Contructor
    def __init__(self, id, img_path = 'test_distance.jpg'):
        self._id = id
        self._img_path = img_path

    # Open camera
    def read_distance(self):
        # Capture video from camera
        cap = cv.VideoCapture(0)
        play = True
        while(play):
            # Capture frame by frame
            ret, frame = cap.read()

            # Do something to each frame here
            #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imwrite('frame.jpg', frame)
            image = cv.imread('frame.jpg')
            marker = self.find_marker(image)

            # Find distance to camera
            inches = self.distance_to_camera(11, 24, marker[1][0])

            # draw bounding box
            box = cv.cv.BoxPoints(marker) if imutils.is_cv2() else cv.boxPoints(marker)
            box = np.int0(box)
            cv.drawContours(image, [box], -1, (0,255,0), 2)
            cv.putText(image, '%.2fft' % (inches/12),
            (image.shape[1] - 200, image.shape[0] - 20), cv.FONT_HERSHEY_SIMPLEX,
            2.0, (0, 255, 0), 3)
            cv.imshow('image', image)

            # Quit if prompted to quit (press q)
            if cv.waitKey(1) & 0xFF == ord('q'):
                play = False

        # Release and destroy everything when the simulation is over
        cap.release()
        cv.destroyAllWindows()

    # Calibrate camera
    def calibrate(self):
        # Known info about paper
        known_distance = 24
        known_width = 11

        # Read image
        image = cv.imread(self._img_path)

        # Find the paper in the image
        marker = self.find_marker(image)

        # Calculate focal length of the camera
        focal_length = ((marker[1][0] * known_distance) / known_width)
        return focal_length

    # Find distance to object
    def distance_to_camera(self, known_width, focal_length, per_width):
        return (known_width * self.focal_length)/per_width

    @property
    def focal_length(self):
        # Known info about paper
        known_distance = 24
        known_width = 11

        # Read image
        image = cv.imread(self._img_path)

        # Find the paper in the image
        marker = self.find_marker(image)

        # Calculate focal length of the camera
        self._focal_length = ((marker[1][0] * known_distance) / known_width)
        return self._focal_length

    @focal_length.setter
    def focal_length(self, val):
        self._focal_length = val

    @staticmethod
    def find_marker(image):
        # Convert image to grayscale, blur it and detect edges (edged img output)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (5,5), 0)
        edged = cv.Canny(gray, 35, 125)

        # Find contours in edged image and keep largest one
        cnts = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key = cv.contourArea)

        # Compute the bounding box of the paper and return it
        return cv.minAreaRect(c)




camera = Camera('sat1')
camera.read_distance()
