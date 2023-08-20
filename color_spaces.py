# switch between color 

import cv2 as cv
import matplotlib.pyplot as plt
# read images
img=cv.imread('photos/pic4.jpg')

cv.imshow('Cat',img)

# plt images
# plt.imshow(img)
# plt.show()


gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Grey',gray)

# BGR to HSV
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)


#BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('LAB',lab)

#  BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()


# HSV to BGR
hsv_bgr =cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV--BGR',hsv_bgr)



# HSV to BGR
lab_bgr =cv.cvtColor(lab,cv.COLOR_HSV2BGR)
cv.imshow('LAB--BGR',lab_bgr)

cv.waitKey(0)
