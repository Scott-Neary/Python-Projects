import cv2 as cv
import numpy as np
# Import object_detection program developed by Pysource
from object_detection import ObjectDetection
import math
from detect_reg_V2 import RegDetectionClassV2

class VehicleTracking:
    def __init__(self, vid):
      self.vid = vid
    
    def track_vehicle(self):
        # Initialise Object Detection
        od = ObjectDetection()

        # Instanstiate registration detection object
        reg_detect = RegDetectionClassV2()
                    
        # Initialise frame count and tracking values
        frame_count = 0
        tracking_objects = {}
        track_id = 0

        # Get the frames from the video in a loop
        while True:
            ret, frame = self.vid.read()
            frame_count += 1
            if not ret:
                break
            
            # Point of current frame
            center_points_cur_frame = []
            
            # Detect objects on frame
            # class_ids = what type of object (car, truck, person etc)
            # scores = how confident the algorithm is about the detected object
            # boxes = the bounding box of each object
            (class_id, accuracy_score, boxes) = od.detect(frame)
            for box in boxes:
                (x, y, w, h) = box
                
                # Calculate the centre points of the object
                cx = int((x + x + w) / 2)
                cy = int((y + y + h) / 2)
                center_points_cur_frame.append((cx, cy))
                
                # print("FRAME No ", frame_count, " ", x, y, w, h)
                
                # Draw full circle at the centre point of each object
                # cv.circle(frame, (cx, cy), 5, (0,0,255), -1)
                # Draw rectangle bounding box around objects
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
            tracking_objects_copy = tracking_objects.copy()
            center_points_cur_frame_copy = center_points_cur_frame.copy()
            
            # Comparison between previous and current frame
            for object_id, point_prev in tracking_objects_copy.items():
                object_exists = False    
                for point_cur in center_points_cur_frame_copy:
                    object_distance = math.hypot(point_prev[0] - point_cur[0], point_prev[1] - point_cur[1])
                    
                    # Update the position of the object ID
                    if object_distance < 25:
                        tracking_objects[object_id] = point_cur
                        object_exists = True
                        if point_cur in center_points_cur_frame:
                            center_points_cur_frame.remove(point_cur)
                        continue

                # Remove the object IDs that are no longer detected
                if not object_exists:
                    tracking_objects.pop(object_id)
                
                print("Frame Number - ", frame_count)
                
                # ! Lines 82 - 86 are temporary to check if reg plates are being picked - will need to add a db/spreadsheet that checks existing reg plates
                if object_exists:
                    reg_found = reg_detect.detect_reg_plates(frame)
                    print(reg_found)
        
            # Add new track IDs of detected objects
            for point_cur in center_points_cur_frame:
                tracking_objects[track_id] = point_cur
                track_id += 1
            
            # Visualise tracking IDs onto objects
            for object_id, point_cur in tracking_objects.items():
                cv.circle(frame, point_cur, 5, (0,0,255), -1)
                cv.putText(frame, str(object_id), (point_cur[0], point_cur[1] - 7), 0, 1, (0, 0, 255), 1)          
            
            cv.imshow("Video Frame", frame)
            
            # Press escape key to leave frame
            key = cv.waitKey(1)
            if key == 27:
                break
            
        self.vid.release()
        cv.destroyAllWindows()