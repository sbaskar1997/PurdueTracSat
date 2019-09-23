#!usr/bin/env python
# Import native modules
from imutils import paths
import numpy as np
import imutils
import cv2

def find_marker(image):
    # Convert image to grayscale, blur it and detect edges (edged img output)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edged = cv2.Canny(gray, 35, 125)

    # Find contours in edged image and keep largest one
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key = cv2.contourArea)

    # Compute the bounding box of the paper and return it
    return cv2.minAreaRect(c)

def distance_to_camera(known_width, focal_length, per_width):
    return (known_width * focal_length)/per_width


# Known info about paper
known_distance = 24
known_width = 11

# Read image
image = cv2.imread('test_distance.jpg')

# Find the paper in the image
marker = find_marker(image)

# Calculate focal length of the camera
focal_length = ((marker[1][0] * known_distance) / known_width)

# Find distance to camera
inches = distance_to_camera(known_width, focal_length, marker[1][0])

# draw bounding box
box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
box = np.int0(box)
cv2.drawContours(image, [box], -1, (0,255,0), 2)
cv2.putText(image, '%.2fft' % (inches/12),
(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
2.0, (0, 255, 0), 3)
cv2.imshow('image', image)
cv2.waitKey(3000)
