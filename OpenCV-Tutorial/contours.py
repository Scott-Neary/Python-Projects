# Contour Detection
import cv2 as cv 
import numpy as np 

# * Contours are the boundaries of objects
# * Useful for shape analysis, object detection and recognition

img = cv.imread('OpenCV-Tutorial/Photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# * findContours method looks at structuring element/edges of image and returns 2 values
# * contours = python list of all coordinates of the contours that were found in the image
# * hierarchies = hierarchy representation of contours 
# * (i.e. Have a rectangle, inside that is a square, and inside that is a circle)
# * RETR_LIST = returns all the contours it finds in the image
# * CHAIN_APPROX_NONE = how we want to approximate the contour, just returns all contours
# * CHAIN_APPROX_SIMPLE = comporesses into the 2 end points
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)