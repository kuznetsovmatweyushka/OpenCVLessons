import cv2
import numpy as np

img = cv2.imread('images/face.jpg')
# отзеркалим 0 по горизонтали, 1 по вертикали, -1 и так и так
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
#img = cv2.flip(img, -1)

# функция вращения


def rotate(img_param, angle):
    hieght, width = img.shape[:2]
    point = (width // 2, hieght // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img, mat, (width, hieght))


#img = rotate(img, 90)

# смещение картинки
def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1],img_param.shape[0]))

img = transform(img, 30, 200)    


cv2.imshow('res', img)
cv2.waitKey(0)
