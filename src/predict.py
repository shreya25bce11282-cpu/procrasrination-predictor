import joblib
import pandas as pd

model = joblib.load("model.pkl")

columns = [
    "task_difficulty",
    "deadline_days_left",
    "past_procrastination_rate",
    "screen_time",
    "sleep_hours",
    "motivation_level",
    "distractions"
]

sample = pd.DataFrame([[7, 2, 80, 7, 5, 3, 8]], columns=columns)

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Will procrastinate 😬")
else:
    print("Will NOT procrastinate 💪")