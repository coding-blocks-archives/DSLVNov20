import cv2
import numpy as np


cam = cv2.VideoCapture(1)
model = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

face_data = []
skip =0
name = input("Enter your name: ")

while True:
	ret , frame = cam.read()
	if not ret:
		continue

	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	faces = model.detectMultiScale(frame, 1.5)

	if len(faces)==0:
		continue


	for face in faces:
	    x,y,w,h = face
	    frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 4 )


	    # Crop your face
	    offset = 10
	    face_section = frame[y-offset : y+h+offset, x-offset : x+offset+w]
	    face_section = cv2.resize(face_section, (100,100) )

	    skip+=1
	    if skip%10==0:
	    	face_data.append(face_section)
	    	print(len(face_data))



	cv2.imshow("My photo", frame)
	cv2.imshow("Face Section", face_section)
	
	# wait for user input - q, then stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break



face_data = np.array(face_data)
face_data = face_data.reshape(face_data.shape[0], 10000 )
print(face_data.shape)

# save this data

np.save('./data/'+ name+'.npy', face_data )

cam.release()
cv2.destroyAllWindows()