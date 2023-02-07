# imports
import cv2 as cv

# reading videos
capture = cv.VideoCapture('OpenCV-Tutorial/Videos/dog.mp4')

while True:
    # * reads video frame by frame
    isTrue, frame = capture.read()
    # * displays each frame
    cv.imshow ('Video', frame)
    
    # * if letter 'd' is pressed, then exit loop and stop playing video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
# * if error 215:Assertion failed is encountered, it means that no frame was detected at the specified location
# * in this tutorial, it is due to the reaching the end of the video where no frames are remaining

capture.release()
cv.destroyAllWindows()