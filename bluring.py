import cv2 as cv
import numpy as np

# read images
img=cv.imread('photos/pic4.jpg')

cv.imshow('Cat',img)

# Averaging
average = cv.blur(img,(3,3),0)
cv.imshow('Average blur',average)


# Gaussion  blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussion blur',average)


# Medion blur
medeian = cv.blur(img,(7,7))
cv.imshow('mdefian blur',medeian)

# 
blatera = cv.bilateralFilter(img,4,15,15)
cv.inshow('Blatera',blatera)