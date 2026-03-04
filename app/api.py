from flask import Flask, request, jsonify
from app.predict import predict_performance
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
print("API FILE LOADED SUCCESSFULLY")


@app.route("/")
def home():
    return "Skill Gap Prediction API is Running Successfully"

@app.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ENDPOINT HIT")
    data = request.get_json(force=True)
    if "sequence" not in data:
        return jsonify({"error": "Sequence missing"}), 400

    sequence = data["sequence"]
    if len(sequence) != 12:
        return jsonify({"error": "Sequence must contain exactly 12 values"}), 400

     # 🔹 Step 1: Get AI Prediction
    prediction = predict_performance(sequence)

    # 🔹 Step 2: Explainable AI Logic (Feature Analysis)

    # Extract week-wise features
    practice_hours = [sequence[0], sequence[4], sequence[8]]
    assignment_scores = [sequence[1], sequence[5], sequence[9]]
    error_counts = [sequence[2], sequence[6], sequence[10]]
    quiz_scores = [sequence[3], sequence[7], sequence[11]]

    # Calculate averages
    avg_practice = sum(practice_hours) / 3
    avg_assignment = sum(assignment_scores) / 3
    avg_errors = sum(error_counts) / 3

    # Determine Skill Gap Level (0–100 scale)
    if prediction < 60:
        skill_gap_level = "High Skill Gap"
    elif prediction < 75:
        skill_gap_level = "Moderate Skill Gap"
    else:
        skill_gap_level = "Low Skill Gap"

    # Identify Weak Area (Adjusted for dataset scale)

    if avg_practice < 4:
        weak_area = "Low Practice Hours"
        recommendation = "Increase weekly practice hours to strengthen understanding."

    elif avg_assignment > 1:
        weak_area = "High Assignment Delay"
        recommendation = "Submit assignments on time to improve performance."

    elif avg_errors > 12:
        weak_area = "High Error Rate"
        recommendation = "Review mistakes carefully and practice error correction."

    else:
        weak_area = "Balanced Performance"
        recommendation = "Maintain consistent effort across all activities."
 
    # 🔹 Step 3: Return Extended Response
    return jsonify({
        "predicted_quiz_score": prediction,
        "skill_gap_level": skill_gap_level,
        "weak_area": weak_area,
        "recommendation": recommendation
    })

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
