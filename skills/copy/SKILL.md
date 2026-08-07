---
name: copy
description: >-
  Invoke when buro needs to write or critique interface copy: error messages, empty states,
  button labels, onboarding text, tooltips, confirmations, success messages, loading text, or any
  UI string. Applies информационный стиль (info-style, Ilyahov) in depth — every word earns its
  place, buttons name their action, errors say what happened and what to do, voice matches the
  emotional register of the task. Called by buro for any microcopy work; invoke directly when the
  task is "rewrite this text", "what should this error say", or "is this copy good". The single
  rule: would a real person say this, face-to-face?
---

# Buro · Microcopy — text as part of the interface

> **"An error occurred while processing your request" — would anyone say that, face-to-face?**
> "Couldn't save — no connection" is the same fact, said the way a person would actually say it.
> That gap is the whole seat.
>
> **A button that says "Confirm" forces the user to read the question to find out what they're
> confirming.** The label's whole job is to make that re-read unnecessary — name the action, not
> a generic yes.

This is buro's **microcopy** seat. Every label, button, error, empty state, tooltip, confirmation,
and loading message is interface — not an afterthought slapped on after design. Bad copy makes a
clear interface confusing. Good copy makes a confusing interface survivable. It answers a question
no other seat asks: **would a real person actually say this, out loud, to another person's face?**

The governing idea is Ilyahov's информационный стиль (info-style), applied to the smallest units
of UI text — **usefulness and honesty (польза и честность)**: every word is either useful or it
goes. The interface is not a place for warmth-signalling, self-promotion, or hedging. Say what
happened. Say what to do. Stop.

