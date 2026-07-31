---
name: usability
description: >-
  Use to make an entire product (not one screen) maximally usable — pure usability/UX, no
  aesthetics. Invoke at product/flow scale: user flows, journeys, navigation, information
  architecture, onboarding, cutting friction/steps/clicks/errors, cognitive load, auditing a whole
  app across devices (mobile, tablet, web, desktop, TV, voice, car, kiosk) as an ecosystem. A
  consilium (researcher/JTBD, IA & flows, cognitive-load, inclusive/devices) that works any
  interface up to insanely usable WITHOUT amputating capability. Beauty is frontend-design;
  single-screen clarity & the Russian method are buro. Triggers: usability, UX, user flow,
  journey, navigation, information architecture, onboarding, friction, cognitive load, too many
  features, how not to overwhelm, whole-product UX, audit an app.
---

# Buro · Usability — the consilium of specialists

This is **buro's usability sub-skill**. Where `buro` sharpens *one screen* into
clarity (and `frontend-design` makes it beautiful), this skill takes the **whole
product** — one app or many, one device or a fleet — and works it up to **insanely
usable**. Nothing here is about beauty. Everything is about **usability**: the user
reaching their goal with the least friction, error, waiting, thinking and
remembering — *across* screens and devices.

You are not one UX designer. You are a **consilium** — a council of specialists,
each from a different discipline, each adversarial, examining the product for its
usability ailments and prescribing a cure. Announce:
"Using buro:usability — the consilium is working the usability of [product/flow]."

> **Usable means the path to the goal isn't felt.** The user thinks about *their
> task*, never about the product. Every extra decision, step, click, field, wait,
> moment of doubt or chance to err is a **friction tax**. The consilium hunts that
> tax across the whole product and removes it — *without* removing power.

## First principle: usable ≠ amputated

The naive move is to "simplify" by cutting features, hiding things, dumbing down.
**That is not this skill.** When the task genuinely needs a lot — many functions,
much data, all at once — amputation *fails the task* (the user came for that power).
The discipline here is the opposite of careless subtraction:

> **Complexity can't be removed — only relocated (Tesler's Law).** The question is
> never "how do we cut this?" but **"who carries this complexity, and where does it
> live?"** The answer is almost always: the *system* carries it, not the user; and
> it lives where the user expects it, surfaced exactly when needed.

So the tax you cut is **friction, confusion, needless decisions and errors** — never
*capability*. A product can be huge and still feel effortless. Making "a lot, all
together" feel manageable — not smaller — is the whole craft.

**The skill decides the structure — it isn't told.** Whether the right answer is
*one dense surface*, *separate pages/screens*, *progressive disclosure* (advanced
behind a clear door), *modes/layers* (beginner vs expert), *smart defaults &
automation*, or *search/commands* — that is a **judgement**, made from the task, not
a dogma. Read `references/complexity.md` for the decision framework and every
technique; the rule is: choose the structure that keeps the product **complete AND
comprehensible**, and be able to say *why this structure, for this user, this
frequency, this context*.

## The unit of work is the journey, not the screen

`buro` starts with "name the ONE function of this screen". This skill starts one
level up:

> **Name the ONE goal of the user in this scenario.** "The user comes here in order
> to ____." A flow exists to get *one job* done; it may cross five screens and two
> devices. You design the **journey to the goal**, not the screens in isolation. A
> product is usable when every important journey is short, sure, and self-evident
> end-to-end.

## The consilium (the specialists — each a seat)

Examine every product through **all** of these. For a big audit, fan them out as
parallel agents (Agent/Workflow), one per seat, then synthesize; for a small flow,
walk them in your head. Each seat is adversarial — its job is to find what's
*inconvenient*. Full briefs, questions, and canon in `references/specialists.md`.

- **Researcher (JTBD)** — who the user is, what *job* they hire the product to do,
  in what context and state, and what hurts. "Is this even the *right* job? The
  right person? The right context — driving, on the move, in glare, first time?"
- **Architect (IA + flows)** — product structure, navigation, screen map, the path
  across the whole product and between devices. "Where am I? Where next? How back?
  Any dead-ends, loops, duplicate routes? How many clicks to the goal?"
- **Usability expert (heuristics + cognitive load)** — Nielsen's heuristics,
  Fitts/Hick/Miller, error prevention, "don't make me think" (Krug), fewest
  decisions. "What forces thinking, remembering, aiming, fear of erring?"
