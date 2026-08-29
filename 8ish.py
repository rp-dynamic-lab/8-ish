import random

answers = [
    "DO IT.",
    "NOPE.",
    "PROBABLY.",
    "NOT TODAY.",
    "EH. MAYBE.",
    "WHY NOT?",
    "I'D WAIT.",
    "TOO ISH.",
    "SEEMS FINE.",
    "BAD IDEA.",
    "GO ON THEN.",
    "ASK AGAIN."
]

def get_answer(question):
    word_count = len(question.split())

    if word_count < 4:
        return "TOO ISH."

    return random.choice(answers)

while True:
    question = input("\nAsk 8ish something (or type quit): ")

    if question.lower() == "quit":
        print("...ish out.")
        break

    answer = get_answer(question)
    print(answer)
