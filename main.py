import streamlit as st
from app.question_generator import get_question
from app.answer_analyzer import analyze_answer
from app.feedback_generator import generate_feedback

# ✅ Rerun logic for Streamlit Cloud (safe for all versions)
if "rerun_flag" in st.session_state:
    del st.session_state.rerun_flag
    st.experimental_rerun()

# Set page title
st.set_page_config(page_title="AI Interview Assistant", layout="centered")

st.title("🎙️ AI Interview Assistant")
st.markdown("Prepare for interviews with real-time AI feedback!")

# ✅ Step 1: Show interview question (with session state)
if "question" not in st.session_state:
    st.session_state.question = get_question()

st.header("🧠 Interview Question")
st.markdown(f"**{st.session_state.question}**")

# 🔁 Step 2: Next Question button
if st.button("🔁 Next Question"):
    st.session_state.question = get_question()
    st.session_state.answer = ""  # clear old answer
    st.session_state.rerun_flag = True

# ✍️ Step 3: User input
answer = st.text_area("📝 Type your answer or paste here:", key="answer")

# ✅ Step 4: Evaluate Button
if st.button("✅ Evaluate Answer"):
    if answer.strip() == "":
        st.warning("Please enter an answer to evaluate.")
    else:
        # Analyze answer
        score, keywords_covered, tone = analyze_answer(answer, st.session_state.question)

        # Generate feedback
        feedback = generate_feedback(score, keywords_covered, tone)

        # Show feedback
        st.markdown("### ✅ Feedback")
        st.success(feedback)

        # Optional: Show score bar
        st.progress(score / 100)

# Footer
st.markdown("---")
st.caption("🧠 Powered by Deep Learning • Created by Dolly Tripathi 💻")
