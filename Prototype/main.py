import cv2 as cv
from object_tracking import VehicleTracking

# Read the video
vid = cv.VideoCapture("Vehicle-Detection/Videos/cars3.mp4")

# Instanstiate registration detection object
veh_tract = VehicleTracking(vid)
veh_tract.track_vehicle()