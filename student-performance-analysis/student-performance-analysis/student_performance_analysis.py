"""
Student Performance Analysis
------------------------------
Analyzes academic data using Python to identify factors influencing
student performance.

Author: Hussain Sadriwala
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = "data/student_data.csv"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows, {df.shape[1]} columns")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    before_missing = df["AttendancePercentage"].isna().sum()

    # Fill missing attendance with the overall median
    df["AttendancePercentage"] = df["AttendancePercentage"].fillna(
        df["AttendancePercentage"].median()
    )

    print(f"Filled {before_missing} missing attendance values")
    return df


def explore_data(df: pd.DataFrame) -> None:
    print("\n--- Summary Statistics ---")
    print(df[["StudyHoursPerDay", "AttendancePercentage", "FinalScore"]].describe())

    print("\n--- Average Final Score by Parental Education ---")
    print(df.groupby("ParentalEducation")["FinalScore"].mean().sort_values(ascending=False).round(1))

    print("\n--- Correlations with Final Score ---")
    print(df[["StudyHoursPerDay", "AttendancePercentage", "FinalScore"]].corr()["FinalScore"])


def visualize_data(df: pd.DataFrame) -> None:
    # 1. Study hours vs final score
    plt.figure(figsize=(8, 5))
    plt.scatter(df["StudyHoursPerDay"], df["FinalScore"], color="#2E5077", alpha=0.6)
    plt.title("Study Hours per Day vs Final Score")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Final Score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_hours_vs_score.png", dpi=150)
    plt.close()

    # 2. Attendance vs final score
    plt.figure(figsize=(8, 5))
    plt.scatter(df["AttendancePercentage"], df["FinalScore"], color="#3D6A96", alpha=0.6)
    plt.title("Attendance % vs Final Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Final Score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "attendance_vs_score.png", dpi=150)
    plt.close()

    # 3. Average score by parental education
    avg_by_edu = df.groupby("ParentalEducation")["FinalScore"].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    avg_by_edu.plot(kind="bar", color="#1B3A57")
    plt.title("Average Final Score by Parental Education")
    plt.xlabel("Parental Education")
    plt.ylabel("Average Final Score")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "score_by_parental_education.png", dpi=150)
    plt.close()

    print(f"\nCharts saved to '{OUTPUT_DIR}/'")


def main():
    df = load_data(DATA_PATH)
    df = clean_data(df)
    explore_data(df)
    visualize_data(df)


if __name__ == "__main__":
    main()
