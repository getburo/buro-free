# Buro Studio — Orchestration (the seams)

> Quality is made on the parts. **Cohesion is made on the seams.** The full studio's many
> seats are the parts — each already excellent. This document is the seams: how they combine
> into *one* production, so a large studio stays one studio and not many tools. **This free
> tier ships 17 of them**; this document describes the full studio and is kept for reference.

This is the playbook `buro:process` (the conductor) points to. It answers: what is the
studio *about*, how do the seats hand off, what's the core motion, and — for the common
productions — which seats run, in what order, and who owns the integration.

---

## 1. The concept (the one arbiter)

Every cohesive product has one checkable, exclusionary idea every decision is measured
against. The studio's is its **honesty law**, and it is the arbiter every seat already
carries:

> **Subtract decoration, never a capability. Every seat both DIRECTS (method + critique)
> and PRODUCES (the artifact, self-critiqued). Quality, fun, and retention are EARNED by
> mastery and delivered value — never extracted by dark patterns, FOMO, or manipulation.**

What it rules OUT (the border): loot boxes, energy timers, FOMO, pay-to-win, fake
urgency, growth-hacking spam, vanity metrics, amputation-disguised-as-simplification,
and producing that phones it in. A seat, a mechanic, or a feature that violates this
doesn't enter — "good, but not here" is a full verdict.

