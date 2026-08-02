# Buro — free tier

**Technical design, as a family of Claude Code skills — one full-strength seat per department
(16 of the full studio's 59), each with its own method and a critique that pushes back, shipped
at full depth. No thinning: every included seat directs and produces exactly as it does in the
full studio. The rest of each department's bench lives in the full commercial
Buro studio, a separate commercial product.**

A design bureau in the engineering sense: not taste, not decoration, but design as a discipline
with a method you can check and a critique that argues. Name the task and one dispatcher
(`buro`) routes it to the seat that owns that craft — where every seat both **directs** (method
+ a ruthless critique) **and produces** (writes the chapter, stages the scene, specs the object,
names the brand, lays out the level — self-critiqued before it ships).

It is not a tool for one medium: the same discipline covers a screen, a level, a document, a
name, a scene, and a product decision.

**The one law is the spine — not any single medium:**

> **Subtract decoration, never a capability. Quality is earned by mastery and delivered value,
> never extracted by dark patterns, FOMO, planned obsolescence, or hype past the product. Every
> seat both directs and produces — and producing is never an excuse to phone it in.**

That law is what makes buro *one* studio. **No craft sits above another** — a translator, a
game designer, an industrial designer, and the interface seats are equal members; their outputs
rhyme because they share the arbiter, not a subject. The seats span words, screen (film &
animation), visual art, games & worlds, physical / industrial design, marketing & comms,
interfaces & UX, product & business, a reception wing that plays the hostile audience, and a
leadership wing that holds a multi-seat production together — and it **bridges to
[Superpowers](https://github.com/obra/superpowers) and feature-dev** for real engineering.

## The mission

**You give one task; the studio assembles the team and takes the whole project to done.** For a
single-craft job (rewrite this error, name this, critique this screen) one seat runs and returns
the verdict. For a **whole project** — a website, a greeting card, a game, a cartoon, a film, a
product, a campaign — buro runs the full lifecycle: **market analysis & the first idea →
production → post-production → post-launch**. The seats form teams and call one another,
conducted by `process` (which sequences the phases), with `creative-director` holding one vision
and `producer` shipping it. Done is the conductor's call — never one optimistic pass.

---

## How it works

`buro` is the top dispatcher: it reads the task, routes to the right seats, and synthesises the
verdict. Invoke any seat directly with the colon syntax:

```
buro:buro                the studio dispatcher (entry point)
buro:docs                write / fix a README, reference, runbook
buro:director            stage a scene
buro:gamedesign          the core loop, mechanics, balance
buro:industrial-design   the form of a physical product
buro:critic              judge a finished work against the best of its form
buro:creative-director   make many seats cohere into one work
```

Two spines, one brain:

- **Buro** owns *what* and *why* — intent, taste, honesty, and the artifact itself.
- **Superpowers / feature-dev** own *how to build safely* — brainstorming → plans → TDD → review.
- **`buro:process`** is the switchman between them; the make-seats critique what comes back.

## The seats

Ten departments — **peers, not a hierarchy** — this tier ships one full-depth seat from each,
16 seats total (+ the `buro` dispatcher and `selftest`). The seat named is complete: same method,
same panel, same PRODUCE gate as the full studio. The `(full studio)` seats do not ship here.

| Department | Seats | Full-studio bench (not shipped here) |
|---|---|---|
| **Words** | `docs` · `editor` | prose, screenwriter, copy, brand, verse, translator, transcreation |
| **Screen** (film / animation) | `director` | storyboard, edit, sound, animation, performance |
| **Visual / art** | `art-director` | concept |
| **Games & worlds** | `gamedesign` | combat-design, level, narrative, game-ui, roblox-engineering, asset-sourcing, live-ops |
| **Physical / industrial design** | `industrial-design` | cmf, packaging, spatial, manufacturing |
| **Marketing / comms** | `ad-creative` | campaign, content, launch-pr, sales |
| **Interfaces & UX** (the Russian school) | `lebedev` · `gorbunov` · `copy` · `usability` | dataviz, exotic, motion, a11y |
| **Product / business / process** | `pm` · `process` | analyst, experiment, growth, retention |
| **Reception / stress** | `critic` · `tester` | audience, chaos, detective |
| **Leadership / production** | `creative-director` | producer, curator |

Where two seats look alike, the dispatcher carries a **Seam rules** table scoped to what this
tier can actually route between (the full table, e.g. playable space → `level`, invented
geography → `level`, lives in the full studio).

Each seat is a folder under `skills/` with a `SKILL.md` (frontmatter → epigraphs → core chain →
lenses → an adversarial panel → method gates → a **PRODUCE** section with a self-critique gate →
the verdict format → discipline & boundaries → "slop it kills on sight") and a `references/`
canon.

## What this tier makes

| Task | Seats engaged (this tier) |
|---|---|
| A screen or small flow, critiqued | `lebedev` + `gorbunov` + `copy` + `usability` |
| Documentation — README, reference, runbook | `docs` (+ `editor` to tighten a draft) |
| A game system's design — loop, mechanics, balance | `gamedesign` |
| A scene, staged | `director` |
| A physical object's form (specs, not manufacturing) | `industrial-design` |
| One ad set | `ad-creative` |
| Prioritization / a PRD | `pm` |
| A small project idea → ship | `process` (conductor) + `creative-director` (vision) + the relevant make seat + `tester`/`critic` |

Full-medium pipelines (a whole game, book, film, marketing campaign, physical-product line, or
Roblox build) need seats outside this tier — the full commercial studio.

## Install

This is a Claude Code **plugin**. Point Claude Code at this repository as a plugin source (or
add it to a marketplace) and the seats become available as `buro:<seat>`.

```bash
# from GitHub
/plugin marketplace add getburo/buro-free   # registers the marketplace manifest
/plugin install buro-free                   # installs the plugin
# then invoke any seat: buro:buro, buro:docs, buro:critic, …
```

```bash
# from a local clone
/plugin marketplace add ~/path/to/claude_plugin_buro_free
/plugin install buro-free
```

## Layout

**16 seats across 10 departments** (+ the `buro` dispatcher and `selftest`) — the free tier of
the full commercial Buro studio. Seat descriptions are kept lean so the always-on cost stays modest;
each seat's full method loads on demand when it's invoked. See
[`docs/STUDIO-PLAN.md`](docs/STUDIO-PLAN.md) for the architecture and the seat template.

```
.claude-plugin/   plugin + marketplace manifests
docs/             architecture
evals/            routing eval (surface + cases + results) + check-consistency.py
skills/           one folder per seat: SKILL.md + references/
```

Adding or renaming a seat touches more places than it looks — four rosters, the routing surface,
the seam table, the seat counts in three documents. `python3 evals/check-consistency.py` verifies
all of them and `--fix` regenerates the surface; it is also `buro:selftest` §4. Every one of its
seven checks exists because that drift already happened at least once.

## Credits

Each seat draws on its field's canon — Lebedev's *Kovodstvo* and the Birman / Gorbunov bureau
method for interfaces, and McKee, Field, Snyder, Le Guin, Gardner, the Disney 12 principles,
Murch, Tufte, Stanislavski, Lynch, Rams, Christaller and more across the other disciplines —
credited inside the relevant seat's `references/canon.md`.

## License

All rights reserved — see [LICENSE](LICENSE).

This is proprietary software. Free-tier access grants a personal, non-transferable right to use
it — not to copy, modify, distribute, sublicense, or create derivative works. No open-source or
future-conversion license applies.

