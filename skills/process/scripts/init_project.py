#!/usr/bin/env python3
"""buro:process — the starter kit. Scaffolds `.buro/` into a project.

    python3 skills/process/scripts/init_project.py ~/path/to/project --name "The Shift"
    python3 skills/process/scripts/init_project.py . --name "X" --kind game

It writes the loop's physical home — state, registers, log, decisions — in the shape
`references/cycle.md` and `SKILL.md` require, then prints the one line to paste into
`/loop`. Nothing else is needed to start: the rules live in the seat, not in the copy.

⛔ It writes a SKELETON, not a plan. The first tick's job is to derive the registers
from the project's own specification (`cycle.md` §2b) — every object, place, mechanic
and state the documents rule, one row each, at `intent`. A register regenerated from
what got built can only ever find what is badly made.

Refuses to touch an existing `.buro/` unless `--force`.
"""

import argparse
import sys
from pathlib import Path

KINDS = {
    "generic": ["product", "design", "build", "content"],
    "game": ["features", "story", "world", "regions", "systems", "assets", "ui"],
    "app": ["product", "flows", "systems", "content", "growth"],
}

REGISTER_HEADER = """# Register — {dept}

> One row per thing this project's **specification** says must exist (`buro:process` →
> `references/cycle.md` §2b). ⛔ **Derived from the documents, never from the product** — a sweep
> over what is built can only find what is badly made; it can never see what was never started.
>
> `source:` — the document or decision that rules the thing must exist. A row without one came from
> looking at the product. `artifact:` — where it lives once it is real; at `built` and above the
> path must exist on disk. `ends-when:` must be able to FAIL. `budget:` is in ticks; `moved:` is the
> tick its number last CHANGED, never the tick someone touched it.
>
> **Ladder:** `intent → specced → built → verified → received` · `parked` (needs a `revive-if`).
> **The one-state rule:** no row may sit more than one state ahead of the lowest in this register,
> and no register more than one ahead of the lowest register.

| id | item | seat | state | acceptance | budget | spent | moved |
|----|------|------|-------|------------|--------|-------|-------|
"""

EXAMPLE_ROW = ("| {id} | *example — delete me.* source: `docs/01 §2` · artifact: `src/x.ts` "
               "| {seat} | intent |  |  |  |\n")

ACTIVE = """# {name} — active state · updated tick t0

> The **live state**, regenerated from the product each tick — never trusted over it.
> Rules are in `buro:process` and its `references/cycle.md`; **this file carries no rules.**

**Tick: t0**

## Concept
<one checkable sentence + its border: "…, NOT …">

## Goals
North-star: <the one number, from buro:analyst>
**Goal-distance: 0 of 0 artifacts exist · 0 verified · 0 at intent**
⛔ Derived from the registers, and it is 0 of 0 because the inventory has not been derived yet.
That is tick 1's job (`cycle.md` §2b) — until then this project cannot say how far it is.

## COMPLIANCE
platforms: <…> · markets: <…> · age rating: <…> · the author's own: <…>
⛔ The ONLY grounds for a BLOCKED verdict. Undeclared = no BLOCKED tier exists.

## Phase / Round
Phase 0 · R1 · Gate: open

## RE-REVIEW QUEUE
## IDEA-ARCHIVE
## Composition
## TABLE
## REFRAMES
"""

LOOP = """# The loop — standing instructions for {name}

> The `/loop` prompt is one line:
> **"Read `.buro/loop.md` and continue the {name} spiral."**

**The rules are NOT here.** They are in `buro:process` (the tick, the phases, the done-call) and its
`references/cycle.md` (the slice, registers, the one-state rule, the stall rule, the absence pass).
⛔ **Copying a rule into this file makes two homes for it, and they will disagree by round five.**
This file carries only what is specific to THIS project.

## Files

| File | Job |
|---|---|
| `loop.md` | this file — what is specific here. Rarely changes |
| `active.md` | live state: concept, goals, goal-distance as a COUNT, phase, round |
| `registers/` | one per department: the bill of materials, derived from the spec |
| `log/` | append-only history, one numbered entry per tick |
| `decisions.md` | ADRs — written once, superseded never edited |

## Every tick

```
0  read active.md + registers
0b ABSENCE: three things the spec rules — does each have an artifact? Missing → a row, at intent
1  STALL check the item in hand: spent vs budget, tick − moved ≥ 2 → take an exit, not another try
2  DIRECT → 3  PRODUCE → 4  BUILD → 5  VERIFY (a number) → 6  RECEIVE
7  write: registers · ONE log entry · decisions if one was made · active.md · the docs pass
```

**Validate before reporting progress:**
```
python3 <plugin>/skills/process/scripts/state_check.py .
```

## Specific to this project

- The specification lives in: `<docs/…>`
- The product lives in: `<src/…>`
- Verified how: `<the command or the instrument>`
- The owner decides: **scope, and what the product IS.** Everything else routes to a seat.
"""

