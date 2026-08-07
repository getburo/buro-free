#!/usr/bin/env python3
"""buro:process — the loop's state check.

Validates a CONSUMING project's .buro/ directory (never this repo's). It is the
mechanical half of `references/cycle.md`: a report that the loop is going well is
worth nothing until these counts pass.

    python3 skills/process/scripts/state_check.py /path/to/project

Exit 0 = every check green. Exit 1 = at least one FAIL (warnings do not fail).
"""

import re
import sys
from pathlib import Path

LADDER = ["intent", "specced", "built", "verified", "received"]
RANK = {s: i for i, s in enumerate(LADDER)}
PARKED = "parked"

# An acceptance line that cannot fail is not an acceptance line (cycle.md §3).
UNFALSIFIABLE = re.compile(
    r"\b(feels?|feel good|looks? (right|good|nice)|is fun|fun\b|polish(ed)?|"
    r"nice|better|smooth(er)?|optimi[sz]ed|responsive|immersive)\b", re.I)

REQUIRED_HEADINGS = ["Concept", "Goals", "COMPLIANCE", "Phase / Round"]

# Tier 0 of the priority ladder (cycle.md §2a): a product that does not run has
# exactly one item on its board. These words in a `Runs:` line mean it is open.
BROKEN = re.compile(r"\b(no|not|never|broken|crash(es|ed|ing)?|fails?|failed|"
                    r"won'?t start|does ?n[o']?t (start|load|run|launch)|unplayable|"
                    r"cannot be played|black screen|hangs?|freezes?)\b", re.I)

# A cut is executed, never annotated (cycle.md §2h). A row that says the thing is
# gone while still carrying a ladder state keeps being counted, ranked and rebuilt.
CUT_ANNOTATION = re.compile(
    r"(no longer (exists|exist|in the game|in the design|used|planned|needed)|"
    r"\b(cut|removed|dropped|scrapped) from (the )?(game|scope|design|product|spec)\b|"
    r"\bwas (cut|removed|scrapped|deleted)\b|"
    r"\b(obsolete|deprecated|superseded|descoped|de-scoped)\b|"
    r"\bdoes ?n[o']?t exist any ?more\b)", re.I)

fails: list[str] = []
warns: list[str] = []
inventory: list[str] = []      # every live row's state, for the goal-distance count


def fail(check: str, msg: str) -> None:
    fails.append(f"  FAIL  {check:<12} {msg}")


def warn(check: str, msg: str) -> None:
    warns.append(f"  warn  {check:<12} {msg}")


def parse_tables(text: str):
    """Yield dict rows from every markdown table that has an 'id' column."""
    rows = []
    header, idx = None, {}
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if header is None:
            if any(c.lower() == "id" for c in cells):
                header = [c.lower() for c in cells]
                idx = {name: i for i, name in enumerate(header)}
            continue
        if set("".join(cells)) <= set("-: "):   # the |---|---| separator
            continue
        row = {name: (cells[i] if i < len(cells) else "") for name, i in idx.items()}
        if row.get("id"):
            rows.append(row)
    return rows


def mentions(root: Path, term: str, dirs: list[str]) -> int:
    """How many files under `dirs` mention the term at all. -1 if grep is unavailable."""
    import subprocess
    try:
        r = subprocess.run(["grep", "-rliI", "--", term, *dirs],
                           cwd=root, capture_output=True, text=True)
    except (FileNotFoundError, OSError):
        return -1
    return len([l for l in r.stdout.splitlines() if l.strip()])


