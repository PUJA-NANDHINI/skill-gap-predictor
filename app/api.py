from flask import Flask, request, jsonify
from app.predict import predict_performance

app = Flask(__name__)

@app.route("/")
def home():
    return "Skill Gap Prediction API is Running Successfully"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    sequence = data["sequence"]

    prediction = predict_performance(sequence)

    return jsonify({
        "predicted_quiz_score": prediction
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
