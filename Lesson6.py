#Побитовые операции и маски
import cv2
import numpy as np

photo = cv2.imread('images/face.jpg')
photo = cv2.resize(photo, (photo.shape[1] // 2, photo.shape[0] // 2))
img = np.zeros(photo.shape[:2],dtype='uint8')

circle = cv2.circle(img.copy(),(260, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25),(250, 350), 255, -1)

img = cv2.bitwise_and(photo,photo, mask=circle) #вырезали у фото, все что за кругом (всё что совпадает)
#img = cv2.bitwise_or(circle,square) #полное объединение
#img = cv2.bitwise_xor(circle,square) #объединение двух обьектов, но всё что совпадало вырезано
#img = cv2.bitwise_not(circle) #инверсия,круг был белым

cv2.imshow('res',img)
cv2.waitKey(0)