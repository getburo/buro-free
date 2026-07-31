# The consilium — specialists in depth (the seats)

Read this when you want each seat to bite hard. The consilium is adversarial: every
specialist's job is to find what's *inconvenient* and prescribe a concrete cure —
never to praise. For a big audit, run each as a parallel agent and synthesize; for a
small flow, walk them in your head. None of them touches aesthetics — that's
`frontend-design`. They care only about **usability**: the user reaching the goal
with the least friction, error, waiting, thinking, and remembering.

A diagnosis from any seat must name **what's wrong**, **where** (which step/screen/
device), **the cure as a concrete change**, and **the law** behind it.

---

## 1. Researcher (JTBD & context)

**Who to study:** Clayton Christensen & Alan Klement (Jobs-to-be-Done), Indi Young
(mental models, listening), Steve Portigal (interviewing), Erika Hall (just-enough
research). **Owns gate 0.**

**What it establishes:**
- **Who** — the real user, not a flattering persona. Their expertise, their stakes.
- **What job they hire the product to do** — phrased as a *job*, in the user's
  words: "when __, I want to __, so that __". Not "uses the dashboard" but "when I
  start my shift, I want to see in 10 seconds what's on fire, so I don't miss a
  failure."
- **In what context and state** — driving, on the move, in the cold with gloves, in
  bright glare, for the very first time, under stress, with a child on one arm.
  Context decides more than features do.
- **What "done" means** — the observable outcome that means the job is complete.

**Failures it hunts:**
- A beautifully convenient flow for **the wrong job** or the wrong person.
- Designing for the demo context (calm, two hands, big screen) when the real context
  is hostile (interrupted, one hand, glare, panic).
- Optimizing a step the user doesn't actually care about while the real pain is
  elsewhere in the journey.
- Assuming the goal instead of naming it — "they want to manage settings" is almost
  never a real job.

**Cures it prescribes:** rewrite the job in the user's words; move effort to the
moment/context the user is actually in; kill a "feature" that serves no job; re-aim
the whole journey at the real outcome.

---

## 2. Architect (information architecture & flows)

