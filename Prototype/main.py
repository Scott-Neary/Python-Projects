import cv2 as cv
from object_tracking import VehicleTracking

# Read the video
vid = cv.VideoCapture("Prototype/Videos/cars2.mp4")

# Instanstiate registration detection object
veh_tract = VehicleTracking(vid)
veh_tract.track_vehicle()