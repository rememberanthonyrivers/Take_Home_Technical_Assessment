from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome To The Index Page"