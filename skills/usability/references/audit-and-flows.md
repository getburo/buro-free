# Project-scale mapping, the audit, and before/after

This file is the *how* of working a whole product rather than one screen: how to map
it, how to run an audit across many journeys, and what good cures look like. Use it
with the method and the consilium in `SKILL.md`.

---

## Mapping a product (existing or not-yet)

Before the consilium can diagnose, you need the terrain. Build, at minimum:

1. **Users & jobs (JTBD).** The handful of real users and the jobs each hires the
   product for. One line per job.
2. **Journey inventory.** The list of journeys that matter — "sign up", "log a
   workout", "pay a bill", "recover a password", "share with a teammate". Mark each
   by **frequency** and **stakes**. This ranking decides where rounds get spent.
3. **Screen / space map.** Every screen (or, for a not-yet product, every screen you'd
   need) and the links between them — the navigation graph. Note dead-ends, loops,
   and duplicate routes.
4. **Device matrix.** Which devices each journey touches, and where it hands off
   (`devices-and-ecosystem.md`).
5. **The friction ledger.** For the top journeys, the step-by-step path with the tax
   counted per step (decisions, taps, fields, waits, memory, error-risk).

For a product that doesn't exist yet, you *design* these artifacts instead of
auditing them — same structure, forward instead of backward.

---

## Counting the tax (make friction measurable)

For each step in a journey, tally:
- **Decisions** — choices the user must make (could any be a default?).
- **Taps/clicks/keystrokes** — physical actions (could any be merged or removed?).
- **Fields** — data entered (could any be prefilled, derived, or sensed?).
- **Waits** — anything over ~400 ms (Doherty) — is progress honest, can they keep
  working?
- **Memory** — anything carried from a previous screen (recognition-over-recall
  violations).
- **Error-risk** — ways to get it wrong here (could the error be designed out?).

Sum per step, then per journey. **Friction concentrates** — usually a couple of steps
hold most of the tax. Those are where the consilium operates first (peak-end: fix the
worst moment before the average).

---

## Running the audit (a worked shape)

For a real audit of a multi-journey product:

1. **Pick the journeys** worth the most rounds (frequent × high-stakes first).
2. **Per journey, fan out the consilium** — one agent per seat
   (`specialists.md`) over that journey's map and tax ledger; or walk the seats in
   your head for a small one.
3. **Synthesize** into the verdict shape (`SKILL.md`): diagnoses worst-first, each
   naming seat + law + concrete cure; the one change that matters most; round number;
   Draft | Usable.
4. **Apply the top cures**, moving cost to the system, never cutting capability.
5. **Re-test** — walk it again as the user in the real context; ideally a fresh
   first-timer (a person, or an agent with no prior context) tries the journey.
6. **Re-diagnose** — the friction landscape shifted; new bottlenecks appear, and a
   cure may have added its own tax. Re-count and loop.
7. **Stop at convergence** — a full round adds nothing, sign-off is green, a
   first-timer succeeds unaided. Report which journeys converged and which still owe
   rounds.

Be honest about coverage: a polished sign-up does not mean the product is usable if
"cancel subscription" is still a maze. Say what was and wasn't worked.

---

## Before / after

**1. Signup — the tax nobody counted (Tesler, Hick, recognition)**
> **Before:** 11 fields including "city", "state", "timezone"; a "how did you hear
> about us?" required dropdown; password rules revealed only on error; email retyped
> for confirmation. Tax: 11 fields, 3 needless decisions, 1 designed-in error.
> **After:** email + password only; city/state/timezone derived from IP (override
> available); "how did you hear" optional and async; password rules shown up front
> with live validation; no confirm-email field (use undo/verify link instead). Tax:
> 2 fields, 0 needless decisions. Nothing the business needed was lost — it moved off
> the user (Tesler).

**2. The buried daily action (Fitts, Hick)**
> **Before:** the action a driver does every shift — "start trip" — is three taps
> deep under a menu; a rarely-used "vehicle settings" sits on the home screen.
> **After:** "Start trip" is a single large button in the thumb zone on launch;
> settings move to a labelled, one-tap-away section. Frequency now drives placement.

**3. "Are you sure?" instead of forgiveness (error prevention, Apple forgiveness)**
> **Before:** deleting an item pops "Are you sure you want to delete? This cannot be
> undone." Users still delete the wrong thing — and now everyone is interrupted.
> **After:** delete happens immediately with a 6-second "Deleted · Undo" toast;
> nothing is interrupted, mistakes are reversible. The dialog is gone; safety went up.

**4. Ecosystem seam (continuity, Birman)**
> **Before:** a user fills a cart on mobile; on the web later it's empty, and "remove"
> on mobile is "delete" on web. Two products wearing one logo.
> **After:** the cart syncs and resumes at the same point; the action is named and
> placed identically on both; switching devices feels like the same product. State
> follows the user (Tesler); the language is one (Birman).

**5. Complexity tamed, not cut (usable ≠ amputated)**
> **Before, attempt A (amputation):** a pro audio tool hides EQ, routing, and
> automation to "look simple" → pros abandon it.
> **Before, attempt B (overwhelm):** everything on one wall of identical knobs → new
> users freeze.
> **After:** stable, grouped channel strips (chunking) with smart per-track defaults
> (Tesler); an "Auto" that does 90% then lets you refine; advanced routing behind a
> clearly-labelled expander (progressive disclosure); a command palette to jump to any
> function. Full power, comprehensible — the band between amputation and overwhelm.

---

## When to bring in the siblings

This skill owns usability. Hand off deliberately:
- **`buro`** — once a *single screen* in the flow needs its layout, hierarchy,
  control grammar, spacing, microcopy, or dense-data treatment sharpened.
- **`frontend-design`** — for beauty: type, palette, atmosphere, motion. Not this
  skill's job, by design.
A usable product that's ugly is this skill succeeding and `frontend-design` not yet
run; a beautiful product that's confusing is the reverse. Run all three.
