---
name: copy
description: >-
  Invoke when buro needs to write or critique interface copy: error messages,
  empty states, button labels, onboarding text, tooltips, confirmations, success
  messages, loading text, or any UI string. Applies информационный стиль
  (info-style, Ilyahov) in depth — every word earns its place, buttons name their
  action, errors say what happened and what to do, voice matches the emotional
  register of the task. Called by buro for any microcopy work; invoke directly when
  the task is "rewrite this text", "what should this error say", or "is this copy
  good". The single rule: would a real person say this, face-to-face?
---

# Buro · Microcopy — text as part of the interface

This is **buro's copy sub-skill**. Every label, button, error, empty state,
tooltip, confirmation, and loading message is interface — not an afterthought
slapped on after design. Bad copy makes a clear interface confusing. Good copy
makes a confusing interface survivable.

The governing idea is Ilyahov's информационный стиль (info-style), applied to the
smallest units of UI text:

> **Usefulness and honesty (польза и честность).** Every word is either useful or it goes. The interface
> is not a place for warmth-signalling, self-promotion, or hedging. Say what
> happened. Say what to do. Stop.

The single real-person test: **"Would a real person say this, face-to-face?"**
"An error occurred while processing your request" — would anyone say that?
"Couldn't save — no connection" — yes.

Full before/after pairs in `references/copy-examples.md`.

---

## Info-style (информационный стиль) — the rules

**Every word earns its place.** Read every string aloud. If a word can go
without losing meaning — it goes. No exceptions.

**The button names the action — nothing grander.** The button text is the verb +
object of the action it performs. "Submit Form" → "Save changes". "Confirm" →
"Delete account". "Proceed" → "Pay $1,200". When the verb and object are clear
from context, the object can be dropped: "Save", "Delete", "Send".

**Headings are a task, not an announcement.** "Settings" is a heading, not a feature
advertisement. "Welcome to our platform!" says nothing — replace with what the
user can *do*. "Where do you want to start?" or just the content.

**Avoid:**
- Stop-words: please, kindly, feel free to, don't hesitate to
- Hedging: may, might, could, perhaps, it seems
- Self-praise: powerful, seamless, best-in-class, robust
- Filler openers: "In order to…", "Please note that…", "You can…"
- Passive voice when active is possible

---

## Error messages

The formula: **what happened + what to do.** Both. Always.

| Anti-pattern | Right |
|-------------|-----------|
| "An error occurred" | "Couldn't save — no connection. Try again." |
| "Error 403" | "You don't have access to this file. Ask the owner for access." |
| "Invalid format" | "Card number must be 16 digits" |
| "Something went wrong" | "Couldn't load — the server isn't responding. Refresh the page." |
| "This field is required" | "Enter your email — we'll send a sign-in link" |

Rules:
- Name the object that failed ("photo didn't upload", not "upload failed")
- Name the cause if known ("no connection", "file too large", "link expired")
- Name the action ("try again", "refresh the page", "choose another file")
- Never blame the user ("you entered an invalid…" → "phone number not found")
- Never use technical codes as the main message — codes go in small print for
  support, the human message goes big
- Errors are inline, calm, and terse — not a modal apology

---

## Empty states

Two elements: **what will be here + one action to begin.**

| Anti-pattern | Right |
|-------------|-----------|
| (blank screen) | "No tasks yet. Create the first one →" |
| "No data available" | "Your purchases will show up here. Go to the catalog →" |
| "No results" | "Nothing for 'concrete'. Try 'building materials'." |
| "List is empty" | "You haven't added any contacts yet. Invite colleagues →" |

Rules:
- The empty state is not an error — don't use error styling
- One action max — the most natural first step for this screen
- If the empty state is caused by a filter/search, offer to clear it as the action
- If the empty state is a good thing ("inbox zero"), say so: "All caught up.
  Take a break." — still no filler, just honest warmth

---

## Buttons and links (labels)

