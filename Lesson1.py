import cv2
import numpy as np

img = cv2.imread('images/face.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

img = cv2.GaussianBlur(img, (9, 9), 0)  # только нечётные значения
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Контуры, чем меньше числа,тем больше "точность"
img = cv2.Canny(img, 100, 100)

# Создали матрицу 5*5 со значениями 1, np.uint8-формат чисел
kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
# Уменьшили количество белых точек
img = cv2.erode(img, kernel, iterations=1)
# Вывод с обрезанием картинки cv2.imshow('Result',img[0:100, 0:150])
cv2.imshow('Result', img)

# Картинка показывается бесконечное кол-во времени пока не остановим сами
cv2.waitKey(0)

""" cap = cv2.VideoCapture(0)
cap.set(3,500)
cap.set(4,300)
while True:
    succes, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 """