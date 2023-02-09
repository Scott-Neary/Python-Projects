import cv2 as cv 

img = cv.imread('OpenCV-Tutorial/Photos/cat.jpg')
cv.imshow('Cat', img)


cv.waitKey(0)