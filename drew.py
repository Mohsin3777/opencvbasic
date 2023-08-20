import cv2 as cv
import numpy as np

# Draw on images

blank = np.zeros( (500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
#  xxxxxxxxxxxxxxxxxxxxxxxxxxx

# green img
# blank[:]= 0,255,0
# cv.imshow('Green',blank)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 2 draw a rectangle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)

# xxxxxxxxxxxxxxxxxxxxx

# draw circle
# cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)
# xxxxxxxxxxxxxxxx


# draw line
# cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
# cv.imshow('Line',blank)
# xxxxxxxxxxxxxxxx


# write text
cv.putText(blank,'Hello my name is mohsin',(0,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
# xxxxxxxxxxxxxxx





# read images
# img=cv.imread('photos/pic4.jpg')

# cv.imshow('Cat',img)


cv.waitKey(0)