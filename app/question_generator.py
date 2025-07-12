import random

questions = [
    "What is overfitting in machine learning?",
    "Explain how backpropagation works.",
    "What are CNNs used for?",
    "What is the difference between AI, ML, and Deep Learning?",
]

def get_question():
    return random.choice(questions)
