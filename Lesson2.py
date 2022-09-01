import cv2
import numpy as np
# Изображение 300 на 300 пикселей
photo = np.zeros((300, 300, 3), dtype='uint8')
photo[:] = 255, 255, 255
# cv2.rectangle(photo, (3, 3), (100, 100), (0, 0, 0), thickness=cv2.FILLED)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1],
         photo.shape[0] // 2), (0, 0, 0), thickness=1)
cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2),
           50, (0, 0, 0), thickness=cv2.FILLED)
cv2.putText(photo, 'hello', (100, 150),
            cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 3)
cv2.imshow('Photo', photo)
cv2.waitKey(0)


