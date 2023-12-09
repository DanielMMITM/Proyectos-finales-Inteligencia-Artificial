import numpy as np
import cv2 as cv
# import imutils
import math

cap = cv.VideoCapture(0)
i = 728

while True:
    i = i + 1
    ret, frame = cap.read()
    
    # aux = frame.copy()
    frame = cv.rectangle(frame, (220, 50), (550, 400), (0, 255, 0), 5)
    
    
    # frame2 = aux[40:400, 210:550]
    frame2 = frame[40:400, 210:550]
    
    # frame2 = imutils.resize(frame2, width=15, height=15)
    
    cv.imwrite('C:\\Users\\Edani\\Downloads\\CubrebocasDataset\\Face Mask Dataset\\Train\\n\\nluz' + str(i) + '.jpg', frame2)
    cv.imshow("frame", frame)
    
    cv.imshow("dataset", frame2)
    
    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()