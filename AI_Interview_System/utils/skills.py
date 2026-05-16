skills_db = {

    "python": [
        "Explain Python decorators.",
        "What are Python generators?",
        "Explain list comprehension."
    ],

    "machine learning": [
        "What is overfitting?",
        "Explain bias-variance tradeoff.",
        "Difference between supervised and unsupervised learning?"
    ],

    "deep learning": [
        "What is CNN?",
        "Explain RNN.",
        "What is backpropagation?"
    ],

    "sql": [
        "What is normalization?",
        "Difference between DELETE and TRUNCATE?"
    ],

    "nlp": [
        "What is tokenization?",
        "Explain TF-IDF.",
        "What are transformers?"
    ],

    "react": [
        "What are hooks in React?",
        "Explain virtual DOM."
    ]
}

def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in skills_db.keys():

        if skill in text:

            detected_skills.append(skill)

    return detected_skills

def generate_questions(skills):

    questions = []

    for skill in skills:

        questions.extend(
            skills_db[skill]
        )

    return questions