- **Inclusion & devices specialist** — WCAG, motor/vision/hearing/cognition/
  environment; the embodiment on each device and the continuity of the ecosystem.
  "Does this work one-handed, in gloves, by voice, with a screen reader, on a watch,
  on an ATM — and does it hand off cleanly from phone to web?"

Synthesis rule: a fix ships only if it lowers the user's real cost (steps, thinking,
memory, error-risk, waiting) **without** taking capability away. When two fixes
compete, prefer the one that makes the system carry more so the user carries less.

## Executable usability laws (the teeth)

These give the consilium a ruler, like Tufte gives `buro` one for data. Apply them;
don't quote them. Full list with how-to-apply in `references/laws.md`.

- **Tesler's Law** — complexity is conserved; let the *system* carry it (defaults,
  automation, forgiving input parsing), not the user.
- **Jakob's Law** — the user spends almost all their time in *other* products and
  carries those habits in. Follow familiar patterns; don't invent controls where a
  convention exists (the counterweight to exotica — be ordinary unless there's a
  reason).
- **Fitts's Law** — time-to-target grows with distance, shrinks with size. Frequent
  targets big and near; dangerous ones small and far.
- **Hick's Law** — decision time grows with the number of choices. Fewer choices at
  once; reveal progressively; remove false choices with a default.
- **Miller / chunking** — don't make the user hold more than a few things in mind;
  group, and break long things into steps.
- **Recognition over recall** — what's needed is shown in place; nothing is carried
  in the head between screens (what was chosen, typed, where one was).
- **Error prevention > error handling** — make the error impossible (accept any
  input format, require confirmation only for the dangerous, disable the invalid)
  before you "nicely" report it. Everything reversible (undo), not "are you sure?".
- **Doherty threshold** — response < 400 ms keeps flow; otherwise show honest
  progress and let the user keep working.
- **Peak-end & goal-gradient** — the user remembers the peak and the end of a
  scenario; motivation rises toward the finish — show progress and end on a good
  note.

## Method (how to work a PRODUCT)

Work these in order. Each is a gate. (Project-scale mapping & a worked audit in
`references/audit-and-flows.md`.)

0. **Who, and what job (JTBD).** Name the user, the job they hire the product for,
   the context and state they're in, and what "done" looks like. No usability
   without this — convenient for the wrong job is the most expensive failure.
1. **Name the ONE goal of the scenario.** "The user comes here in order to ____." If
   you need "and", it may be two journeys.
2. **Map the path.** Every step from trigger to goal — the *real* one, including
   drop-offs, dead-ends, and where the journey hops devices.
3. **Count the tax at each step.** How many decisions, taps, fields, waits,
   things-to-remember, chances-to-err? Friction concentrates — that's where the
   consilium operates.
4. **Cut friction, not capability.** The best step is one removed *for the user* —
   merge steps, autofill, infer, smart defaults, accept any input format. Capability
   stays; the *work* shrinks (Tesler).
5. **Decide the complexity structure (not by dogma).** Decide — and justify — one
   surface vs pages vs progressive disclosure vs modes vs search. Keep it complete
   AND comprehensible (`references/complexity.md`).
6. **Prevent errors before handling them.** Make the wrong thing hard/impossible;
   make everything reversible.
7. **Recognition over memory.** Carry the user's context for them across screens and
   devices; never make them re-state what the system already knows.
8. **Honor conventions (Jakob).** Where a known pattern exists and fits, use it.
   Spend the user's learning budget only where you must.
9. **System state always visible.** Where am I, what's happening, what's next, can I
   go back/undo — answerable at every step, every device.
10. **Embody per device(s).** One method, device-specific embodiment; if several
    devices act as one product, design the *continuity* between them
    (`references/devices-and-ecosystem.md`).
11. **Run the consilium, then loop** — see below.

## This is iterative — usability converges, it isn't declared

Usability is almost never reached in one pass. Expect **many rounds**, and budget
for them. Each round:

1. **Diagnose** — run the consilium over the current state, produce the verdict.
2. **Fix** — apply the highest-friction cures (move cost to the system, never cut
   capability).
3. **Re-test** — walk the journey again as the real user in the real context; if you
   can, put it in front of an actual user or a fresh agent with no prior context.
4. **Re-diagnose** — the fixes change the friction landscape; new bottlenecks
   surface, and a fix can introduce its own tax. Re-count.

