# The cycle — one tick, one slice, and the rule that stops the grind

The tick rule and the state-file are in `SKILL.md`. This file is what a **multi-department build**
(a game, an app with art and story in it) needs on top: registers with states, a budget per item,
the stall rule, and where the dev log lives. It is the how-we-work home for all of it — a project's
`.buro/` holds *state*, never rules.

---

## 0. Two sources of truth — and the QUESTION decides which one you open

> **The design document rules INTENT. The product rules STATE.**
> *What must exist, what it is for, what it must deliver* — the document, always. Code cannot answer
> it; code can only report what somebody once built.
> *What is true right now* — the product, always. The document cannot answer it; it describes what
> was decided, not what shipped.

⛔ **Mixing them is the most expensive habit an agent has**, and it runs one way: opening the code to
work out *what the thing should be*. That is not research — it is **re-deriving the design from
whatever was easiest to implement**, and it ends with a product whose intent is the history of its
own shortcuts. The document then gets "corrected" to match the code, and the last record of what was
wanted is gone.

**The rule of thumb, and it is mechanical:**

| The question | Open |
|---|---|
| what must exist · what is this for · what must it deliver · is this in scope | **the design document** |
| does it exist · does it behave · how many · how fast · does it still hold | **the product** |
| the two disagree | **a FINDING, not a tie-break** — see below |

**When the code and the document disagree, the DEFAULT is that the code is wrong.** Not because
documents are more reliable — they rot — but because the document is the only place intent is
recorded, and code is the only place it can be silently replaced. Three outcomes, and each is a
different row: *the code drifted* (fix the code) · *the decision changed and nobody updated the
document* (update it, and say who ruled it — `§4c`) · *the document was always wrong* (a decision, so
it is ruled and recorded, never quietly overwritten).

⚠ **"Where this disagrees with the product, the product wins" is a rule about the BACKLOG**, and it
is right there: a list of open work regenerated from a stale guess is worse than one read off the
real thing. **It is not a rule about the design.** Generalising it is how a project's centre of
gravity moves from what it wants to be into what it happens to be — measured in one project as a
loop that read code for seven ticks straight while two whole design documents had never been opened
at all.

## 1. The unit of a tick is a SLICE, never a department

A loop that runs "today narrative, tomorrow level" produces, at project scale, exactly the failure
`buro:level` documents at area scale: two finished corners and a lot of ground. One **vertical
slice** — one thing a player can actually do — advances through the departments it touches, and
every register moves with it.

**Fan or sequential, decided by width, not by mood:**
- **≤ 3 departments** in the slice → run the seats **sequentially in one context**. Cheaper, and
  cohesion is free because one reader sees all of it.
- **≥ 4 departments** → **fan**: each department produces in parallel, and their verdicts are
  **collided** at step 6, not merged politely. Whoever seats the fan owns the stitching.

## 2. Registers — state per department

One file per department under `.buro/registers/`, each a table. This is the project-scale version of
`buro:level`'s region manifest, and it exists for the same reason: **a flat backlog cannot show that
one department has run three states ahead of another.**

```
| id | item | seat | state | acceptance — the number/observation that ENDS it | budget | spent | moved |
|----|------|------|-------|--------------------------------------------------|--------|-------|-------|
| S3 | BMX handling | roblox-engineering | built | clears a 3-stud ledge ≥9/10 at 30fps on mid phone | 3 | 5 | t11 |
```

- `budget` — ticks this item may consume, declared when it reaches `specced`.
- `spent` — ticks it has consumed.
- `moved` — the tick when its acceptance number last **changed**. Not when someone worked on it.

**Two fields make a row accountable, written inline in the item cell:**
- **`source:`** — the document, section or decision that **rules this thing must exist**
  (`docs/04 §the manhole is the exit`). A row with no source came from looking at the product.
- **`artifact:`** — where it lives once it is real (`world/build_manhole.luau`). At `built` and above
  the path must exist on disk; **a state that claims `built` with no artifact is the lie this whole
  file exists to catch.**

