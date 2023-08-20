import cv2 as cv

# read images
# img=cv.imread('photos/pic4.jpg')

# cv.imshow('Cat',img)

# cv.waitKey(0)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxx

capture= cv.VideoCapture('videos/vid1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break

capture.release()
cv.distroyAllWindows()

# cv.waitKey(0)



# resize re scale