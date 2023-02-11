import cv2 as cv 
import numpy as np 

img = cv.imread('OpenCV-Tutorial/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.rectangle(blank, (img.shape[1]//2,img.shape[0]//2), (img.shape[1]//2 + 100,img.shape[0]//2 + 100), 255, -1)
mask = cv.imshow('Mask', mask)

# ! Problem - Image is not getting masked (1:56:00 of tutorial video)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)