**The state ladder:** `intent → specced → built → verified → received`, plus `parked`.

| State | Means |
|---|---|
| `intent` | named, one line of purpose, nothing designed |
| `specced` | its seat designed it; **acceptance line and budget written** |
| `built` | it exists in the product |
| `verified` | measured against the acceptance line; the number is recorded |
| `received` | survived a reception round (tester → audience → critic) |
| `parked` | deliberately not now, with a `revive-if` condition |

**The one-state rule.** Inside a register, `front − floor ≤ 1` (ignoring `parked`). Across registers,
`max(front) − min(front) ≤ 1`. Nothing may be polished to `received` while a department it ships
with has items at `intent`. This is the single rule that prevents a beautiful, unplayable corner.

## 2b. The inventory comes from the SPEC, not from the product

> **Regenerating the backlog from the product can only ever find what is badly made. It cannot find
> what was never started.**

The state file's rule — *the backlog is an output of the sweep, regenerated from the product* — is
right for defects and **exactly backwards for completeness**. A sweep over the world sees the world.
The thing that was ruled in a document and never built casts no shadow there: it fails no audit,
because audits read geometry and code that exist, and **absence is never red**.

So the registers are **derived from the specification first**, once, and only then reconciled with
the product:

1. **Enumerate what the documents rule must exist** — every named object, place, mechanic, state and
   transition: *the exit you open · the vendor yard · the way onto the level · the roles · the
   eight-minute session*. One register row each, at `intent`, with its `source:`.
2. **Reconcile with the product.** A row whose artifact exists moves up the ladder. A row with no
   artifact **stays at `intent` and is now visible** — that is the whole point.
3. **Only then** sweep the product for defects and add rows for what is built badly.

**Measured case (the failure this exists to prevent):** a project's design document ruled *"the
manhole is the exit"*, in 33 places across its docs. Zero builders built one; no interaction to open
one existed anywhere in the source. Every audit was green, the backlog was "consumed", and the loop
spent twenty ticks polishing luminance and seams — while the game's exit did not exist and a session
lasted 33 seconds against a documented eight minutes. **Nothing in the loop could see it, because
everything in the loop looked at what was there.**

## 2c. The absence pass — a required step, not a sweep to remember

Every tick, before picking work:

> **Name three things the documents rule and check whether each has an artifact.** Rotate through
> the spec so the whole of it is covered every N ticks; log which three.

And once per round, mechanically, over the whole spec: **for every noun and mechanic the documents
rule, does a builder, a service or a file implement it?** Anything living only in prose is a
register row at `intent` — not a finding to mention, a row to carry.

**Absence outranks defect.** A missing mechanic beats a badly-made one in the order, always: the
polish of a thing that exists cannot be worth more than the existence of a thing the design requires.

## 2d. Goal-distance is a COUNT

⛔ **`Goal-distance: maximal` is not a distance.** An adjective cannot move, so a conductor writing
one cannot tell advance from polish — and polish is always available, which is why it wins.

```
Goal-distance: 41 of 68 required artifacts exist · 22 verified · 9 at intent with no artifact
               (the exit · the vendor yard · the way in · …)
```

Derived from the registers, so it moves only when a row moves. **A goal-distance that has not changed
for three ticks is itself the finding** — and if it cannot be computed, the inventory does not exist
and step 2b was skipped.

## 2e. Order by the SIZE OF THE GAP, not by the size of the task

A per-item score — pain × fit × timing × worth × execution — is computed **one row at a time**, and
that arithmetic systematically promotes the small and certain over the large and murky. The result
is a queue that polishes while the product's biggest number stays where it was.

> **The row with the largest measured distance to its bar goes first** — until it is closed, or
> deferred out loud with a reason and a date.

**Measured, the case this rule comes from:** a game whose session ran **33 seconds against a
documented eight minutes** — 93% short, the largest gap on the board — while twenty ticks went to
luminance ceilings and prop kits, each a few per cent from its own bar. Every one of those items was
real. None of them was the biggest.

