# imports
import cv2 as cv

# reading images
img = cv.imread('OpenCV-Tutorial/Photos/cat.jpg')

# displaying image in a new window
# * 'Cat' = name of the window
# * img = pixels to be displayed
cv.imshow('Cat', img)

# * waits for a time for key to be pressed
# * 0 = infinite wait
cv.waitKey(0)