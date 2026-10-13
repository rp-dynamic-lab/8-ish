# 8-ish work log

## October 13, 2026

A note on the quiet stretch in the commit history.

Since the last push in early September, most of my work around 8-ish has happened before the code.

I have been trying to get clearer about what the project is actually for, what belongs inside it, and what I want the next technical work to teach me.

8-ish started as a deliberately bad decision engine: ask a question, get an answer. That gave me something simple enough to build while I learned Python, Git, Flask, deployment, sessions, and APIs.

Since then, the questions underneath it have gotten more interesting.

I have been working on how the app should handle context without pretending that more information automatically produces a better answer. Some of those questions have also split into related experiments rather than being forced back into 8-ish.

I have also been keeping the live version intentionally small. I do not want to keep adding heuristics just to make it seem smarter.

The next phase is observability.

I am going to instrument 8-ish with PostHog and use the project to learn what happens between an action in the browser and the data that appears on the other side.

That means working with events, session replay, feature flags, identity, browser developer tools, network requests, and an API.

I also want to break parts of the instrumentation on purpose and work out why they stopped working.

The app is still the experiment.

The experiment is just moving into a different part of the system.
