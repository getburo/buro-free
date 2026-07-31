# The skeletons — start here, then cut

Contents: the **stamp** · README · how-to · tutorial · reference entry · explanation · ADR ·
runbook · release notes · one-pager · technical design doc · pipeline doc · onboarding path ·
**a worked example** of the seat's produced shape (last section).

Each skeleton is the **minimum shape that satisfies its mode** (`modes.md`). Fill it, then delete
every line this reader does not need — a skeleton is a floor for structure, never a quota for
length. `<…>` is a slot. The stamp line is not optional (gate 7).

**The stamp, used by every document except an ADR:**
```
Owner: <@person or @team> · Verified: <YYYY-MM-DD> against <version / build / commit>
```
Never "reviewed". Never "the team". If it could not be executed, say so here in the open:
`not re-run since <date> — treat steps 4–6 as unverified`.

---

## README — an entrance, not a manual

```markdown
# <name>

<One sentence: what it is and who it is for. No adjectives you cannot defend.>

## Quickstart
<3–6 lines. Install, run, see something work. The first command inside the first screen.>

## Then
- Learn it end to end → docs/tutorials/<…>
- Do a specific thing → docs/how-to/
- Look something up → docs/reference/
- Understand why → docs/explanation/

## Status
<Alpha / stable / maintained-not-developed. Say it plainly; silence reads as "stable".>

Owner: … · Verified: …
```
Kills: a marketing page, a badge wall, four modes at once, a feature list where the quickstart
should be, an apology for the state of the docs.

## How-to — a recipe

```markdown
# <Do the thing, in the reader's words>

<One line: what you will have when this is done. Optional: when NOT to use this path.>

**Before you start**
- [ ] <prerequisite>
- [ ] <prerequisite>

1. <One action.>
   `<command>`
   You should see: <observable result>
   If <the failure that actually happens>: <the exact way out>
2. …

**Done when** <the observable end state>.
**Related:** <the reference page for the flags> · <the explanation for why>

Owner: … · Verified: …
```
Kills: teaching, every flag, a troubleshooting appendix at the bottom instead of recovery at the
step, prose prerequisites.

## Tutorial — a lesson

```markdown
# <Build a <thing>>

By the end you will have <the working artifact>. Takes about <n> minutes.
You need: <the shortest honest list>.

## 1. <First step toward something visible>
<Every command given. No choices.>
You should now see: <…>

## <n>. <Working result>
<What they have. One sentence on what to open next.>

Owner: … · Verified: <date> against <version>, run on a clean machine
```
Kills: options, alternatives, configuration tables, "as an exercise", explanation that belongs in
`explanation/`. A tutorial must work **every time** — verified on a clean checkout or it does not ship.

## Reference entry — a map

```markdown
### <exact name>

<One-line description of what it is / does. Stated, not advised.>

| | |
|---|---|
| Type / signature | <…> |
| Default | <…> |
| Units / range | <…> |
| Raises / errors | <…> |
| Since | <version> |

<Minimal example — illustration, not a lesson.>
```
Kills: rationale, instructions, entries with a different layout from their neighbours (the eye
learns the layout once — break it and scanning dies).

## Explanation — a discussion

```markdown
# Why <the thing> works this way

## The constraint
<What was actually true: scale, deadline, platform, team, cost.>

## The approach, and what it buys
<…>

## What we rejected, and why
<Named alternatives, honestly — including "the better option we could not afford".>

## What this makes hard
<The predictable consequences. This is the part that makes the system predictable.>
```
Kills: steps, a command the reader is expected to run, a rewrite of history that omits the
uncomfortable constraint.

## ADR — written once, never rewritten

```markdown
# <NNNN>. <Decision, in the present imperative: "Use Postgres for the ledger">

Date: <YYYY-MM-DD> · Status: Proposed | Accepted | Superseded by <NNNN>

## Context
<What was true when we decided. Constraints, forces, what we did not know.>

## Decision
<What we will do. One decision per record.>

## Consequences
<What becomes easy, what becomes hard, what we now have to live with.>
```
No stamp — an ADR is not kept fresh, it is superseded. **Never edit an accepted record to match a
later opinion**: add a new one and link both directions. Never let it grow into a design document.

## Runbook — for someone under pressure at 3am

