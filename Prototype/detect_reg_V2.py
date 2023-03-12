# import required libraries
import cv2 as cv
import numpy as np

class RegDetectionClassV2:
    def __init__(self, img):
        self.img = img
        
    def detect_reg_plates(self):
        
        gray_image = self.image_filters()
        
        # read haarcascade for number plate detection
        cascade = cv.CascadeClassifier('Car-Reg-V2/Haarcascades/haarcascade_russian_plate_number.xml')

        # Detect license number plates
        plates = cascade.detectMultiScale(gray_image, 1.2, 5)
        print('Number of detected license plates:', len(plates))
        
        if len(plates) == 0:
            print('No registration plates found!')
            return False
        
        self.detect_reg_no(gray_image, plates)
        return True
    
    def image_filters(self):
        # convert input image to grayscale
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        return gray
    
    def detect_reg_no(self, gray, plates):
        # loop over all plates
        for (x,y,w,h) in plates:
   
            # draw bounding rectangle around the license number plate
            cv.rectangle(self.img, (x,y), (x+w, y+h), (0,255,0), 2)
            gray_plates = gray[y:y+h, x:x+w]
            color_plates = self.img[y:y+h, x:x+w]
            
            # save number plate detected
            # cv.imwrite('Numberplate.jpg', gray_plates)
            cv.imshow('Number Plate', gray_plates)
            cv.imshow('Number Plate Image', self.img)
            cv.waitKey(0)   
        cv.destroyAllWindows()        