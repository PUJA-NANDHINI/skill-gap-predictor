import pandas as pd
import numpy as np
from load_data import load_student_data


# Load dataset
df = load_student_data()


# Features we want the model to learn from
FEATURES = ["quiz_score", "practice_hours", "assignment_delay", "errors"]

SEQUENCE_LENGTH = 3  # number of weeks per sequence

X = []
y = []

# Group data by student
for student_id, student_df in df.groupby("student_id"):
    student_df = student_df.sort_values("week")
    feature_values = student_df[FEATURES].values
    
    for i in range(len(feature_values) - SEQUENCE_LENGTH):
        X.append(feature_values[i:i + SEQUENCE_LENGTH])
        y.append(feature_values[i + SEQUENCE_LENGTH][0])  # next quiz_score

X = np.array(X)
y = np.array(y)

print("Sequence shape (X):", X.shape)
print("Target shape (y):", y.shape)
