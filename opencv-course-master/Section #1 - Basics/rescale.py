import cv2 as cv #Importação da biblioteca OpenCV

#Atribuindo imagem a uma variável
img = cv.imread('opencv-course-master\Resources\Photos\cat_large.jpg')

# Método para chamar a imagem cv.imshow(nome, fonte)
cv.imshow('Cat', img)

# Método para manter a imagem até pressionar alguma tecla, parâmetro 0 para manter estático
cv.waitKey(0)

# Função para redimensionar
def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img, 0.45)

cv.imshow('Cat', resized_image)

cv.waitKey(0)

# Reading Videos - Leitura de videos
capture = cv.VideoCapture('opencv-course-master\Resources\Videos\dog.mp4')
# Laço de repetição para leitura completa do video, frame a frame
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

def changeRes(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)


capture.release()
cv.destroyAllWindows()