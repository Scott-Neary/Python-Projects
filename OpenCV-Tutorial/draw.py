import cv2 as cv
import numpy as np

# * uint8 = datatype of an image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. paint the image a certain colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

cv.waitKey(0)