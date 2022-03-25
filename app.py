from flask import Flask
import random

app = Flask(__name__)

@app.route('/speed')
def speed():
    return 267 + 3 * (random.random())

@app.route('/throttle_level')
def throttle():
    return "High"

@app.route('/steering_angle')
def angle():
    return 0

if __name__ == "__main__":
    app.debug = True
    app.run()