from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_answer(answer, question):
    sentiment = sentiment_pipeline(answer)[0]
    return {
        "sentiment": sentiment,
        "relevance_score": len(set(answer.lower().split()) & set(question.lower().split())) / len(set(question.split())),
        "length": len(answer.split())
    }
