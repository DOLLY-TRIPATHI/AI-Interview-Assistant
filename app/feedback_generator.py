def generate_feedback(analysis):
    sentiment = analysis['sentiment']
    score = int(analysis['relevance_score'] * 100)

    if sentiment['label'] == "POSITIVE":
        tone = "confident"
    else:
        tone = "improvable"

    summary = f"Your tone seems **{tone}**, and your answer covers about **{score}%** of the key terms."
    return {"summary": summary, "score": score}
