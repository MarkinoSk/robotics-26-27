import cv2 as cv
# from keras.src.quantizers import capture

#video live reading

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()