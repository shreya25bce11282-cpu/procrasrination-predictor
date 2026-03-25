import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="Procrastination Predictor", page_icon="🧠")

# Title
st.title("🧠 Procrastination Predictor")
st.caption("Because your future self deserves honesty 😌")

st.divider()

# Inputs in columns (looks cleaner)
col1, col2 = st.columns(2)

with col1:
    task_difficulty = st.slider("Task Difficulty", 1, 10)
    past_procrastination_rate = st.slider("Past Procrastination (%)", 0, 100)
    sleep_hours = st.slider("Sleep Hours", 1, 10)
    distractions = st.slider("Distractions", 1, 10)

with col2:
    deadline_days_left = st.slider("Days Left", 1, 14)
    screen_time = st.slider("Screen Time (hrs)", 1, 10)
    motivation_level = st.slider("Motivation Level", 1, 10)

st.divider()

# Predict
if st.button("🔮 Predict My Fate"):
    input_data = pd.DataFrame([{
        "task_difficulty": task_difficulty,
        "deadline_days_left": deadline_days_left,
        "past_procrastination_rate": past_procrastination_rate,
        "screen_time": screen_time,
        "sleep_hours": sleep_hours,
        "motivation_level": motivation_level,
        "distractions": distractions
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ You’re likely to procrastinate… maybe just one more reel?")
    else:
        st.success("✅ You’ll stay productive. Main character energy 💅")

    st.info("Tip: Try changing motivation or distractions to see how it affects results!")