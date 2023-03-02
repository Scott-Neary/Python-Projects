import cv2 as cv
import numpy as np
from detect_reg_class import RegDetectionClass

# Read the image
img = cv.imread('Car-Reg-Detection/Images/car5.jpg')

# Instanstiate registration detection object
reg_detect = RegDetectionClass(img)

reg_detect.detect_reg_no()

# Below code maybe for extracting objects
# roi = frame[y: y +h, x: x + w]
# cv.imshow("ROI", roi)