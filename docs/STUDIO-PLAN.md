# Buro — architecture

> A **bureau of master seats** bound by one law: subtract decoration never capability, quality
> earned never extracted, every seat both **directs** (method + critique) and **produces** (the
> artifact, self-critiqued). No craft sits above another — words, screen, visual art, games,
> physical / industrial design, marketing, interfaces, product, reception, leadership are peers;
> their outputs cohere because they share the arbiter, not a subject. Bridged to **Superpowers**
> for engineering.

**16 seats across 10 departments** (+ the `buro` dispatcher and `selftest`) — the free tier of
the full commercial Buro studio, packaged as the plugin `buro-free@buro-free-dev`. One full-depth
seat per department, no thinning; the roadmap and the remaining bench live in the full studio,
a separate commercial product.

---

## 1. Principle: two spines, one dispatcher

```
                        ┌─────────────┐
   user  ──────────────▶│    buro     │  top studio dispatcher (plugin entry)
                        │  (studio)   │  reads the task → routes → synthesises
                        └──────┬──────┘
             ┌─────────────────┼──────────────────┐
             ▼                 ▼                  ▼
     TASTE / METHOD SPINE   PROCESS SPINE      EXECUTION SPINES
     buro seats             buro:process       superpowers + feature-dev
     (what is good, why,    (which phase,      (build discipline / TDD / review
      + produce artifact)    order, gates)       + codebase-native feature work)
```

- **Buro owns WHAT and WHY** — the intent, the taste, the honesty laws — including
  "we need a site / a game / a book".
- **Superpowers owns HOW to build safely** — brainstorming → writing-plans →
  executing-plans / TDD → code-review.
- **`buro:process` is the switchman** — on the *build* phase it hands the baton to
  Superpowers, then returns the finished artifact to the relevant Buro seats for a
  critique pass.

This respects `using-superpowers` ("process skills first"): the chain is
**buro (frame) → superpowers (build) → buro (critique)**. That is how Buro "codes"
without rewriting engineering discipline — it conducts it.

---

## 2. Every seat is dual-nature: DIRECT + PRODUCE

The studio's defining decision: each seat operates in two modes.

- **DIRECT** — method, canon, critique ("what's wrong and why"). This is how Buro
  behaves today.
- **PRODUCE** — the seat itself emits the artifact: a chapter, a scene, a dialogue,
  a storyboard, a shot list, a page of code.

The Buro **honesty law extends to both**: *producing is not an excuse to phone it in.
An artifact must pass the seat's own critique before it is delivered.* Where a seat
cannot literally produce the final medium (a concept artist cannot paint pixels), it
produces the honest adjacent artifact — a precise brief / spec — and says so plainly.

**The third mode — RECEIVE.** Beyond making seats, the studio has a whole department
that plays the *audience and the adversary*: it throws a finished artifact at simulated
naive, hostile, and unhinged reception (`tester`, `audience`, `critic`, `chaos`). The
full studio motion is therefore **DIRECT → PRODUCE → RECEIVE → back to the make seats**.

---

## 3. The studio org chart

This chart is the full studio's, kept for reference. **This free tier ships only:**
`lebedev`, `gorbunov`, `copy`, `usability` (Taste/Method), `pm`, `process` (Product/Business),
`gamedesign` (Games & Worlds), `docs`, `editor` (Words), `director` (Screen), `art-director`
(Visual), `industrial-design` (Physical), `ad-creative` (Marketing), `tester`, `critic`
(Reception), `creative-director` (Leadership). Every other name below is full-studio only.

