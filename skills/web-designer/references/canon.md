# Web Designer Canon — Reference

Depth beyond the rules in SKILL.md — the reasoning behind treating execution as its own
discipline, separate from choosing the direction (`buro:art-director`'s job).

**Table of contents:**
- [The Generic Web-Execution Defaults, Named](#the-generic-web-execution-defaults-named) · [Typography as the Cheapest Personality Lever](#typography-as-the-cheapest-personality-lever)
- [The Quality Floor](#the-quality-floor) · [CSS Selector Specificity](#css-selector-specificity)
- [Sources](#sources)

---

## The Generic Web-Execution Defaults, Named

Even once a real point of view has been chosen (`buro:art-director`'s job), execution can quietly
default back to the platform's own conveniences unless each choice is deliberately re-checked. By
the mid-2020s, an enormous share of web products converged on the same *execution* formula
regardless of stated direction: a system-default sans left un-replaced, a blue-to-purple gradient
accent applied because a component library shipped one, cards with a large border-radius and soft
drop shadow, and — where the direction pushed back against that — one of a small number of
recognizable "counter-trend" execution defaults: a warm cream-and-serif editorial register, a
near-black canvas with one saturated accent, or a broadsheet/hairline-rule pastiche. Each of these
is a legitimate execution *choice*; the failure is any of them creeping in as a default during
implementation, after a different, specific direction was already chosen upstream.

**Criterion:** compare the executed screen against `buro:art-director`'s actual direction line by
line — type, colour, motion. Every place they disagree is either an intentional, documented
deviation or an execution default that crept back in; if it's the latter, that's this seat's
finding to fix, not a taste debate to reopen.

---

## Typography as the Cheapest Personality Lever

Of every visual decision available on a screen, typeface choice carries an outsized amount of
perceived personality relative to its cost: the same layout, spacing, and colour palette read as
utterly different products depending on whether the type is a warm humanist serif, a cold
geometric grotesque, or a technical monospace. Execution-level pairing principles that hold up
across contexts: contrast the *role* of two families (a characterful display face for headings
against a quiet, highly legible workhorse for body and UI chrome) rather than picking two faces
similar enough to look like a mismatch; match x-height and stroke contrast between a pairing so
they don't visually fight; and treat weight (light/regular/bold) as part of the personality
decision, not just a hierarchy tool.

Leaving type at the platform default (system-ui, or whatever a component library ships with)
during execution isn't a neutral choice — it's the most common way a chosen direction quietly
loses its personality, because the default renders correctly everywhere and so never prompts a
second look during implementation.

**Criterion:** if the body copy on this screen were set in three different plausible typefaces,
would a viewer notice, and would they describe the product differently? If the honest answer is
"no, it'd look the same," the typeface hasn't actually been executed yet — it's been left at
whatever the framework shipped with.

---

## The Quality Floor

Independent of whatever direction `buro:art-director` committed to, a baseline set of execution
properties has to hold regardless: the layout has to actually work down to a small mobile
viewport, not just look fine in the wide desktop mockup; every interactive element needs a visible
focus state for keyboard users, not just a hover state for a mouse; and anyone who has asked their
system for reduced motion should get a version of the execution that respects it, not the full
animated experience regardless. None of these properties is a matter of taste or direction — they
are the floor an execution has to clear before its fidelity to the direction counts for anything.

**Criterion:** resize to a small mobile width, then tab through the interface with no mouse, then
check the execution with reduced-motion simulated. Any of the three breaking is a finding
independent of how faithfully the direction was otherwise rendered.

---

## CSS Selector Specificity

A recurring, entirely mechanical way a chosen direction quietly breaks during execution: two CSS
selectors targeting the same element through different paths — commonly a type-based selector
(`.section`) and an element/attribute-based one (`.cta`) — can silently cancel or override each
other's rules, especially on spacing properties (padding/margin between sections), with the
winner decided by specificity or source order rather than by anyone's intent. The bug reads as a
design failure ("the spacing looks off here") when the actual cause is purely mechanical.

**Criterion:** when a spacing or layout value looks wrong in only one specific instance rather than
consistently, check for a specificity or ordering conflict between the selectors touching that
element before treating it as a design decision to revisit.

---

## Sources

Widely-documented design-criticism observations on convergent web-execution defaults
(design-tool starter kits, component-library defaults compounding across thousands of unrelated
products) — synthesis, not a single named work.
General typographic pairing principles (contrast of role, x-height/stroke matching, weight as
personality) — standard typography practice, taught across type-design and graphic-design
curricula.
The mobile/keyboard-focus/reduced-motion quality floor — accessibility baselines are standard
WCAG practice.
CSS cascade and specificity behavior — standard, documented CSS mechanics (the specification's own
cascade rules), not a design judgment call.
