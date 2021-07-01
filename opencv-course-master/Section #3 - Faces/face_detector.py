import cv2 as cv

img = cv.imread('opencv-course-master\Resources\Photos\group 1.jpg')
cv.imshow('Grupo de pessoas', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('opencv-course-master\Section #3 - Faces\haar_face.xml')

# Faces em retangulos faces_rect
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Rostos Detectados', img)

cv.waitKey(0)