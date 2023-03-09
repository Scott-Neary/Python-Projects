# Import Dependencies
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

# ! NOTE - This program will only be able to detect the vehicle reg plates of car2.jpg and car3.jpg
# ! The following code will enable car1.jpg to be scanned more accurately
# ! bfilter = cv.bilateralFilter(gray, 14, 21, 21)
# ! edged = cv.Canny(bfilter, 50, 160)

# Read the image
img = cv.imread('Car-Reg-Detection/Images/car01.jpg')

# Grayscale the image 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# plt.imshow(cv.cvtColor(gray, cv.COLOR_BGR2RGB))
# plt.show()

# Apply filtering to for noise reduction in the image
bfilter = cv.bilateralFilter(gray, 11, 17, 17)

# Edge Detection
edged = cv.Canny(bfilter, 30, 200)

# plt.imshow(cv.cvtColor(edged, cv.COLOR_BGR2RGB))
# plt.show()

# Find Contours
keypoints = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
# Return the top 10 contours in descending order
contours = sorted(contours, key=cv.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
    
print('Location = ', location)

# Apply Mask
# Create blank mask with the same shape as grayscaled image
mask = np.zeros(gray.shape, np.uint8)
# Draw registration plate contour
new_image = cv.drawContours(mask, [location], 0,255, -1)
# Overlay mask over orignal image
new_image = cv.bitwise_and(img, img, mask=mask)

# plt.imshow(cv.cvtColor(new_image, cv.COLOR_BGR2RGB))
# plt.show()

# Remove blank spaces around registration plate in the image
(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]

# plt.imshow(cv.cvtColor(cropped_image, cv.COLOR_BGR2RGB))
# plt.show()

# EasyOCR Reader with English language passed in
reader = easyocr.Reader(['en'])
# Use readtext method to read the registration plate from the image
result = reader.readtext(cropped_image)
print(result)

# Extract text output from array of results
text = result[0][-2]
# Specify font
font = cv.FONT_HERSHEY_SIMPLEX
# Apply text to image
res = cv.putText(img, text=text,org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv.LINE_AA)
# Draw rectangle around registration plate
res = cv.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)

plt.imshow(cv.cvtColor(res, cv.COLOR_BGR2RGB))
plt.show()