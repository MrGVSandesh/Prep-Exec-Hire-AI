import pandas as pd

df = pd.read_csv(
    "data/interview_questions.csv"
)

def get_questions(role):

    filtered = df[
        df['role'] == role
    ]

    return filtered