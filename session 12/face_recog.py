import cv2
import numpy as np
import os
from scipy import stats

# ===============KNN Code==================

def distance(p1, p2):
    """ euclidean distance between p1 and p2 """
    return np.sum((p1-p2)**2)**0.5


def kNN(X, y, x_query, k = 7):
    m = X.shape[0]
    
    all_distances = []
    
    for i in range(m):
        d = distance(X[i], x_query)
        all_distances.append((d, y[i]))
    
    all_distances = sorted(all_distances)
    all_distances = np.array(all_distances)
    
    top = all_distances[:k]
    
    labels = top[:, 1]
    
    val = stats.mode(labels)
    pred = int(val[0][0])
    
    return pred
# =============================================




# Data Collection
face_data = []
face_labels = []

class_Id = 0
names = {}


for fx in os.listdir('./data'):
	if fx.endswith('.npy'):
		# create a mapping between class_Id and name
		names[class_Id] =  fx[:-4]
		print("loaded : "+ fx)
		data_item = np.load('./data/'+fx)
		face_data.append(data_item)

		# labels for current class
		target = [class_Id]*data_item.shape[0]
		face_labels.append(target)
		class_Id+=1


X = np.concatenate(face_data, axis=0)
Y = np.concatenate(face_labels, axis=0)


print(X.shape,Y.shape)






cam = cv2.VideoCapture(1)
model = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')


while True:
	ret , frame_rgb = cam.read()
	if not ret:
		continue

	frame = cv2.cvtColor(frame_rgb,cv2.COLOR_BGR2GRAY)

	faces = model.detectMultiScale(frame, 1.5)

	if len(faces)==0:
		continue


	for face in faces:
	    x,y,w,h = face
	   

	    # Crop your face
	    offset = 10
	    face_section = frame[y-offset : y+h+offset, x-offset : x+offset+w]
	    face_section = cv2.resize(face_section, (100,100) )
	    face_section = face_section.reshape(1, 10000)


	    # Call knn function get prediction
	    pred = kNN(X, Y,face_section )
	    pred_name = names[pred]
	    print(pred_name)

	    # displaying results.
	    frame_rgb = cv2.rectangle(frame_rgb, (x, y), (x+w, y+h), (0,255,0), 4 )
	    cv2.putText(frame_rgb, pred_name, (x, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0))


	cv2.imshow("Faces", frame_rgb)
	
	# wait for user input - q, then stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break


cam.release()
cv2.destroyAllWindows()