from flask import Flask
app = Flask(__name__)

@app.route("/")
def oh_hi_there():
    return "Howdy sailor!"
