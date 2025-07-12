import streamlit as st
from app.question_generator import get_question
from app.answer_analyzer import analyze_answer
from app.feedback_generator import generate_feedback

# ✅ Safe rerun logic (doesn't crash on Streamlit Cloud)
try:
    if "rerun_flag" in st.session_state:
        del st.session_state.rerun_flag
        st.rerun()
except:
    pass

# 🎯 Page config
st.set_page_config(page_title="AI Interview Assistant", layout="centered")

st.title("🎙️ AI Interview Assistant")
st.markdown("Prepare for interviews with real-time AI feedback!")

# ✅ Load or keep question
if "question" not in st.session_state:
    st.session_state.question = get_question()

st.header("🧠 Interview Question")
st.markdown(f"**{st.session_state.question}**")

# 🔁 Next Question button
if st.button("🔁 Next Question"):
    st.session_state.question = get_question()
    st.session_state.rerun_flag = True

# ✍️ Input box for answer (no session key conflict)
answer = st.text_area("📝 Type your answer or paste here:")

# ✅ Evaluate answer
if st.button("✅ Evaluate Answer"):
    if answer.strip() == "":
        st.warning("Please enter an answer to evaluate.")
    else:
        score, keywords_covered, tone = analyze_answer(answer, st.session_state.question)
        feedback = generate_feedback(score, keywords_covered, tone)

        st.markdown("### ✅ Feedback")
        st.success(feedback)

        st.progress(score / 100)

# Footer
st.markdown("---")
st.caption("🧠 Powered by Deep Learning • Created by Dolly Tripathi 💻")
