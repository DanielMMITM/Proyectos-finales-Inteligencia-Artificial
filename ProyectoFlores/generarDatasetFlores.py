import cv2 as cv
from time import sleep
cap = cv.VideoCapture('C:\\Users\\Edani\\Downloads\\nochebuena\\nochebuena2.mp4')
i=2875
while cap.isOpened():
    ret, im = cap.read()
    
    if ret==False:
        break
    
    # Obtén las dimensiones de la imagen
    height, width, _ = im.shape
    #print(im.shape)

    # Calcula las coordenadas del rectángulo para que esté en el centro
    x1 = int(width / 2) - 190  #mas alto mas a la izquierda
    x2 = int(width / 2) + 220  #mas alto mas a la derecha 
    
    y1 = int(height / 2) - 200 #mas alto mas arriba 
    y2 = int(height / 2) + 200 #mas alto mas abajo 
    
    im = cv.rectangle(im, (x1,y1), (x2,y2), (0,255,0), 2)
    cuadro = im[y1:y2, x1:x2]
    mini = cv.resize(cuadro,(28,21))
    
    cv.imshow('Video', im)
    cv.imshow('Cuadro', cuadro)
    cv.imshow("Mini", mini)
    k=cv.waitKey(1)
    if k == ord('s'):
        i=i+1
        cv.imwrite('C:\\Users\\Edani\\Downloads\\DatasetFlowers\\Nochebuena\\' + str(i)+'.jpg', mini)
    if k == 27:
        break
    sleep(1/25)
cap.release()
cv.destroyAllWindows()  