LOG_README = """# Log — history, append-only

One numbered file per tick: `NNNN-slug.md`. **Never edited after it is written** — a wrong line
becomes precedent the next tick reads as settled.

`active.md` is rewritten every tick, so it is not a record. **Without these entries the project has
no memory at all** after one context compaction.

**Per department:** this file is the INDEX — link entry numbers under a heading per department.
⛔ A per-department log that restates entries is two histories that will disagree.

**An entry, minimum:** what slice · which seats · what was done · **what was measured (the number)** ·
what it cost in ticks · what is next and why.
"""

LOG_FIRST = """# 0001 · The loop is installed · tick t0

Slice: none yet.
Did: scaffolded `.buro/` — state, registers, log, decisions.
Measured: nothing. Goal-distance is 0 of 0 because the inventory has not been derived.
Next: tick 1 derives the registers from the specification (`cycle.md` §2b) — every object, place,
mechanic and state the documents rule, one row each at `intent`, each with its `source:`. Only then
sweep the product for defects.
"""

DECISIONS = """# Decisions — append-only, written once

One record per decision that would be expensive to re-litigate. **Superseded, never edited**: a
record edited to match today's opinion destroys the only thing it exists for — the ability to see
that a past decision was reasonable given what was known.

```
## D001 · <decision, present imperative> · <YYYY-MM-DD> · Status: Accepted | Superseded by D0NN
Context   <what was true when we decided; the constraints, what we did not know>
Decision  <what we will do — one decision per record>
Consequences  <what becomes easy, what becomes hard, what we now live with>
```
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a buro loop into a project.")
    ap.add_argument("path", help="project root")
    ap.add_argument("--name", default=None, help="project name (default: folder name)")
    ap.add_argument("--kind", choices=sorted(KINDS), default="generic",
                    help="which register set to lay down (default: generic)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing .buro/")
    a = ap.parse_args()

    root = Path(a.path).expanduser().resolve()
    if not root.is_dir():
        print(f"no such directory: {root}")
        return 1
    buro = root / ".buro"
    if buro.exists() and not a.force:
        print(f"{buro} already exists. Refusing to overwrite it — pass --force if that is what you want.")
        return 1

    name = a.name or root.name
    (buro / "registers").mkdir(parents=True, exist_ok=True)
    (buro / "log").mkdir(parents=True, exist_ok=True)

    (buro / "active.md").write_text(ACTIVE.format(name=name), encoding="utf-8")
    (buro / "loop.md").write_text(LOOP.format(name=name), encoding="utf-8")
    (buro / "decisions.md").write_text(DECISIONS, encoding="utf-8")
    (buro / "log" / "README.md").write_text(LOG_README, encoding="utf-8")
    (buro / "log" / "0001-the-loop-is-installed.md").write_text(LOG_FIRST, encoding="utf-8")

    for dept in KINDS[a.kind]:
        seat = {"regions": "level", "story": "narrative", "world": "worldbuilding",
                "features": "gamedesign", "systems": "roblox-engineering", "ui": "game-ui",
                "assets": "asset-sourcing", "flows": "usability", "growth": "growth",
                "design": "buro", "build": "superpowers", "content": "copy",
                "product": "pm"}.get(dept, "buro")
        body = REGISTER_HEADER.format(dept=dept) + EXAMPLE_ROW.format(
            id=dept[:2].upper() + "01", seat=seat)
        (buro / "registers" / f"{dept}.md").write_text(body, encoding="utf-8")

    plugin = Path(__file__).resolve().parents[3]
    print(f"""Scaffolded {buro}  ({a.kind}: {', '.join(KINDS[a.kind])})

Next, in order:
  1. Fill `active.md` — the concept and its border, the north-star, the COMPLIANCE regime.
     ⛔ Undeclared compliance means no BLOCKED tier exists; every prohibition is TASTE.
  2. Tick 1 derives the registers FROM THE SPECIFICATION, not from what is built
     (buro:process → references/cycle.md §2b). Delete the example rows.
  3. Run the loop with one line:

       /loop Read .buro/loop.md and continue the {name} spiral.

  4. Validate before believing any progress report:

       python3 {plugin}/skills/process/scripts/state_check.py {root}

  Optional: BURO_DONE_GATE=block with the plugin's Stop hook makes a premature "done" impossible.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
