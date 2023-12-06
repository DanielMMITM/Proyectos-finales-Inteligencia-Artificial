import cv2 as cv

rostro = cv.CascadeClassifier('C:\\Users\\Edani\\Downloads\\CubrebocasDataset\\Face Mask Dataset\\Train\\classifier\\cascade.xml')
cap = cv.VideoCapture(0)


while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #scalefactor = 1.01, minNeighbors = 6 o 10 //// 1.1 y 4 C:\\Users\\Edani\\OneDrive\\Documentos\\IA\\Caras\\classifier\\cascade.xml
    rostros = rostro.detectMultiScale(gray, scaleFactor= 1.41, minNeighbors= 20, minSize=(70, 70))
    #scalefactor = 1.24, minNeighbors = 50 / 35
    for (x, y, w, h) in rostros:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame, 'Persona con cubrebocas', (x, y), 2, 0.7, (0, 255, 0), 2, cv.LINE_AA)

    cv.imshow('Rostro con cubrebocas', frame)

    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()