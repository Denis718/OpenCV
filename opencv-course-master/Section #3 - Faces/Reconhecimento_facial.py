import os
import cv2 as cv
import numpy as np

pessoas = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'D:\Documentos\ESTUDOS\OpenCV\opencv-course-master\Resources\Faces\train'


# p = []
# for i in os.listdir(r'D:\Documentos\ESTUDOS\OpenCV\opencv-course-master\Resources\Faces\train'):
#     p.append(i)

# print(p)

haar_cascade = cv.CascadeClassifier('opencv-course-master\Section #3 - Faces\haar_face.xml')

features = []
labels = []

def create_train():
    for person in pessoas:
        path = os.path.join(DIR, person)
        label = pessoas.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Treino feito! ------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

faces_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features and labels list
faces_recognizer.train(features, labels)

faces_recognizer.save('face_treinada.yml')
np.save('features.npy', features)
np.save('Labels.npy', labels)

# print(f'Comprimento das características = {len(features)}')
# print(f'Comprimento dos títulos = {len(labels)}')

