# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load models
model_a = joblib.load(os.path.join("models", "model_a.pkl"))
model_b = joblib.load(os.path.join("models", "model_b.pkl"))

@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Check if model choice and features are provided
    if 'model' not in data or 'features' not in data:
        return jsonify({"error": "Model choice and features are required"}), 400

    model_choice = data['model']
    features = data['features']

    # Validate model choice
    if model_choice not in ["A", "B"]:
        return jsonify({"error": "Invalid model choice. Choose 'A' or 'B'."}), 400

    # Validate features format
    if not isinstance(features, list) or not all(isinstance(x, (int, float)) for x in features):
        return jsonify({"error": "Features must be a list of numbers"}), 400

    # Choose the correct model and make a prediction
    try:
        if model_choice == "A":
            prediction = model_a.predict([features])[0]
        elif model_choice == "B":
            prediction = model_b.predict([features])[0]
        else:
            return jsonify({"error": "Unknown error occurred with model choice"}), 500

        return jsonify({"model": model_choice, "prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
