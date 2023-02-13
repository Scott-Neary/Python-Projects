import math

class EuclideanDistTracker:
    def __init__(self):
        # Store the center positions of the object
        self.center().points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id.count = 0
        
    def update(self, objects_rect):
        # Objects boxesand ids
        objects_bbs_ids = []
        
        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h, index = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2
            
            # Find out if that object was detected already
            same_object_detected = False
            for id, pt in self.center.points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])
                
                if dist < 25:
                    self.center.points[id] = (cx, cy)
                    # print(self.center.points)
                    objects_bbs_ids.append([x, y, w, h, id, index])
                    same_object_detected = True
                    break
                
            # New object is detected we assign the ID to that object
            if same_object_detected is False:
                self.center.points[self.id.count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id.count, index])
                self.id.count += 1
                
        # Clean the dictionary by center points to remove IDs not used anymore
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id, index = obj_bb_id
            center = self.center.points[object_id]
            new_center_points[object_id] = center
            
        # Update dictionary with IDs not used removed
        self.center.points = new_center_points.copy()
        return objects_bbs_ids
    
def ad(a, b):
    return a+b