"""
    This code is an experiment for evaluating video data streaming
    over a web server.
"""

# Import required libraries
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()