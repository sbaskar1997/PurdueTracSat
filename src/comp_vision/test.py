#!/usr/bin/env python
import cv2 as cv
import numpy as np


# Capture video from camera
cap = cv.VideoCapture(0)

while(1):
    # Capture frame by frame
    ret, frame = cap.read()

    # Change frame to gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Show frame
    cv.imshow('frame', gray)

    # Quit if prompted to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release and destroy everything when the simulation is over
cap.release()
cv.destroyAllWindows()



# Function to find distance of something
