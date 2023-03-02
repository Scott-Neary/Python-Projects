import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

class RegDetectionClass:
    def __init__(self, img):
        self.img = img
        
    def detect_reg_no(self):

        gray_image, image_edge = self.image_filters()
        reg_location, reg_approx = self.image_contours(image_edge)
        cropped_image = self.image_mask(gray_image, reg_location)
        result = self.image_text_extract(reg_approx, cropped_image)
        
        plt.imshow(cv.cvtColor(result, cv.COLOR_BGR2RGB))
        plt.show()
        
    def image_filters(self):
        
        # Grayscale the image 
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        # Apply filtering to for noise reduction in the image
        bfilter = cv.bilateralFilter(gray, 11, 17, 17)
        # Edge Detection
        edged = cv.Canny(bfilter, 30, 200)
        return gray, edged
    
    def image_contours(self, edged):
        
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
        return location, approx
    
    def image_mask(self, gray, location):
        
        # Create blank mask with the same shape as grayscaled image
        mask = np.zeros(gray.shape, np.uint8)
        # Draw registration plate contour
        new_image = cv.drawContours(mask, [location], 0,255, -1)
        # Overlay mask over orignal image
        new_image = cv.bitwise_and(self.img, self.img, mask=mask)
        
        # Remove blank spaces around registration plate in the image
        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped = gray[x1:x2+1, y1:y2+1]
        return cropped
        
    def image_text_extract(self, reg_approx, cropped_image):
        
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
        res = cv.putText(self.img, text=text,org=(reg_approx[0][0][0], reg_approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv.LINE_AA)
        # Draw rectangle around registration plate
        res = cv.rectangle(self.img, tuple(reg_approx[0][0]), tuple(reg_approx[2][0]), (0,255,0),3)
        return res