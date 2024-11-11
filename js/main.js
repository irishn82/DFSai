// frontend/js/main.js

async function makePrediction() {
    const model = document.getElementById("model").value;
    const featuresInput = document.getElementById("features").value;
    const resultDiv = document.getElementById("result");

    // Clear previous results or messages
    resultDiv.innerText = "";
    resultDiv.style.color = "#333"; // Default color

    // Check for empty input
    if (!featuresInput) {
        resultDiv.innerText = "Please enter feature values.";
        resultDiv.style.color = "red";
        return;
    }

    // Parse and validate features
    const features = featuresInput.split(",").map(Number);
    if (features.some(isNaN)) {
        resultDiv.innerText = "Features must be numbers separated by commas.";
        resultDiv.style.color = "red";
        return;
    }

    // Show loading message
    resultDiv.innerText = "Loading...";
    resultDiv.style.color = "#333";

    try {
        const response = await fetch("http://dfsai.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ model, features })
        });

        const result = await response.json();

        if (response.ok) {
            resultDiv.innerText = `Success! Model: ${result.model}, Prediction: ${result.prediction}`;
            resultDiv.style.color = "green"; // Success message color
        } else {
            resultDiv.innerText = `Error: ${result.error}`;
            resultDiv.style.color = "red"; // Error message color
        }
    } catch (error) {
        console.error("Error:", error);
        resultDiv.innerText = "An error occurred while making the prediction. Please try again.";
        resultDiv.style.color = "red";
    }
}
