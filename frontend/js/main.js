// main.js

async function makePrediction() {
    const model = document.getElementById("model").value;
    const featuresInput = document.getElementById("features").value;
    const resultDiv = document.getElementById("result");

    // Clear previous results
    resultDiv.innerText = "";
    resultDiv.style.color = "#333";

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

    try {
        const response = await fetch("https://your-app-name.onrender.com/predict", { // Replace with Render URL
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ model, features })
        });

        const result = await response.json();

        if (response.ok) {
            resultDiv.innerText = `Model: ${result.model}, Prediction: ${result.prediction}`;
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
