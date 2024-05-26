import cv2

path = 'kamal.jpg'
img = cv2.imread(path)
print(img.shape)

width, height = 400, 400
img_size = cv2.resize(img, (width, height))
print(img_size.shape)

img_croped = img[0:540, 0:1280]
img_croped_resize = cv2.resize(img_croped, (img.shape[1], img.shape[0]))

cv2.imshow('img', img)
cv2.imshow('resize', img_size)
cv2.imshow('croped',img_croped)
cv2.imshow('crop_resize', img_croped_resize)

cv2.waitKey(0)