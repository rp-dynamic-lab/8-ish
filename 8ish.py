import random

question = input("Ask 8ish something: ")

answers = [
    "DO IT.",
    "NOPE.",
    "PROBABLY.",
    "NOT TODAY.",
    "EH. MAYBE.",
    "ASK AGAIN."
]

answer = random.choice(answers)

print(answer)
