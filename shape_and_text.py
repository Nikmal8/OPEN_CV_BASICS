import cv2
import numpy as np

img = np.zeros((522, 522, 3), np.uint8)

cv2.putText(img, 'Nikmal', (200, 270), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 1)

cv2.imshow('img', img)

cv2.waitKey(0)
