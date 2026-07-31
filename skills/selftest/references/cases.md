# Self-test cases — the core loop (`buro:process`)

The three checks the `selftest` seat runs. Extend this file (not the SKILL.md) to add facets later.

---

## §1 — Machinery markers (deterministic)

Grep `skills/process/SKILL.md` for each phrase. Every one must be present; a missing marker means
the loop lost a limb → FAIL, name it.

| # | Limb | Grep phrase (case-insensitive) |
|---|---|---|
| 1 | Spiral of rounds | `deepen forever, never terminate` |
| 2 | Iteration to convergence | `two clean rounds` |
| 3 | Completeness loop | `empty backlog is NEVER` |
| 4 | Idea-archive | `revive-if` |
| 5 | Composition pass | `emergence at any arity` |
| 6 | Convergence to goals | `measured against the goals` |
| 7 | Done-call to the conductor | `executor NEVER self-declares done` |
| 8 | State-file | `.buro/active.md` |

Suggested one-liner:
```
for p in "deepen forever, never terminate" "two clean rounds" "empty backlog is NEVER" \
  "revive-if" "emergence at any arity" "measured against the goals" \
  "executor NEVER self-declares done" ".buro/active.md"; do
  grep -qiF "$p" skills/process/SKILL.md && echo "OK  $p" || echo "MISSING  $p"
done
```

---

## §2 — Behavioural toy project (agent-driven)

Dispatch ONE agent. Give it the brief below verbatim and have it **play `buro:process`** for ~3
ticks, reading and rewriting state at `<scratchpad>/buro-selftest/.buro/active.md` — **never in the
repo**. The agent reads `skills/process/SKILL.md` as ground truth first.

**Brief (verbatim to the agent):**
> Toy project: a one-screen "coin dash" mini-game.
> Concept: "grab coins before the timer runs out — one more run."
> Goal / north-star: "a first-timer wants a second run within 30 seconds."
> Initial backlog (deliberately thin, to test re-derivation): `[ ] player moves`,
> `[ ] coins spawn`, `[ ] timer`.
> Run the loop as `buro:process`: R1 blockout → R2 deepen → a polish/feel pass → re-review. At each
> tick, READ then REWRITE `.buro/active.md`. **Do not stop when the three backlog items are done.**

**PASS conditions (ALL required — grade strictly, no author-charity):**
1. **Spiral advances** — at least a dev round AND a polish/deepen round are actually run (not one pass).
2. **Re-derive, not quit** — after the three listed items are done, the loop **regenerates work from
   the product's state** (e.g. no juice, no reason for a 2nd run, no fail state, no feedback on a
   coin grab) instead of declaring done on the emptied backlog.
3. **Idea-archive used** — ≥1 pruned idea logged as `cut: <lens> · revive-if: <condition>`.
4. **Composition ≥ arity 2** — at least one interaction tested together (e.g. `coins × timer`) with
   an outcome recorded (promoted / fixed / cut / inert).
5. **Goal-distance tracked** — the state shows a distance to "second run within 30s", and it moves.
6. **No self-declared done** — the executor keeps the loop turning; nothing is stamped
   `Gate: CLOSED (converged)` here, because it hasn't converged.

**FAIL if** it empties the backlog and stops · polishes one thing once and calls it done · never
writes `.buro/active.md` · or self-declares done without the conductor's rubric + two clean rounds.

The agent returns: the final `.buro/active.md` it produced, plus PASS/FAIL on each of the six
conditions with a one-line evidence each.

---

## §3 — Hook cases (deterministic)

Run `hooks/buro-done-gate.sh` in the scratchpad with `CLAUDE_PROJECT_DIR` pointed at each mock.

| # | Setup (`.buro/active.md`) | Env | Expected |
|---|---|---|---|
| a | file absent | — | exit 0, no output |
| b | `Gate: blocked by art` + `Goal-distance: far` | — | reminder on stderr, exit 0 |
| c | `Gate: CLOSED (converged)` + `Goal-distance: 0` | — | exit 0, no output |
| d | same as (b) | `BURO_DONE_GATE=block` | reminder, exit 2 |

Any deviation → FAIL (name the case). This is the same battery the hook shipped with; it is here so
the self-test re-runs it as a regression guard.

---

## §4 — Studio consistency (deterministic)

```
python3 evals/check-consistency.py          # report; exit 1 on any failure
python3 evals/check-consistency.py --fix    # regenerate surface.txt first
```

Seven checks over the on-disk studio. Each exists because the corresponding drift **actually
happened** — this facet is a scar record, not a hypothetical.

| # | Check | Catches | The drift that motivated it |
|---|---|---|---|
| 1 | `frontmatter` | unparseable YAML; `name:` not matching the folder | — (guard) |
| 2 | `surface` | `evals/surface.txt` out of sync with the descriptions it is generated from | `growth` shipped in v0.14.0 with a stale surface row; three more had drifted before that |
| 3 | `eval-targets` | a routing case expecting a seat that doesn't exist or isn't on the surface | `selftest` was missing from the surface while a case routed to `a11y` |
| 4 | `cross-refs` | a `buro:X` reference with no seat behind it | — (guard) |
| 5 | `rosters` | a seat missing from any of the four rosters that must list every seat | `combat-design` was added in v0.13.0 and never reached README or the org chart |
| 6 | `counts` | a claimed "N seats" that no longer matches the folders | README and STUDIO-PLAN claimed 54 when there were 55; ORCHESTRATION still claimed 44 at v0.15.0 |
| 7 | `ref-copies` | the same reference filename owned by two seats — a copy waiting to drift | the dispatcher kept its own copies of four seat references; every one had drifted by v0.15.0 |

The four rosters check 5 reads: the dispatcher's ten-departments paragraph, the dispatcher's
sub-skill map, README's department table, and STUDIO-PLAN's org chart. **A seat the rosters
don't name is a seat the dispatcher will never route to** — this is the check that makes adding
a seat safe.

`docs/research/` is excluded from check 4 on purpose: those are dated captures and may name
seats that were only ever *planned* — the queued camera and systems/economy seats, for
instance. The literal `seat` placeholder is allowlisted, since STUDIO-PLAN uses it to document
the colon syntax itself.

*(Note the constraint this file lives under: check 4 scans it too, so examples of dangling
references are described rather than written out. A check that exempted its own documentation
would be a check with a hole in it.)*

**PASS = exit 0 / all seven green.** Any red is a FAIL; name the check and the specific item.

**Meta-check (run when the script itself changes):** a green that cannot go red is theatre.
Copy the repo to a scratch dir and confirm each check fails on its own fault class — break a
`name:`, edit a description without regenerating, point a routing case at a seat that doesn't
exist, add a dangling seat reference, create an unregistered seat folder. All six must go red,
and the scratch copy must return to green when reverted. Never run this against the real
repository.
