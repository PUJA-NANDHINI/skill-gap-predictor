from prepare_sequences import X, y
from model.lstm_model import build_lstm_model
from sklearn.model_selection import train_test_split

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build model
model = build_lstm_model((X.shape[1], X.shape[2]))

# Train model
model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=2,
    validation_data=(X_test, y_test)
)

# Save model
model.save("model/skill_gap_lstm.h5")

print("Model training complete and saved!")
