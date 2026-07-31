# Studio examples — before/after

Read this when a principle feels abstract and you need to see the move. Each pair
is **before → after** with the law it serves. The point isn't to copy the examples —
it's to internalise the *move* so you can make it on any screen.

---

## Understanding the task (понимание задачи) — gate 0

The same screen, designed for two different "tasks":

- **Wrong task:** "show the user their subscriptions" → a tidy table of every
  subscription with columns for everything.
- **Real task:** "Who: a person who was just charged and doesn't understand what
  for. What they do: looking for what this charge is and how to cancel it. Worked
  if: in 10 seconds they found the subscription and the cancel button."
- **Result:** the hero becomes the *most recent charge* with a one-tap "Cancel",
  not an exhaustive grid. Same data, different screen — because the task is
  different. *Law 1, gate 0.*

---

## Информационный стиль (info-style) — law 8 / text

Cut filler, hedging, and cliché. Say what happened and what to do.

| before | after | why |
|--------|-------|-----|
| "An error occurred while performing the operation" | "Didn't save — no connection" | what + why, no filler |
| "Please wait, data is loading…" | "Loading…" | the rest is noise |
| "Welcome! We're glad to see you here" | "Hi. Where do we start?" | greeting ≠ function |
| "Are you sure you really want to delete this item?" | "Delete the account? This is permanent." | name the object + stakes |
| Button: "Submit form" | Button: "Pay 1,200 ₽" | name the real action |
| "Data saved successfully" | (quietly: a checkmark + "Saved") | success rarely needs a sentence |

Move: read every string aloud. If a word can go without losing meaning, it goes.
A button names the action it performs — nothing grander.

---

## Внутреннее ≤ внешнее (inner ≤ outer) — law 4 / spacing

Grouping should read from *space*, not from boxes or lines.

- **before:** label and its input are 16px apart; the next field's label is also 16px
  away. Everything floats at one rhythm — the eye can't tell what belongs together.
- **after:** label→input = 4px (inner), field→field = 24px (outer). Now each
  field reads as one object, and the form reads as a list of objects. No borders
  needed. *Law 4.*

- **before:** a card with `padding: 12px` sits in a grid with `gap: 8px` — the gap
  *between* cards is tighter than the padding *inside* them, so the cards visually
  bleed together.
- **after:** `padding: 12px`, `gap: 24px` — внутреннее ≤ внешнее restored; cards
  separate cleanly without a single divider line.

Move: when you add a level of hierarchy, re-price *every* gap top to bottom.

---

## Contrast, not nuance (Gorbunov's method)

Make differences obvious or remove them.

- **before:** H1 is 17px, body is 16px. The "heading" reads as a slightly-bigger
  paragraph — looks like a bug.
- **after:** H1 is 28px/bold, body is 16px/regular. Now it's obviously a heading.
  *If* you didn't want that much hierarchy, make them *identical* (16px) and group
  by spacing instead. What you may not do is "almost".

- **before:** primary button `#3B82F6`, secondary `#60A5FA` — two close blues; users
  can't tell which is primary.
- **after:** primary = solid filled, secondary = text-only link. One affordance is
  clearly primary. *Law 4 + contrast.*

---

## The magic of subtraction (law 2 + 7)

- **before:** a settings panel with a card, inside it another card per setting, each
  with an icon, a title, a subtitle, a divider, and a chevron.
- **after:** a flat list — label on the left, control on the right, hairline
  between rows. Deleted: nested cards, icons that named nothing, chevrons that led
  nowhere, the third line of text. Nothing broke → it was all noise. *Law 2.*

Move: delete each element and ask "what broke?" If nothing, it's gone.

---

## Мордоворот (the hero, face-to-user) — law 10

- **before:** a dashboard where the chart, the filters, the export button, and the
  date range all compete at equal weight — the user's eye lands nowhere.
- **after:** the number the user actually came for (e.g. "Revenue this month") is
  huge and first; the chart supports it; filters recede to a quiet row; export is
  a small text action. One thing faces the user. *Law 10.*

---

## All states (law 9)

For one "list of items" screen, design all of these *before* shipping the happy path:

- **first-run / empty:** not a blank — one line saying what goes here + the one
  action to add the first item.
- **loading:** skeleton in the shape of the content, not a centred spinner.
- **error / offline:** inline, in place, with what happened and a retry — never a
  modal or a route change.
- **edges:** one item, 10 000 items, a 200-character name, no permission to see it.

A screen that only handles the happy path is a third done.
