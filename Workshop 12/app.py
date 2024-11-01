import warnings
import pickle
import numpy as np
from pymongo import MongoClient
import time
from flask import Flask, jsonify, render_template

warnings.filterwarnings("ignore")

# Initialize Flask app
app = Flask(__name__)

# Load the model and scaler
with open('svm_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Connect to MongoDB
client = MongoClient("mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Replace with your MongoDB URI
db = client["HAR"]  # Replace with your database name
collection = db["Lab_Web"]  # Replace with your collection name

# Global variable to store the latest prediction
latest_prediction = "Waiting for data..."

def calculate_features(data):
    x_values = np.array(data.get('x_values', []))
    y_values = np.array(data.get('y_values', []))
    z_values = np.array(data.get('z_values', []))

    if x_values.size > 0 and y_values.size > 0 and z_values.size > 0:
        x_mean = np.mean(x_values)
        y_mean = np.mean(y_values)
        z_mean = np.mean(z_values)
        x_range = np.max(x_values) - np.min(x_values)
        y_range = np.max(y_values) - np.min(y_values)
        z_range = np.max(z_values) - np.min(z_values)
        xy_corr = np.corrcoef(x_values, y_values)[0, 1] if x_values.size > 1 else 0
        yz_corr = np.corrcoef(y_values, z_values)[0, 1] if y_values.size > 1 else 0
        xz_corr = np.corrcoef(x_values, z_values)[0, 1] if z_values.size > 1 else 0
        return np.array([[x_mean, y_mean, z_mean, x_range, y_range, z_range, xy_corr, yz_corr, xz_corr]])
    else:
        return np.zeros((1, 9))

def fetch_and_predict():
    global latest_prediction
    last_id = None

    while True:
        query = {} if last_id is None else {"_id": {"$gt": last_id}}
        data = collection.find_one(query, sort=[("_id", 1)])

        if data:
            last_id = data["_id"]
            features = calculate_features(data)
            features_normalized = scaler.transform(features)
            predicted_label = model.predict(features_normalized)[0]

            # Update latest prediction based on model output
            if predicted_label == 0:
                latest_prediction = "Walking"
            elif predicted_label == 1:
                latest_prediction = "Sitting"
            else:
                latest_prediction = "Unknown activity"

        # Wait for a specified interval before checking for new data
        time.sleep(5)

# Start the prediction loop in a separate thread
import threading
threading.Thread(target=fetch_and_predict, daemon=True).start()

# Flask route to serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Flask route to provide the latest prediction as JSON
@app.route('/prediction')
def get_prediction():
    return jsonify(prediction=latest_prediction)

if __name__ == "__main__":
    app.run(debug=True)
