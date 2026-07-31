# Studio critique — the full sign-off pass

Run this before shipping any screen. Each line is pass/fail. A "fail" is not a
nitpick — it means the screen is still a draft. Walk the seats in order; the
Method seat opens (no task → no design) and the Skeptic (Усомнитель)
has veto (delete-it test).

## 0. The task (the Method seat — understanding the task)
- [ ] The real task fits in one or two plain sentences, in the user's/business's
      language — not design jargon.
- [ ] Success is named: you can say what "this worked" looks like.
- [ ] This screen solves *that* task, not a decorative proxy for it.
- [ ] If the deadline were tomorrow, you know what ships (*needed*) and what defers
      (*nice-to-have*) — ФФФ, not a watered-down everything.

## 1. Function & hero (Art director)
- [ ] The screen's ONE function fits in one sentence (no "and").
- [ ] The hero element *is* that function and owns the space (≈50–70%).
- [ ] First eye-landing point is the hero, not chrome or an ad for itself.
- [ ] Visual hierarchy matches importance (biggest = most important).
- [ ] Nothing competes with the hero for attention.

## 2. Control grammar (Interaction designer)
- [ ] A fixed vocabulary: primary action, toggle, stepper, segmented choice.
- [ ] Same function uses the same control, in the same place, everywhere
      (interface as a *language* — Birman).
- [ ] Exactly one "primary" affordance on the screen.
- [ ] Words, not icons — unless the icon is unambiguous to a first-timer.
- [ ] Controls are grouped by *meaning* (one goal = one cluster).
- [ ] Targets are comfortably tappable; reachable by keyboard.

## 3. Feedback & state (Bidirectional feedback)
- [ ] Every control produces an immediate, visible effect.
- [ ] Each state is reflected in *every* place it's relevant, live.
- [ ] No dead controls; no state that's silently true.
- [ ] Changing one thing updates everything downstream (label + visual + data).

## 4. All states designed (Volumetric thinking)
- [ ] First-run / empty.
- [ ] Loading.
- [ ] Error / denied / offline — inline, never a modal or route change.
- [ ] Success / done.
- [ ] Edges: long text, zero items, huge numbers, no permission.

## 5. Spacing & grid (Typographer — inner and outer)
- [ ] `внутреннее ≤ внешнее`: gaps inside a group are tighter than gaps between
      groups, at every level (letters < words < lines < blocks; padding < gap).
- [ ] Grouping reads from spacing alone — no borders or cards doing the job.
- [ ] Layout sits on a modular grid (модульная сетка); every break from it is deliberate.
- [ ] Adding a level of hierarchy triggered a re-check of *all* spacings.

## 6. Contrast, not nuance (the Method seat)
- [ ] Things meant to differ differ **obviously** (size, weight, meaningful colour).
- [ ] Things meant to match match **exactly**.
- [ ] No almost-same sizes, greys, or weights that read as mistakes.

## 7. Typography (Typographer)
- [ ] One type family in a tight, intentional scale.
- [ ] Tabular numbers for any value that changes.
- [ ] Real punctuation: « » „ " quotes, em dash —, non-breaking spaces.
- [ ] No orphans/widows; optical (not just metric) alignment.
- [ ] No label or number duplicated.

## 8. Colour & surface (Information designer)
- [ ] Colour carries at most two meanings, and they're named.
- [ ] A semantic colour appears nowhere decoratively (that would be a lie).
- [ ] Surface is flat: no gradient, no shadow, no nested cards, no rounding-for-
      rounding.
- [ ] Structure comes from spacing and hairlines, not boxes.

## 9. Text — информационный стиль (Information designer — Ilyahov)
- [ ] Every label, button, hint, empty-state and error is useful and true.
- [ ] No filler, clichés, or hedging ("An error occurred…", "Please wait…").
- [ ] Buttons name the action they perform — nothing grander.
- [ ] Error text says what happened and what to do, plainly.

## 9b. Dense data — tables & charts (Information designer — Tufte)
*Apply only if the screen has a table, chart, dashboard, or report. Full rules in
`references/tables-and-charts.md`.*
- [ ] Data-ink: every gridline, border, fill, shadow, legend earns its place by
      helping read a value; the rest is deleted.
- [ ] Numbers right-aligned with tabular figures; text left; units in the header,
      not in every cell.
- [ ] No zebra, no cell borders, no vertical rules; rows separated by space; totals
      by contrast, not fill.
- [ ] Charts: lines/segments labelled directly, not via a legend.
- [ ] Bar-chart value axis starts at zero; no axis or area distorts magnitude.
- [ ] Sorted/laid out for the comparison the task needs.
- [ ] Dashboard has one hero metric, not twelve equal tiles.

## 10. Honesty (Honesty)
- [ ] No fake progress, no inflated/only-up numbers, no button overpromising.
- [ ] What the screen claims — in pixels *and* in words — is literally true.

## 11. Subtraction veto (the Skeptic (Усомнитель))
- [ ] Every element was tested with "delete it — what breaks?" and survived.
- [ ] No duplicate affordances, no decoration, no "just in case" controls.
- [ ] The chosen direction *removes* more than it adds.

## 12. The first-timer test (Clarity)
- [ ] A new user understands the screen with **no** instructions.
- [ ] Nothing on the screen has to be *learned* to be used.

If every box is checked, it's done. If not, name the failing law and fix it.