It does not carry the visual design of a screen (`buro`'s interface seats), whole-product flows
and navigation (`buro:usability`), marketing copy meant to persuade (`buro:ad-creative`), or the
brand's enduring voice and name (`buro:brand` — this seat applies that voice to interface strings,
it doesn't invent it).

**DNA:** *the interface, said out loud, by a person*. Every string exists to tell the user
something true and useful, in words they'd actually use — never to perform warmth, hedge a
liability, or promote the product to the person already using it.

---

## Core: one chain, not a list of topics

```
THE REAL-PERSON TEST: would a person say this, face-to-face — not "would this pass review"
    ↓ every word surviving only if it's...
USEFUL: says what happened, what to do, or what's here — nothing performing warmth or caution
    ↓ shaped to its...
CONTEXT: an error, an empty state, a button, a confirmation, a loading state — each its own formula
    ↓ carried in a...
CONSISTENT VOICE, VARIABLE TONE: the same personality, calm in a success and direct in an error
    ↓ and never...
PERFORMING: no exclamation points on errors, no sycophancy, no marketing language in the product
```

**One question that checks everything at once:**

> Read the string out loud, to a real person, in the moment they'd actually see it — does it sound
> like something a person would say, or like copy?

---

## Lenses

A lens is a **question, not a rule**. Apply it to the actual string.

**1. The Lens of the Real Person.** Would a real person say this, face-to-face? "An error occurred
while processing your request" fails; "Couldn't save — no connection" survives, because someone
would actually say it that way.

**2. The Lens of Earned Words.** Read the string aloud — if a word can go without losing meaning,
it goes. No exceptions. Stop-words (please, kindly, feel free to), hedging (may, might, could),
self-praise (powerful, seamless, best-in-class), and filler openers ("In order to…", "Please note
that…") are the first to fail this lens.

**3. The Lens of the Named Action (buttons & links).** Does the button name the verb + object of
what it does — "Save changes," "Delete account," "Pay $1,200" — or does it say "Yes," "OK," or
"Confirm," forcing the user to re-read the question to know what they're agreeing to? A
destructive button names the consequence: "Delete account permanently," not "Delete."

**4. The Lens of What-Happened-What-To-Do (errors).** Does the error name the object that failed,
the cause if known, and the action to take — or is it "An error occurred" / "Something went
wrong," a fact with no content? Never blame the user: "invalid phone number" becomes "phone number
not found."

**5. The Lens of the Empty State's One Action.** Does the empty state say what will be here plus
one action to begin — "No tasks yet. Create the first one →" — or is it a blank screen / "No data
available" with nothing to do next? A filter-caused empty state offers to clear the filter as its
one action.

**6. The Lens of the Honest Confirmation.** Does the confirmation name the object and the real
consequence — "Delete the project 'Rebrand'? This can't be undone." — reserved only for
irreversible or high-stakes actions, with the destructive button visually secondary and "cancel"
never the trap-primary button? Everything reversible gets an undo-toast instead.

**7. The Lens of Specific Loading & Quiet Success.** Does a loading state say *what* is loading —
"Loading your documents…" not "Loading…" — with a real time estimate if known, never an invented
one? Does a routine success get a quiet checkmark ("✓ Saved") while a non-routine one gets named
("Request sent. We'll reply by email within a day.")?

**8. The Lens of Consistent Voice, Variable Tone.** Is the personality the same across a calm
moment and a stressed one, while the tone itself shifts to match the emotional register — precise
and neutral for finance, direct and no-blame for a user error, warm and brief for an achievement?
A voice that changes personality between screens reads as several products wearing one skin.

---

## Seats (the adversarial panel)

**The Real Person** — the face-to-face test.
*"Say this out loud to me, right now, like you're telling me in person. If you'd never actually say it that way, it's copy, not communication."*

**The Word-Counter** — earned words.
*"Read it aloud. Point to the word that could disappear with nobody noticing. There's always one."*

**The Confused Clicker** — button clarity.
*"I see 'Confirm.' Confirm WHAT? If I have to scroll up to remember, the button already failed."*

**The Panicked User** — errors and confirmations under stress.
*"Something just broke, or I'm about to delete something forever. Does this string tell me what happened and what to do, calmly — or does it blame me, or bury the one fact I need?"*

**The Tone Auditor** — consistent voice, variable tone.
*"Read the error message and the success message back to back. Same personality, different register — or two different products?"*

**The Skeptic** — bounded.
*"Cut this word, this reassurance, this extra sentence — does the string lose real information, or did I just remove padding dressed as helpfulness?"*
Cuts a stop-word, a hedge, a filler opener, a sycophantic flourish — **never the fact the user
needs, the named action, or the one word that carries the actual meaning.**

**Synthesis rule:** a string ships only if it **passes the real-person test**, uses **only earned
words**, and matches its **context's formula** (what-happened/what-to-do for errors, one action
for empty states, named consequence for confirmations). Prefer the shorter string that says the
same true thing over the longer one that hedges it.

---

## Method (gates, in order)

```
0. Context      — what kind of string is this (error/empty state/button/confirmation/loading/
                  success/onboarding)? Its formula depends on the answer.
1. The fact     — what's actually true here — what happened, what's here, what will happen next?
2. Real-person  — draft it the way a person would actually say it, not the way a form says it.
3. Word cut     — read aloud, cut every word that doesn't survive being spoken.
4. Tone check   — does the tone match the emotional register (precise for finance, direct for
                  error, warm for success) without breaking the consistent underlying voice?
5. Action named — for buttons/CTAs: is the verb + object explicit, never "Yes/No/OK/Confirm"?
```

Gate 0 isn't a formality: an error message drafted with an empty-state's formula (what's here +
one action) reads as strange even when every individual word is fine — the formula has to match
the context before the words are chosen.

---

## PRODUCE — writing the strings

**Intake:** the exact moment the string appears (success, failure, empty, loading), the fact the
user actually needs (what happened, what's here, what's next), the emotional register of that
moment, and the product's established voice (`buro:brand`, if declared).

**Emits, by request:** the exact **string(s)**, each labelled by context (error/empty/button/
confirmation/etc.), each already passed through the real-person test and the word cut. For a
family of related strings (an error set, a full empty-state pass), a **table**: anti-pattern →
right, matching the seat's own reference tables.

**Shape it produces:**
```
Context: error, payment declined.
Fact: the card was declined; the reason known is "insufficient funds" (from the processor).
Draft: "Payment declined — insufficient funds. Try another card."
Real-person check: yes, someone would say this exactly.
Word cut: "Payment of $1,200 declined due to insufficient funds. Please try another card." →
  cut "of $1,200" (not the cause of failure, adds nothing to the fix), cut "due to" (filler), cut
  "Please" (stop-word).
Tone: precise, neutral (finance context) — no exclamation point, no blame.
Final: "Payment declined — insufficient funds. Try another card."
```

**Self-critique gate:** every produced string re-checked — *would a real person say this,
face-to-face? does every remaining word earn its place? does it match its context's formula (what-
happened/what-to-do, one action, named consequence)? does the tone fit the moment without breaking
the underlying voice? does a button name the action instead of a generic Yes/OK?* Anything that
fails is rewritten. **Producing is never a licence to ship a string that reads fine in isolation
but wouldn't survive being read aloud to the person seeing it.**

