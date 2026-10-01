import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("model/model.pkl")


# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# Title
st.title("🎓 Student Performance Predictor")

st.write(
    "Enter the student's details below to predict whether "
    "the student is likely to Pass or Fail."
)


# User inputs
study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=15.0,
    value=5.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=60.0,
    step=1.0
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=7,
    step=1
)


# Prediction button
if st.button("🔮 Predict Performance"):

    input_data = pd.DataFrame({
        "StudyHours": [study_hours],
        "Attendance": [attendance],
        "PreviousMarks": [previous_marks],
        "Assignments": [assignments]
    })

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100

    st.divider()

    if prediction == "Pass":
        st.success(f"### ✅ Prediction: PASS")
    else:
        st.error(f"### ❌ Prediction: FAIL")

    st.info(f"Prediction confidence: {confidence:.2f}%")