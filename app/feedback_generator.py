def generate_feedback(score, keywords_covered=None, tone=None):
    feedback = ""

    if score >= 80:
        feedback += "Great job! Your answer is very relevant. "
    elif score >= 50:
        feedback += "Decent attempt. Try to add more relevant points. "
    else:
        feedback += "Your answer lacks depth. Consider studying the topic more. "

    if tone:
        if "confident" in tone.lower():
            feedback += "You sound confident. "
        elif "improvable" in tone.lower():
            feedback += "Your tone seems improvable. "

    if keywords_covered is not None:
        feedback += f"You covered about {keywords_covered}% of key terms."

    return feedback