**How to compare gaps across different units:** as a **fraction of the bar**, not in raw units.
93% short beats 4% off. If a row has no bar, it cannot be ranked — that is the acceptance line
missing (§3), not a reason to rank it by feel.

⚠ **Instruments are the cheapest thing to build and the easiest to mistake for progress.** A gate
makes a failure visible; it does not close a gap. When the top of the queue by magnitude is a design
problem, building another checker is avoidance with a clean conscience.

## 2f. Before picking work: could these be ONE cause?

The sweep in the other direction already exists — *cut a mechanism, name what stood on it*. This is
its mirror, and nothing was running it:

> **When several open rows could share one upstream cause, the cause is the work.** Not the symptoms,
> and not the loudest of them.

Ask it as arithmetic: list the open rows, and for each ask *what would have to be true for this to
be a child of something else?* Rows that keep pointing at the same missing thing are one item.

**Measured:** four separately-tracked rows — *"the exit you open does not exist"*, *"a job runs 33 s
not 8 min"*, *"the map has one route, not three"*, *"decision spacing 0 of 8, the bar costs thirteen
exits"* — were one node: **where the player is forced to go, and how far.** They sat in three
different files and were worked as four.

⛔ **Clustering is `buro:detective`'s craft, not a guess made while ranking.** When two or more rows
plausibly share a cause, open that seat and let it bisect — a shared cause named by intuition is a
new belief, not a finding.

## 2g. Is this finding already the documented design?

**Measured, twice in one project:** *"two findings turned out to be history, not defects"* and *"an
audit that existed was treated as one that didn't."* Work was queued to fix behaviour the documents
already ruled, with the reason written down — and one of those reasons explicitly said *cutting this
deletes what the earlier measurement was taken with.*

> **Before a finding becomes work, read what the documents say about it.** If it is already ruled,
> the finding is against the DOCUMENT — either it is out of date, or the finding is.

Three outcomes, and each is a different row: **the design changed and the doc is stale** (fix the
doc) · **the finding is real and the doc is wrong** (re-open the decision, `§4c`) · **the doc is
right and the finding is the loop re-litigating a settled call** (close it, and say which document
settled it). ⚠ **The third is the expensive one**, because it looks exactly like diligence.

## 3. The acceptance line — no number, no build

**An item may not leave `specced` without a line that can fail.** "Make the bike feel good" cannot
fail, so work on it never ends; that is not a discipline problem, it is a specification problem.

- Good: *"corners at 40 studs/s without flipping in ≥9 of 10 runs"* · *"first loot pickup inside 45s
  for a new player in 4 of 5 sessions"* · *"server step stays under 4 ms with 12 players and 300 props"*.
- Not a line: "feels responsive", "looks right", "is fun", "is optimised".
- **Physics and feel are the canonical grinders** because they invite unfalsifiable iteration. If the
  only instrument is the author's hand on the keyboard, the item is not measurable — either build the
  measurement (a scripted test, a counted trial, a recorded number: `buro:roblox-engineering`
  §verification, arithmetic before screenshot) or `park` it. Iterating on an unmeasured feel is the
  most expensive way to spend a loop.

## 4. The STALL rule — the grind is a finding, not diligence

At the top of every tick, for the item in hand:

> **STALL** when `spent ≥ budget`, **or** when two ticks have passed with no change in the acceptance
> number (`tick − moved ≥ 2`).

A stall is **not** a reason to keep going, and never a reason to raise the effort. It is a finding
with four exits, taken **in this order** and stated out loud:

1. **Adopt the standing solution.** The prior-art gate (`SKILL.md` §RECON) already says name the
   field's standard before inventing — a stall means that gate was skipped or its answer refused.
   Take the engine's stock behaviour, the documented pattern, the asset that already works.
2. **Cut to the honest minimum** that unblocks the slice — ФФФ: the date is fixed, the scope flexes.
   A bike that drives adequately unblocks the level; the *feel* is a later round at a higher bar, and
   it goes to the `RE-REVIEW QUEUE` so the cut is visible rather than forgotten.
