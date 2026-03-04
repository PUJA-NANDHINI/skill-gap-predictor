async function predict() {

    const sequence = [
        Number(document.getElementById("w1_ph").value),
        Number(document.getElementById("w1_as").value),
        Number(document.getElementById("w1_ec").value),
        Number(document.getElementById("w1_qs").value),

        Number(document.getElementById("w2_ph").value),
        Number(document.getElementById("w2_as").value),
        Number(document.getElementById("w2_ec").value),
        Number(document.getElementById("w2_qs").value),

        Number(document.getElementById("w3_ph").value),
        Number(document.getElementById("w3_as").value),
        Number(document.getElementById("w3_ec").value),
        Number(document.getElementById("w3_qs").value)
    ];

    if (sequence.some(isNaN)) {
        alert("Please fill all fields properly.");
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

        const data = await response.json();

        const score = data.predicted_quiz_score.toFixed(2);

        let interpretation = "";

        if (score < 4) {
            interpretation = "High Skill Gap";
        } else if (score < 7) {
            interpretation = "Moderate Skill Gap";
        } else {
            interpretation = "Low Skill Gap";
        }

        document.getElementById("result").innerText =
            "Predicted Quiz Score: " + score + " (" + interpretation + ")";

    } catch (error) {
        alert("Failed to get prediction. Check your network or API.");
    }
}