"""
generate_data.py
Creates a synthetic student performance dataset.
Run this once to (re)create data/student_data.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(21)

N = 300
genders = ["Male", "Female"]
parent_education = ["High School", "Bachelor's", "Master's", "PhD"]

student_id = np.arange(1, N + 1)
gender = np.random.choice(genders, N)
study_hours = np.round(np.random.uniform(0, 10, N), 1)
attendance_pct = np.round(np.random.uniform(50, 100, N), 1)
parental_edu = np.random.choice(parent_education, N, p=[0.35, 0.35, 0.2, 0.1])

# final score influenced by study hours + attendance + some noise
base_score = (study_hours * 6) + (attendance_pct * 0.35) + np.random.normal(0, 8, N)
final_score = np.clip(base_score, 0, 100).round(1)

df = pd.DataFrame({
    "StudentID": student_id,
    "Gender": gender,
    "StudyHoursPerDay": study_hours,
    "AttendancePercentage": attendance_pct,
    "ParentalEducation": parental_edu,
    "FinalScore": final_score,
})

# a handful of missing attendance values, as would happen in real records
missing_idx = np.random.choice(df.index, 8, replace=False)
df.loc[missing_idx, "AttendancePercentage"] = np.nan

Path("data").mkdir(exist_ok=True)
df.to_csv("data/student_data.csv", index=False)
print(f"Saved {len(df)} rows to data/student_data.csv")
