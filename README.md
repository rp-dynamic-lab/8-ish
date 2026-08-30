# 8-ish 🎱

**For when the answer is… ish.**

8-ish started with a Magic 8-Ball.

Not because I particularly needed a digital Magic 8-Ball, but because it is almost a perfect object for examining judgment.

You ask it a question full of context, history, consequence, contradiction, and uncertainty.

It ignores all of that.

Then it confidently gives you a random answer.

That felt like a useful place to start.

**Live prototype:** https://eight-ish.onrender.com/


## Why build this?

I spend a lot of time thinking about what happens when context moves.

A new piece of information arrives. Something that looked obvious stops looking obvious. The thing we thought we knew changes because the frame around it changed.

The Magic 8-Ball gives me an intentionally terrible baseline for playing with that problem.

At V0, 8-ish does what the original object does:

**question → random certainty**

The interesting part begins when the system is allowed to notice that its answer may not be warranted.

What would it need to know before answering?

Can it recognize that it understands the topic but still does not understand the situation?

If another piece of context arrives, should that change the answer?

Should it ask for more information at all?

At what point is there enough?

And eventually: **how much judgment can we actually package into the space between a question and an answer?**


## What 8-ish does now

The current version is intentionally primitive.

8-ish can:

- take a question
- make a crude distinction between topic words and decision-related context
- notice when it does not have enough information and respond with `too ish.`
- hold the previous turn in session memory
- bring that earlier context forward when the user adds another piece of information
- return a short Magic-8-Ball-style response once its very simple context threshold has been met

The judgment is still deliberately bad.

For example, the system currently uses hand-built language rules to decide whether a question contains enough context. Those rules fail. Misspellings can look meaningful. A connective word like `because` can carry too much weight. Stored context may not actually belong to the next turn.

Those failures are part of the project.


## Why keep the randomness?

I don't want to remove the Magic 8-Ball too quickly.

The random answer gives 8-ish something to interrogate.

Instead of beginning with:

> What is the correct answer?

I can begin with:

> I produced an answer. Can I justify it?

That creates a useful progression:

```text
random response
      ↓
is there enough context?
      ↓
no → too ish.
      ↓
more context arrives
      ↓
reconsider
