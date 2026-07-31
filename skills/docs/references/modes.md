# The four modes — and the collisions between them

Diátaxis (Daniele Procida, 2020) splits documentation by **what the reader is doing**, not by
subject matter. Two axes: *studying vs working*, and *practical vs theoretical*. The result is
four documents that look superficially similar and are structurally incompatible.

|  | Practical (doing) | Theoretical (thinking) |
|---|---|---|
| **Studying** (learning) | **Tutorial** — teaches | **Explanation** — justifies |
| **Working** (a job at hand) | **How-to** — solves | **Reference** — states |

The framework's own claim is that it settles three things at once: **content** (what to write),
**style** (how to write it), and **architecture** (how to organise it).

---

## Tutorial — a lesson

**Reader:** does not know what they don't know. Has no goal of their own yet; the goal is yours.
**Success:** they finish with something working and the confidence to continue.

- **You are responsible for what happens.** Every command is given; nothing is left "as an
  exercise". The reader should not have to make a single decision you did not make for them.
- **It must work every time.** A tutorial that fails at step 7 does more damage than no tutorial:
  the reader concludes the product is broken, and they are not wrong to.
- Concrete over general. One path, chosen by you, even if three exist.
- Results the reader can see at each step — "you should now see…". Visible progress is the
  mechanism; without it they cannot tell whether they are on the rails.
- **No options, no alternatives, no configuration tables.** Every "you could also…" is a decision
  handed to a person not yet equipped to make it.
- Explain almost nothing. The urge to justify is strong here and it is the main way tutorials rot
  into essays. Link to the explanation instead.

## How-to — a recipe

**Reader:** has a goal and usually a problem. Competent. Interrupted. Impatient — correctly so.
**Success:** they solve it and leave.

- **Titled by the goal, in the reader's words:** "Restore a deleted branch", not "Branch recovery
  subsystem".
- Assume competence. Skip what a working practitioner already knows.
- Prerequisites as a **checklist**, not prose, at the top, before anything else.
- Numbered steps: one action each, with what they should see.
- Handles the real world: the branch here, the variant there. A how-to may fork; a tutorial may not.
- **Error recovery inline**, at the step where the error happens — not collected in a
  troubleshooting appendix nobody scrolls to.
- No teaching. If they wanted the lesson they would have opened the tutorial.

## Reference — a map

**Reader:** knows what they want and needs the exact fact. Arrives by search, leaves in seconds.
**Success:** the fact, correct, found fast.

- **Structured by the product's own shape** — module, endpoint, class, flag — not by any narrative.
  Reference is the one mode where the machine's structure beats the reader's story.
- Consistent, boring, complete. Every entry identical in layout so the eye learns it once.
- **Describe, do not instruct.** State what a thing *is* and what it *does*. The moment reference
  starts advising, it has become a how-to and stopped being scannable.
- Facts only: types, defaults, units, constraints, errors raised, since-version.
- Examples are welcome and must be minimal — an example is illustration here, never a lesson.
- This is the mode most safely generated from source. Generated reference plus hand-written
  tutorials and how-tos is a healthy shape; generated *everything* is a shape with no way in.

## Explanation — a discussion

**Reader:** not working right now. Wants to understand why the thing is the way it is.
**Success:** they can predict how the system behaves in a case nobody documented.

- Free to discuss alternatives, history, trade-offs, and what was rejected and why.
- Names the constraints that produced the design. This is where the honest "we chose the worse
  option because of X" belongs — and it is what makes a system predictable.
- Explicitly **not** something to follow along with. No steps.
- Best read away from the keyboard, and should be written as though it will be.

---

## The collisions — how mixing actually fails

**Tutorial + reference** (the most common). A lesson interrupted by a table of every flag. The
learner loses the thread; the fact-seeker cannot find the table again tomorrow, because it is
buried in a lesson they have no reason to reopen.

**How-to + tutorial.** A recipe that starts teaching fundamentals. The reader had a broken
production system and got a curriculum. This is the failure most likely to be praised in review
("very thorough!") and most likely to be abandoned in use.

**Reference + explanation.** Facts padded with rationale. Scanning dies: the eye can no longer
predict where the default value sits, because sometimes there are two paragraphs first.

**Explanation + how-to.** A discussion that suddenly issues instructions. The reader wasn't at
their keyboard and now feels they missed something.

**All four in one README.** The universal default, and the reason the phrase "nobody reads the
docs" exists. A README is best treated as an **entrance**: what this is, the shortest possible
first success, and four honest doors.

---

## Diagnosing an existing document

1. **Read the first screen and name the mode it promises.**
2. **Read the last screen and name the mode it delivers.** Different? That is the finding.
3. Find the first paragraph that belongs to a different mode. That is usually the split point,
   and usually the whole fix is a cut and a link.
4. Ask what the reader was doing when they opened it. If more than one answer is plausible, the
   document is serving two readers and should be two documents.

**The fix is nearly always separation, not rewriting.** Most bad documentation is good material
in the wrong container — cut along the mode lines, link across them, and the same words start
working.

Where the separated pieces go, and the folder that makes the four visible: `structure.md`. The
minimum shape of each: `templates.md`.
