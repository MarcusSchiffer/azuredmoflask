from flask import Flask

app = Flask(__name__)

@app.route("/marcus")
def hello_world():
    return "<p>Hello Marcus!</p>"
