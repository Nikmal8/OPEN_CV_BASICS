import cv2

"""***  Read the image *** """

img = cv2.imread('kamal.jpg')

cv2.imshow('kamal', img)

cv2.waitKey(0)
