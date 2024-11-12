# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

# Home route to confirm the backend is running
@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Get model choice and features from request
    model_choice = data.get("model")
    features = data.get("features")

    # Placeholder prediction logic (replace with real model predictions as needed)
    if model_choice == "A":
        prediction = 1  # Replace with actual model A prediction logic
    elif model_choice == "B":
        prediction = 0  # Replace with actual model B prediction logic
    else:
        return jsonify({"error": "Invalid model choice"}), 400

    return jsonify({"model": model_choice, "prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
