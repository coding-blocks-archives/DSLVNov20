import cv2

cam = cv2.VideoCapture(1)
model = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

while True:
	ret , frame = cam.read()
	if not ret:
		continue

	faces = model.detectMultiScale(frame, 1.5)

	for face in faces:
	    x,y,w,h = face
	    frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 4 )

	cv2.imshow("My photo", frame)
	
	# wait for user input - q, then stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break


cam.release()
cv2.destroyAllWindows()