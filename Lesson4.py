#Находим контуры изображения
import cv2
import numpy as np

img = cv2.imread('images/face.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
new_img = np.zeros(img.shape, dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0) #размытие для оптимизации

img = cv2.Canny(img,100, 140) # Контуры(всё что ниже 100 будет черным, а что выше 140 белым)

con,hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (230,150,111), 1)

cv2.imshow('res', new_img)
cv2.waitKey(0)