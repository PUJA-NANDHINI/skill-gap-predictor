import numpy as np
from tensorflow.keras.models import load_model
import os

# Get the absolute path to the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "skill_gap_lstm.h5")

def predict_performance(sequence):
    # Lazy load the model inside the function
    model = load_model(MODEL_PATH)
    print("Model loaded successfully inside predict function")

    # Convert input to numpy array and reshape for LSTM
    sequence = np.array(sequence)
    sequence = sequence.reshape(1, 3, 4)  # 1 sample, 3 weeks, 4 features

    prediction = model.predict(sequence)

    return float(prediction[0][0])
