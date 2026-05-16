import streamlit as st

from utils.parser import extract_text_from_pdf

from utils.skills import (
    extract_skills,
    generate_questions
)

from utils.evaluator import evaluate_answer

from utils.feedback import generate_feedback

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="AI Interview System",
    page_icon="🎯",
    layout="wide"
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a,
            #111827,
            #1e293b
        );
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 55px;
        font-weight: bold;
        color: #38bdf8;
        text-shadow: 0px 0px 20px #38bdf8;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #cbd5e1;
        margin-bottom: 40px;
    }

    .card {
        background: rgba(255,255,255,0.05);
        padding: 25px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0px 0px 20px rgba(56,189,248,0.3);
        margin-bottom: 25px;
    }

    .skill-box {
        background: linear-gradient(
            90deg,
            #06b6d4,
            #3b82f6
        );
        padding: 10px 18px;
        border-radius: 12px;
        color: white;
        font-weight: bold;
        display: inline-block;
        margin: 5px;
        font-size: 16px;
    }

    .question-box {
        background: rgba(15,23,42,0.9);
        padding: 20px;
        border-left: 5px solid #38bdf8;
        border-radius: 15px;
        margin-bottom: 15px;
        color: white;
        font-size: 18px;
    }

    .score-box {
        background: linear-gradient(
            135deg,
            #16a34a,
            #22c55e
        );
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 24px;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
        box-shadow: 0px 0px 20px rgba(34,197,94,0.5);
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 40px;
        font-size: 15px;
    }

    div.stButton > button {
        background: linear-gradient(
            90deg,
            #06b6d4,
            #3b82f6
        );
        color: white;
        border-radius: 12px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        width: 100%;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 20px #38bdf8;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ======================================
# HEADER
# ======================================

st.markdown(
    "<div class='main-title'>AI Interview Preparation System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Transformer-Based Smart Interview Evaluator</div>",
    unsafe_allow_html=True
)

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("⚡ AI Interview Dashboard")

st.sidebar.info(
    "Upload your resume and get AI-generated interview questions based on your skills."
)

st.sidebar.success("Powered by NLP + Transformers")

# ======================================
# RESUME UPLOAD SECTION
# ======================================

st.markdown(
    "<div class='card'>",
    unsafe_allow_html=True
)

uploaded_resume = st.file_uploader(
    "📄 Upload Resume PDF",
    type=["pdf"]
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# ======================================
# PROCESSING
# ======================================

if uploaded_resume:

    with st.spinner("Analyzing Resume..."):

        with open(
            "temp_resume.pdf",
            "wb"
        ) as f:

            f.write(uploaded_resume.read())

        resume_text = extract_text_from_pdf(
            "temp_resume.pdf"
        )

        detected_skills = extract_skills(
            resume_text
        )

        questions = generate_questions(
            detected_skills
        )

    # ======================================
    # SKILLS SECTION
    # ======================================

    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.subheader("🧠 Detected Skills")

    for skill in detected_skills:

        st.markdown(
            f"<span class='skill-box'>{skill.upper()}</span>",
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # ======================================
    # QUESTIONS SECTION
    # ======================================

    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.subheader(
        "🎯 AI Generated Interview Questions"
    )

    total_score = 0

    for i, question in enumerate(questions):

        st.markdown(
            f"<div class='question-box'><b>Question {i+1}:</b> {question}</div>",
            unsafe_allow_html=True
        )

        user_answer = st.text_area(
            f"Your Answer {i+1}",
            key=i,
            height=150
        )

        ideal_answer = question

        if user_answer:

            score = evaluate_answer(
                user_answer,
                ideal_answer
            )

            feedback = generate_feedback(
                score
            )

            total_score += score

            st.success(
                f"✅ Score: {score}%"
            )

            st.info(
                f"💡 Feedback: {feedback}"
            )

            st.progress(
                int(score)
            )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # ======================================
    # FINAL SCORE
    # ======================================

    if len(questions) > 0:

        final_score = (
            total_score / len(questions)
        )

        st.markdown(
            f"""
            <div class='score-box'>
            🚀 FINAL INTERVIEW SCORE <br><br>
            {round(final_score,2)}%
            </div>
            """,
            unsafe_allow_html=True
        )

        if final_score >= 80:

            st.balloons()

            st.success(
                "Excellent Interview Performance"
            )

        elif final_score >= 60:

            st.warning(
                "Good Performance — Improve Technical Depth"
            )

        else:

            st.error(
                "Needs Improvement"
            )

# ======================================
# FOOTER
# ======================================

st.markdown(
    """
    <div class='footer'>
    Developed using Streamlit • NLP • Transformers • Sentence-BERT
    </div>
    """,
    unsafe_allow_html=True
)