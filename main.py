import streamlit as st
import streamlit.components.v1 as components
from app.question_generator import get_question
from app.answer_analyzer import analyze_answer
from app.feedback_generator import generate_feedback

# 🎤 Voice input dependencies
from streamlit_mic_recorder import mic_recorder


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


# 🎤 JavaScript-based mic input
st.subheader("🎤 Or Speak Your Answer")

components.html("""
  <button onclick="startDictation()" style="padding:10px 20px; font-size:16px;">🎙 Speak Your Answer</button>
  <br><br>
  <textarea id="transcript" rows="5" style="width:100%; font-size:16px;" placeholder="Your answer will appear here..."></textarea>

  <script>
    function startDictation() {
      if (window.hasOwnProperty('webkitSpeechRecognition')) {
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = "en-US";
        recognition.start();

        recognition.onresult = function(e) {
          document.getElementById('transcript').value = e.results[0][0].transcript;
          const inputEvent = new Event('input', { bubbles: true });
          document.getElementById('transcript').dispatchEvent(inputEvent);
          recognition.stop();
        };

        recognition.onerror = function(e) {
          alert("Speech recognition error: " + e.error);
          recognition.stop();
        };
      } else {
        alert("Speech recognition not supported in this browser.");
      }
    }
  </script>
""", height=300)
# ✍️ User input (linked with voice)
answer = st.text_area("📝 Answer (auto-filled or typed):", key="answer")

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
