# 🧠 Procrastination Predictor

## 📌 Overview
This project predicts whether a student is likely to procrastinate based on behavioral and situational factors.

It combines machine learning with an interactive web interface for real-time predictions.

---

## ⚙️ Features Used
- Task Difficulty
- Deadline Days Left
- Past Procrastination Rate
- Screen Time
- Sleep Hours
- Motivation Level
- Distractions

---

## 🤖 Model
- Logistic Regression
- Accuracy: ~89%
- Includes controlled noise to simulate real-world human inconsistency

---

## 🌐 Web App
Built using Streamlit for interactive predictions.

---

## 🚀 How to Run

### 1. Install dependencies
pip install pandas scikit-learn streamlit joblib


### 2. Train model
py src/train.py


### 3. Run app
py -m streamlit run app.py


---

## 💡 Key Insight
This project focuses not just on accuracy, but on modeling realistic human behavior by introducing controlled inconsistencies in the dataset.

---

## 🔮 Future Improvements
- Use real-world data
- Add psychological features
- Try advanced ML models
- Deploy online