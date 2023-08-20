import cv2 as cv
import numpy as np
img=cv.imread('photos/pic4.jpg')

cv.imshow('Cat',img)
# grey image
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Grey',gray)


# blur
blur =cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# # create edges
canny =cv.Canny(blur,125,175)
# cv.imshow('Canny Edges',canny)

blank =np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank',blank)


ret,thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)


contours , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')



cv.drawContours(blank, contours, -1,(0,0,255),1)
cv.imshow('Contours Drawn ',blank)


cv.waitKey(0)