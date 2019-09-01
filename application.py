from flask import Flask

app = Flask(__name__)#name is this file/app is a Flask app

@app.route("/")#when user goes to / the function index is run
def index():
	return "Hello, world!"