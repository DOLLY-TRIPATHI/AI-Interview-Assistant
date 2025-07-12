import streamlit as st
from app.question_generator import get_question
from app.answer_analyzer import analyze_answer
from app.feedback_generator import generate_feedback

st.title("🎙️ AI Interview Assistant")
st.markdown("Prepare for interviews with real-time AI feedback!")

# Get random question
question = get_question()
st.subheader("🧠 Interview Question")
st.write(question)

# User input
answer = st.text_area("✍️ Type your answer or paste here:")

if st.button("🧪 Evaluate Answer"):
    analysis = analyze_answer(answer, question)
    feedback = generate_feedback(analysis)
    st.success("✅ Feedback")
    st.write(feedback['summary'])
    st.progress(int(feedback['score']))