- **Verb + object:** "Save changes", "Delete account", "Pay $1,200", "Add member"
- **Verb only** (when object is clear from context): "Save", "Delete", "Sign in", "Cancel"
- **Never:** "Yes", "No", "OK", "Confirm" — these force the user to read
  the question to know what they're confirming. The button names the action.
- **Destructive actions** name the consequence: "Delete account permanently",
  not "Delete"
- **Links** name the destination or the action, not "click here" or "learn more"
  without context

---

## Confirmations

The question names the object and the consequence. The buttons name the actions.

| Anti-pattern | Right |
|-------------|-----------|
| "Are you sure?" [Yes] [No] | "Delete the project 'Rebrand'? This can't be undone." [Delete project] [Keep] |
| "Confirm action?" [OK] [Cancel] | "Cancel your subscription? Access ends June 15." [Cancel subscription] [Keep] |

Rules:
- Show confirmation *only* for irreversible or high-stakes actions
- Everything reversible gets an undo-toast instead of a dialog (see `buro:usability`)
- The destructive button is the secondary button visually (less prominent)
- Never make "cancel" the primary button — that's a trap

---

## Loading states

- Be specific about *what* is loading: "Loading your documents…" not "Loading…"
- If you know the time, say it: "This usually takes ~10 seconds"
- If you don't know, don't invent progress: use indeterminate, label it "Loading…"
- Don't add a period to "Loading…" — the ellipsis already implies continuation
- Skeleton screens: no text, just the shape of the content — nothing to read

---

## Success messages

Routine actions get quiet acknowledgment. Non-routine actions get named.

| Situation | Text |
|----------|-------|
| Form save | ✓ Saved (quiet, no modal) |
| Request submission | "Request sent. We'll reply by email within a day." |
| Item deletion | "Deleted. Undo →" (toast, 5–6 s) |
| Payment | "Paid. Receipt sent to your email." |

Rules:
- "Successfully saved" → "Saved" (successfully is a stop-word)
- Routine successes don't need a sentence — a checkmark and a word are enough
- Tell the user what happens *next* when that's useful

---

## Onboarding (first-run copy)

- Lead with what the user can *do*, not what the product *is*
- No "Welcome to X!" as a headline — that's the product promoting itself
- The first screen's job: orient + give one action
- Don't front-load everything — introduce features as they become relevant
- Permissions: ask at the moment of need, explain the benefit in plain terms:
  "Allow the mic so you can record a voice note" not "We need microphone access"

---

## Voice and tone

The content of the message is fixed by facts. The *tone* is set by the emotional
register of the task. Match them:

| Context | Tone | Example |
|----------|-----|--------|
| Finance, medicine, law | Precise, neutral | "Payment of $1,200 declined. Check your card details." |
| Learning, progress | Supportive, direct | "Clean. That step's done." |
| User error | Direct, no blame | "Phone number not found. Check the number." |
| Success, achievement | Warm, brief | "First one done. That's the path." |
| Empty state | Neutral, orienting | "Your tasks will show up here." |

The voice is consistent; the tone shifts. "Consistent voice, variable tone" is
the rule — the same personality in a calm moment and a stressed one.

**Never:**
- Exclamation points on errors ("Error!")
- Sycophancy ("Great choice!")
- Irony or jokes on errors
- Marketing language inside the product ("Unlock the power of our platform")

---

## Reference

Full before/after library in `references/copy-examples.md`.

`references/canon.md` — depth beyond these rules: the full three-criteria definition of информационный стиль (info-style), the "useful action / goal / tasks" triad, all five stop-word categories with verbatim quotes, the six-step anti-канцелярит (anti-bureaucratese) sequence, instruction/multi-step structure, paragraph autonomy, and the "фальшь" (fake tone) test — all sourced from Ilyahov & Sarycheva, *Пиши, сокращай* ("Write, Cut"). Open it for an exact quote or a deeper before/after example.
