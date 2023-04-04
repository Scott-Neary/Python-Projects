# import required libraries
import cv2 as cv
import numpy as np
import easyocr
from db_class import Database
class RegDetectionClassV2:
    def __init__(self, haarcascade='Prototype/Haarcascades/haarcascade_russian_plate_number.xml'):
        self.cascade = haarcascade
        
    def detect_reg_plates(self, frame):
        
        grayscale_image = self.image_filters(frame)
        
        # read haarcascade for number plate detection
        cascade = cv.CascadeClassifier(self.cascade)

        # Detect license number plates
        plates = cascade.detectMultiScale(grayscale_image, 1.2, 5)
        print('Number of registration plates detected:', len(plates))
        
        if len(plates) == 0:
            print('No registration plates found!')
            return False
        
        # Instantiate database
        self.db = Database()
        
        self.detect_reg_no(frame, grayscale_image, plates)
        
        return True
    
    def image_filters(self, frame):
        # Convert the frame into grayscale filter
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return gray
    
    def detect_reg_no(self, frame, grayscale_image, plates):
        # Loop through the detected registration plates
        for (x,y,w,h) in plates:
   
            # Produce a bounding box around the registration plate
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            grayscale_plates = grayscale_image[y:y+h, x:x+w]
            
            # EasyOCR Reader with English language passed in
            reader = easyocr.Reader(['en'])
            
            # Use readtext method to read the registration plate from the image
            result = reader.readtext(grayscale_plates)
            reg_value = result[0][-2]
            reg_accuracy = result [0][-1]
            
            # Next iteration if accuracy is low
            if reg_accuracy < 0.5:
                continue
            
            cv.imshow('Number Plate Image', frame)
            cv.imshow('Number Plate', grayscale_plates)
            
            print("Registration Number - ", reg_value)
            print("Accuracy Score - ", reg_accuracy)
            
            # Compare registration number in database
            car_exists = self.db.does_car_exist(reg_value)
            # Add registration number to database
            if car_exists == False:
                self.db.add_car(reg_value, reg_accuracy)
            else:
                print("Car with registration ", reg_value, " already exists!")
            
            key = cv.waitKey(0)
            if key == 27:
                quit()   
        cv.destroyAllWindows()        
        return reg_value, reg_accuracy