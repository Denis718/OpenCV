import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

retangulo = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circulo = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Retangulo', retangulo)
cv.imshow('Circulo', circulo)


# bit a bit ou bitwise AND
bitwise_and = cv.bitwise_and(retangulo, circulo)
cv.imshow('BitWise_AND', bitwise_and)

# bit a bit ou bitwise OR
bitwise_or = cv.bitwise_or(retangulo, circulo)
cv.imshow('BitWise_OR', bitwise_or)

# bit a bit ou bitwise XOR
bitwise_xor = cv.bitwise_xor(retangulo, circulo)
cv.imshow('BitWise_XOR', bitwise_xor)

# bit a bit ou bitwise NOT
bitwise_not = cv.bitwise_not(circulo)
cv.imshow('BitWise_NOT', bitwise_not)

cv.waitKey(0)