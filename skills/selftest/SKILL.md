---
name: selftest
description: >-
  The self-test seat of Buro — verifies the CORE loop actually runs AND that the studio still
  describes itself truthfully. Four checks: machinery (the loop's parts are present), behaviour
  (drive a toy project a few ticks — does the spiral turn dev->polish, is .buro/active.md kept,
  does it refuse to self-declare done on an emptied backlog), the Stop-gate hook, and studio
  consistency (evals/check-consistency.py — frontmatter, the routing surface in sync with the
  descriptions, eval targets, buro:X cross-refs, the four rosters that must name every seat, and
  the claimed seat count). Invoke explicitly; run consistency after adding or renaming a seat.
  Triggers: selftest, self-test, test the bureau, does buro work, verify buro:process, does the
  development loop run, regression check the loop, consistency check, did I register the new seat,
  is the seat wired into the dispatcher, docs drift, seat count wrong, surface out of sync.
---

# Buro · Self-test — does the core loop actually turn?

> **A method you can't verify is a claim, not a capability.** `buro:process` promises to run
> development and polish in rounds until the product converges to its goals, never quitting from
> the inside. This seat proves it turns — or finds where it stopped.

**Scope: the core loop — `buro:process` — and the studio's self-description.** Two things
everything else rides on. First, that the spiral of rounds actually turns, the state survives, and
"done" is *earned*, not *declared*. Second, that a seat which exists is a seat the dispatcher can
actually reach: **a seat missing from the rosters or the routing surface is invisible no matter how
well it is written.** (Lens-fires, per-seat disciplines and the honesty law are still to come — see
*Scope* at the end.)

Grading follows **`buro:tester` + `buro:audience` discipline: adversarial, reproducible, no
author-charity.** A pass means the behaviour was **observed**, not that the skill *says* it should
happen.

---

## What it checks (four levels: cheap → behavioural)

### 1. Machinery check (deterministic) — are the loop's limbs still there?
Guards against a regression where an edit silently removes a piece of the loop. Confirm
`skills/process/SKILL.md` still carries, by name, each marker in `references/cases.md §1`:
the **spiral of rounds**, **iteration to convergence** (two clean rounds), the **completeness
loop** (an empty backlog is NEVER done), the **idea-archive** (revive-if), the **composition pass**
(arity 2 → N), **convergence measured against the goals**, **the done-call belongs to the
conductor**, and the **state-file** (`.buro/active.md`). Any missing marker is a FAIL — the loop
lost a limb.

### 2. Behavioural check (agent-driven) — does the loop TURN?
The real test. Dispatch **one** agent to *play* `buro:process` on a tiny toy project for ~3 ticks,
writing state to a **scratch** `.buro/active.md` (never in the repo). It must observe the loop
cycling **development → polish → re-review**, round after round. The toy project and the exact PASS
conditions live in `references/cases.md §2`. In short, PASS only if:
- the spiral **advances** through rounds (a dev round *and* a polish/deepen round — not one pass);
- an **emptied initial backlog is re-derived — defects from the product, missing things from the
  SPEC** (`buro:process` → `cycle.md` §2b) — NOT declared done;
- at least one idea is **pruned to the idea-archive** with a `revive-if`;
- the **composition pass runs at arity ≥ 2** and records an outcome;
- **goal-distance is tracked** and only closes on the rubric + two clean rounds;
- the executor **never self-declares done** — the loop keeps turning until the conductor's gate.

A run that empties a list and quits, or polishes one thing once and calls it done, is a **FAIL** —
that is the exact failure this seat exists to catch.

### 3. Hook check (deterministic) — is "done" enforced, not just advised?
Run `hooks/buro-done-gate.sh` against the mock state-files in `references/cases.md §3`: silent with
no state-file; reminds when the converged stamp is absent; silent when stamped; `exit 2` under
`BURO_DONE_GATE=block`. Any deviation is a FAIL — the gate is the difference between a rule that is
*enforced* and one that can be *ignored*.

### 4. Studio consistency (deterministic) — does the studio still describe itself truthfully?
`python3 evals/check-consistency.py`. Seven checks (`references/cases.md §4`): frontmatter, the
routing surface in sync with the descriptions it is generated from, eval targets that exist and are
routable, `buro:X` cross-references that resolve, the **four rosters that must name every seat**,
the claimed seat count, and no reference file copied into two seats. Exit 0 and all-green is the
PASS; `--fix` regenerates `surface.txt`.

This facet is a **scar record** — every check is there because that exact drift already happened
(a seat added but never listed, a description that moved while the surface stayed put, a count that
quietly went stale, four references copied into the dispatcher and then edited in one place only). Run it after adding, renaming, or re-describing any seat: **a seat the rosters
don't name is one the dispatcher will never route to**, however good the file is.

---

## How to run it

1. Read `references/cases.md`.
2. **Machinery** — grep `skills/process/SKILL.md` for each §1 marker; tally, name any missing limb.
3. **Behaviour** — dispatch ONE agent with the §2 toy-project brief; it drives ~3 ticks in a scratch
   dir and returns the observed loop behaviour graded against the PASS conditions. If the agent
   stalls (0 actions), re-dispatch once — that is harness flakiness, not a buro result.
4. **Hook** — run the four §3 hook cases in the scratchpad.
5. **Consistency** — `python3 evals/check-consistency.py`; report the failing check by name.
6. Synthesise the scorecard.

---

## Output (the scorecard)

```
buro self-test — the core loop (buro:process) + studio consistency

1. Machinery    <N/8 markers present · or which limb is missing>
2. Behaviour    <PASS/FAIL · spiral turned dev→polish? refused to self-quit? kept .buro/active.md?>
3. Hook         <N/4 cases · or which gate behaviour broke>
4. Consistency  <N/6 checks · or which check is red and on what item>

Verdict: <Holds — the loop cycles to convergence, "done" is earned, and the studio
           describes itself truthfully
         | Broken — the one thing that stopped the loop turning
         | Drifted — the loop turns but the studio misdescribes itself (name the check)>
— <the single most important finding>
```

Rules:
- Grade on **observed behaviour**, not on what the skill says.
- Sort findings worst-first.
- A green machinery check with a **FAILED behaviour check is still a FAIL** — the limbs are present
  but the loop doesn't turn.

---

## Scope & honesty

- This is a **behaviour test of the on-disk skill**, driven by an agent playing the conductor — not
  a guarantee of how a *live* session auto-triggers (that needs a restart on the installed plugin).
- **Consistency is not routing.** §4 proves a seat is *reachable* — registered in every roster, on
  the routing surface, its references resolving. It does **not** prove the dispatcher picks the
  right seat for a given task; that is `evals/routing-eval.json`, and it only means something run
  **blind**, by someone who has not read the expected answers.
- Still to come: lens-fires, per-seat disciplines, and the honesty law as separate facets in
  `references/cases.md`. This seat is the **standing regression guard** — for the loop everything
  rides on, and now for the self-description that makes any of it findable.

`references/cases.md` — the toy project, the machinery markers, the hook cases, and the six
consistency checks with the drift each one was written for.
