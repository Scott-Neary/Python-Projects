import cv2 as cv 

img = cv.imread('OpenCV-Tutorial/Photos/group 1.jpg')
cv.imshow('Group of 5 people', img)

# Grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('OpenCV-Tutorial/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
cv.imshow('Detected Face', img)
print(f'Number of faces found = {len(faces_rect)}')
cv.waitKey(0)