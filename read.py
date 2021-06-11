import cv2 as cv
#img =cv.imread('photo\cat.jpg')
#cv.imshow('cat',img)

#cv.waitKey(0)
capture = cv.VideoCapture('Videos/cat.mp4')


while True:
	isTrue, frame = capture.read()
	cv.imshow('video',frame)
	
	if cv.waitKey(20) & 0xFF==ord('d'):
		break
capture.release()
cv.destroyAllWindows()