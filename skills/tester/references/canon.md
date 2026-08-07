# Testing · canon — the sources behind the lenses

Compressed reference for the `buro:tester` seat. Tools, not rules.

## Equivalence partitioning & boundary-value analysis

- **Equivalence partitioning:** group inputs into classes that should behave the same (e.g.
  "valid age 18–65", "too young 0–17", "too old 66+"), and test one representative per class
  rather than every value.
- **Boundary-value analysis:** bugs cluster at the *edges* of those classes. Test the boundary
  and just inside/outside it: for 1–100, test 0, 1, 2, 99, 100, 101. Most off-by-one and
  validation bugs live exactly here.

## The unhappy-path taxonomy

For any feature, enumerate beyond the happy path:
- **Empty / absent:** no input, no results, no permission, no network.
- **Wrong:** wrong type, wrong format, wrong order, wrong user.
- **Too much / too little:** max, over-max, zero, one, huge, one character.
- **Interrupted:** cancel, back, refresh, close mid-flow, timeout, kill.
- **Repeated:** double-submit, retry, replay.
- **Hostile:** injection, script tags, path traversal, unicode/emoji, adversarial payloads.

## State and interruption

Most "worked in the demo" failures are **state** failures: the flow interrupted (back button,
refresh, app backgrounded), done out of order (step 3 before step 2), or resumed from a stale
state. Test flows by breaking them in the middle and checking the resulting state is valid and
recoverable — no orphaned records, no stuck screens, no lost data.

## Concurrency and races

Two things at once: two tabs editing one record, a click during a load, a callback arriving
after the screen changed, two users on shared state. Races are **rare per run, common in
aggregate** — low reproduction rate, high severity. Note the repro rate honestly (e.g. "3/10").

## The error path is a feature

When something fails, *how* it fails is a design surface: a clear message, no data loss, a
recovery route — vs a blank screen, a raw stack trace, a corrupted save. An unhandled error is
usually the bug *behind* the bug the user reported. Test that failures fail well.

## Severity × likelihood

Rank every bug on two axes:
- **Severity:** data loss > crash/blocker > wrong result > degraded > cosmetic.
- **Likelihood:** common path > occasional > rare edge.

A data-loss on checkout (severe × common) dwarfs a cosmetic glitch in a rarely-visited settings
pane (cosmetic × rare). Fix order follows the product, not the order bugs were found.

## How to write a reproduction

From a **clean, known state**, the **minimal** steps, the exact **input**, the **expected** vs
the **actual** result, the **environment** (OS/version/build), and the **reproduction rate**. A
bug without a reliable repro gets closed "cannot reproduce" — the repro *is* the bug report.

## The honest boundary with code testing

This seat is **black-box and experiential**: it plays the artifact adversarially and files
reproducible bugs. It *designs* what to test. The **executable** automated tests (unit,
integration), the test-first TDD loop, and a code regression's root cause are `buro:dev`. This
seat names the failure and its repro; `buro:dev` builds the automated guard and finds the line
of code.

## Shipping Known-Broken to Hit a Date (Cautionary — Synthesis, Not Citation)

⚠️ Unlike the sections above, this one isn't drawn from a testing methodology — it's this seat's
own reading of a well-documented launch failure, flagged as **cautionary — synthesis, not
citation** rather than dressed as an authority it doesn't have. The named product is the evidence;
the principle is the failure to *avoid*, never to emulate.

*Cyberpunk 2077* (2020) shipped with known, severe defects on last-gen consoles in order to hit a
date. The principle: **when known SEV-1/SEV-2 bugs are WAIVED to hit a date, that is a business
DECISION the QA seat must SURFACE loudly, with its evidence — never silently swallow.** The honest,
reproduced, severity-ranked bug list is the QA seat's power *precisely* at the moment of schedule
pressure, when everyone else wants the green check. A waived critical is not a closed ticket — it's
a **documented risk**: owned by a named person, dated, and decided in the open, so the call is made
knowingly rather than discovered by users at launch. The seat's job is not to grant or refuse the
waiver; it is to make sure no critical is waived *quietly*.
