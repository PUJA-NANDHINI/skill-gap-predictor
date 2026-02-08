from flask import Flask, request, jsonify
from app.predict import predict_performance
import os

app = Flask(__name__)
print("API FILE LOADED SUCCESSFULLY")

@app.route("/")
def home():
    return "Skill Gap Prediction API is Running Successfully"

@app.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ENDPOINT HIT")

    try:
        data = request.get_json(force=True)

        if "sequence" not in data:
            return jsonify({"error": "Sequence missing"}), 400

        sequence = data["sequence"]

        if len(sequence) != 12:
            return jsonify({"error": "Sequence must contain exactly 12 values"}), 400

        # Call prediction function
        prediction = predict_performance(sequence)

        if prediction is None:
            return jsonify({"error": "Invalid input or prediction failed"}), 400

        return jsonify({"predicted_quiz_score": prediction})

    except Exception as e:
        print("Error in /predict endpoint:", e)
        return jsonify({"error": "An unexpected error occurred"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
