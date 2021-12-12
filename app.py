"""
    This code is an experiment for evaluating video data streaming
    over a web server.
"""

# Import required libraries
from flask import Flask, render_template, Response
import cv2

# Creating Flask app
app = Flask(__name__)

# Video processing variables
cam = cv2.VideoCapture(0)  # local webcam

# Video processing methods


def gen_frames():
    """
    This method reads data from camera, encodes the values to a 
    .jpg format which are later concatenated and returned within
    a Generator.
    """
    while True:
        success_read, frame = cam.read()
        if success_read:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Frame concatenation
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            print("Error while reading")
            break

# Routes


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/video")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run()
 