**The border is the STUDIO's taste — it becomes a prohibition only when something says so.**
Buro is not the author's regulator. Each item above is tiered per project: **BLOCKED** (named law
/ platform / rating policy in the declared `## COMPLIANCE` regime) · **CONDITIONAL** (allowed on
a stated condition) · **TASTE** (said once, author's call). With no regime declared there is no
BLOCKED tier. An unsourced ban is weaker than a sourced one — it gets ignored wholesale instead
of applied exactly where it is mandatory — and imposing the studio's taste as law on someone
else's work is extraction of their decision.

**The border names PATTERNS, not MECHANISMS — and the difference is the whole discipline.**
Every item above is a *use* of a neutral mechanism, and banning the mechanism to avoid the
pattern is amputation wearing the law's uniform:

| Banned pattern | The mechanism it uses — which stays legitimate |
|---|---|
| loot box | **randomness** — crits, loot tables, procgen, roguelike runs, card draw. What is vetoed is *money in → random out → odds hidden*; remove any one and the veto lifts |
| FOMO event | **a time-limited event** — a season, a raid window, a launch. What is vetoed is manufactured anxiety, not the calendar |
| fake urgency | **a real deadline** — which is honest when it is true |
| engagement bait | **a notification** — which is honest when it carries something the person wanted |
| pay-to-win | **paid content** — cosmetics, expansions, a fair price for real work |

The test is the same one law 7 uses: **what does the USER lose?** Ban the pattern and they lose
a manipulation. Ban the mechanism and they lose a capability — the game's uncertainty, the
season, the reminder. That is the amputation this studio exists to refuse. When a verdict says
"remove X", check which of the two it just removed.

Because all seats share this arbiter, their outputs *rhyme* by themselves. Cohesion is
the consequence of the shared arbiter, not a separate task.

---

## 2. The core motion — RECON → DIRECT → PRODUCE → RECEIVE → revise

The studio's fundamental loop, true for any medium:

```
RECON    — before inventing: how is this ALREADY solved, by whom, and what does that
           solution buy? Then adopt / adapt / deviate — out loud. Deviation is legitimate;
           deviation by ignorance is not. (buro:process → the prior-art gate)
DIRECT   — the make-seat brings method, canon, and a critique of the intent.
PRODUCE  — the same seat emits the artifact (chapter, scene, level, HUD, Luau…),
           and passes it through its OWN self-critique gate before delivery.
RECEIVE  — the reception wing throws it at a hostile world:
             buro:tester (does it break?) · buro:audience (do real users bounce?) ·
             buro:critic (is it good vs the best of its form?) · buro:chaos (hidden
             assumptions?) · buro:detective (if a quality regressed — when & why?)
revise   — findings go back to the make-seat. Loop until it converges.
```

**RECON is the newest and the most skipped.** Every one of the five reception seats looks
*inward* — at the artifact and its assumptions. None looks *outward*, at the field. Without
RECON the studio's characteristic failure is not a bad answer but a beautifully critiqued
re-invention of what the genre settled years ago: the critique quality is exactly what makes
it convincing. Naming a work as a reference is not RECON — RECON is being able to say what
that work actually *does*, the mechanism and not the vibe.

Nothing "ships" from one pass. Two clean rounds beat one optimistic pass
(`buro:process`, iteration-to-convergence).

**Compressed: the table.** When the material won't get past *competent* under a single lens,
`buro:process` runs that whole motion inside **one move** at a table of three or four — a **RIFF**
(generator → distorter → judge → back to the generator, rounds until nothing rises) to *birth*
something, or a **FAN** (every lens on the same material at once, verdicts collided) to *judge*
it. Same law, same gates, tighter loop. The protocol, the three chairs, the discipline, and the
canonical tables live in `buro:process` → *The table*; the standing rosters are §4b below.

---

## 3. The handoff rule — dispatch, don't duplicate

Every seat owns one competence and **hands off** the rest (each seat's "Discipline &
integration" section names its own boundaries). The three integration owners:

- **`buro:process`** — owns the *phase and gate*: which stage we're in, what unblocks the
  next, which seat to call now. The conductor sequences; it doesn't re-carry craft.
- **`buro:creative-director`** — owns *coherence*: makes N seats' outputs add up to ONE
  work; the final taste call when two seats conflict; the studio consilium.
- **`buro:producer`** — owns *delivery*: scope, dependency map, critical path, the
  value-ranked cut-list, and the ship date.

Rule of thumb: **process** says *what phase / which seat*; **creative-director** says
*does it cohere*; **producer** says *does it ship*. Engineering (`superpowers`,
`feature-dev`, `buro:roblox-engineering`) builds the code; the make-seats critique what
comes back.

---

## 4. Standard production pipelines

Concrete "who, in what order, who integrates." These are defaults, not cages —
`buro:process` loops back when meaning demands.

### Roblox game (idea → publish → operate) — the current primary path
```
process(gate the whole) + creative-director(vision) + producer(ship)  ← integration owners
 0 analyst        — is it worth building, for whom, how it pays
 1 gamedesign     — the core loop, the verb of the next 30s, economy (+ references/roblox.md)
 2 level          — the world's geography + the playable spaces · narrative — story/quests
 3 art-director   — one visual language → concept — the specific assets (design)
   animation — motion · sound — audio/music · game-ui — HUD/menus under pressure
 3b asset-sourcing — turn the concept/sound briefs into ACTUAL assets, by PRIORITY: build-own
    (code/CSG/EditableMesh) → Roblox AI (Cube/Material/Texture) → web-free + post-process (CC0/CC-BY,
    converted/optimized) → commission/external-AI → Toolbox LAST (scanned + license-checked). Vet all.
 4 roblox-engineering — server authority, DataStores, remotes, AnalyticsService, and the
    mandatory script-SCAN + import of any sourced free model (the build)
 5 RECEIVE        — tester + audience + critic + chaos, then revise (detective if a quality regresses)
 6 PUBLISH        — one click from Roblox Studio (store page: art-director icon/thumbnail + copy + brand)
 7 OPERATE        — live-ops(cadence/events/incidents) + retention + growth + experiment
                    (metrics: Roblox Creator Dashboard + AnalyticsService + native A/B)
```

### Film / animation (script → cut)
```
creative-director(vision) + producer(ship)
 screenwriter → director → storyboard → (animation, if animated) → performance →
 sound → edit → RECEIVE(critic + audience)
```

### Book (idea → manuscript)
```
curator(is it worth doing / on-voice) → creative-director(vision) →
 prose (+ verse for songs) → editor → art-director(cover/illustration brief) →
 RECEIVE(critic) → translator (if localized)
```

### Website / app (idea → ship)
```
process → analyst → pm → usability → buro (+ interface family: gorbunov/lebedev/dataviz/
 exotic/motion/a11y/copy) → superpowers / feature-dev (build) → docs (README, reference, the
 how-tos, the decision records) → RECEIVE(tester/audience) → retention + growth + experiment
```

---

### 4b. Standard tables (seats playing at once, not in order)

A pipeline is **who goes next**. A table is **who plays together**. Seat one when a single seat
would only reach *competent* — the seats are named by role, and the round repeats until two rounds
in a row raise nothing (cap 3–4; still hot after that → it's a spiral round, give it a pillar).

| Table | Generator → Distorter → Judge | Seated when |
|---|---|---|
| **Idea** | `gamedesign` → `chaos` → `critic` | a mechanic or feature from nothing |
| **World** | `level` → `narrative` → `gamedesign` | geography that must also *play* |
| **Screen** | `gorbunov` → `a11y` / `chaos` → `lebedev` | a new interface pattern, not a fix |
| **Word** | `copy` / `prose` → `audience` → `editor` | text that has to work read aloud, cold |
| **Frame** | `director` → `storyboard` → `critic` | a scene that isn't landing |
| **Thing** | `industrial-design` → `tester` → `cmf` | an object in atoms |
| **Market** | `analyst` → `chaos` → `curator` | *should this exist at all* |

**Every table opens with the SCOUT step** — how is this already solved, by whom — before the
generator plays. All three chairs look inward, so three inward lenses amplify a wrong frame
instead of catching it; the table then returns the best possible version of something that should
never have been built.

Not listed? Compose one: the seat that **owns the artifact**, a seat with a **genuinely different
lens** licensed to break things, and a seat that **holds the bar of the form**. Never two seats
from one department at one table (that's one lens in two voices); never more than four chairs
(past that it's a meeting). Conflicts between seats are **not** settled at the table — they go to
`buro:creative-director`. Full protocol: `buro:process` → *The table*.

---

## 5. Discoverability — how a user picks among many seats

A user does **not** memorise the roster. They state the task; **`buro:buro` (the dispatcher)
routes.** The two entry patterns:

- **Direct door:** you know the seat → invoke `buro:<seat>` (e.g. `buro:level`).
- **One obvious entry:** you don't → invoke `buro` and describe the task; it picks the
  seats, runs them, and synthesises. For a whole production, start with `buro:process`
  (it sequences the rest) and, for multi-seat work, `buro:creative-director` +
  `buro:producer`.

Both doors always stay open (dual access — never one removed to look "simpler").

---

## 6. The seams checklist (cohesion under growth)

Run this whenever the studio grows or a big production assembles:

- **Grammar budget** — a new seat/pattern enters only if no existing one fits. All 44
  seats share one template; keep it.
- **Concept filter** — a new seat/feature passes only if it's inside the honesty law and
  earns its place (the Skeptic: "delete it — what does the *user* lose?").
- **One arbiter** — the honesty law is in every seat; if a new seat doesn't carry it, it
  doesn't belong.
- **Gut-check** — take three random seats: *one studio, or three?* They should share the
  voice, the DIRECT+PRODUCE nature, the adversarial panel, and the honesty law.
- **No bloat** — the parts have converged. Further growth is at the *seams*
  (docs like this one) or a real new medium — not more specialists. Adding a seat that
  overlaps an existing one is cohesion debt, not coverage.

---

## 7. Where the studio is

Parts: converged, one grammar. Seam management: this document. The honest
next frontier is **not** more seats — it's the multi-engine engineering track (Unity /
Unreal / Godot / web), which is a deliberate expansion past Roblox with its own
spec → plan → build cycle (see `STUDIO-PLAN.md` → Roadmap), not an incremental seat.
