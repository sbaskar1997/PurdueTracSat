from PIL import Image
from numpy import asarray
import cv2
import numpy as np
from numpy import *



### IMAGE
# "data" is an numpy array that can be reconverted into image "new_image" using fromarray(data)
# load the image
image_old = Image.open('tracsat.jpg')

# convert image to numpy array
data = asarray(image_old)
print(type(data))

# create Pillow image
image_new = Image.fromarray(data)
print(type(image_new))

# summarize image details
print(image_new.mode)
print(image_new.size)

print(data)


### VIDEO
vid = cv2.VideoCapture('test.mp4')
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 800,800)

while(vid.isOpened()):
    ret, frame = vid.read()
    #np_frame = cv2.imread('video', frame) # does not work
    #np_frame = np.asarray(cv2.GetMat(frame)) # does not work
    #print(np_frame.shape)
    print(frame.shape)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()