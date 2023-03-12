# import required libraries
import cv2 as cv
import numpy as np

# Read input image
img = cv.imread("Car-Reg-V2/Images/car01.jpg")

# convert input image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# read haarcascade for number plate detection
cascade = cv.CascadeClassifier('Car-Reg-V2/Haarcascades/haarcascade_russian_plate_number.xml')

# Detect license number plates
plates = cascade.detectMultiScale(gray, 1.2, 5)
print('Number of detected license plates:', len(plates))

# loop over all plates
for (x,y,w,h) in plates:
   
   # draw bounding rectangle around the license number plate
   cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
   gray_plates = gray[y:y+h, x:x+w]
   color_plates = img[y:y+h, x:x+w]
   
   # save number plate detected
   cv.imwrite('Numberplate.jpg', gray_plates)
   cv.imshow('Number Plate', gray_plates)
   cv.imshow('Number Plate Image', img)
   cv.waitKey(0)
cv.destroyAllWindows()