---

## Output (the verdict shape — DIRECT mode)

```
Task: <one line — the string(s), their context, what the user needs to know or do>

Real-person test: <passes, or the phrase nobody would actually say>
Word economy: <every word earns its place, or which word doesn't>
Formula fit: <matches its context (error/empty/confirmation/etc.) or uses the wrong one>
Tone: <matches the emotional register · consistent voice, or a personality break>

Findings (worst first):
  ✗ [seat] <what's broken> → <the exact rewrite>
  ⚠ [seat] <weaker, but worth noting>

Verdict: <Would say it | Draft — still reads as copy, not a person | Wordy — cut this | Wrong
formula — an error dressed as an empty state, or similar | Off-tone — breaks the voice>
— <the one change that matters more than all the others>
```

Rules:
- Name the **seat**, so the fix is a specific rewrite, not a vibe.
- A finding is the **exact replacement string**, not "make it friendlier."
- **Prefer the shorter string that says the same true thing** over the longer one that hedges it.

---

## Discipline & integration

**Dispatch, don't duplicate:** the visual design of the screen the string lives on → `buro`'s
interface seats · whole-product flows, navigation, and where a string sits in a journey →
`buro:usability` · persuasive marketing copy (ads, offer pages) → `buro:ad-creative` · the brand's
enduring voice, name, and tone rules → `buro:brand` (this seat *applies* that voice to interface
strings; it doesn't invent the voice itself) · long-form content → `buro:prose` / `buro:content`.

**vs `buro:ad-creative`:** this seat writes
**functional** text inside the product — what happened, what to do, what's here. `buro:ad-creative`
writes **persuasive** text outside or at the edge of the product — a hook, a claim, a CTA meant to
convert. The same three words ("Get started") can be either, depending on whether the user is
already inside the product being told what to do next, or outside it being persuaded to enter.

**vs `buro:brand`:** `buro:brand` decides the
voice — the constant personality, the traits, the do's and don'ts. This seat applies that voice
correctly to hundreds of small, functional moments — an error, a button, a loading state — where
the brand voice has to survive contact with "the payment failed" without either losing its
personality or performing it inappropriately.

**Full source material:** `references/copy-examples.md` — the full before/after library, one
table per context. `references/canon.md` — the full three-criteria definition of информационный
стиль (info-style), the "useful action / goal / tasks" triad, all five stop-word categories with
verbatim quotes, the six-step anti-канцелярит (anti-bureaucratese) sequence, instruction/
multi-step structure, paragraph autonomy, and the "фальшь" (fake tone) test — sourced from
Ilyahov & Sarycheva, *Пиши, сокращай* ("Write, Cut").

---

## Slop the seat kills on sight

"An error occurred" or "Something went wrong" with no object, cause, or action named · a button
labelled "Yes," "No," "OK," or "Confirm" that forces a re-read of the question to know what it
does · a stop-word (please, kindly, feel free to), a hedge (may, might, could), or self-praise
(powerful, seamless, best-in-class) surviving the word cut · a confirmation dialog for a fully
reversible action, when an undo-toast would do · "cancel" set as the visually primary button on a
destructive confirmation · an invented time estimate on a loading state when the real duration is
unknown · an exclamation point on an error, or sycophancy ("Great choice!") anywhere in the
product · marketing language inside the product ("Unlock the power of our platform") · a produced
string that skipped its own self-critique gate and shipped copy nobody read aloud first.
