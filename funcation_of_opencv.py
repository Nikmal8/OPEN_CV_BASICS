import cv2
import numpy as np

kernal = np.ones((5, 5), np.uint8)
print(kernal)

path = 'kamal.jpg'
img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
img_canay = cv2.Canny(img_blur, 100, 100)
img_dilationn = cv2.dilate(img_canay, kernal, iterations = 1)
img_eroded = cv2.erode(img_dilationn, kernal, iterations = 1)

cv2.imshow('img', img)
cv2.imshow('grayscale', img_gray)
cv2.imshow('GraySacler', img_blur)
cv2.imshow('canny', img_canay)
cv2.imshow('dilation', img_dilationn)
cv2.imshow('eroded', img_eroded)
cv2.waitKey(0)
