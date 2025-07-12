from transformers import pipeline
import re

# Load sentiment analysis model once
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_answer(answer, question):
    # ✅ Score based on length
    word_count = len(answer.split())
    if word_count > 100:
        score = 90
    elif word_count > 50:
        score = 70
    elif word_count > 20:
        score = 50
    else:
        score = 30

    # ✅ Keyword overlap (basic relevance)
    keywords = re.findall(r'\b\w{6,}\b', question.lower())
    keywords_covered = sum(1 for kw in keywords if kw in answer.lower())

    # ✅ Sentiment / Tone
    tone_result = sentiment_pipeline(answer)[0]
    tone = tone_result['label'].lower()

    # ✅ Return expected keys
    return {
        "score": score,
        "keywords_covered": keywords_covered,
        "tone": tone
    }
