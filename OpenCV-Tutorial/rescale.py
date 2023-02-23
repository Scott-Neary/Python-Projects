import cv2 as cv

img = cv.imread('OpenCV-Tutorial/Photos/cats.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75):
    # * works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    # * resizes the frame to a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# def changeRes(width,height):
#     # * works for live videos (i.e. external camera or webcam)
#     capture.set(3,width)
#     capture.set(4,height)
    
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)

# read/rescale video
# capture = cv.VideoCapture(0)

# while True:
#     isTrue, frame = capture.read()
    
#     frame_resized = rescaleFrame(frame, scale=.2)
    
#     cv.imshow ('Video', frame)
#     cv.imshow ('Video Resized', frame_resized)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()