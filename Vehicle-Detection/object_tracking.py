import cv2 as cv
import numpy as np
# Import object_detection program developed by Pysource
from object_detection import ObjectDetection
import math

# Initialise Object Detection
od = ObjectDetection()

# Load the video footage
cap = cv.VideoCapture("Vehicle-Detection/Videos/los_angeles.mp4")

# Initialise frame count
count = 0
center_points_prv_frame = []

tracking_objects = {}
track_id = 0

# Get the frames from the video in a loop
while True:
    ret, frame = cap.read()
    count += 1
    if not ret:
        break
    
    # Point of current frame
    center_points_cur_frame = []
    
    # Detect objects on frame
    # class_ids = what type of object (car, truck, person etc)
    # scores = how confident the algorithm is about the detected object
    # boxes = the bounding box of each object
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        center_points_cur_frame.append((cx, cy))
        print("FRAME No ", count, " ", x, y, w, h)
        
        # Draw full circle at the centre point of each object
        # cv.circle(frame, (cx, cy), 5, (0,0,255), -1)
        # Draw rectangle bounding box around objects
        cv.rectangle(frame, (x, y), (x + w, y +h), (0, 255, 0), 2)
    
    for pt in center_points_cur_frame:
        for pt2 in center_points_prv_frame:
            distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
            
            if distance < 10:
                tracking_objects[track_id] = pt
                track_id += 1
    
    for object_id, pt in tracking_objects.items():
        cv.circle(frame, pt, 5, (0,0,255), -1)
        # ! Warning - below line throws error at the moment
        cv.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), -2)          
    
    print ("TRacking objects")
    print(tracking_objects)
    
    print("CUR FRAME")
    print(center_points_cur_frame)
    
    print("PREV FRAME")
    print(center_points_prv_frame)
    
    cv.imshow("Frame", frame)
    
    # Make a copy of the points
    center_points_prv_frame = center_points_cur_frame.copy()
    
    key = cv.waitKey(0)
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()