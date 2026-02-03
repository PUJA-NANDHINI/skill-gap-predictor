from app.predict import predict_performance

# Example student weekly data
sample_sequence = [
    [70, 5, 1, 2],
    [75, 6, 0, 1],
    [80, 7, 0, 1]
]

result = predict_performance(sample_sequence)

print("Predicted Next Quiz Score:", result)
