---
name: gorbunov
description: >-
  The craft of Gorbunov's method — the executable HOW of
  the Russian school, for a screen's STRUCTURE (NOT its motion/timing/easing — that's
  buro:motion): understanding the task (понимание задачи), ФФФ (fixed deadline / flexible scope),
  inner ≤ outer spacing (внутреннее ≤ внешнее), contrast, the modular grid, info-style
  (информационный стиль), interface-as-language (Birman), the 7-seat studio panel, and the
  standard critique output format. The backbone of every buro critique. Pairs with buro:lebedev
  (the philosophy / the what); called by buro automatically for any screen work.
---

# Buro · Gorbunov's method — craft and critique

This is **buro's craft engine**. Where `buro:lebedev` gives the laws that judge
*what* is good, this sub-skill gives the **executable tools** — how you actually
produce a screen or critique that lives up to those laws.

---

## Gorbunov's method — the craft tools

These are the measurable, executable techniques. Not opinions — the *how* behind
laws 1, 2, 4, and 8.

### Understanding the task (понимание задачи) — gate 0, mandatory before anything else

Before naming a function or touching a pixel, understand the **real task** — in
the user's and business's language, not design jargon. Write it in three lines
and treat it as the contract. A screen beautifully designed for the wrong task is
the most expensive kind of failure.

> **Who:** who is in front of this screen, in what situation.
> **What they do:** the real job they came to get done (their words, not "UX").
> **Worked if:** the observable outcome that means it worked.

If you can't write these three lines — you're not ready to design or critique.

**Before the three lines, audit the question they came in.** A request is usually
solution-shaped ("add a filter"), symptom-shaped ("it's ugly"), borrowed jargon, or the wrong
scope — and answering it as asked is the expensive failure this gate exists to prevent. Full
four-way check and the reframe-out-loud rule: `buro:process` → *The question audit*.

### ФФФ — fixed deadline, flexible scope

"First what's needed, then what's nice to have." Ship the most important thing by
the deadline; defer the optional. You can only flex correctly once you understand
the task — you know what's *needed* vs *nice-to-have*. This is law 7 applied to
scope, not just to elements: don't water everything down to fit, ship the core solid.

### The inner-and-outer rule: `внутреннее ≤ внешнее` (inner ≤ outer spacing)

Distances *inside* an object are smaller than the distances *around* it:
```
letters < words < lines < blocks
padding inside a card < gap to the next card
label → input < input → next label
```
This is what makes grouping *read* without boxes or lines. When you add a level
of hierarchy, **re-check every spacing in the layout** — the new relationship
re-prices all the gaps. This is the measurable engine behind law 4.

### Contrast, not nuance

Two elements are either **clearly the same** or **clearly different** — never
almost-the-same. A 2px size difference, a barely different grey, a heading
slightly bigger than body — all read as mistakes. Make the difference obvious or
remove it. Contrast creates hierarchy; nuance creates doubt.

### Modular grid (модульная сетка)

Lay the screen on a column/row grid so alignment is a decision once, not a fight
on every element. But the grid **helps, it doesn't dictate** — break it
deliberately when meaning demands, never by accident.

### Информационный стиль — Ilyahov's info-style

Every label, button, hint, empty-state and error is *text*, and text obeys
инфостиль: cut stop-words, clichés, hedging and filler; say the thing plainly;
**польза и честность** (usefulness and honesty) — useful and true.

Quick rule: read every string aloud. If a word can go without losing meaning,
it goes. A button names the action it performs — nothing grander.

| before | after |
|--------|-------|
| "An error occurred while performing the operation" | "Didn't save — no connection" |
| "Please wait, data is loading…" | "Loading…" |
| "Welcome! We're glad to see you here" | "Hi. Where do we start?" |
| Button: "Submit form" | Button: "Pay 1,200 ₽" |

Full before/after pairs in `references/examples.md`.

### Interface is a language (Birman)

