import cv2 as cv
import numpy as np

# * uint8 = datatype of an image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# * (blank.shape[1]//2, blank.shape[0]//2) = coordinates of centre
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
# * (250,250) = coordinates of centre
# * 40 = radius (in pixels)
# * (0,0,255) = colour (red)
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text on an image
cv.putText(blank, 'Hello, my name is Scott!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)