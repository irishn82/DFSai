# backend/generate_models.py

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import joblib
import os

# Load sample data
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a simple model (Model A)
model_a = LogisticRegression(max_iter=200)
model_a.fit(X_train, y_train)

# Save Model A
os.makedirs("models", exist_ok=True)
joblib.dump(model_a, "models/model_a.pkl")

# Optionally create a second model (Model B)
model_b = LogisticRegression(max_iter=200)
model_b.fit(X_train, y_train)
joblib.dump(model_b, "models/model_b.pkl")

print("Models have been generated and saved to the 'models' directory.")
