8-ish 🎱

For when the answer is… ish.

8-ish started with a Magic 8-Ball.

Not because I particularly needed a digital Magic 8-Ball, but because it is almost a perfect object for examining judgment.

You ask it a question full of context, history, consequence, contradiction, and uncertainty.

It ignores all of that.

Then it confidently gives you a random answer.

That felt like a useful place to start.

Live prototype: https://eight-ish.onrender.com/

**Why build this?**

I spend a lot of time thinking about what happens when context moves.

A new piece of information arrives. Something that looked obvious stops looking obvious. The thing we thought we knew changes because the frame around it changed.

The Magic 8-Ball gives me an intentionally terrible baseline for playing with that problem.

At V0, 8-ish does what the original object does:

question → random certainty

The interesting part begins when the system is allowed to notice that its answer may not be warranted.

What would it need to know before answering?

Can it recognize that it understands the topic but still does not understand the situation?

If another piece of context arrives, should that change the answer?

Should it ask for more information at all?

At what point is there enough?

And eventually: how much judgment can we actually package into the space between a question and an answer?

**What 8-ish does now**

The current version is intentionally primitive.

8-ish can:

take a question
make a crude distinction between topic words and decision-related context
notice when it does not have enough information and respond with too ish.
hold the previous turn in session memory
bring that earlier context forward when the user adds another piece of information
return a short Magic-8-Ball-style response once its very simple context threshold has been met

The judgment is still deliberately bad.

For example, the system currently uses hand-built language rules to decide whether a question contains enough context. Those rules fail. Misspellings can look meaningful. A connective word like because can carry too much weight. Stored context may not actually belong to the next turn.

Those failures are part of the project.

**Why keep the randomness?**

I don't want to remove the Magic 8-Ball too quickly.

The random answer gives 8-ish something to interrogate.

Instead of beginning with:

What is the correct answer?

I can begin with:

I produced an answer. Can I justify it?

That creates a useful progression:

random response
↓
is there enough context?
↓
no → too ish.
↓
more context arrives
↓
reconsider

The randomness matters because it gives me a clean, stupid baseline.

There is no hidden intelligence to confuse with judgment. If the system gets better, I can ask what actually changed between the random answer and whatever comes next.

Did more context change the answer?

Did it only make the system sound more informed?

Was the additional information even relevant?

Should it have asked for any of it in the first place?

That is the part I want to keep pulling apart.

The little blue triangle can stay the same while the judgment underneath it changes.

**Where it goes next**

Right now, 8-ish can preserve context without really knowing whether it has preserved the right context.

If it says too ish., it assumes the next thing the user tells it belongs to the same question.

That is enough to make the current interaction work. It is obviously not enough to call judgment.

The next versions need to start dealing with the harder problem: what should actually happen when context changes?

I want 8-ish to get better at recognizing whether new information belongs to the thing already under consideration. I want to test whether that information materially changes the answer rather than simply adding more words.

Eventually, tell me one more thing should not be the default solution. Sometimes there may be one genuinely useful question to ask. Sometimes more context will not resolve anything. Sometimes the useful move may be to test something small instead of continuing to reason.

And sometimes the ambiguity may simply need to stay ambiguous.

Further out, I want someone to be able to return and tell 8-ish what happened.

Then the object gets more interesting:

situation → interpretation → move → consequence → reinterpretation

At that point, the question is no longer just whether 8-ish can give a better answer.

It is whether it can become better at navigating what happens when the answer was necessarily provisional in the first place.

I don't know yet how much of that judgment can be packaged.

That's the experiment.

**Why this repo looks the way it does**

This is also an apprenticeship project.

I am learning the technical medium by keeping one small object alive long enough to understand what changes underneath it.

8-ish began as a few lines of Python choosing randomly from a list.

Then I made it repeat.

I moved the answer behavior into a function.

I passed the question into that function even though the program did not know what to do with it yet.

I started making context visible. I separated a crude sense of topic from a crude sense of decision context. I added working memory. Then I let the next turn actually use something from that memory.

After that, I moved the same experiment from the terminal into Flask, built the browser interface, gave the object its liquid blue answer window, and deployed it.

The commit history is intentionally part of the artifact.

I don't want the trail to look as though I already knew the finished architecture and simply typed it out.

I want it to show what I noticed, what broke, and what the next version made possible.

**Next experiment**

The next useful step is not adding a pile of smarter rules by myself.

It is giving 8-ish to a small group of real users.

I want to see what people actually do with too ish. Do they naturally add useful context? Do they understand what the system is asking for? When does carrying earlier context forward work? When does it become obviously wrong?

Once there is real behavior to observe, I plan to instrument the interaction with PostHog.

I am much more interested in behavioral events than collecting the actual content of people's questions.

Things I may want to observe include:

question_submitted
too_ish
context_added
answer_shown
context_carried_forward
session_returned

Then I can use actual interaction to decide what deserves to change next instead of making the system more complicated because I can.

**Current stack**
Python
Flask
Jinja
HTML / CSS
Gunicorn
Render
Git / GitHub

The interface is based on the answer side of a Magic 8-Ball: a black orb, recessed window, and a liquid blue triangle carrying a very small answer.

**Run it locally**

Clone the repo and install the dependencies:

pip install -r requirements.txt

Run the Flask development server:

python3 app.py

Then open:

http://127.0.0.1:5000

For a production-style local run:

gunicorn app:app

**Status**

Very much …ish.

That's the point.

I like this version much more for what you’re trying to show. The important addition is that it now makes clear that user testing + PostHog is the immediate next experiment, while the actual project trajectory is about progressively packing better judgment into the object. It doesn’t make PostHog sound bolted on for the application. It explains why you would use it.
