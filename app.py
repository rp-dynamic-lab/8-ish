import os
import random

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "8ish-dev-key")


answers = [
    "DO IT.",
    "NOPE.",
    "PROBABLY.",
    "NOT TODAY.",
    "EH. MAYBE.",
    "WHY NOT?",
    "I'D WAIT.",
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


def build_context(question, history):
    if len(history) == 0:
        return question

    last_item = history[-1]

    if last_item["answer"] == "TOO ISH.":
        return last_item["context"] + " " + question

    return question


def get_answer(question):
    topic_words = get_topic_words(question)
    decision_signals = get_decision_signals(question)

    if len(topic_words) < 2:
        return "TOO ISH."

    if len(decision_signals) == 0:
        return "TOO ISH."

    return random.choice(answers)


@app.route("/", methods=["GET", "POST"])
def home():
    history = session.get("history", [])

    answer = None

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if question:
            context = build_context(question, history)
            answer = get_answer(context)

            history.append({
                "question": question,
                "context": context,
                "answer": answer
            })

            session["history"] = history

    return render_template(
        "index.html",
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)