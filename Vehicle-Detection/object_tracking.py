import cv2 as cv
import numpy as np
# Import object_detection program developed by Pysource
from object_detection import ObjectDetection

# Initialise Object Detection
od = ObjectDetection()

# Load the video footage
cap = cv.VideoCapture("Vehicle-Detection/Videos/los_angeles.mp4")

# Get the frames from the video in a loop
while True:
    _, frame = cap.read()

    # Detect objects on frame
    # class_ids = what type of object (car, truck, person etc)
    # scores = how confident the algorithm is about the detected object
    # boxes = the bounding box of each object
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        print(box)

    cv.imshow("Frame", frame)
    key = cv.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()