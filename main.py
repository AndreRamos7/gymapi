from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Worlds!</p>"

@app.route("/cluster")
def cluster():
    return "<p>Hello, Cluster!</p>"

@app.route("/prevision")
def prevision():
    return "<p>Hello, Prevision!</p>"