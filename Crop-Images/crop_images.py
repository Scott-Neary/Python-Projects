import cv2 as cv 
import numpy as np 

img = cv.imread("Crop-Images/colors.jpg")
rows, cols, _ = img.shape
print("Rows", rows)
print("Cols", cols)

# Cut image
cut_img = img[426: 526, 250: 1280]

# ROI (Region of interest) aka Crop portion of the image
cv.rectangle(img, (385, 155), (851, 613), (0, 255, 0), 3)

roi = img[155: 613, 385: 851]

cv.imshow("Colours", img)
cv.imshow("Cut Image", cut_img)
cv.imshow("ROI", roi)
cv.waitKey(0)