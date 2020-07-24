import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\smnav\\Desktop\\facedetection\\haarcascade_frontalface_default.xml")


cap = cv2.VideoCapture(0)


while True:
    _ ,i =cap.read()

    gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray)

    for(x,y,w,h) in faces:
        cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',i)

    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

