import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('opencv-course-master\Section #3 - Faces\haar_face.xml')

pessoas = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

faces_recognizer = cv.face.LBPHFaceRecognizer_create()
faces_recognizer.read(r'opencv-course-master\Section #3 - Faces\face_trained.yml')

img = cv.imread(r'opencv-course-master\Resources\Faces\val\jerry_seinfeld\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = faces_recognizer.predict(faces_roi)
    print(f'Label = {pessoas[label]} with a confidence of {confidence}')

    cv.putText(img, str(pessoas[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
 
cv.imshow('Detected face', img)

cv.waitKey(0)