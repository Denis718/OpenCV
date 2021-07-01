import cv2 as cv

img = cv.imread('opencv-course-master\Resources\Photos\cat.jpg')

cv.imshow('cat', img)

# Converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur Borrar- Desfoque de imagens
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade ou Cascata de bordas
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the Image Dilatar os contornos da cascata de bordas
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resizing Redimensionando interpolation=cv.INTER_CUBIC usado para 
# ampliação de imagem sem perda de qualidade
resized = cv.resize(img, (300,300),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping - Recortando
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)