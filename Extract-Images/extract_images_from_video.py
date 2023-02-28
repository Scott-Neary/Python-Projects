import cv2 as cv 
import os

# Load the video
vid = cv.VideoCapture('Extract-Images/Videos/cars3.mp4')

# Initialise the frame count
current_frame = 0

if not os.path.exists('data'):
    os.makedirs('data')
    
while (True):
    success, frame = vid.read()
    
    cv.imshow("Output", frame)
    cv.imwrite('./data/frame' + str(current_frame) + '.jpg', frame)
    
    # Increment the frame count by 1
    current_frame +=1
    
    # Option to continue extracting frames until video ends or manually by pressing the Q key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break