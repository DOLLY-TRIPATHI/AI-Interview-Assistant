import streamlit as st
from app.question_generator import get_question
from app.answer_analyzer import analyze_answer
from app.feedback_generator import generate_feedback

st.set_page_config(page_title="AI Interview Assistant", layout="centered")

st.title("🎙️ AI Interview Assistant")
st.markdown("Prepare for interviews with real-time AI feedback!")

if "question" not in st.session_state:
    st.session_state.question = get_question()

# Show current question
st.header("🧠 Interview Question")
st.markdown(f"**{st.session_state.question}**")

# 🔁 Next question
if st.button("🔁 Next Question"):
    st.session_state.question = get_question()

# ✍️ User input
answer = st.text_area("📝 Type your answer or paste here:")

# ✅ Evaluate
if st.button("🧪 Evaluate Answer"):
    if answer.strip() == "":
        st.warning("Please enter an answer to evaluate.")
    else:
        analysis = analyze_answer(answer, st.session_state.question)

        # ✅ Correct usage of score, tone, keywords
        feedback = generate_feedback(
            score=analysis['score'],
            keywords_covered=analysis['keywords_covered'],
            tone=analysis['tone']
        )

        st.markdown("### ✅ Feedback")
        st.success(feedback)
        st.progress(analysis['score'] / 100)

# Footer
st.markdown("---")
st.caption("🧠 Powered by Deep Learning • Created by Dolly Tripathi 💻")
