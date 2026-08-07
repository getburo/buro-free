---
name: lebedev
description: >-
  The philosophical canon of Lebedev Studio — the 10 laws of Ководство. Invoke
  when buro needs first principles: to reason about WHY something is wrong, to
  cite laws in a critique, to evaluate clarity, honesty, subtraction, and
  hierarchy. This is the "what" side of the Russian school — what makes an
  interface good. Pairs with buro:gorbunov (the craft / the how). Called by
  buro automatically when critiquing; invoke directly when you need a
  first-principles answer to a design philosophy question.
---

# Buro · Lebedev's Ководство — the ten laws

This is **buro's philosophy canon**. Where `buro:gorbunov` gives you the
executable craft, this sub-skill gives you the **first principles**: the standards
by which every screen is judged, and the laws you cite when explaining why
something is wrong or right.

> **If the user is forced to *study* the interface — the interface has failed.**
> The interface is not the product. The *function* is. The interface disappears.

Apply the laws — don't quote them. A critique cites a law number (`· law 8`)
so the reader can argue back; it doesn't lecture on what the law says.

---

## Law 1 — Clarity beats beauty

Clarity beats beauty every time. Beautiful-but-confusing is a failure;
plain-but-instantly-clear is a success.

**Apply:** Before any aesthetic move, ask: "Does this make the screen clearer
or less clear?" If less clear — it goes, regardless of how good it looks. A
correct-but-lifeless screen has also failed (see law 11), but the sequence is
*clarity first, beauty second* — never reversed.

---

## Law 2 — Indispensability

If you can delete an element and nothing breaks, **delete it**. Every remaining
part must be load-bearing.

**Apply:** Run the delete test on every element: border, label, icon, colour,
card nesting, line of text. Ask "what breaks if this goes?" If the honest answer
is "nothing" — it goes. The studio's Skeptic (Усомнитель) applies this test last, as veto.
This law makes decorative gradients, drop-shadows, and card-within-cards
disappear not by taste but by logic.

---

## Law 3 — Form follows meaning

Form follows *meaning*, never decoration. Ornament that carries no information
is noise. A border, shadow, or colour must *mean* something or go.

**Apply:** For every visual element, ask: "What meaning does this carry?" If the
answer is "none" or "it looks professional" — it's decoration, and decoration is
law 3 violated. A rounded corner is allowed only if "rounded = interactive" or
"rounded = this type of object" — and only then, consistently.

---

## Law 4 — Unity of form and content

One function → one control, looking and behaving identically everywhere.
Different functions → visibly different controls. **One control grammar** across
the whole product.

**Apply:** Map every function to one affordance and enforce it without exception.
If "submit" is a solid filled button, *every* submit is that button. If "dismiss"
is a text link, *every* dismiss is a text link. The moment the same visual form
serves two different functions, the language is ambiguous and the user must
decode, not read.

---

## Law 5 — Bidirectional feedback

Bidirectional feedback: every state is reflected *everywhere* it is relevant,
**live**; every control shows its effect the instant you touch it. No dead
controls, no hidden state.

**Apply:** For every control on a screen, name its effect and where that effect
should be visible. If a slider changes pitch, the pitch label updates *and* the
canvas shifts *and* the audio changes — in the same frame. A control that acts
invisibly is a lie. In real-time interfaces, law 5 becomes the *teacher* — the
only way a user learns a novel control is by acting on it and immediately seeing
what changed. Slow or coarse feedback doesn't just annoy; it makes the interface
un-learnable.

---

## Law 6 — The designer thinks for the user

The designer does the thinking so the user doesn't. **Defaults are decisions.**
Never punt a choice to the user that you could make correctly for them.

**Apply:** Before surfacing any option, ask: "Can I decide this correctly for the
user?" If yes — make it the default; let them override, but don't burden them
with the decision. The best default is invisible: it's simply correct. Asking
"which of these three do you want?" when one answer fits 90% of users is a
failure of this law.

---

## Law 7 — The magic of subtraction

Done is not when there's nothing left to add, but when there's nothing left to
remove. Subtract until it breaks, then add back one.

**Apply:** After designing a screen, run law 2 on everything. Then ask: "Which
features, steps, or fields could be deferred without breaking the core task?" The
ФФФ (fixed deadline, flexible scope) move (`buro:gorbunov`) is law 7 applied to
scope, not just to elements.

