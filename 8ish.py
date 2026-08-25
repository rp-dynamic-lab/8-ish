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

while True:
    question = input("\nAsk 8ish something (or type quit): ")

    if question.lower() == "quit":
        print("...ish out.")
        break

    answer = random.choice(answers)
    print(answer)
    