3. **Park it** with a `revive-if` condition into `## IDEA-ARCHIVE`, and route the slice around it.
4. **Escalate to the owner** — last, never bare. An escalation carries **the acceptance number that
   failed, the three exits above and why each was refused**. "Physics is hard" is not an escalation.

**Two consecutive stalls on items from the same register** is a different finding: the department is
out of step with the rest, and the conductor moves the loop to the lowest register instead.

## 4b. The spec contract — what a decision must contain before anyone builds

> **An unspecified property is not an open property. It is a decision with no author**, taken by
> whoever holds the mouse, usually by copying the last one.

> **A spec is complete when the builder can execute it without inventing anything that affects the
> product.** Not "without questions" — without *consequential* invention.

**The test, on every blank:** say *"so the builder will decide it"* out loud. Tolerable for the tint
of a doorframe; never for how many doors there are. If it makes you flinch, the field is required.

**The question pass — before producing, not after.** List every decision this spec hands to someone
else; that list *is* the questions, and it is normally long. **Most are not the owner's:**

| The question is about | Goes to |
|---|---|
| rules of play / the mechanic | `buro:gamedesign` |
| what it means, whose it is | `buro:narrative` |
| how it looks | `buro:art-director` |
| can it be built, at what cost | the engineering seat |
| does it fit the date | `buro:producer` |
| **what the product IS — scope, a new system, a new rule** | **the owner. Only these** |

**An unanswered question never becomes a silent guess.** It ships in the verdict as
**`[ASSUMED] <field> = <default> · costs <X> to change later`**. A default that is written down can be
argued with; one that was merely taken is indistinguishable from a decision and will be quoted as one.

⛔ **The builder refuses an incomplete spec** and returns it as a finding naming the field. A builder
that guesses is a second, unaccountable designer, and the first will spend the next round arguing
with its output.

## 4c. A changed decision re-opens its children

Every built thing records **the decision it was built under**. Then:

> **A decision that changes re-opens everything built under it** — listed by name, in the same move
> that changes the decision. Not "consider re-opening".

**Patch or re-derive — three tests, in order:**
1. Does it change **what the thing must let people do**? → re-derive. Patching around a changed
   contract is what produces a product with one real path and several decorative ones.
2. Does it change **what a part is FOR**? → that part is rebuilt, not adjusted.
3. Does it change only **how it looks or is named**? → patch.

**The sunk artifact is not an argument.** What is already built is a cost already paid; keeping it
*because it exists* is the same error as keeping a feature because it was hard to write. State the
rebuild cost in units and ticks and let `buro:producer` cut — that is a scope call.

⚠ **Citations are how this is possible at all.** If a builder names no decision, nothing can list its
children. A citation that points at a moved or deleted address is worse than none: it does not read
as broken, it resolves to something else.

## 5. Three artifacts, three homes — never a fourth copy

| Artifact | Home | Discipline |
|---|---|---|
| **State** — what is true now | `.buro/active.md` + `registers/` | rewritten every tick |
| **History** — what happened and why | `.buro/log/NNNN-slug.md` | **append-only**, numbered, dated |
| **Decision** — why we chose this | `.buro/decisions.md` (ADR) | written once; **superseded, never edited** |

The state file is rewritten each tick, so **it is not a record** — without the log, the project cannot
answer "what did level do in R3 and why", and after one compaction nobody can. A log entry is written
**by the tick that did the work**, not reconstructed later.

**Per-department view is an INDEX, not a second log.** `log/README.md` lists departments and links the
entry numbers; the entries stay chronological and single-homed (`buro:docs` §one home per fact). A
department log that restates entries is two histories that will disagree by round five.

**A log entry, minimum:**
```markdown
# 0042 · Level — the drained canal, seam pass · 2026-07-27 · tick t42
Slice: crossing from Residential to the canal.
Seats: level (fan: level, art-director, roblox-engineering).
Did: gradient band + ridge threshold on the 3↔4 boundary; region 4 stays `blocked` on purpose.
Measured: landmark visible at 91% of 40 sampled points (target ≥90) · crossing 22 s at run speed.
Cost: 2 ticks of 2 budgeted.
Next: region 7 encounters — it is the floor of the register.
```

