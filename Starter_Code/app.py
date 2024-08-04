# Import the dependencies.

from flask import Flask, jsonify
import numpy as np
import datetime as dt

# Create a Flask app
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return (
        "Welcome to the Climate App! Available routes: "
        f"/api/v1.0/precipitation" 
        f"/api/v1.0/stations" 
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>" 
        f"/api/v1.0/<start>/<end>"
    )

# Define the /api/v1.0/precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    last_12_months_precipitation = {}  
    return jsonify(last_12_months_precipitation)

# Define the /api/v1.0/stations route
@app.route('/api/v1.0/stations')
def stations():
    stations_data = {} 
    return jsonify(stations_data)

# Define the /api/v1.0/tobs route
@app.route('/api/v1.0/tobs')
def tobs():
    tobs_data = {} 
    return jsonify(tobs_data)

# Define the /api/v1.0/<start> route
@app.route('/api/v1.0/<start>')
def start_date(start):
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    calculated_data = {} 
    return jsonify(calculated_data)

# Define the /api/v1.0/<start>/<end> route
@app.route('/api/v1.0/<start>/<end>')
def start_end_date(start, end):
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    calculated_data = {}
    return jsonify(calculated_data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)