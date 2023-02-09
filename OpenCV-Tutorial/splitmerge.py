import cv2 as cv 
import numpy as np 

img = cv.imread('OpenCV-Tutorial/Photos/cat.jpg')
cv.imshow('Cat', img)

# * [:2] = first 2 values
blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

# Get the actual colour for each respective colour channel
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge the colour channels
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)