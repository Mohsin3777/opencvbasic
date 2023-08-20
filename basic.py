import cv2 as cv
# read images
img=cv.imread('photos/pic4.jpg')

cv.imshow('Cat',img)

# black and white image
# grey =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('"Gray',grey)
# xxxxxxxxxxxxxxxxxxxx

# Blur iamge
blur =cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
# xxxxxxxxxxxxxxxxxx



# Edge  Cascade
canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)
# xxxxxxxxxxxxxxxxxxxxxxx




# Dialating  the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dialating',dilated)
# xxxxxxxxxxxxxxxxxxxxxxx


# Eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)
# xxxxxxxxxxxxxxxxxxxxxxx


# resize
resized = cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
# xxxxxxxxxxxxxxxxxxxxxxx



# croped
cropped  = img[50:200,200:400]

cv.imshow('Croped',cropped)
# xxxxxxxxxxxxxxxxxxxxxxx
cv.waitKey(0)