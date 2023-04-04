import cv2 as cv
import numpy as np
from object_tracking import VehicleTracking
from detect_reg_V2 import RegDetectionClassV2
from db_class import Database

# Read the video
vid = cv.VideoCapture("Vehicle-Detection/Videos/cars3.mp4")

# Instanstiate registration detection object
veh_tract = VehicleTracking(vid)
veh_tract.track_vehicle()