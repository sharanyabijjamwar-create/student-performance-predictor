# 🎓 Student Performance Predictor

A simple Machine Learning project that predicts whether a student is likely to **Pass or Fail** based on study habits and academic information.

## 📌 About the Project

This project uses **Logistic Regression** to predict student performance.

The model uses four inputs:

* Study Hours per Day
* Attendance Percentage
* Previous Marks
* Assignments Completed

The project also includes a simple **Streamlit web application** where users can enter student details and get a prediction.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Logistic Regression
* Joblib
* Streamlit

## 📂 Project Structure

```text
student-performance-predictor/
│
├── data/
│   └── students.csv
│
├── model/
│   └── model.pkl
│
├── train.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project

```bash
cd student-performance-predictor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Train the model

```bash
python train.py
```

This creates the trained model:

```text
model/model.pkl
```

### 7. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🤖 Machine Learning Model

The project uses **Logistic Regression**, a classification algorithm used to predict one of two outcomes.

The target classes in this project are:

* Pass
* Fail

## 📊 Dataset

The dataset used for this project is a small educational dataset created for demonstration and learning purposes.

Therefore, the reported model accuracy should **not be interpreted as real-world performance**.

## 🎯 Purpose

This project was created as a beginner-friendly Machine Learning project to practice:

* Data preparation
* Classification
* Model training
* Model saving
* Prediction
* Streamlit deployment
* Git and GitHub workflow

## 👩‍💻 Author

**Sharanya**

B.Tech Artificial Intelligence & Machine Learning Student
