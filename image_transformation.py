from this import d
import cv2 as cv
import numpy as np
img=cv.imread('photos/pic2.jpg')

cv.imshow('Cat',img)

# Translate
def translate(img,x,y):
    transMat =np.float32([[1,0,x],[0,1,y]])
    dimenstion = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimenstion)


#  -x --> left
#  -y --> Up
#  x  --> Right
#  y -->Down

translated= translate(img,-100,100)
# cv.imshow('trans',translated)
# xxxxxxxxxxxxxxxxxxx



# Rotation
def rotate(img,angel,rotPoint=None):
    (height,width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angel,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)


rotated= rotate(img,-80)
cv.imshow('Rotate',rotated)



# resize image
resize =cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resize)

# flipping
flip =cv.flip(img,-1)
cv.imshow('Flip',img)


# cropping
cropping =img[200:400, 300:400]
cv.imshow('Crop',cropping)
cv.waitKey(0)