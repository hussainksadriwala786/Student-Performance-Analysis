# Student Performance Analysis

Analyzed academic data using Python to identify factors influencing student
performance.

## Overview

This project looks at how study habits, attendance, and parental education
relate to a student's final score, using basic statistical analysis and
visualization to surface the strongest drivers of performance.

## Dataset

`data/student_data.csv` contains one row per student:

| Column                | Description                              |
|------------------------|-------------------------------------------|
| StudentID              | Unique student identifier                 |
| Gender                 | Male / Female                             |
| StudyHoursPerDay       | Average hours studied per day             |
| AttendancePercentage   | Class attendance percentage                |
| ParentalEducation      | Highest parental education level          |
| FinalScore             | Final exam score (0-100)                  |

Run `generate_data.py` to regenerate the dataset (a few missing attendance
values are injected intentionally so the cleaning step is meaningful).

## What the analysis does

1. **Load** the raw CSV.
2. **Clean** — fills missing attendance values with the median.
3. **Explore**
   - Summary statistics
   - Average final score by parental education level
   - Correlation of study hours & attendance with final score
4. **Visualize**
   - Scatter plot: study hours vs. final score
   - Scatter plot: attendance vs. final score
   - Bar chart: average final score by parental education

Charts are saved to the `outputs/` folder.

## Key Insight

Study hours show a much stronger correlation with final score (~0.88) than
attendance (~0.20) in this dataset — consistent time spent studying matters
more than simply showing up to class.

## Tech Stack

- Python
- Pandas
- Matplotlib

## How to run

```bash
pip install -r requirements.txt
python generate_data.py                  # creates data/student_data.csv
python student_performance_analysis.py   # cleans, explores, and charts the data
```

## Project Structure

```
student-performance-analysis/
├── data/
│   └── student_data.csv
├── outputs/
│   ├── study_hours_vs_score.png
│   ├── attendance_vs_score.png
│   └── score_by_parental_education.png
├── generate_data.py
├── student_performance_analysis.py
├── requirements.txt
└── README.md
```