```
buro  — top studio dispatcher (plugin entry: buro:buro)
│
├─ DEPARTMENT: LEADERSHIP / PRODUCTION                        [NEW]
│    creative-director* · producer* · curator*   (pm lives in Product)
│
├─ DEPARTMENT: TASTE / METHOD — the Russian school (interface)
│    lebedev · gorbunov · dataviz · exotic · motion · a11y · usability · game-ui
│
├─ DEPARTMENT: PRODUCT / BUSINESS / PROCESS
│    analyst · pm · process · experiment · growth · retention
│
├─ DEPARTMENT: GAMES & WORLDS
│    gamedesign · combat-design · narrative · worldbuilding · level · area · roblox-engineering ·
│    asset-sourcing · live-ops
│
├─ DEPARTMENT: WORDS
│    copy · docs · screenwriter · prose · editor · verse · brand · translator · transcreation
│
├─ DEPARTMENT: SCREEN (film / animation)
│    director · storyboard · edit · sound · animation · performance
│
├─ DEPARTMENT: VISUAL / ART
│    art-director · concept
│
├─ DEPARTMENT: PHYSICAL / INDUSTRIAL DESIGN — objects & spaces in atoms   [v0.7.0]
│    industrial-design · cmf · packaging · spatial · manufacturing
│    (specs & briefs; the physical engineering bridge is manufacturing/DFM)
│
├─ DEPARTMENT: MARKETING / COMMS — earning attention honestly             [v0.7.0]
│    campaign · ad-creative · content · launch-pr · sales
│    (de-collided from brand/copy/growth; sales = one-to-one, growth = the system)
│
├─ DEPARTMENT: RECEPTION / STRESS — simulated audience, adversary, investigator
│    tester · audience · critic · chaos · detective
│
└─ BRIDGE TO EXECUTION (sites, game code)
     buro:process ⟶ superpowers (brainstorming → writing-plans → TDD → code-review) ⟶ back for critique
```
`*` = new seat to author. `screenwriter` is authored (exemplar/template).

---

## 4. New seats — mandate and dual nature

| Seat | DIRECT (guides) | PRODUCE (emits) |
|---|---|---|
| `buro:creative-director` | one creative vision: makes N seats cohere into a single work; final taste call | vision brief, cross-seat coherence notes, the "north-star" of the piece |
| `buro:producer` | logistics: schedule, resources, dependencies, risk; herds seats to ship | production plan, dependency map, cut-list under deadline |
| `buro:curator` | selection & body-of-work coherence: what's worth doing, what represents the studio | go/no-go call, curation rationale, portfolio coherence review |
| `buro:level` | one playable space: layout, encounters, pacing, sightlines, gating | level layout, encounter beat sheet, flow map |
| `buro:area` | many places finished together: coverage, region identity, seams, set dressing | region manifest, seam plan, dressing plan, coverage audit |
| `buro:screenwriter` | script structure: 3 acts, sequences, beat sheet, format | scenes, dialogue, screen scripts for film / animation / cutscenes |
| `buro:prose` | long-form prose: POV, scene-sequel, voice, chapter rhythm | novel / short-story / non-fiction chapters |
| `buro:editor` | structural & line editing; text honesty | edited text, "what to cut" breakdown |
| `buro:verse` | poetry / song / lyrics: meter, rhyme, form, the turn | poems, song lyrics, verse to brief |
| `buro:brand` | naming, brand voice, identity system | names, voice guide, brand brief (dispatches visuals to art-director) |
| `buro:translator` | literary translation & localization: register, idiom, culture | translated / localized text that keeps the voice |
| `buro:director` | staging: mise-en-scène, tempo-rhythm, POV, tension | director's treatment of a scene |
| `buro:storyboard` | frame, camera, composition, edit logic | storyboard (per-panel descriptions), shot list |
| `buro:edit` | montage: cut rhythm, sequence assembly | edit list, scene order |
| `buro:sound` | sound / music: diegesis, leitmotif, silence as device | sound-design / score brief, scene sound map |
| `buro:animation` | animation direction: the 12 principles, timing, weight, character acting | animation brief, timing chart, acting notes per shot |
| `buro:performance` | acting & voice direction: intention, line reading, delivery | performance/voice-direction notes, line-read options |
| `buro:art-director` | one visual language: palette, references, style guide | art bible, project visual canon |
| `buro:concept` | concept: character, environment, props | art briefs / prompts and specs (Buro does not paint — it briefs) |
| `buro:tester` | QA & break-testing: edge cases, adversarial inputs, "how it fails" | test plan, bug list, repro steps |
| `buro:audience` | real-user simulation: cold-read personas, first-contact reaction | reaction transcript, "where I'd bounce" report |
| `buro:critic` | professional critique in the voice of a domain critic | a written review, judged against the best of the form |
| `buro:chaos` | reductio ad absurdum, extreme personas, premise fuzzing — for research | failure catalogue, hidden-assumption list |
| `buro:detective` | experiential root-cause: WHEN & WHY a mechanic, location, fun, or beauty broke — bisect the change/playthrough history | root-cause report: the moment, the cause, the fix. Dispatches code regressions to `superpowers:systematic-debugging` |

