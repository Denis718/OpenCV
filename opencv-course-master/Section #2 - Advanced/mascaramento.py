import cv2 as cv
import numpy as np

img = cv.imread('opencv-course-master\Resources\Photos\cats 2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

retangulo = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

forma_estranha = cv.bitwise_and(circle, retangulo)
cv.imshow('Forma Estranha', forma_estranha) 

masked = cv.bitwise_and(img, img, mask=forma_estranha)
cv.imshow('Masked', masked)

cv.waitKey(0)