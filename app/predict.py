import numpy as np
import os
from tensorflow.keras.models import load_model

# Load trained model from the correct folder
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "skill_gap_lstm.h5")
model = load_model(model_path)
print("Model loaded successfully from:", model_path)


def predict_performance(sequence):
    try:
        print("Input sequence received:", sequence)

        # Ensure sequence is numeric
        sequence = np.array(sequence, dtype=float)

        if sequence.shape[0] != 12:
            raise ValueError("Sequence must contain exactly 12 numeric values.")

        # Reshape to match LSTM input (1 sample, 3 weeks, 4 features)
        sequence = sequence.reshape(1, 3, 4)

        # Make prediction
        prediction = model.predict(sequence)
        predicted_value = float(prediction[0][0])
        print("Predicted value:", predicted_value)

        return predicted_value

    except Exception as e:
        print("Error in prediction:", e)
        return None