Controls form a vocabulary and a syntax; the user learns the grammar once and
reads the rest. Same meaning → same word/control → same place. Keep the language
small and consistent so the screen is *legible*, not decoded. This is the same
idea as law 4, stated from the user's side.

---

## The studio method — attacking a screen (in order)

Work these gates sequentially. Each is a blocker — don't advance until answered.

```
0. Understanding the task (above) — if you can't write the three lines, stop.
1. Name the ONE function — one sentence, no "and".
2. Find the hero — the element that IS the function. Give it ≈50–70%.
3. One control grammar — fix the vocabulary; words over icons;
   exactly one primary affordance.
4. Group with spacing — внутреннее ≤ внешнее; one type system;
   colour carries ≤2 meanings; modular grid (модульная сетка).
5. Bidirectional feedback — every control wired to an immediate visible effect.
6. Subtract (ФФФ) — delete everything removable; defer *nice-to-haves*.
7. Contrast — differences are obvious; matches are exact.
8. Text by инфостиль — rewrite every string.
9. All states — empty, loading, error, success, edges. All inline.
10. Beauty — invoke buro:web-designer for the beauty pass.
11. Critique — run the studio panel below.
```

---

## The studio panel — the seven seats

Review every design through **all** of these. Each seat is adversarial — its job
is to find what's wrong. For a large redesign, fan them out as parallel agents;
for a small screen, walk them in your head.

- **Art director** — composition, hierarchy, rhythm, the hero. *"Where do my
  eyes go first? Is that the function? Anything fighting the hero?"*

- **Typographer** — type system, measure, tabular nums, real punctuation (« » „ ",
  em dash —, non-breaking spaces, no orphans/widows), optical alignment,
  `внутреннее ≤ внешнее` spacing. *"Is this one voice or a font zoo? Do the gaps
  group things, or just sit there?"*

- **Interaction designer** — control grammar as a language (Birman),
  every state, feedback loops, target sizes, keyboard. *"Which control lies? Which
  state is undesigned? What has no feedback? Is the vocabulary consistent?"*

- **Information designer** — clarity and honesty of every label, number, and
  colour; text by инфостиль; dense data by Tufte (call `buro:dataviz` if needed).
  *"What does the user have to learn here? What can be cut? Does any word hedge,
  pad, or mislead?"*

- **The Method seat** — understanding the task + contrast. *"What's the
  real task — does this screen solve it, or a jargon version of it? If the
  deadline were tomorrow, what ships? Where is contrast merely almost?"*

- **The Artist (light & material)** — atmosphere, depth, warmth, the emotional
  temperature. *"Is this merely correct — or does it have soul? Would someone
  feel something here?"* For the beauty pass, invoke `buro:web-designer`.

- **The Skeptic (Усомнитель)** — law 2 + 7 incarnate. *"Delete it — what
  breaks? If nothing, it's gone. Why are there two of these? Why is this here?"*
  **Bounded:** the Skeptic deletes elements, decoration, redundant decisions and
  friction — **never a capability or the user's way to reach a function.** Cutting a
  door, a direct path, a mode, or a real option is *amputation*, not subtraction
  (law 7 guardrail). When the urge to cut lands on an ability or its access, the
  verdict is *relocate it to the system / a default* (Tesler), not *remove it*. The
  Skeptic asks two questions, not one: "what breaks on screen?" **and** "what does
  the user lose?"

**Synthesis rule:** a finding ships only if it survives the Skeptic (Усомнитель). Prefer
the change that removes **load** (decoration, steps, decisions, friction) over the
change that adds — but moving a decision onto the system or a default *beats*
removing the user's access to a function (law 7 guardrail: simplify ≠ forbid).
Nothing ships if the Method seat can't see the real task in it, and nothing
ships that amputates a capability to buy tidiness.

---

## How to deliver critique (the output shape)

A studio critique is a verdict you can act on, not a vibe. Always use this shape:

