
from flask import Flask
app = Flask("Hasley")

@app.route("/")
def hello():
    return "Hello World!"


