import os
import numpy as np
from tensorflow.keras.models import load_model

# Load model once at the module level
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "skill_gap_lstm.h5")
model = load_model(model_path)
print(f"Model loaded successfully from: {model_path}")

def predict_performance(sequence):
    sequence = np.array(sequence)
    sequence = sequence.reshape(1, 3, 4)  # 1 sample, 3 weeks, 4 features

    prediction = model.predict(sequence, verbose=0)  # silent predict
    return float(prediction[0][0])
