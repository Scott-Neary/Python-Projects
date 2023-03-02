import cv2 as cv
import numpy as np
# Import object_detection program developed by Pysource
from object_detection import ObjectDetection
import math

class VehicleTracking:
    def __init__(self, vid):
      self.vid = vid
    
    def track_vehicle(self):
        # Initialise Object Detection
        od = ObjectDetection()

        # Initialise frame count
        count = 0

        center_points_prv_frame = []

        tracking_objects = {}
        track_id = 0

        # Get the frames from the video in a loop
        while True:
            ret, frame = self.vid.read()
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
                
                # Calculate the centre points
                cx = int((x + x + w) / 2)
                cy = int((y + y + h) / 2)
                center_points_cur_frame.append((cx, cy))
                
                print("FRAME No ", count, " ", x, y, w, h)
                
                # Draw full circle at the centre point of each object
                # cv.circle(frame, (cx, cy), 5, (0,0,255), -1)
                # Draw rectangle bounding box around objects
                cv.rectangle(frame, (x, y), (x + w, y +h), (0, 255, 0), 2)
            
            # Only at the beginning we compare previous and current frame
            if count <= 2:
                for pt in center_points_cur_frame:
                    for pt2 in center_points_prv_frame:
                        distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
                    
                        if distance < 20:
                            tracking_objects[track_id] = pt
                            track_id += 1
            else:
                
                tracking_objects_copy = tracking_objects.copy()
                center_points_cur_frame_copy = center_points_cur_frame.copy()
                
                for object_id, pt2 in tracking_objects_copy.items():
                    object_exists = False    
                    for pt in center_points_cur_frame_copy:
                        distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
                        
                        # Update IDs position
                        if distance < 20:
                            tracking_objects[object_id] = pt
                            object_exists = True
                            if pt in center_points_cur_frame:
                                center_points_cur_frame.remove(pt)
                            continue
                        
                    # Remove IDs lost
                    if not object_exists:
                        tracking_objects.pop(object_id)
            
                # Add new IDs found
                for pt in center_points_cur_frame:
                    tracking_objects[track_id] = pt
                    track_id += 1
            
            for object_id, pt in tracking_objects.items():
                cv.circle(frame, pt, 5, (0,0,255), -1)
                cv.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), 1)          
            
            print ("Tracking objects")
            print(tracking_objects)
            
            print("CUR FRAME LEFT PTS")
            print(center_points_cur_frame)
            
            # print("PREV FRAME")
            # print(center_points_prv_frame)
            
            cv.imshow("Frame", frame)
            
            # Make a copy of the points
            center_points_prv_frame = center_points_cur_frame.copy()
            
            key = cv.waitKey(0)
            if key == 27:
                break
            
        self.vid.release()
        cv.destroyAllWindows()