```markdown
# <Symptom, as it appears on the dashboard>

**Impact:** <who is affected, how badly> · **Page:** <who owns this> · **Severity:** <…>

## Confirm it is this
<The one check that distinguishes this from the neighbouring alert.>

## Mitigate first
1. <The action that stops the bleeding, before diagnosis.>

## Diagnose
<Ordered checks, each with what its result means.>

## Roll back
<Exact command, and how to confirm it took effect.>

## Escalate
<Who, when, with what in hand.>

Owner: … · Drilled: <YYYY-MM-DD> against <environment>
```
Kills: theory before mitigation, a step that only the author can perform, an untested rollback.
A runbook that was never drilled is folklore with formatting.

## Release notes / patch notes

```markdown
## <version> — <YYYY-MM-DD>

**Breaking** — <what breaks, and the exact migration step.>
**Added** — <what a user can now do.>
**Fixed** — <the symptom they experienced, not the internal cause.>
**Removed / nerfed** — <named plainly, never buried.>
```
Kills: "bug fixes and improvements", commit subjects pasted in, internals described where the
user-visible effect belongs, a nerf hidden under "balance adjustments".

## One-pager (game or product)

```markdown
# <name> — <one-line pitch>

**Pillars:** <3, no more> · **Platform:** <…> · **Audience:** <…>
**Core loop:** <what the player/user does in the next 30 seconds, then why they do it again.>
**Key mechanic / differentiator:** <the one thing.>
**Look & feel:** <two sentences or one reference image.>
```
One page, hard. Its whole value is being cheap to write and cheap to throw away — content is
`buro:gamedesign`'s, the size and the ruthlessness are this seat's (`gamedev.md`).

## Technical design document

```markdown
# <system> — technical design

**Problem** <what must be true that is not true now> · **Owner** <…> · **Status** <draft/agreed>

## Constraints
## Approach
## Alternatives rejected
## Interfaces & data
## Failure modes and what happens on each
## Rollout, and how it is rolled back
## Open questions <named, with who resolves each>
```
Decisions that outlive this document get extracted into ADRs — a TDD is a plan and may be
superseded wholesale; an ADR is the memory that must survive it.

## Pipeline doc

A **how-to**, strictly (`gamedev.md`) — use the how-to skeleton, plus:
```
Tool versions: <exact> · Where the output must land: <path/naming>
Validated by: <the check that says you did it right>
Verified: <date> by <someone who did not write this doc>, on the current build
```
Pipeline docs rot fastest of anything in a studio. The test is behavioural: someone who did not
write it makes the thing by following it, on today's build.

## Onboarding path

Not a document — an **ordered list of existing documents**, and nothing else:
```markdown
# Your first week

Day 1: <set up> → how-to/<…>   (done when: <observable>)
Day 2: <build the thing end to end> → tutorials/<…>
Day 3: <ship something real> → <the actual small task>, how-to/<…>
Who to ask: <name> for <area> · <name> for <area>
```
The moment it starts *explaining* instead of linking, it has become the second copy of everything it
points at (`structure.md`). Its only test: someone who joined last week, whose mentor has left,
ships something real by Friday.

---

## Worked example — what PRODUCE hands over

The seat does not hand over only the document; it hands over the decisions that produced it, so
each one can be argued with. One real case, in the seat's own shape:

```
Doc: "Deploy a preview environment" · reader: a backend dev who just opened their first PR here.
Mode: HOW-TO (a goal and a broken state, not a curriculum). NOT a tutorial — they are not learning
  the platform; NOT reference — they need this one path, not all flags.
Home: docs/how-to/deploy-a-preview-environment.md — goal-shaped name, one of four mode folders.
  The region list and env-var table are NOT restated here — they live in docs/reference/ and are
  linked; the two sentences of that table already drafted are deleted.
Shape: §how-to above — goal line · prerequisites as a 3-item checklist · 6 numbered steps, each
  one command + what you should see.
Time-to-action: first command in line 4. The paragraph on our CI philosophy is deleted; if it is
  wanted at all it is an EXPLANATION document, linked, not inlined.
Recovery: the three failures that actually happen — expired cloud token, port already bound, stale
  lockfile — each at its own step, with the exact fix.
Proof: run end-to-end against build 2026.07.3 on a clean checkout; step 5 was wrong (flag renamed
  last month) and is corrected here.
Stamp: owner @platform-team · verified 2026-07-24 against 2026.07.3.
```

Read the two lines that do the most work: **Home**, which deletes text that was already written
because the fact lives elsewhere, and **Proof**, which reports that the document was wrong before
it was executed. A handover without those two is a draft claiming to be a delivery.
