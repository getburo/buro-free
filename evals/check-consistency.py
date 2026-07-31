#!/usr/bin/env python3
"""Studio consistency check — does the plugin still describe itself truthfully?

Seven deterministic checks over the on-disk studio. Each one exists because a real
drift happened: a seat added but missing from a department list, a description
that moved on while the eval surface stayed behind, a claimed seat count that
stopped matching the folders, a reference file copied into a second seat and then
edited in only one of them.

    python3 evals/check-consistency.py          # report, exit 1 on any failure
    python3 evals/check-consistency.py --fix    # rewrite surface.txt, then report

Run from the repository root. Part of buro:selftest §4.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
SURFACE = os.path.join(ROOT, "evals", "surface.txt")
EVAL = os.path.join(ROOT, "evals", "routing-eval.json")

# `buro` is the dispatcher and `selftest` is a tool — neither is a seat, and
# neither is expected in a department roster.
NON_SEATS = {"buro", "selftest"}

failures = []
notes = []


def fail(check, msg):
    failures.append((check, msg))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def frontmatter(seat):
    """Return (name, description-as-one-line, folded-marker) for a seat."""
    text = read(os.path.join(SKILLS, seat, "SKILL.md"))
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None, None
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+?)\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.*?)(?=^\w+:|\Z)", fm, re.S | re.M)
    if not desc:
        return (name.group(1) if name else None), None, None
    lines = [ln.strip() for ln in desc.group(1).strip().split("\n")]
    marker = lines[0] if lines and lines[0] in (">-", ">", "|-", "|") else None
    body = " ".join(lines[1:] if marker else lines)
    return (name.group(1) if name else None), body, marker


def surface_rows(seats):
    rows = []
    for seat in seats:
        _, body, marker = frontmatter(seat)
        prefix = f"{marker} " if marker else ""
        rows.append(f"buro:{seat} — {prefix}{body}")
    return rows


def dewrap(text):
    """Join references broken across a line: `buro:art-\\n  director` is one name."""
    return re.sub(r"-\n\s*", "-", text)


def tokens_in(region, seats):
    """Seats named in a region — as `buro:x`, in backticks, or bare.

    Rosters write seats three ways (`buro:level`, `level`, and plain `level` in a
    department line), so all three count. Bare-word matching is only safe because
    the region is a tightly bounded list, not open prose.
    """
    text = dewrap(region)
    found = set(re.findall(r"buro:([a-z0-9-]+)", text))
    found |= set(re.findall(r"[a-z0-9-]+", text))
    return found & seats


def region(text, start, end):
    i = text.find(start)
    if i < 0:
        return None
    j = text.find(end, i + len(start))
    return text[i : j if j > 0 else len(text)]


# ── discover ────────────────────────────────────────────────────────────────
all_dirs = sorted(
    d for d in os.listdir(SKILLS)
    if os.path.isdir(os.path.join(SKILLS, d))
    and os.path.exists(os.path.join(SKILLS, d, "SKILL.md"))
)
seats = set(all_dirs) - NON_SEATS

# ── 1. frontmatter is parseable and self-consistent ─────────────────────────
for seat in all_dirs:
    name, body, _ = frontmatter(seat)
    if name is None:
        fail("frontmatter", f"{seat}: no parseable YAML frontmatter")
    elif name != seat:
        fail("frontmatter", f"{seat}: name: '{name}' does not match its folder")
    if not body:
        fail("frontmatter", f"{seat}: empty or unparseable description")

# ── 2. eval surface matches the frontmatter it is generated from ────────────
expected_surface = "\n".join(surface_rows(all_dirs)) + "\n"
if "--fix" in sys.argv:
    with open(SURFACE, "w", encoding="utf-8") as fh:
        fh.write(expected_surface)
    notes.append(f"surface.txt regenerated ({len(all_dirs)} rows)")
actual_surface = read(SURFACE)
if actual_surface != expected_surface:
    have = {ln.split(" — ")[0][5:] for ln in actual_surface.splitlines() if ln.startswith("buro:")}
    missing = sorted(set(all_dirs) - have)
    extra = sorted(have - set(all_dirs))
    detail = []
    if missing:
        detail.append(f"missing rows: {', '.join(missing)}")
    if extra:
        detail.append(f"stale rows: {', '.join(extra)}")
    if not detail:
        detail.append("row text has drifted from the frontmatter")
    fail("surface", "; ".join(detail) + "  (run with --fix)")

# ── 3. every eval case targets a real, routable seat ────────────────────────
cases = json.loads(read(EVAL))["cases"]
on_surface = {ln.split(" — ")[0][5:] for ln in expected_surface.splitlines() if ln.startswith("buro:")}
for case in cases:
    want = case["expected"]
    if want not in all_dirs:
        fail("eval-targets", f"case {case['id']}: expects '{want}', which is not a seat")
    elif want not in on_surface:
        fail("eval-targets", f"case {case['id']}: '{want}' is absent from the routing surface")

# ── 4. every buro:X reference resolves ─────────────────────────────────────
# Scoped to the files that describe the studio as it is NOW. `docs/research/` is
# excluded on purpose: those are dated captures and are allowed to name seats that
# were only ever planned (`buro:camera`, `buro:systems`).
PLACEHOLDERS = {"seat"}  # `buro:seat` documents the colon syntax itself
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "research")]
    for fn in filenames:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(dirpath, fn)
        for ref in set(re.findall(r"buro:([a-z0-9-]+)", dewrap(read(path)))):
            if ref not in all_dirs and ref not in PLACEHOLDERS:
                rel = os.path.relpath(path, ROOT)
                fail("cross-refs", f"{rel}: 'buro:{ref}' does not exist")

# ── 5. every roster covers every seat (the check that catches a new seat) ───
dispatcher = read(os.path.join(SKILLS, "buro", "SKILL.md"))
readme = read(os.path.join(ROOT, "README.md"))
plan = read(os.path.join(ROOT, "docs", "STUDIO-PLAN.md"))

rosters = {
    "dispatcher/departments": region(dispatcher, "**The ten departments", "It bridges to"),
    "dispatcher/trigger table": region(dispatcher, "**Always, for any screen work:**", "\n**BUILD —"),
    "README/department table": region(readme, "| Department | Seats |", "\n\n"),
    "STUDIO-PLAN/org chart": region(plan, "## 3. The studio org chart", "\n`*` ="),
}
for label, text in rosters.items():
    if text is None:
        fail("rosters", f"{label}: could not locate the region — the anchor text moved")
        continue
    named = tokens_in(text, seats)
    missing = sorted(seats - named)
    if missing:
        fail("rosters", f"{label} omits: {', '.join(missing)}")

# ── 6. declared seat counts match reality ──────────────────────────────────
orchestration = read(os.path.join(ROOT, "docs", "ORCHESTRATION.md"))
for label, text in (
    ("README.md", readme),
    ("docs/STUDIO-PLAN.md", plan),
    ("docs/ORCHESTRATION.md", orchestration),
):
    for claimed in {int(n) for n in re.findall(r"(\d+)[ -]seats?\b", text)}:
        if claimed != len(seats):
            fail("counts", f"{label} claims {claimed} seats; there are {len(seats)}")

# ── 7. no reference file is copied into two seats ──────────────────────────
# The dispatcher used to keep its own copies of four seat references. All four
# silently drifted from the originals, so the studio shipped two editions of the
# same rule. A reference belongs to exactly one seat; everyone else links to it.
# `canon.md` is exempt: it is the per-seat template name, not a shared document.
PER_SEAT_REFERENCES = {"canon.md"}
by_basename = {}
for seat in all_dirs:
    refs = os.path.join(SKILLS, seat, "references")
    if not os.path.isdir(refs):
        continue
    for fn in sorted(os.listdir(refs)):
        if fn.endswith(".md") and fn not in PER_SEAT_REFERENCES:
            by_basename.setdefault(fn, []).append(seat)
for fn, owners in sorted(by_basename.items()):
    if len(owners) > 1:
        fail("ref-copies", f"'{fn}' exists in {', '.join(owners)} — one owner, others link")

# ── report ─────────────────────────────────────────────────────────────────
CHECKS = ["frontmatter", "surface", "eval-targets", "cross-refs", "rosters", "counts", "ref-copies"]
print(f"buro studio consistency — {len(seats)} seats, {len(all_dirs)} skill folders\n")
for note in notes:
    print(f"  · {note}")
if notes:
    print()
for check in CHECKS:
    hits = [m for c, m in failures if c == check]
    if hits:
        print(f"  FAIL  {check}")
        for h in hits:
            print(f"          {h}")
    else:
        print(f"  ok    {check}")
print()
if failures:
    print(f"{len(failures)} problem(s) — the studio no longer describes itself truthfully.")
    sys.exit(1)
print(f"All {len(CHECKS)} checks green.")