**Who to study:** Rosenfeld & Morville (information architecture), Donna Spencer
(card sorting), Jakob Nielsen (Jakob's Law), Abby Covert (making sense of any mess),
**Ilya Birman ("the interface is a language" — one consistent vocabulary and grammar
across the *whole* product, not just one screen)**. **Operates at product scale** —
the seat that most distinguishes this skill from `buro`.

**What it builds & checks:**
- **Product map** — every screen/space and how they connect. Is the structure a clean
  tree, a sensible graph, or a tangle?
- **Navigation model** — how the user moves: tabs, hierarchy, hub-and-spoke,
  search-first. Does it match the product's shape and the user's mental model?
- **User flow** — the real sequence from trigger to goal, including the unhappy
  branches and the device hops.
- **One language across the product (Birman)** — the same thing is named the same
  way, looks the same, sits in the same place, on every screen and every device. The
  user learns the grammar once and reads the rest.
- **Depth & breadth** — how many taps to the daily action? How many siblings at each
  level (Hick)?

**Failures it hunts:**
- **Dead-ends** — screens with no obvious "what next".
- **Loops & duplicate routes** — two routes to the same place that feel different, or
  a loop the user can't tell they're in.
- **Lostness** — no answer to "where am I / where next / how back".
- **Dialect drift (Birman)** — the same action called "Delete" here and "Remove"
  there; a control that means one thing on mobile and another on web; inconsistent
  place/label/behaviour that forces re-learning.
- The **daily** action buried deep while a rare one sits up front.
- Navigation invented from scratch where a known pattern (Jakob) would orient the
  user instantly.
- Structure organized by the *company's* org chart, not the user's task.

**Cures it prescribes:** flatten the path to the frequent goal; add a clear "you are
here" and "next"; collapse duplicate routes; unify the product's vocabulary so one
meaning has one word/control/place everywhere (Birman); adopt the conventional nav
pattern; make the journey end-to-end legible — including across devices.

---

## 3. Usability expert (heuristics & cognitive load)

**Who to study:** Jakob Nielsen (10 heuristics), Steve Krug ("Don't Make Me Think"),
Don Norman (affordances, signifiers, mapping, the gulfs of execution & evaluation),
Paul Fitts, William Hick, George Miller, Larry Tesler, **Ilya Birman (interface as a
language: an unambiguous, consistent control vocabulary; his interface laws — "a good
interface is obvious, visual, and unambiguous")**, and **Apple's design principles**
(see box below). The ruler-bearer.

**Apple's design principles (HIG) — the usability core, beauty aside:**
- **Clarity** — text legible at every size, icons precise, function obvious; content
  is the focus, chrome recedes.
- **Deference** — the UI defers to the content and the task; it doesn't compete for
  attention.
- **Depth** — clear visual layers and motion convey hierarchy and *where things come
  from* (a usability cue, not decoration).
- And the classic Macintosh HIG principles that are pure usability: **direct
  manipulation** (act on the thing itself), **see-and-point** (recognition over
  recall), **consistency**, **feedback** (every action has a visible result),
  **user control** (the user initiates and can stop/undo), **forgiveness**
  (reversible actions, safe to explore), **perceived stability** (familiar, steady
  structure), **WYSIWYG / no hidden state**.

**What it scrutinizes — every step:**
- **How many decisions** the user must make, and whether each is real or could be a
  smart default (Hick, Tesler).
- **How much aiming/reaching** — target size and distance for the frequent action
  (Fitts).
- **How much to remember** — anything carried in the head between screens (Miller,
  recognition over recall, Apple see-and-point).
- **Where one can err**, and whether the error is *prevented* or merely reported
  (Apple forgiveness — reversible, safe to explore).
- **Is system state visible** — Nielsen #1 / Apple feedback & no-hidden-state: where
  am I, what's running, what came out.
- **Is the control vocabulary unambiguous (Birman) and consistent (Apple)** — does
  each control clearly say what it does, and does the same control always do the same
  thing?
- **Response speed** — is the user kept in flow (Doherty, < 400 ms) or left staring?

**Failures it hunts:**
- Needless decisions ("which format to save in?" when one default fits 95%).
- Tiny or far targets for the most-used control.
- Re-entry of data the system already has.
- "Are you sure?" dialogs standing in for real undo (an Apple-forgiveness failure).
- Silent state: nothing tells the user what happened or what's happening.
- Jargon, ambiguous icons, controls that look the same but act differently (a Birman
  / Apple-consistency violation — the language lies).

**Cures it prescribes:** replace a decision with a default; enlarge/bring near the
frequent target; carry context forward instead of re-asking; swap confirmation for
undo; surface system state; name controls so they're self-evident; make every step
pass Krug's test — *obvious without thought*.

---

## 4. Inclusion & devices specialist (accessibility, devices & ecosystem)

**Who to study:** WCAG / W3C WAI, the Microsoft Inclusive Design toolkit, the
curb-cut principle, Luke Wroblewski (mobile-first, forms), Josh Clark (touch &
multi-device), and the platform human-interface guidelines — **Apple HIG (iOS,
iPadOS, watchOS, tvOS, visionOS, CarPlay)**, Google Material, and voice-design guides
— for how the same principles re-embody per device. Reads
`references/devices-and-ecosystem.md` for the per-device craft.

**What it tests:**
- **Accessibility** — works for motor (one hand, tremor, switch), vision (low vision,
  blind/screen-reader, colour-blind), hearing, cognition (low literacy, stress,
  unfamiliarity), and **situational** disability (glare, gloves, noise, one hand
  full).
- **Per-device embodiment** — does this embodiment fit the device's input
  (touch/pointer/voice/remote/dial/crown), distance (10 cm watch vs 3 m TV), posture,
  and interruption pattern? A desktop layout on a watch is a failure, not a resize.
  Apple's own platforms model this: the *same* product is re-authored per device, not
  shrunk.
- **Ecosystem continuity** — when several devices act as **one product** (watch +
  phone + web, or kiosk → phone), is the hand-off designed? Same mental model, state
  that follows the user (à la Apple Handoff/Continuity), the right job on the right
  device — not the whole product crammed onto each.

**Failures it hunts:**
- Functionality reachable only one way (mouse-only, sight-only, two-hands-only).
- Targets too small or contrast too low to use in the real environment.
- A "responsive" design that merely shrinks instead of re-thinking for the device.
- An ecosystem where each device feels like a different product, or where switching
  devices loses the user's place.
- Voice/kiosk/ATM flows that assume a keyboard, a long attention span, or privacy the
  context doesn't allow.

**Cures it prescribes:** add an equivalent path for each modality; size for the real
hand and environment; re-author (not shrink) per device; assign each device the job
it's best for and carry state between them; design the hand-off explicitly.

---

## The chair of the consilium (synthesis)

After the seats report, one synthesis pass:
- **Order by friction removed**, worst first — not by seat.
- **Reject any cure that buys convenience by cutting capability.** Send it back: find
  the version that moves the cost to the system (Tesler), not the one that amputates.
- **Resolve conflicts** (e.g. Jakob's "follow convention" vs a genuinely better novel
  flow) by the user's real cost, with the JTBD context as tie-breaker.
- **Remember it's a loop.** One pass is a draft. Produce the verdict in the shape
  defined in `SKILL.md` — diagnoses + the one change that matters most + the round
  number + "Draft | Usable" — then feed the fixes back in and run again until a clean
  round adds nothing.
