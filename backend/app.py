from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enables CORS

# Example home route to test the backend
@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})

# Example prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    model_choice = data.get("model")
    features = data.get("features")

    # Simple logic for prediction example
    if model_choice == "A":
        prediction = 1  # Replace with actual model logic
    elif model_choice == "B":
        prediction = 0  # Replace with actual model logic
    else:
        return jsonify({"error": "Invalid model choice"}), 400

    return jsonify({"model": model_choice, "prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
