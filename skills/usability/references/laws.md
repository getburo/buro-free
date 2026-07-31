# Executable usability laws (the ruler)

These are the consilium's measuring tools. Like Tufte gives `buro` a ruler for data,
these give usability a ruler. **Apply them, don't quote them** — each entry says what
the law is, why it matters, and the concrete move it implies. None of them is about
beauty.

---

## Tesler's Law — conservation of complexity
**Complexity can't be destroyed, only moved.** Every task has an irreducible amount
of complexity; the only question is who carries it — the system or the user.
- **Move it to the system:** smart defaults, automation, inference, forgiving input
  parsing ("+1 (415) 555-0199", "4155550199", "415.555.0199" all accepted), prefill
  from context, derive what can be derived.
- **The move:** for every field, choice, or step, ask "can the system do this instead
  of the user?" If yes, it should. This is the law behind **usable ≠ amputated** —
  you don't delete the complexity, you relocate it off the user.

## Jakob's Law — users live in other products
**The user spends almost all their time on *other* sites and apps, and expects yours
to work the same way.** Familiarity is free usability.
- Follow established patterns for nav, forms, gestures, icons, and flows.
- Spend the user's learning budget *only* where a novel approach is genuinely better
  — and even then, make it teach itself.
- **The move:** before inventing a control, ask "what does the user already know that
  does this job?" Use that. This is the deliberate counterweight to exotic interfaces:
  be ordinary unless there's a real reason not to.

## Fitts's Law — time to a target ∝ distance ÷ size
The bigger and closer a target, the faster and surer the hit.
- Make the **frequent** action big and near the resting position (thumb zone on
  mobile, current focus on desktop).
- Make **dangerous/irreversible** actions small, far, or guarded — friction *here* is
  a feature.
- Edges and corners are infinitely deep targets (the pointer stops there) — use them.
- **The move:** size and place each control by frequency × cost-of-misclick.

## Hick's Law — decision time ∝ number of choices
More options = slower, more error-prone decisions.
- Reduce choices presented at once; reveal the rest progressively.
- Remove false choices by choosing for the user (a default — see Tesler).
- Group and order options so the eye narrows fast.
- **The move:** at each decision point, count the options; if a default fits most
  users, make it and let the rest opt out. (Caution: don't confuse "fewer choices on
  screen" with "fewer capabilities" — see `complexity.md`.)

## Miller's Law & chunking — ~7±2, really "a few"
Working memory is tiny. Don't make the user hold things in their head.
- Break long forms/flows into meaningful steps.
- Group related items into chunks (phone numbers, not 11 loose digits).
- Show, don't make them remember — carry context forward.
- **The move:** anything the user must remember from one screen to act on another is a
  bug; surface it where it's needed.

## Recognition over recall (Nielsen #6 / Apple see-and-point)
Recognizing is easy; recalling is hard.
- Show options, recents, and current selections in place rather than asking the user
  to remember and retype.
- Keep entered data visible and editable; don't hide what was chosen.
- **The move:** replace "type the thing you set earlier" with "here's what you set —
  change it if you like".

## Error prevention > error handling (Nielsen #5 / Apple forgiveness)
The best error message is the one never needed.
- Make invalid states impossible: disable what can't apply, constrain inputs, accept
  any reasonable format, confirm only the genuinely destructive.
- Prefer **undo** over "Are you sure?" — let people act fast and reverse cheaply.
- When an error is unavoidable, say plainly what happened and the way out — never
  blame the user.
- **The move:** for every error path, first try to design the error out; only then
  design the recovery.

## Doherty threshold — keep response under ~400 ms
Below ~400 ms the user stays in flow; above it, attention breaks.
- Make frequent interactions feel instant; do slow work in the background.
- When something is genuinely slow, show **honest** progress (real, not fake) and let
  the user keep working / cancel.
- **The move:** budget latency per interaction; optimistic UI for the common case,
  honest progress for the rare slow one.

## Peak-end rule & goal-gradient — endings and momentum
People judge an experience by its **peak** and its **end**, and push harder as the
goal nears.
- Remove the worst friction point (the peak of pain), not just the average.
- End flows on a clear, satisfying confirmation — the last moment is remembered.
- Show progress toward a goal (steps left, completeness) to pull the user forward;
  pre-fill some progress when you can.
- **The move:** find the single worst moment in the journey and fix *that* first;
  make the finish unmistakable and good.

## Poka-yoke & constraints (designing mistakes out)
Borrowed from manufacturing: shape the interaction so the wrong action can't physically
happen.
- Use constraints (date pickers that can't pick the past, sliders bounded to valid
  ranges) instead of validating after the fact.
- **The move:** prefer a control that *can't* produce a bad value over one that
  accepts then rejects it.

---

## How the laws interact (and where they tension)

- **Hick vs. usable ≠ amputated:** "fewer choices" means fewer choices *at this
  moment*, via disclosure/defaults — **not** fewer capabilities overall. Resolve with
  `complexity.md`: relocate and stage complexity, don't delete it.
- **Jakob vs. a better idea:** convention wins ties; a novel pattern must *clearly*
  beat the familiar one on the user's real cost, and must teach itself.
- **Fitts (big, near) vs. error prevention (dangerous = far):** they agree — frequent
  & safe → big and near; rare & dangerous → small and far. Use frequency × risk to
  place everything.
- **Doherty vs. honesty:** never fake speed; an honest progress bar beats a fake
  instant result that lies about state.
