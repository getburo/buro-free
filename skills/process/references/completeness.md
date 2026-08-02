# The completeness loop — concentric top-down passes

Depth beyond `SKILL.md`'s summary. Open this when running the loop for a multi-round, multi-
department build (a game, an app with content that grows past its own spec) — general phase/gate
sequencing lives in `SKILL.md` itself, not here.

> **An empty backlog is not a finished product.** The backlog and the GDD are a *guess made at the
> start*; clearing them means the guess is exhausted, not that the product is complete.

Re-derive the work from the *product's actual state*, never from an emptied list.

**Concentric passes (general → detail, repeated):** each pass **re-reads the WHOLE product from the
top**. Pass 1 is coarsest (does every major piece exist at all?); each later pass goes one level
deeper — is each piece *filled*? *good*? *fun*? *polished*?

**The GDD is a seed, not a ceiling.** A number in the doc ("5 districts", "10 weapons") is a floor,
not a cap. A district that is **empty or thin is NOT "done, as specified" — it is a gap to FILL**.
The design is expected to grow past the doc where growth serves the concept, and the doc gets
updated as the product teaches you what it needs.

**Each pass runs this loop — against the concept, not the list:**
```
1. Re-scan the WHOLE product vs the concept + the completeness rubric — top to bottom.
2. Re-review every "done" — actually done to the bar, or a STUB / EMPTY / off-concept?
                            Empty-but-listed is NOT done → re-open it.
3. Gap-hunt — what's MISSING that a complete product needs but nobody put on the list?
                            (empty zones, thin mid/late game, no failure states, no reason to return.)
4. Fill & fun — for every thin/empty piece: what gives the player more to DO? Add it
                            (via buro:gamedesign / level / narrative / live-ops).
5. Prune — what's off-concept or didn't work? Cut it (subtract, don't amputate) → filed in the
                            IDEA-ARCHIVE, never deleted.
6. Regenerate the backlog from 1–5, and loop. The list is an OUTPUT of the sweep.
```

**Exit ONLY on real convergence:** the completeness rubric is green, **and** two full top-down
passes in a row surface nothing worth adding/filling/fixing/cutting, **and** a fresh player with no
context experiences a whole product, not a shell. If the list is empty but the rubric isn't green,
**the list was wrong — regenerate it**.

**The completeness rubric (definition-of-done for the PRODUCT):**
- the core loop is fun with rewards stripped (the toy test — `buro:gamedesign`);
- real content **volume** — early / mid / late game each exist and are filled, not stubbed;
- progression doesn't run out; there's a reason to keep playing and a reason to **return**;
- every system, zone, and level is **filled**, not an empty shell that "exists per the doc";
- onboarding teaches by playing; failure states exist; the endgame / loop closes;
- no gap a real player hits in the first hour; the polish pass is done.

## The spiral of rounds

Development is a spiral of named rounds — each a full top-down pass, each **deeper** than the last,
then spiralling back to re-deepen everything at the new bar. A canonical spiral for a game (a
*template* — rename per project, keep the shape):

| Round | Goal (each pass goes DEEPER) | Owner seats |
|---|---|---|
| **R1 Blockout** | greybox skeleton — every district/system roughed in (the first ~2%) | level, gamedesign, roblox-engineering |
| **R2 Deepen** | real content — quests, behaviours, each zone's gameplay identity, the whole map FILLED | gamedesign, level, roblox-engineering |
| **R3 Live world** | the multiplayer/social layer actually lived-in (presence, shared events) | gamedesign, live-ops, retention |
| **R4 Feel** | <100ms juice, camera, sound, the moment-to-moment | motion, sound, gamedesign |
| **R5 Assets** | greybox → real art, one-world coherence | asset-sourcing, art-director, concept |
| **R6 Critique / converge** | the adversarial panel + a real playtest → converge | pm/process, experiment, usability |
| **→ back to R2** | re-open zones/quests/systems at the higher bar | (repeat, forever) |

## Re-review discipline — nothing stays done forever

- Every completed item is **stamped with the round it was done in** — `(done R2)`.
- When the spiral returns to that layer the item is **mandatorily re-opened** as
  `[~] re-review @ higher bar` and **re-run through its seat** — a full re-discussion, not
  assumed-good. Core loop, zones, and quests especially.
- The backlog keeps a **`## RE-REVIEW QUEUE`**; `buro:pm` / `buro:process` sets the cadence.

## The idea-archive — pruned is logged, never deleted

Every rejected or pruned element goes to a kept **idea-archive** with two lines: **why it was cut**
(which lens killed it) and its **revival condition** — the one thing that would have to change for
it to work. The archive is a **source the generate/deepen step reads**: a later round, at a higher
bar or beside a new neighbouring element, can revive an idea whose condition is now met. This is
how the process compounds instead of forgetting.

- **Revival is re-entry, not reinstatement** — a revived idea returns as a *candidate* and re-earns
  its place through critique.
- **Distinct from the RE-REVIEW QUEUE:** that queue re-opens *done* items at a higher bar; the
  archive re-opens *rejected* ones when their condition is met.
- It is a real kept artifact, not a mental note, so an idea from R2 is still legible at R9.

## The done-call belongs to the conductor

The agent doing the work is **forbidden to declare the project done.** The tick rule:

```
each tick:
  → READ .buro/active.md — the concept, the round, the backlog, the queue, the goal-distance
  → RE-READ THE REQUEST IN THE ASKER'S OWN WORDS, quoted. Read the last answer back into that
    sentence: does it survive its number, its subject, its scope? If a reframe happened and was
    never said out loud, that is finding #1 — before any new work.
  → ask buro:pm / buro:process for the CURRENT round's top slice (or read the backlog it ordered)
  → BEFORE inventing: name the standing solution in the field → adopt | adapt | deviate, out loud
  → route that design to its seat — or SEAT A TABLE (riff) where one lens won't birth it →
    produce the verdict → flag anything unverified → commit → next tick
  → a lesson about HOW WE WORK goes to the studio (the seat / this skill), never to active.md
  → every so often, buro:process re-opens a completed item for mandatory re-review
  → WRITE .buro/active.md — advance the round, regenerate the backlog: DEFECTS from the product,
    MISSING THINGS from the spec (references/cycle.md §2b — a sweep over the world cannot see what
    was never started), update
    goal-distance, log any prune to the IDEA-ARCHIVE and any interaction to Composition
when a round's pillars are all at-bar → buro:process declares the NEXT round / the next spiral.
the loop NEVER terminates from inside; "done" is buro:process's call, made ONLY on the completeness
rubric + two clean rounds + a fresh player — NEVER because the executor ran out of tasks.
```

**PRODUCE (for a real project):** a project-specific **spiral dev-cycle plan** (the concept + its
border, the named rounds, the owner-seats per round), a **backlog with a `## RE-REVIEW QUEUE`**, a
kept **`## IDEA-ARCHIVE`**, and the **loop/tick prompt** — all living in one `.buro/active.md`.
Naming the biggest missing thing as a **new pillar** is part of the deepen pass.
