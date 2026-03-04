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
        const score = (data.predicted_quiz_score * 10).toFixed(2);

        document.getElementById("result").innerHTML =
             "<strong>Predicted Quiz Score:</strong> " + score + "<br><br>" +
             "<strong>Skill Gap Level:</strong> " + data.skill_gap_level + "<br>" +
             "<strong>Weak Area:</strong> " + data.weak_area + "<br>" +
             "<strong>Recommendation:</strong> " + data.recommendation;
        
    } catch (error) {
        alert("Failed to get prediction. Check your network or API.");
    }
}