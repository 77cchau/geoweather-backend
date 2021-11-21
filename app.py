from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import weather

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/verify", methods=["POST"])
def get_weather():
    if (request.form["state"] and request.form["city"]):
        try:
            report = weather.get_forecast_data(request.form["city"], request.form["state"]) 
            return jsonify(report)
        except:
            return "400"
    else:
        return "400"
