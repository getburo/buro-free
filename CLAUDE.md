# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Buro — a **Claude Code plugin**, not an application. There is no build step, no
package manager, no runtime. The deliverable is prose: 57 seats (+ the `buro` dispatcher and
the `selftest` tool) under `skills/`, each a folder with a `SKILL.md` and a `references/`
canon. Editing this repo means editing skill prose, and the only "tests" are the consistency
check and the routing eval.

## Commands

```bash
python3 evals/check-consistency.py          # the test suite — seven checks, exit 1 on failure
python3 evals/check-consistency.py --fix    # regenerate evals/surface.txt from frontmatter, then report
BURO_DONE_GATE=block hooks/buro-done-gate.sh   # exercise the Stop hook in blocking mode
python3 skills/dataviz/scripts/validate_palette.py "#EA630C,#07A4A4,#0280F7"   # a runnable seat method
python3 skills/process/scripts/init_project.py /path/to/project --name X --kind game  # the starter kit
python3 skills/process/scripts/state_check.py /path/to/consuming/project   # the loop's state check
```

Run `check-consistency.py` from the repo root after **any** change to a seat's name, folder,
frontmatter description, or to a roster/count in README/STUDIO-PLAN/ORCHESTRATION. It is also
`buro:selftest` §4. Each of its seven checks exists because that drift already shipped once —
including check 7, which fires when one reference file ends up owned by two seats.

There is no automated runner for the routing eval (`evals/routing-eval.json`): it is a **blind**
check — an agent gets only `evals/surface.txt` (the always-on descriptions) plus one case prompt
and must name the seat, with no access to the expected answer. Results are recorded by hand in
`evals/routing-results.json`.

## Architecture

**Two spines, one dispatcher.** `buro:buro` reads a task and routes it. Buro owns *what* and
*why* (intent, taste, honesty, the artifact); `superpowers` / `feature-dev` own *how to build
safely*; `buro:process` is the switchman between them, and the make-seats critique what comes
back. See `docs/STUDIO-PLAN.md` (architecture, seat template, roadmap) and
`docs/ORCHESTRATION.md` (the seams: handoffs, standard production pipelines).

**Every seat is dual-nature** — DIRECT (method, canon, critique) **and** PRODUCE (emits the
artifact, through its own self-critique gate). A third mode, RECEIVE, lives in the reception
department (`tester` · `audience` · `critic` · `chaos` · `detective`). The studio's motion is
DIRECT → PRODUCE → RECEIVE → revise.

**The one law**, carried by every seat, is what makes the ten departments one studio rather
than 57 tools: *subtract decoration never a capability; quality earned by mastery and delivered
value, never extracted by dark patterns, FOMO, or hype; producing is never an excuse to phone
it in.* Cohesion is a consequence of the shared arbiter, not a separate task — so a new seat
that doesn't carry the law doesn't belong.

**No craft above another.** The ten departments are peers. Where two seats look alike, the
dispatcher's **Seam rules** table (`skills/buro/SKILL.md`) is the tie-breaker (playable space or
invented geography → `level`, real built environment → `spatial`, and so on);
the eval's `seam` field mirrors those pairs.

**Cost discipline.** Only the frontmatter descriptions are always-on (~9.8k tokens); each seat's
full method loads on demand. That is why descriptions are trimmed hard — but they are also the
*only* thing routing sees, so a description must keep its lane, its seam callouts, and its
trigger phrases.

## Adding or renaming a seat

Adding a seat touches more places than it looks. All of these must be updated together, and
`check-consistency.py` is what verifies it:

1. `skills/<seat>/SKILL.md` — frontmatter `name:` must equal the folder name; follow the
   universal template (frontmatter → epigraphs → core chain → lenses → adversarial panel →
   method gates → **PRODUCE** with a self-critique gate → verdict format → discipline &
   boundaries → "slop it kills on sight"), plus `references/canon.md`.
2. Four rosters, each of which must name every seat: the dispatcher's **ten departments** block
   and its **trigger table** (`| The task is… | Seat |` — one row saying *when to open it*, never
   what it carries; that lives in the seat's own always-on description), the README department
   table, and the `docs/STUDIO-PLAN.md` org chart.
3. Seam rules in the dispatcher, if the new seat collides with an existing one.
4. Seat counts in `README.md`, `docs/STUDIO-PLAN.md` and `docs/ORCHESTRATION.md` (`N seats` is
   matched by regex).
5. `evals/surface.txt` — regenerate with `--fix`, never hand-edit.
6. Ideally a routing case + seam pair in `evals/routing-eval.json`.

Every `buro:X` reference in any `.md` outside `docs/research/` must resolve to a real seat
folder (`docs/research/` is exempt: those are dated captures naming seats that were only ever
planned). A reference file has exactly one owning seat — never copy one into a second seat, link
to it. `canon.md` is the one exempt filename, being the per-seat template name.

Two seats have an executable method. `buro:dataviz`: `scripts/validate_palette.py`
implements the colour checks its `references/colour.md` documents, and the seat's PRODUCE gate
refuses an unvalidated palette. If you change a threshold, change it in both places.
`buro:process`: `scripts/state_check.py` validates a **consuming** project's `.buro/` against
`references/cycle.md` — the state ladder, the one-state rule, the acceptance line, the stall
budget, provenance, the absence check, the log. `scripts/init_project.py` scaffolds that same
`.buro/` into any project (the starter kit) and its output must pass `state_check.py` unedited.
Same rule as dataviz: change a threshold in a script and in `cycle.md` together.

## Conventions

- **Commits**: `vX.Y.Z: <what changed>` — the version in the message must match the bumped
  `version` in **both** `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
  A new seat or department is a minor bump; an audit/fix pass is a patch.
- **Language**: framework and explanation in English. **Every NAME is Latin** — the studio
  (`Buro`, never `Бюро`) and every person, studio or bureau credited: `Gorbunov's method`
  (never `метод Бюро Горбунова`), `Lebedev Studio`, Ilyahov, Birman, Tufte. Craft **terms**
  keep their original form with an English gloss (Kovodstvo, info-style / информационный
  стиль, ФФФ/FFF, понимание задачи, внутреннее ≤ внешнее) — a term is knowledge, a name is
  a label, and only the term loses something in translation.
- **The reader is a model, not a person.** Every word here is prompt. A sentence earns its place
  only if it **changes a decision the model would otherwise make wrong** — everything else is
  weight that dilutes what matters. Prefer the imperative, the threshold, the table.
  **Cut on sight:** an epigraph that restates the paragraph under it · motivation ("this is where
  teams fall apart") · the same rule stated twice in one file · a historical anecdote once its rule
  is extracted (keep *"a date is not a gate"*, drop the retelling) · self-praise about the studio ·
  a paraphrase of a neighbouring seat instead of a link to it.
  **Never cut:** a gate, threshold, or checklist item · an output format · a seam rule · the honesty
  law · a concrete before/after (the densest signal a model gets) · a canon credit.
  A seat that grew past ~2500 words is a re-organisation candidate, not a richer seat.
- **Credits**: a discipline's canon is credited inside that seat's `references/canon.md`, not
  in the README.
- `hooks/buro-done-gate.sh` is a Stop hook that reads `.buro/active.md` (a *consuming* project's
  state file, never this repo's) and refuses a premature "done". Advisory by default;
  `BURO_DONE_GATE=block` makes it blocking. It exits silently when there is no state file.
