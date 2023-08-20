import cv2 as cv
import numpy as np



img=cv.imread('photos/pic4.jpg')

cv.imshow('img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r =cv.split(img)


blue =cv.merge([b,blank,blank])
green =cv.merge([blank,g,blank])
red =cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)


print(img.shape)
print(blue.shape)
print(green.shape)
print(red.shape)


# merge images
merged =cv.merge([b,g,r])
cv.imshow('Merged Images',merged)

cv.waitKey(0)