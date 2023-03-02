import cv2 as cv
import numpy as np
from object_tracking import VehicleTracking
from detect_reg_class import RegDetectionClass

# Read the video
vid = cv.VideoCapture("Vehicle-Detection/Videos/cars3.mp4")

# Instanstiate registration detection object
veh_tract = VehicleTracking(vid)
veh_tract.track_vehicle()

# Read the image
# img = cv.imread('Car-Reg-Detection/Images/car5.jpg')

# Instanstiate registration detection object
# reg_detect = RegDetectionClass(img)
# reg_detect.detect_reg_no()

# Below code maybe for extracting objects
# roi = frame[y: y +h, x: x + w]
# cv.imshow("ROI", roi)