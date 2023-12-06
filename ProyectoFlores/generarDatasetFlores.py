import cv2 as cv
from time import sleep
cap = cv.VideoCapture('C:\\Users\\Edani\\Downloads\\girasol\\girasol2.mp4')
i=686
while cap.isOpened():
    ret, im = cap.read()
    
    if ret==False:
        break
    
    height, width, _ = im.shape

    x1 = int(width / 2) - 200  
    y1 = int(height / 2) - 360  #arriba
    x2 = int(width / 2) + 200
    y2 = int(height / 2) + 70 
    
    im = cv.rectangle(im, (x1,y1), (x2,y2), (0,255,0), 2)
    cuadro = im[y1:y2, x1:x2]
    mini = cv.resize(cuadro,(28,21))
    
    cv.imshow('Video', im)
    cv.imshow('Cuadro', cuadro)
    cv.imshow("Mini", mini)
    k=cv.waitKey(1)
    if k == ord('s'):
        i=i+1
        cv.imwrite('C:\\Users\\Edani\\Downloads\\datasetGirasol\\' + str(i)+'.jpg', mini)
        if (i == 2833 or i == 4400):
            print(i)
    if k == 27:
        break
    sleep(1/25)
cap.release()
cv.destroyAllWindows()  