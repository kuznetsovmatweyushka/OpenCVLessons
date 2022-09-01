#Цветовые форматы(HSV, LAB)
import cv2
import numpy as np

img = cv2.imread('images/face.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_LAB2LBGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)#Разбивает картинку по слоям

img = cv2.merge([r, g , b])#Соединили слои

cv2.imshow('res', img)
cv2.waitKey(0)