**Guardrail — simplify ≠ forbid (subtraction removes *load*, never
*capability*).** This is the most easily misread of the laws, and a misread is
destructive. Subtraction deletes what carries no information and adds no function:
decoration, redundant decisions, dead steps, friction, a second control for one
job. It does **not** delete a capability the user needs, or a *way to reach* a
function. Removing a door, a direct path, a mode, or an option that serves a real
job is **amputation**, not subtraction — it fails the very task it was meant to
serve. The tell: ask *"what does the user lose?"*, not only *"what breaks on
screen?"*. If the honest answer to the first is "a thing they came to do" or "the
only path to it" — stop, you're amputating.

Complexity is conserved (Tesler's law): you can't delete it, only **relocate** it.
The right simplification moves the load onto the *system* — a correct default
(law 6), automation, forgiving input, a guided path for the undecided — while the
direct way to the function stays open for whoever already knows what they want.
"Simpler" means *fewer decisions and less load*, never *fewer abilities*. A guided
entry and a direct door are dual access, not redundancy — keep both. When the urge
to subtract lands on a capability or its access, that's the signal to *relocate*,
not remove. (Whole-product version of this rule: `buro:usability` — usable ≠
amputated.)

---

## Law 8 — Honesty

The interface must not lie: no fake progress, no inflated numbers, no decorative
use of a colour that elsewhere *means* something, no button that pretends to do
more than it does. This extends to **the words**.

**Apply by dimension:**
- **Colour:** if green means "success" somewhere, green is not used decoratively
  anywhere. A decorative green button is a lie.
- **Motion:** if a progress bar fills at a fixed rate regardless of actual
  progress, it lies. Honest progress shows where you actually are.
- **Numbers:** a score that only ever goes up, a "99 available" that never
  decreases, a percentage rounded up to look better — all lies.
- **Words (информационный стиль, Ilyahov's info-style):** "An error occurred" is
  a lie by omission — it says nothing happened rather than saying what did. Plain
  language that names the real situation is honest. (Full infostyle rules in
  `buro:gorbunov`.)
- **Real time (exotic interfaces):** a tuner dot that shows where your pitch *was*
  200 ms ago lies about where it *is*. Lag is a lie about now.

---

## Law 9 — Volumetric thinking (all states)

Design the whole system and **all its states** — empty / first-run, loading,
error/denied, success, and the ugly edges (long text, zero items, huge numbers,
no permission) — not just the happy path.

**Apply:** Before shipping any screen, enumerate every state it can be in. Design
each. Error and no-permission states are *inline* — they don't get a modal or a
route change. An empty state is not a blank — it's one line naming what goes here
and one action to add the first item. A screen that only handles the happy path
is a third done.

---

## Law 10 — The hero, face-to-user (мордоворот)

Turn the important thing to face the user: the hero is biggest, first, and
unmissable; everything else recedes.

**Apply:** Name the ONE function of the screen. Find the one element that *is*
that function. Give it ≈50–70% of the visual weight. Everything else gets out of
its way. If the eye can't tell what the screen is for in under a second, the
мордоворот (the hero turned face-to-user) hasn't happened. A dashboard where
twelve tiles weigh the same answers
nothing.

---

## Law 11 — Beauty through craft, not decor

Clarity is the floor, not the ceiling. A correct-but-lifeless screen has failed
too. Beauty is earned by craft: a distinctive type pairing, a palette with real
light (warm/cool, glow, considered shadow), texture/grain, material and depth,
motion with soul. Make it *clear* — then make it *beautiful*, and let it feel
like the thing it's for.

**Apply:** Laws 1–10 produce clarity. Law 11 takes it further — the craft that
makes a screen feel like the product it's part of. This is **not** decoration
(that's laws 2, 3, 8 violated) — it's the difference between a correct screen
and a screen that feels alive. For the beauty pass, invoke `buro:web-designer`.

---

## Citing laws in a critique

Laws are numbered so critiques stay argumentative, not vague. Use the number:
`· law 8` after a finding so the author knows which principle was violated and
can push back. If a finding spans two laws, cite both: `· law 2, 7`.

The Skeptic (Усомнитель) (`buro:gorbunov`) applies law 2 + 7 as veto: if a finding
doesn't survive "delete it — what breaks?", the finding itself is noise.
