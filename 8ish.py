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

filler_words = [
    "should",
    "i",
    "do",
    "it",
    "this",
    "that",
    "a",
    "an",
    "the",
    "is",
    "are",
    "am",
    "to",
    "of",
    "for",
    "at",
    "my",
    "me",
    "we",
    "you",
    "have"
]

decision_markers = [
    "because",
    "but",
    "if",
    "unless",
    "since",
    "after",
    "before",
    "instead"
]

# This list holds the conversation while 8ish is running.
history = []

# Learning note:
# Context words can identify the topic without giving enough context
# for a decision.
#
# Example:
# "Should I take the train?"
# tells 8ish what the question is about, but not enough about the
# situation to justify an answer.

# TODO:
# Misspellings can still create false positives.
# Example: "Shold I take the train?" may treat "shold" like
# meaningful information.

# Learning note:
# 8ish can now store earlier questions and answers during a session.
# It remembers what happened, but it does not use that memory yet.
#
# Next problem:
# Can new information be combined with earlier context before
# 8ish makes another judgment?


def get_topic_words(question):
    words = (
        question.lower()
        .replace("?", "")
        .replace(",", "")
        .replace(".", "")
        .split()
    )

    topic_words = []

    for word in words:
        if word not in filler_words and word not in decision_markers:
            topic_words.append(word)

    return topic_words


def get_decision_signals(question):
    words = (
        question.lower()
        .replace("?", "")
        .replace(",", "")
        .replace(".", "")
        .split()
    )

    signals = []

    for word in words:
        if word in decision_markers:
            signals.append(word)

    return signals


def get_answer(question):
    topic_words = get_topic_words(question)
    decision_signals = get_decision_signals(question)

    print("Topic:", topic_words)
    print("Decision signals:", decision_signals)

    if len(topic_words) < 2:
        return "TOO ISH."

    if len(decision_signals) == 0:
        return "TOO ISH."

    return random.choice(answers)


def show_history():
    print("\n8ish remembers:")

    if len(history) == 0:
        print("Nothing yet.")
        return

    for item in history:
        print("Question:", item["question"])
        print("Answer:", item["answer"])
        print()


while True:
    question = input("\nAsk 8ish something (or type quit/history): ")

    if question.lower() == "quit":
        print("...ish out.")
        break

    if question.lower() == "history":
        show_history()
        continue

    answer = get_answer(question)

    history.append({
        "question": question,
        "answer": answer
    })

    print(answer)
    