`copy` stays the interface/marketing micro-copy seat (Ilyahov's info-style). The
three lanes in the Words department are kept distinct on purpose:
- `copy` — interface & marketing micro-copy,
- `prose` — long-form fiction / non-fiction,
- `screenwriter` — screen scripts.

---

## 5. On-disk layout (plugin)

```
claude_plugin_buro/                 ← git repo / plugin root
├─ .claude-plugin/
│   ├─ plugin.json
│   └─ marketplace.json
├─ docs/
│   └─ STUDIO-PLAN.md               ← this file
└─ skills/
    ├─ buro/SKILL.md                ← dispatcher = buro:buro (entry)
    ├─ lebedev/SKILL.md             ← buro:lebedev
    ├─ narrative/SKILL.md           ← buro:narrative
    ├─ screenwriter/SKILL.md        ← buro:screenwriter (new)
    └─ …one folder per seat, each with SKILL.md + references/
```
The colon syntax `buro:seat` comes for free from being packaged as a plugin; the
folder name after `skills/` is the part after the colon.

---

## 6. Universal seat template

Every seat is a folder with a `SKILL.md`:

1. **frontmatter** — `name`, `description` with a sharp lane of responsibility and
   trigger phrases (de-collision: `copy`=interface/marketing micro, `prose`=long
   fiction/non-fiction, `screenwriter`=screen script).
2. **mandate** — what the seat OWNS.
3. **dispatches** — what it hands to neighbours (`storyboard`→`director`; world
   physics/economics→`worldbuilding`; actual build→`process`→superpowers).
4. **DIRECT section** — method + canon + critique output format.
5. **PRODUCE section** — how it emits the artifact + a self-critique gate before delivery.
6. **honesty law** — what this seat forbids.
7. `references/` — the discipline's canon.

---

## 7. Buro ⇄ Engineering handoff protocol (Superpowers + feature-dev)

For any task that needs a real build (code — sites, game code), `buro:process` is the
switchman. It hands off to **two engineering spines**, chosen by the shape of the work:

**Superpowers** — the *discipline & process* spine (the rigorous default):
- `superpowers:brainstorming` → `superpowers:writing-plans` →
  `superpowers:executing-plans` / `test-driven-development` →
  `superpowers:requesting-code-review`; plus `systematic-debugging` for regressions.

**feature-dev** — the *codebase-native feature* spine (when working inside an existing
codebase and the shape must match what's already there):
- `feature-dev:code-explorer` (trace & map the existing feature/architecture) →
  `feature-dev:code-architect` (blueprint that follows the codebase's own patterns) →
  implement → `feature-dev:code-reviewer` (confidence-filtered review).

Routing rule of thumb:
- **Greenfield / process-first / TDD-critical** → Superpowers.
- **Brownfield / "fit the existing codebase" / architecture-blueprint-first** → feature-dev.
- They compose: e.g. `code-explorer` to understand, then Superpowers TDD to build, then
  both reviewers. `buro:detective` sends *code* regressions to `superpowers:systematic-debugging`.

**Return leg (always):** the finished artifact comes back to Buro seats for a taste and
usability critique pass (`usability`, `dataviz`, `a11y`, `motion`, `copy` …) and, on a
multi-seat production, to `creative-director` for coherence.

Engineering spines own build safety and codebase fit; Buro owns intent and the taste
critique. Neither re-implements the other.

---

## 8. "Make anything" — medium → seats map

| Medium | Seats engaged |
|---|---|
| Websites | buro (design) + superpowers (build) + analyst/pm/process |
| Games | gamedesign/narrative/worldbuilding + buro (HUD) + superpowers (code) + sound/art |
| Short / interface / marketing text | copy |
| Books | prose + editor + art-director (cover / illustration brief) |
| Cartoons (animation) | screenwriter + director + storyboard + sound + art-director + narrative |
| Films | screenwriter + director + storyboard + edit + sound |
| Scripts | screenwriter (+ narrative for structure) |
| Narrative | narrative |
| Design | the Buro taste/method department |

---

## 9. Language convention

Framework and explanation are in English, and the line runs between **names** and **terms**.

**Every name is Latin.** The studio is `Buro` — never `Бюро`. So is everyone credited:
`Gorbunov's method` (never `метод Бюро Горбунова`), `Lebedev Studio`, Ilyahov, Birman, Tufte.
A name is a label; transliterating it costs the reader nothing and spares them a script they
may not read.

**Terms keep their original form, with an English gloss** — Kovodstvo, info-style /
информационный стиль, ФФФ/FFF, понимание задачи, внутреннее ≤ внешнее, мордоворот. A term
carries knowledge that the English gloss only approximates, so the original stays as the
precise handle and the gloss does the explaining. Translate the term and the precision is
gone; keep the name in Cyrillic and nothing is gained.
