import cv2 as cv

rostro4 = cv.CascadeClassifier('C:\\Users\\Edani\\Downloads\\CubrebocasDataset\\Face Mask Dataset\\Train\\classifier\\cascade.xml')

cap = cv.VideoCapture(0)


while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    rostros = rostro4.detectMultiScale(gray, scaleFactor= 1.28, minNeighbors= 30, minSize=(70, 70))
    
    
    
    for (x, y, w, h) in rostros:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame, 'Cubrebocas detectado', (x, y), 2, 0.7, (0, 255, 0), 2, cv.LINE_AA)

    cv.imshow('Rostro con cubrebocas', frame)

    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()