## 6. The tick, in full

```
0 READ    active.md + registers. Question audit (SKILL.md gate 0).
0b ABSENCE three things the spec rules — does each have an artifact? Missing → a row, at intent.
0c CLUSTER could several open rows be one cause? Then the cause is the work (§2f, buro:detective).
0d PICK    absence > defect; then the LARGEST GAP as a fraction of its bar (§2e); then the lowest
          register front, on buro:producer's critical path — never what was last complained about.
1 STALL   check the item in hand: spent vs budget, tick − moved. Stalled → take an exit, log it, done.
2 DIRECT  3–5 seats, sequential if the slice touches ≤3 departments, fan if ≥4.
3 PRODUCE artifacts through each seat's own self-critique gate.
4 BUILD   superpowers / feature-dev + the engine seat. TDD where it is code.
5 VERIFY  the acceptance number, measured. A tick that produced no number produced no progress.
6 RECEIVE tester → audience → critic → chaos, on the slice. Findings become register rows.
7 WRITE   registers (states, spent, moved) · one log entry · decisions if one was made · active.md
          (round, goal-distance, archive) · the docs pass: what did this change make untrue?
```

**Step 7's docs pass is not optional.** Every tick asks which document now lies — the GDD, the TDD,
a pipeline doc — and either fixes it or stamps it stale in the open (`buro:docs`: freshness is
evidence, dated and owned).

## 7. Autonomy and the budget

The loop never terminates from inside (`SKILL.md` §the done-call). Running it unattended therefore
needs a **budget**, not an ending:

- **A tick budget** — N ticks, then report and wait, whatever the state.
- **Hard stops that beat the budget:** an unresolved question that changes the concept · a
  COMPLIANCE `BLOCKED` finding · a **third** stall in a row · a register that cannot advance without
  the owner (an asset, an account, a decision only they can make).
- **`BURO_DONE_GATE=block`** (the Stop hook) keeps a premature "done" from ending the run; the budget
  keeps an endless one from burning the day. Both, together.

## 8. The starter kit — one command, any product

```bash
python3 skills/process/scripts/init_project.py ~/path/to/project --name "X" --kind game
```

`--kind`: `generic` (product · design · build · content) · `game` (features · story · world ·
regions · systems · assets · ui) · `app` (product · flows · systems · content · growth). It writes:

```
.buro/
  loop.md          what is specific to THIS project + the one-line /loop instruction
  active.md        live state — schema in SKILL.md §the state-file, with Tick and a COUNTED
                   goal-distance
  registers/       one per department — THE BILL OF MATERIALS (§2b)
  log/             README.md (the department index) + NNNN-slug.md entries, append-only
  decisions.md     ADRs, append-only, superseded never edited
```

⛔ **The registers ARE the inventory. There is no separate inventory file** — a row already carries
`source:` (the document that rules the thing) and `artifact:` (where it lives). A second file
listing the same things is the duplicated fact, and it will disagree by round five.

⛔ **`loop.md` carries no rules** — they are in this seat, and a copy drifts. It holds only what is
specific: where the spec lives, where the product lives, how this project verifies.

Validate mechanically before trusting any report about it:

```bash
python3 skills/process/scripts/state_check.py /path/to/project
python3 skills/process/scripts/state_check.py /path/to/project --code=src,world   # + term check
```

`--code` warns when a row's artifact exists but nothing in the code mentions the thing — a row
naming the wrong file. **The limit of its green:** it proves every row has a source, a real
artifact, a falsifiable acceptance line, a live budget and a department in step. It does **not**
prove the thing works, and it is blind to a row nobody wrote — which is why §2b and §2c are a seat's
job every round, not a script's.

It fails on a register row with no state, an acceptance line missing at `specced`+, a broken
one-state rule, a stalled item nobody exited, and a tick that left no log entry. **An unvalidated
"the loop is going well" is the project-scale version of the screenshot of the good corner.**
