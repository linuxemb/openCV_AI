import cv2 as cv

cap = cv.VideoCapture(1)
cap.set(3,640) #set width
cap.set(4,480) #set heigh

##video recording

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc,20.0, (640,480))

##video recording
x=20
y=20
w=10
h=10
while(True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    ## save rcoded video
    out.write(frame)
    cv.imshow('frame window to capture video',frame)
    cv.putText(gray,"lisa",(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0), thickness=2)
    cv.rectangle(gray,(x,y), (x+y,y+h),(0,255,0), thickness=2)
    cv.imshow('gray',gray)
    k = cv.waitKey(30)
    if k== 27: # Press ESC to quit
        break
cap.release()
out.release()
cv.destroyAllWindows()