from flask import Flask, render_template, request
import pickle
# master variable
app = Flask("__main__")


#routes --> different request me karna kya hai

with open("model.pkl", 'rb') as f:
	model = pickle.load(f)


@app.route("/")
def kuch_bhi():
	return render_template("home.html"  )


# Marks prediction
@app.route("/marks", methods=['POST'])
def marks():
	if request.method == 'POST':
		hours = request.form['inp_hours']
		
		print(type(model))
		marks = model.predict([[int(hours)]])

		return render_template("home.html", marks = round(marks[0][0], 2))


if __name__ == '__main__':
	#to create a web server

	# app.debug = True
	app.run(debug = True)