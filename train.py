import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv("data/students.csv")

# Input features
X = data[["StudyHours", "Attendance", "PreviousMarks", "Assignments"]]

# Target
y = data["Result"]


# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create the ML model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)


# Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model trained successfully!")
print(f"Accuracy: {accuracy * 100:.2f}%")


# Save the trained model
joblib.dump(model, "model/model.pkl")

print("Model saved successfully to model/model.pkl")