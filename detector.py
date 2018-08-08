import cv2
import numpy as np
import os
from PIL import Image

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face_LBPHFaceRecognizer.create()
rec.read("recognizer\\trainningData.yml")
id=0
www=""
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
	ret,img = cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		id,conf=rec.predict(gray[y:y+h,x:x+w])
		if(id==1):
			#id="Anirban"
			www = 'Anuj'
		elif(id==2):
			www = "Akash"
		#cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
		cv2.putText(img,www,(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
	cv2.imshow("Face",img)
	if(cv2.waitKey(1)==ord('q')):
		break
	if www == 'Anuj':
		print("login")
		os.system('python mainapp.py')
		break
	else:
		print("login error")
cam.release()
cv2.destroyAllWindows()