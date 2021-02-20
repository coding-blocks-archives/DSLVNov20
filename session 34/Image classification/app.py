from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# master variable
app = Flask(__name__)

dic = {
	0 : 'cat',
	1 : 'dog',
	2 : 'horse',
	3 : 'human'
}

model = load_model('./model.h5')


def predict_new_img(img_path):
	# read img first
	i = image.load_img(img_path, target_size= (224,224))
	i = image.img_to_array(i)
	i = i.reshape(1, 224,224,3)
	prob = model.predict(i)
	p = np.argmax(prob, axis = -1)

	return dic[int(p)], np.round(prob[0][p], 2)


#routes --> different request me karna kya hai

@app.route("/")
def kuch_bhi():
	return render_template("home.html")


@app.route("/submit", methods=['POST', 'GET'])
def submit():
	if request.method == 'POST':
		img = request.files['inp_file']
		img_path = "static/"+ img.filename 
		img.save(img_path)

		pred = predict_new_img(img_path)


		return render_template("home.html", prediction = pred, img_path = img_path )

if __name__ == '__main__':
	#to create a web server

	# app.debug = True
	app.run(debug = True)