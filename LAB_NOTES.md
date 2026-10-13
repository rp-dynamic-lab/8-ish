# 8-ish lab notes

## October 13, 2026 — PostHog, first pass

Started instrumenting 8-ish with PostHog.

### What worked

PostHog is now installed in the browser version of 8-ish on the `posthog-lab` branch.

I verified the connection in Chrome DevTools rather than assuming the installation worked. Loading 8-ish produced requests to PostHog, including the event endpoint at:

`https://us.i.posthog.com/e/`

The requests returned `200 OK`.

I also used the browser console to send a custom `instrumentation_test` event and confirmed that it appeared in PostHog.

### What I traced

I added a `question submitted` event to the form.

The form listener existed and Chrome showed one submit listener attached to it.

A synthetic submit from the browser console successfully produced the `question submitted` event in PostHog.

A normal form submission did not reliably show the custom event.

That narrowed the problem. The event itself works. The listener works. The next thing to investigate is what happens when the real form submission causes the page to navigate.

### Where to start next time

Start from the clean `posthog-lab` branch.

The PostHog installation is committed and working.

Next:

1. Re-add `question submitted` without sending the question text.
2. Work out how to make the event survive the normal Flask form submission.
3. Verify it in Chrome Network and PostHog Activity.
4. Commit that event separately once it works.
5. Then move on to session replay and privacy.
