from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to world of flask"


@app.route("/home")
def home():
    return "home page"
