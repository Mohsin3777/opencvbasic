# resize re scale
import cv2 as cv
from matplotlib.pyplot import sca


img=cv.imread('photos/pic4.jpg')

cv.imshow('Cat',img)

def rescaleFrame(frame, scale=0.75):
    # this method for images , vidoes m, live videos
    width=int(frame.shape[1] * scale)
    height= int(frame.shape[0] *scale)

    dimension =(width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

resize_image = rescaleFrame(img)
cv.imshow("Image",resize_image)

# Change resulation
def changeRes(width,height):
    # Live Video
    capture.set(3,width)
    capture.set(4,height)


# Reding video
capture= cv.VideoCapture('videos/vid1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=.2)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break

capture.release()
cv.distroyAllWindows()


cv.waitKey(0)