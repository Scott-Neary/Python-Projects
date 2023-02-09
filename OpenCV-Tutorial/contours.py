# Contour Detection
import cv2 as cv 

# * Contours are the boundaries of objects
# * Useful for shape analysis, object detection and recognition

img = cv.imread('OpenCV-Tutorial/Photos/cats.jpg')

cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# * findContours method looks at structuring element/edges of image and returns 2 values
# * contours = python list of all coordinates of the contours that were found in the image
# * hierarchies = hierarchy representation of contours 
# * (i.e. Have a rectangle, inside that is a square, and inside that is a circle)
# * RETR_LIST = returns all the contours it finds in the image
# * CHAIN_APPROX_NONE = how we want to approximate the contour, just returns all contours
# * CHAIN_APPROX_SIMPLE = comporesses into the 2 end points
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)