from flask import Flask, render_template

# master variable
app = Flask("__main__")


#routes --> different request me karna kya hai


my_age = 17

# my_intro = [my_name, my_age, my_hobby]
my_intro = {
	"name" : "Rohit",
	"age" : 19,
	"hobby" : "Singing"
}


dog = "https://i.ytimg.com/vi/7xh1DAKIdng/maxresdefault.jpg"


@app.route("/")
def kuch_bhi():
	return render_template("home.html", intro = my_intro, age = my_age, dog_img = dog  )


@app.route("/orders")
def order():
	return "I'm a order page"

if __name__ == '__main__':
	#to create a web server

	# app.debug = True
	app.run(debug = True)