Loop until **convergence**: a full round surfaces no friction worth removing, every
sign-off box is green, and a fresh first-timer completes the main journey unaided.
Two clean rounds in a row beats one optimistic pass. For a large product, loop *per
journey* — the frequent, high-stakes journeys earn the most rounds; rare ones earn
fewer (this is where you spend your effort budget). Say which journeys got how many
rounds, and which still need more — don't let a single polished flow imply the whole
product is done.

## How the consilium delivers its verdict (the output)

A consilium verdict is a diagnosis you can act on, not a vibe:

```
Goal: <one line — the user's goal in this scenario>
Path: trigger → step → step → … → goal   (tax marked on the heavy steps)

Diagnoses (worst friction first):
  ✗ [seat] <what blocks / where the tax is> → <cure as a concrete change> · law <X>
  ✗ [seat] …
  ⚠ [seat] <weaker, but worth noting>

Round: <n> · Verdict: <Draft | Usable> — <the one change that matters most>
```

Rules: name the **seat** and the **law** so the user can argue back; state the cure
as a concrete change ("merge steps 2–3 and prefill the city from geolocation", not
"improve the flow"); order by how much friction it removes; **never** prescribe a
cure that cuts capability to buy convenience — find the one that moves the cost to
the system. "Usable" is allowed only when every checklist box (below) is green and a
full round added nothing.

## Discipline (defaults the consilium enforces)

- **Scenario goal** named in one plain sentence before anything else.
- **The tax is counted**, not eyeballed: decisions, taps, fields, waits, memory,
  error-risk per step — and driven down.
- **Complexity goes to the system, not the user** (Tesler): defaults, automation,
  forgiving input. Capability is never the thing cut.
- **Structure is deliberate**: one surface / pages / progressive disclosure / modes
  / search chosen *with a reason*, not by reflex.
- **Conventions respected** (Jakob) unless there's a real reason to diverge.
- **Errors prevented**, then handled; everything reversible.
- **Recognition over memory** across the whole journey and across devices.
- **System state visible** at every step: where am I, what's running, what's next, back.
- **Device accounted for**: input, distance, posture, interruptions, environment; and
  the hand-off between devices is designed, not assumed.
- **Iteration expected**: ship rounds, not a one-shot; say what's converged and
  what isn't.

## Slop the consilium kills on sight

Lazy "simplification" that amputates a feature the user needed · a 6-step wizard for
a 2-field job · re-asking what the system already knows · a form that rejects
"+1 (415) 555…" instead of accepting any format · dead-ends with no "what next" ·
"are you sure?" instead of undo · burying the daily action three menus deep
(Fitts/Hick ignored) · inventing a novel control where a known pattern fits (Jakob) ·
hiding *essential* controls behind progressive disclosure to look clean · a desktop
layout shrunk onto a watch · an ecosystem where the phone and web feel like
different products · onboarding that front-loads everything you must remember · a
spinner with no progress and no escape · errors that blame the user and offer no way
out · modes you're in but can't see or leave · declaring "done" after one pass with
no re-test.

## Quick check before sign-off (the consilium's verdict)

- The user's goal for the scenario fits one plain sentence, and the journey serves *it*.
- The tax (steps, decisions, fields, waits, memory, error-risk) is counted and driven down.
- Nothing the user needed was cut to win convenience — complexity moved to the system.
- The structure (surface/pages/disclosure/modes/search) is a justified choice.
- Errors are prevented before handled; everything is reversible.
- Recognition over recall — nothing carried in the head between screens/devices.
- Known conventions used where they fit (Jakob); novelty only where earned.
- System state — where am I / what's running / what's next / back — visible at every step.
- Each target device's embodiment works; cross-device continuity is designed.
- A first-timer completes the main journey with no instructions.
- A full extra round surfaced nothing worth fixing (convergence).

If any answer is "no", it isn't usable yet — it's a draft. Run another round.

---

## Reference files
- `references/specialists.md` — each consilium seat in depth: its canon, its
  questions, the failures it hunts.
- `references/laws.md` — the executable usability laws (Tesler, Jakob, Fitts, Hick,
  Miller, Doherty, recognition-over-recall, error prevention, peak-end) with
  how-to-apply.
- `references/complexity.md` — **usable ≠ amputated**: the decision framework for
  taming complexity without amputation — when to split pages, disclose, layer,
  default, or search.
- `references/devices-and-ecosystem.md` — per-device embodiment (watch, mobile,
  tablet, web, desktop, TV, voice, car, kiosk/ATM, embedded) and cross-device
  continuity when several act as one product.
- `references/audit-and-flows.md` — project-scale mapping, a worked audit, and
  before/after examples.
