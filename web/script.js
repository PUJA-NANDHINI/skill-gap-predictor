async function predict() {
    const input = document.getElementById("sequence").value;
    const sequence = input.split(",").map(Number);

    if (sequence.length !== 12) {
        alert("Please enter exactly 12 numbers");
        return;
    }

    try {
        const response = await fetch("https://skill-gap-predictor-pwav.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ sequence: sequence })
        });

        if (!response.ok) {
            const error = await response.json();
            alert("Error: " + (error.error || "Something went wrong"));
            return;
        }

        const data = await response.json();
        document.getElementById("result").innerText = 
            "Predicted Quiz Score: " + data.predicted_quiz_score.toFixed(2);

    } catch (error) {
        console.error("Error:", error);
        alert("Failed to get prediction. Check your network or API URL.");
    }
}
