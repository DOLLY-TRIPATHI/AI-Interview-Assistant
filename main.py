import streamlit as st
from app.question_generator import get_question
from app.answer_analyzer import analyze_answer
from app.feedback_generator import generate_feedback

# 🎤 Voice input dependencies
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
import io

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

# 🎤 Voice Input Section
st.subheader("🎤 Or Speak Your Answer")
audio = mic_recorder(start_prompt="Start recording", stop_prompt="Stop recording", just_once=True, key="voice")

if audio:
    recognizer = sr.Recognizer()
    audio_data = sr.AudioFile(io.BytesIO(audio["bytes"]))
    with audio_data as source:
        recorded = recognizer.record(source)
        try:
            transcribed_text = recognizer.recognize_google(recorded)
            st.success("✅ Transcribed: " + transcribed_text)
            st.session_state['answer'] = transcribed_text
        except sr.UnknownValueError:
            st.error("⚠️ Sorry, could not understand the audio.")
        except sr.RequestError:
            st.error("⚠️ Speech service is down. Try again later.")

# ✍️ User input (linked with voice)
answer = st.text_area("📝 Type your answer or paste here:", value=st.session_state.get("answer", ""), key="answer_box")

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
