import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 

# * Histrogram - shows distribution of pixels in an image

img = cv.imread('OpenCV-Tutorial/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray,', gray)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

# Masking the image
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)

# Grayscale histrogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histrogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour histogram
plt.figure()
plt.title('Colour Histrogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colours = ('b', 'g', 'r')
for i,col in enumerate(colours):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim(0,256)
    
plt.show()

cv.waitKey(0)