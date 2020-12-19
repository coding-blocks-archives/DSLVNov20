import cv2
import numpy as np



face_data = []

model = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

img = cv2.imread('./akshay.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = model.detectMultiScale(img, 1.2)

for _ in range(20):
	for face in faces:
	    x,y,w,h = face
	    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 4 )


	    # Crop your face
	    offset = 10
	    face_section = img[y-offset : y+h+offset, x-offset : x+offset+w]
	    face_section = cv2.resize(face_section, (100,100) )

	    face_data.append(face_section)



face_data = np.array(face_data)
face_data = face_data.reshape(face_data.shape[0], 10000 )
print(face_data.shape)

# save this data

np.save('./data/akshay.npy', face_data )