def dangling(root: Path, source: str) -> list[str]:
    """Does a row's `source:` still resolve? (cycle.md §4d)

    A source reads `docs/04-world.md §the manhole is the exit`. Only path-shaped
    citations are checked — a source naming a decision ('ADR-7') or a meeting is
    not resolvable here and is left alone. Missing file or missing §section = the
    design changed in the spec and this row was never re-stated.
    """
    cite = source.strip().strip("*`")
    doc, _, anchor = cite.partition("§")
    doc = doc.strip().strip("*`").rstrip(",;")
    if not doc or not re.search(r"[/\\]|\.(md|txt|rst|adoc)$", doc, re.I):
        return []
    path = root / doc
    if not path.is_file():
        return [f"source: `{doc}` does not exist"]
    anchor = re.sub(r"\s+", " ", anchor.strip().strip("*`").rstrip(".,;")).lower()
    if not anchor:
        return []
    text = re.sub(r"\s+", " ", path.read_text(encoding="utf-8", errors="replace")).lower()
    return [] if anchor in text else [f"source: `{doc}` no longer contains '§{anchor}'"]


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    code_dirs: list[str] = []
    for a in sys.argv[1:]:
        if a.startswith("--code="):
            code_dirs = [d for d in a.split("=", 1)[1].split(",") if d]
    root = Path(argv[0] if argv else ".").expanduser().resolve()
    buro = root / ".buro"
    print(f"buro:process — state check · {root}\n")

    if not buro.is_dir():
        print(f"  FAIL  layout       no .buro/ in {root} — the loop has no state file")
        return 1

    # ---- layout -----------------------------------------------------------
    active = buro / "active.md"
    registers_dir = buro / "registers"
    log_dir = buro / "log"
    for p, what in [(active, "active.md"), (buro / "loop.md", "loop.md"),
                    (buro / "decisions.md", "decisions.md")]:
        if not p.is_file():
            fail("layout", f"missing .buro/{what}")
    register_files = sorted(registers_dir.glob("*.md")) if registers_dir.is_dir() else []
    if not register_files:
        fail("layout", "no .buro/registers/*.md — a flat backlog cannot show a department out of step")
    log_entries = sorted(p for p in log_dir.glob("*.md") if p.name.lower() != "readme.md") \
        if log_dir.is_dir() else []
    if not log_entries:
        fail("layout", "no .buro/log/NNNN-*.md — the state file is rewritten each tick, so without "
                       "the log this project has no history at all")

    # ---- active.md --------------------------------------------------------
    tick = None
    if active.is_file():
        text = active.read_text(encoding="utf-8", errors="replace")
        # `#{2,3}` and not `#{1,3}`: the H1 is the project title, so under re.I a project named
        # `Concepta` or `Goalpost` satisfied its own heading check on the title line. The trailing
        # \b stops `## Goalsetting` from passing as `## Goals`.
        for h in REQUIRED_HEADINGS:
            if not re.search(rf"^#{{2,3}}\s*{re.escape(h)}\b", text, re.I | re.M):
                fail("active", f"no '## {h}' section")
        m = re.search(r"\bTick:\s*t?(\d+)", text, re.I)
        if not m:
            fail("active", "no 'Tick: t<N>' counter — stalls are measured in ticks")
        else:
            tick = int(m.group(1))
        gd = re.search(r"Goal-distance:\s*([^\n]*)", text, re.I)
        if not gd:
            fail("active", "no 'Goal-distance:' line")
        elif not re.search(r"\d", gd.group(1)):
            fail("active", f"Goal-distance '{gd.group(1).strip()[:40]}' is an adjective, not a "
                           f"count — an adjective cannot move, so it cannot tell advance from "
                           f"polish. Write 'K of N artifacts exist · L verified'")
        if re.search(r"Gate:[^|\n]*CLOSED\s*\(converged\)", text, re.I) and \
           not re.search(r"Goal-distance:\s*0(\D|$)", text, re.I):
            fail("active", "Gate CLOSED but Goal-distance is not 0 — the done-gate contradicts itself")

        # ---- tier 0: does the thing RUN, and was that measured recently? (§2a) ----
        runs = re.search(r"\bRuns:\s*([^\n]*)", text, re.I)
        if not runs:
            fail("liveness", "no 'Runs:' line — tier 0 of the priority ladder is whether the "
                             "product starts and survives one loop end to end. Unmeasured, the "
                             "ordering rules below it rank an unbuilt cosmetic at 100% short of "
                             "its bar and fog a game nobody can start")
        else:
            claim = runs.group(1).strip()
            mv = re.search(r"\bt(\d+)\b", claim)
            if not mv:
                fail("liveness", f"Runs: '{claim[:48]}' names no tick — liveness is a measurement "
                                 f"with a date on it, not a belief. Write what happened when you "
                                 f"started it and on which tick (t<N>)")
            elif tick is not None and tick - int(mv.group(1)) >= 2:
                fail("liveness", f"Runs: last measured at t{mv.group(1)}, now t{tick} — "
                                 f"{tick - int(mv.group(1))} ticks stale. Start the product and "
                                 f"play one loop before picking any other work (§2a step 0a)")
            if BROKEN.search(claim) and \
               re.search(r"Gate:[^|\n]*CLOSED\s*\(converged\)", text, re.I):
                fail("liveness", f"Runs: '{claim[:48]}' reports the product does not run, and the "
                                 f"gate says CLOSED (converged) — a done-call over a product "
                                 f"nobody can start")

    # ---- registers --------------------------------------------------------
    fronts: dict[str, int] = {}
    for rf in register_files:
        name = rf.stem
        rows = parse_tables(rf.read_text(encoding="utf-8", errors="replace"))
        if not rows:
            warn("registers", f"{name}: no rows yet")
            continue
        live = []
        for r in rows:
            rid, state = r.get("id", "?"), r.get("state", "").lower()

            # ---- a cut is executed, never annotated (§2h) ----
            cut = CUT_ANNOTATION.search(" ".join(r.values()))
            if cut:
                fail("cut", f"{name}/{rid}: says '{cut.group(0)}' but still carries state "
                            f"'{state or '—'}' — an annotated row is still counted in the "
                            f"goal-distance, still ranked, and still re-derived from the spec. "
                            f"Delete the row, delete or amend its source:, re-open what stood "
                            f"on it, and put the history in log/ + decisions.md")

            if state == PARKED:
                if "revive-if" not in " ".join(r.values()).lower():
                    fail("registers", f"{name}/{rid}: parked with no revive-if condition")
                continue
            if state not in RANK:
                fail("registers", f"{name}/{rid}: state '{state or '—'}' is not on the ladder "
                                  f"({' → '.join(LADDER)})")
                continue
            live.append((rid, RANK[state], r))
            inventory.append(state)

            blob = " ".join(r.values())

            # ---- provenance: did this row come from the SPEC or from the product? ----
            src = re.search(r"\bsource:\s*(.+?)(?:\s*[|·]|$)", blob, re.I)
            if not src:
                fail("inventory", f"{name}/{rid}: no 'source:' — a row with no document behind it "
                                  f"came from looking at what got built, and a sweep over the "
                                  f"product cannot see what was never started")
            else:
                # ---- the dangling citation a design change leaves behind (§4d) ----
                for msg in dangling(root, src.group(1)):
                    fail("citation", f"{name}/{rid}: {msg} — a citation that no longer resolves is "
                                     f"worse than none: the change landed in the spec and nowhere "
                                     f"else, so this row was never re-stated (§4d move 2)")

            # ---- the absence check: 'built' with nothing on disk ----
            if RANK[state] >= RANK["built"]:
                m = re.search(r"artifact:\s*([^\s|·,]+)", blob, re.I)
                if not m:
                    fail("absence", f"{name}/{rid}: at '{state}' with no 'artifact:' path — "
                                    f"a state that claims built and names nothing is unfalsifiable")
                else:
                    path = m.group(1).strip("`*")
                    if not (root / path).exists():
                        fail("absence", f"{name}/{rid}: claims '{state}' but {path} does not "
                                        f"exist — the row is a description of an intention")
                    elif code_dirs:
                        term = re.sub(r"[*`]", "", r.get("item", "")).split(".")[0].split("—")[0]
                        term = term.strip()[:40]
                        if term and mentions(root, term, code_dirs) == 0:
                            warn("absence", f"{name}/{rid}: {path} exists, but nothing in "
                                            f"{'/'.join(code_dirs)} mentions '{term}' — the row may "
                                            f"name the wrong artifact")

            if RANK[state] >= RANK["specced"]:
                acc = r.get("acceptance", "")
                acc_clean = re.sub(r"[—–\-\s]", "", acc)
                if not acc_clean:
                    fail("registers", f"{name}/{rid}: at '{state}' with no acceptance line — "
                                      f"an item that cannot fail never ends")
                elif UNFALSIFIABLE.search(acc) and not re.search(r"\d", acc):
                    fail("registers", f"{name}/{rid}: acceptance '{acc[:48]}' cannot fail — "
                                      f"no number, no measurable observation")
                budget = r.get("budget", "")
                if not re.fullmatch(r"\d+", budget.strip()):
                    fail("registers", f"{name}/{rid}: at '{state}' with no tick budget")

            # ---- the stall rule -------------------------------------------
            spent, budget = r.get("spent", ""), r.get("budget", "")
            if spent.strip().isdigit() and budget.strip().isdigit():
                if int(spent) >= int(budget) and RANK[state] < RANK["verified"]:
                    fail("stall", f"{name}/{rid}: spent {spent} of {budget} ticks and still "
                                  f"'{state}' — take an exit (adopt / cut / park / escalate), "
                                  f"do not raise the effort")
            mv = re.search(r"t?(\d+)", r.get("moved", ""))
            if tick is not None and mv and RANK[state] < RANK["verified"]:
                idle = tick - int(mv.group(1))
                if idle >= 2:
                    fail("stall", f"{name}/{rid}: acceptance number unchanged for {idle} ticks — "
                                  f"that is a STALL, not diligence")

        if live:
            front = max(rank for _, rank, _ in live)
            floor = min(rank for _, rank, _ in live)
            fronts[name] = front
            if front - floor > 1:
                fail("one-state", f"{name}: front '{LADDER[front]}' is {front - floor} states "
                                  f"ahead of floor '{LADDER[floor]}' — finish the pass, "
                                  f"do not polish one corner")

    if len(fronts) > 1:
        hi, lo = max(fronts.values()), min(fronts.values())
        if hi - lo > 1:
            ahead = [n for n, v in fronts.items() if v == hi]
            behind = [n for n, v in fronts.items() if v == lo]
            fail("one-state", f"{'/'.join(ahead)} at '{LADDER[hi]}' vs {'/'.join(behind)} at "
                              f"'{LADDER[lo]}' — move the loop to the lowest register")

    # ---- the log ----------------------------------------------------------
    if tick is not None and log_entries:
        blob = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in log_entries)
        if not re.search(rf"\bt{tick}\b", blob):
            fail("log", f"no log entry references tick t{tick} — a tick that left no entry "
                        f"did not happen as far as the next context is concerned")

    # ---- docs freshness (warning only) ------------------------------------
    docs = root / "docs"
    if docs.is_dir():
        unstamped = [p.name for p in sorted(docs.glob("*.md"))
                     if not re.search(r"Verified:", p.read_text(encoding="utf-8", errors="replace"), re.I)]
        if unstamped:
            warn("docs", f"{len(unstamped)} unstamped: {', '.join(unstamped[:6])}"
                         f"{' …' if len(unstamped) > 6 else ''} — undated is a claim about the past")

    # ---- report -----------------------------------------------------------
    for line in warns:
        print(line)
    for line in fails:
        print(line)
    if inventory:
        by_state = {s: sum(1 for v in inventory if v == s) for s in LADDER + [PARKED]}
        exists = sum(1 for v in inventory if RANK.get(v, -1) >= RANK["built"])
        print(f"  info  inventory    {len(inventory)} rows · {exists} at 'built' or above "
              f"(claimed, not re-verified here) · "
              + " · ".join(f"{n} {s}" for s, n in by_state.items() if n))
        print(f"  info  goal-distance {exists} of {len(inventory)} claim an artifact · "
              f"{by_state.get('verified', 0) + by_state.get('received', 0)} verified · "
              f"{by_state.get('intent', 0)} at intent with no artifact")

    if not fails:
        print("  ok    layout · active · registers · inventory · absence · one-state · stall · log")
        print(f"\nState check green"
              f"{f' at tick t{tick}' if tick is not None else ''}"
              f"{f' · {len(warns)} warning(s)' if warns else ''}.")
        return 0
    print(f"\n{len(fails)} failure(s). The loop does not get to report progress until these pass.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