```
Task: <one line — the real task; if you can't state it, that's finding #1>

Findings (worst first):
  ✗ [seat] <what's wrong> → <the fix, stated as a concrete change> · law <n>
  ✗ [seat] …
  ⚠ [seat] <weaker, but worth noting>

Verdict: <Draft | Ship-ready> — <the one change that matters most>
```

Rules:
- Name the **seat** and the **law** so the author can argue back.
- State the fix as a *concrete change* ("merge these two greys into one", not
  "improve contrast").
- Order by severity — not by panel seat order.
- **Prefer the fix that removes.**
- `Ship-ready` only when every checklist item in `references/critique-checklist.md`
  is green.
- Keep it short: three sharp findings beat fifteen soft ones.

---

## Discipline (defaults the studio enforces)

- **Task:** one or two plain sentences, agreed before design starts. No design
  without it.
- **Typography:** one grotesque/text family, tight scale. Tabular numbers for
  live values. Real quotes and dashes. Numbers and labels never duplicated.
- **Spacing:** `внутреннее ≤ внешнее` everywhere; grouping reads from spacing,
  not boxes; on a modular grid (модульная сетка); every break intentional.
- **Contrast:** clearly same or clearly different — never almost.
- **Text:** информационный стиль — every word useful and true.
- **Colour:** mostly ink + one neutral; colour for ≤2 meanings; nowhere decorative.
  *Designer advice — how to build the palette:*
  - Start with one neutral background (dark or light). Typography creates hierarchy
    through weight and size — not colour.
  - One interactive colour: used only on controls the user can act on. Nowhere else.
  - One semantic "good" colour (success, in-tune, pass) and one "wrong" colour
    (error, off-pitch, fail). These appear nowhere decoratively — ever. A decorative
    use of either is a lie (law 8).
  - Warm dark background + cool accent reads as intimate, focused (studio, console).
    Cool background + warm accent reads as clinical + human (medical, finance).
    The palette has a light source — decide where it is and be consistent.
  - Dim (reduced opacity) is a semantic value: "present but secondary". Don't
    overuse it — three levels of dim collapse hierarchy into mush.
  - Test the palette in greyscale: if hierarchy disappears, it was built on colour
    not contrast. Fix the contrast; colour amplifies, it doesn't create.
- **Surface:** flat. No gradient, shadow, nested cards, or rounding-for-rounding.
- **Movement:** explains a change only. Never decoration. Respect prefers-reduced-motion.
- **States:** every control reflects its own state; nothing silently true.

---

## Slop the studio kills on sight

Purple-on-white gradients · drop-shadows for "depth" · cards inside cards ·
everything rounded · icon-only toolbars to decode · a settings gear hiding real
controls · decorative use of a semantic colour · duplicated labels · a third line
of text · fake progress bars · scores that only ever go up · the happy path with
no empty/error state · "AI-generic" centred-hero-with-three-cards · almost-equal
spacing (nuance instead of contrast) · groups separated by boxes not by
`внутреннее ≤ внешнее` · filler microcopy ("An error occurred while performing the
operation", "Welcome!", "Please wait…") · a gorgeous screen for
the wrong task · zebra-striped tables · cell borders and vertical rules · units
in every cell · centred or left-aligned numbers · chart legends where direct
labels would do · 3D/shadowed/gradient charts · a truncated bar-chart axis that
lies · a dashboard where every tile weighs the same · **amputation dressed as
subtraction** — removing a door, a direct path, a mode, or a real option to look
"simpler" (simplify ≠ forbid: cut load, never capability — relocate to a
default/system instead).

---

## Reference files

- `references/examples.md` — before/after pairs for every major technique:
  understanding the task, инфостиль, внутреннее≤внешнее, contrast, the magic of
  subtraction, мордоворот (the hero, face-to-user), all states.
- `references/critique-checklist.md` — full sign-off pass (12 sections, 50+
  checks). Run before declaring `Ship-ready`.
