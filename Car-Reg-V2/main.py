# Import libraries
import cv2 as cv
import pytesseract
import numpy as np

# ! This program currently doesn't work

# Point to Tesseract engine path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cascade = cv.CascadeClassifier("Car-Reg-V2/haarcascade_russian_plate_number.xml")
# memory_tags={"BD":"Birmingham","SD":"Glasgow"}

# 1. Upload image of car
# 2. Detect the number plate
# 3. Recognise the number plate
# 4. Get the licence plate return number

def extract_num(img_name):
    global read 
    # Read image
    img = cv.imread(img_name)
    cv.imshow('Test', img)
    # Grayscale image
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Detect the number plate from the image
    no_plate = cascade.detectMultiScale(gray,1.1,4)
    
    for (x,y,w,h) in no_plate:
        # Crop the number plate
        a,b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
        plate = img[y+a:y+h-a, x+b:x+w-b, :]
        
        # Image processing
        kernel = np.ones((1, 1), np.uint8)
        plate = cv.dilate(plate, kernel, iterations=1)
        plate = cv.erode(plate, kernel, iterations=1)
        plate_gray = cv.cvtColor(plate, cv.COLOR_BAYER_BG2GRAY)
        (thresh, plate) = cv.threshold(plate_gray, 127, 255, cv.THRESH_BINARY)
        
        read = pytesseract.image_to_string(plate)
        print(read)
        read = ''.join(e for e in read if e.isalnum())
        # Read first two characters of number plate
        stat = read[0:2]
        # try:
        #     print('Car memory tag-', memory_tags[stat])
        # except:
        #     print('Memory tag recognised!')
        print(read)
        cv.rectangle(img, (x,y), (x+w, y+h), (51,51,255), 2)
        cv.rectangle(img, (x, y - 40), (x + w, y), (51,51,255), -1)
        cv.putText(img, read, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 2) 
        cv.imshow('Plate', plate)
        
    cv.imshow("Result", img)
    # cv.imwrite('result.jpg', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
extract_num('Car-Reg-V2/Images/frame403.jpg')