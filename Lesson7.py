# Распознавание лиц
import cv2
import numpy as np

img = cv2.imread('images/face2.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# берет файл и вытягивает как натренированную модель
faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor= 2, minNeighbors=4)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h),(0, 0, 255),thickness=3)
    
cv2.imshow('res', img)
cv2.waitKey(0)
