# Buro — architecture

> A **bureau of master seats** bound by one law: subtract decoration never capability, quality
> earned never extracted, every seat both **directs** (method + critique) and **produces** (the
> artifact, self-critiqued). No craft sits above another — words, screen, visual art, games,
> physical / industrial design, marketing, interfaces, product, engineering, reception, leadership
> are peers; their outputs cohere because they share the arbiter, not a subject.

**This is the FREE tier: 17 seats across 12 departments** (+ the `buro` dispatcher and
`selftest`), packaged as the plugin `buro-free@buro-free-dev` — one full-depth seat from every
department, no thinning. The architecture below is the **full studio's** and is kept whole for
reference; the roadmap, the remaining bench, and every seat not in this tier's roster live in
the full commercial studio.

**61 seats across 12 departments** (+ the `buro` dispatcher), packaged as the plugin
`buro@buro-studio-dev`. Seat descriptions are kept lean (always-on ~9.8k tokens); each seat's
full method loads on demand. A blind routing check (`evals/`) covers 75 tasks, 61 of them
look-alike seam pairs; the last recorded blind run scored **53/61** on the cases that existed at
the time; the 14 cases added since await their first blind run.

## Roadmap — planned, not yet built

- **`librarian` — the corpus seat.** Decided 2026-07-24, not built. `buro:docs` owns **the
  document** (its mode, shape and truth); `librarian` would own **the corpus** — where a thing
  lives, how it is addressed, how it is found again: faceted classification over single
  hierarchies (Ranganathan's PMEST; "a growing organism"), hard-limit addressing
  (Johnny.Decimal — 10 areas × 10 categories × 100 IDs), meaning through links (Zettelkasten,
  Matuschak's evergreen notes), action-status layering (PARA), and controlled vocabulary with
  named ownership of tagging quality (DAM practice). Named by role, like `curator` and
  `producer`, because organising a corpus is stewardship rather than a craft.
  **Blocked on two seams before it can be authored:** against `buro:usability`, which already
  owns product information architecture, and against `buro:asset-sourcing`, which procures assets
  but does not shelve them. Sources: `docs/research/2026-07-24-documentation-craft-sources.md`.

- **A ceiling on specification depth — what the target can actually SHOW.** Opened 2026-08-06,
  **deliberately deferred**, and one attempt has already been reverted (`v0.49.0` → `v0.49.1`).

  **The failure.** The design seats specify as though the picture were unlimited, and the target
  system's *visualisation* limits mean a large part of that specification cannot land in the
  finished product. `buro:level` is where it is most visible, because its machinery is the richest:
  a **three-tier landmark hierarchy** whose skyline tier presumes a rendered horizon · `references/
  dressing.md`'s **story-of-use in the wear on a prop**, which presumes the player gets close
  enough, at a resolution where it reads · **seams with foreshadow and echo**, which presume the
  next region is visible in advance · a **region manifest** whose distinctness is checked by
  "a HUD-less screenshot is placeable". None of these asks whether the target renders it. The
  design self-critiques against its own gates, passes, and the divergence surfaces in the build.
  By the studio's own law this is the class of *"a green check that wasn't run"*: a specification
  that cannot be realised, delivered as design.

  **What the fix is NOT.** Not a frame budget, not memory, not milliseconds. Resource optimisation
  is engineering's responsibility and putting it on a design seat is the wrong lane — that is
  precisely what `v0.49.0` got wrong and why it was withdrawn. The correct shape is a **ceiling that
  cuts the seat's own output**: declare what the target can show (view distance and fog, how many
  distinct things read at once, screen size and viewing distance, whether the player ever stops to
  look), then refuse to specify below what lands — an unseen landmark tier is not written, a prop
  function that cannot read on the target screen is not specified. It belongs in each seat's PRODUCE
  self-critique gate and its *slop it kills on sight* list, not as a new required section.

  **Why deferred.** It is sensitive (it touches how every design seat decides how much to say),
  expensive (`buro:level` and `buro:gamedesign` are both over budget and shrink-only, so any gate
  must be paid for by trimming), and it pulls attention off the work in hand. Do it as its own
  spec → plan → build cycle, not as a rider on something else.

- **Multi-engine game engineering.** General, engine-agnostic software (web, backend, CLI,
  library, infra) is covered today by `buro:dev`; Roblox/Luau is covered by
  `buro:roblox-engineering`. Still planned: **game-engine-specific** engineering seats for
  **Unity (C#), Unreal (C++/Blueprint), and Godot (GDScript)** — plus the non-Roblox
  release/devops that comes with them (Steam, console, mobile stores). This is the studio's
  biggest capability ceiling once it moves beyond Roblox; a buro:pm/gamedesign audit ranked it
  the top **WAIT** item (high value, deferred only because current game-engine scope is Roblox).
  It is a multi-seat track, not a one-off, and should get its own spec → plan → build cycle when
  the studio expands past Roblox.

- **Finish the template migration, and verify the routing surface it changed.** Opened 2026-08-03,
  partly built. `v0.45.0` recorded "the last eleven seats migrate to the current template" but
  stopped one department short: the product/business block plus `buro:exotic` were never migrated,
  and nothing checked for it. `check-consistency.py` now has three checks that make this visible —
  §8 `template` (PRODUCE · slop list · a `references/` canon, with named waivers), §9 `desc-length`
  (a description over 1550 chars gets truncated by the harness before its trigger tail), §10
  `seat-size` (a ratchet: `LOAD_BEARING` names the six seats allowed 4000 words, everything else
  holds 2500, and `OVER_BUDGET` records existing debt as shrink-only).

  **Do these in order — the first one verifies work already shipped:**

  | # | Item | Size |
  |---|---|---|
  | 1 | **Re-run the routing eval.** Ten always-on descriptions were rewritten (five heavily) and `surface.txt` regenerated; `evals/routing-results.json` still holds pre-change results. Seventy-two cases, blind, no automated runner (`CLAUDE.md` § Commands). **Until this runs, every routing claim about those seats is unverified.** | 72 cases |
  | 2 | `buro:motion` — trim from ~2900 to ≤2500 | ~5 edits |
  | 3 | `buro:experiment` · `buro:growth` · `buro:retention` · `buro:analyst` — migrate | 4 parts each |
  | 4 | `buro:pm` · `buro:exotic` — migrate | 6 and 8 parts |
  | 5 | `buro:usability` — migrate **last** | 6 parts, ~100 words of headroom |

  **What "migrate" actually means here is bigger than it looks:** none of the seven has a Lenses
  section at all — they are an older generation built on gates alone — so the work is closer to
  re-authoring a seat than to bolting a PRODUCE section on. Thirty-six template sections in total,
  plus a `references/` canon written from scratch for `buro:growth` and `buro:retention`
  (neither has one). Roughly 8–10k words.

  **The two hard ones are hard for the same reason:** `buro:usability` (~2400 words, ~100 of
  headroom) and `buro:analyst` (~2200) must **shed content into `references/` before anything is
  added**, or they blow the 2500 cap the moment PRODUCE lands. `buro:usability` already has a large
  canon to shelve into; `buro:analyst` has a smaller one. Do not start either by writing new prose.

  **Lesson from the two already migrated** (`buro:motion`, `buro:a11y`), worth re-reading before
  the next one: both were first drafted at ~3200 words and both times the instinct was to conclude
  the template has a floor around 2700. It does not. Measured against a compliant seat
  (`buro:verse`, ~2400), `buro:a11y` was **leaner** on lenses and panel — the whole overage sat in
  the preamble, the slop list, and a bloated Reference paragraph. Cut the flab, keep the gates.
  A lens that restates a gate threshold is not a lens; it is the same rule stated twice.

  **Optional, once the above is done:** `skills/a11y/scripts/check_contrast.py`, so that seat's
  "RUN IT" gate has teeth the way `buro:dataviz`'s `validate_palette.py` does — today the gate
  tells the model to run a real keyboard and screen-reader pass and report `UNVERIFIED` otherwise,
  but nothing in the repo can enforce it. Same rule as dataviz: a threshold changed in the script
  is changed in the canon in the same pass.

  **Not required:** the fifteen entries in `OVER_BUDGET`. The ratchet already stops them growing,
  and §10 fails if one drops under its cap without being removed from the list, so the debt cannot
  quietly go stale. Bringing them under is a separate pass that nothing depends on.

- **Rename `buro:roblox-engineering` → `game-engineering`.** Decided 2026-08-02, not built.
  Ties into the multi-engine item above — the intent is a rename/broadening, not a second seat: as
  the studio picks up Unity/Unreal/Godot, name the seat for the discipline (game-engine platform
  engineering) rather than the one platform it started on. Needs the same rename discipline as any
  other seat rename (`CLAUDE.md` § Adding or renaming a seat): every `buro:roblox-engineering`
  reference across rosters, seam rules, docs, and `evals/` updated in the same pass, plus a call on
  whether the Roblox-specific method content stays as-is under the new name or splits into a
  shared cross-engine layer once Unity/Unreal/Godot seats actually exist. Sequencing: likely rides
  along with (or right after) the multi-engine build-out above, not before it.

---

## 1. Principle: two spines, one dispatcher

```
                        ┌─────────────┐
   user  ──────────────▶│    buro     │  top studio dispatcher (plugin entry)
                        │  (studio)   │  reads the task → routes → synthesises
                        └──────┬──────┘
             ┌─────────────────┼──────────────────┐
             ▼                 ▼                  ▼
     TASTE / METHOD SPINE   PROCESS SPINE      ENGINEERING SPINE
     buro seats             buro:process       buro:dev (general software) +
     (what is good, why,    (which phase,      buro:roblox-engineering (Roblox/Luau)
      + produce artifact)    order, gates)      (architecture / TDD / review, in-house)
```

- **Buro owns WHAT and WHY** — the intent, the taste, the honesty laws — including
  "we need a site / a game / a book".
- **Buro owns HOW to build safely, in-house** — `buro:dev` carries the general
  discipline (architecture → tests-first → implement → review → verify → ship);
  `buro:roblox-engineering` carries the Roblox/Luau platform-specific layer on top of it.
- **`buro:process` is the switchman** — on the *build* phase it hands the baton to
  the engineering department, then returns the finished artifact to the relevant Buro
  seats for a critique pass.

The chain is **buro (frame) → dev/roblox-engineering (build) → buro (critique)** — the
studio conducts its own engineering discipline rather than routing it outside the plugin.

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

## 2b. The GENERAL + DELTA pattern

**Decided 2026-08-01**, after a repeated routing collision surfaced it. Some pairs of seats look
like siblings competing for the same finding, but are actually a **general craft** and a
**medium-specific delta** on top of it — the same competence, applied once broadly and once
narrowly, never two competing answers to the same question.

**The shape:** a GENERAL seat owns a competence for *any* medium (structure, visual language,
a11y, data density…). A DELTA seat owns only what a *specific* medium adds on top of that general
competence — it never re-derives the general finding from scratch, and the general seat is never
asked to work the medium-specific execution itself.

**The pairs, as they stand:**
- `buro:gorbunov` / `buro:lebedev` (general interface craft) → `buro:game-ui-designer` (the
  game-specific delta: HUD, real-time pressure, controller focus) and `buro:web-designer` (the
  web/software-specific delta: typography pairing, CSS tokens, the cropped-screenshot test).
- `buro:art-director` (general visual language, any medium) → `buro:web-designer` (the
  web/software-specific execution of that direction).

**Why a routing collision is the tell, not a bug to word around:** when two seats keep getting
confused for the same task no matter how the frontmatter is reworded, check first whether they're
actually a general/delta pair before adding another disambiguating sentence — wordsmithing a flat
seam has a ceiling that a structural fix (naming which seat is general and which is the delta, and
saying so in both directions) doesn't.

**Criterion for a new seat:** before authoring a seat that sounds like "X, but for medium Y," check
whether X already exists as a general competence somewhere in the studio. If it does, the new seat
is a DELTA — its own frontmatter must name the general seat it takes direction from, and the
general seat's frontmatter must name the delta back. A delta seat that never mentions its general
counterpart (or vice versa) is how this collision happens in the first place.

---

## 3. The studio org chart

```
buro  — top studio dispatcher (plugin entry: buro:buro)
│
├─ DEPARTMENT: LEADERSHIP / PRODUCTION                        [NEW]
│    creative-director* · producer* · curator*   (pm lives in Product)
│
├─ DEPARTMENT: TASTE / METHOD — interface craft (Russian-school backbone: lebedev + gorbunov;
│    the rest carry their own canon — Tufte/Cleveland, WCAG, Nielsen/Norman)
│    lebedev · gorbunov · dataviz · exotic · motion · a11y · usability · game-ui-designer ·
│    web-designer
│
├─ DEPARTMENT: PRODUCT / BUSINESS / PROCESS
│    brainstorm · pm · process · experiment · growth · retention
│
├─ DEPARTMENT: INTEL — RESEARCH & INTELLIGENCE                            [NEW]
│    analyst · osint · detective
│    (what is true before you build · whether a claim survives scrutiny ·
│     what went wrong after. osint supplies the evidence analyst reasons from)
│
├─ DEPARTMENT: GAMES & WORLDS
│    gamedesign · combat-designer · narrative · level ·
│    asset-sourcing · live-ops
│
├─ DEPARTMENT: ENGINEERING                                                [NEW]
│    dev (general software) · roblox-engineering (Roblox/Luau platform)
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
│    industrial-designer · cmf · packaging · spatial · manufacturing
│    (specs & briefs; the physical engineering bridge is manufacturing/DFM)
│
├─ DEPARTMENT: MARKETING / COMMS — earning attention honestly             [v0.7.0]
│    campaign · ad-creative · content · launch-pr · sales
│    (de-collided from brand/copy/growth; sales = one-to-one, growth = the system)
│
├─ DEPARTMENT: RECEPTION / STRESS — simulated audience and adversary
│    tester · audience · critic · chaos · emo
│    (emo reads the FELT result: what it makes a person feel, and whether that was the intent)
│
└─ EXECUTION, in-house (sites, game code)
     buro:process ⟶ buro:dev / buro:roblox-engineering (architecture → TDD → review) ⟶ back for critique
```
`*` = new seat to author. `screenwriter` is authored (exemplar/template).

---

## 4. New seats — mandate and dual nature

| Seat | DIRECT (guides) | PRODUCE (emits) |
|---|---|---|
| `buro:creative-director` | one creative vision: makes N seats cohere into a single work; final taste call | vision brief, cross-seat coherence notes, the "north-star" of the piece |
| `buro:producer` | logistics: schedule, resources, dependencies, risk; herds seats to ship | production plan, dependency map, cut-list under deadline |
| `buro:curator` | selection & body-of-work coherence: what's worth doing, what represents the studio | go/no-go call, curation rationale, portfolio coherence review |
| `buro:level` | a world's physical/economic logic, real or invented, down to one playable space, and many such places finished together: layout, encounters, pacing, sightlines, gating, coverage, region identity, seams, set dressing | world map, level layout, encounter beat sheet, flow map, region manifest, seam plan, dressing plan, coverage audit |
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
| `buro:detective` | experiential root-cause: WHEN & WHY a mechanic, location, fun, or beauty broke — bisect the change/playthrough history | root-cause report: the moment, the cause, the fix. Dispatches code regressions to `buro:dev` |
| `buro:osint` | open-source research & verification: the source ladder down to a primary document, then the five checks (provenance, source, date, place, integrity) — perimeter first | evidence file: each fact with its source, archive, retrieval date, confidence, and the one thing that would change it |
| `buro:dev` | architecture, code review, code quality — the contract, the boundary, the test that could have failed | a diff with its failing-first test, run and verified this session; a code review against the twelve lenses |
| `buro:brainstorm` | ideation: reframe the ask, generate genuinely divergent options, name the assumption baked into the question | a reframe note, an option set (mechanism + failure mode per option), a spread check |
| `buro:web-designer` | the beauty pass for web/software UI: name the generic default, commit to a real point of view, pass the cropped-screenshot test | a style direction — palette, type pairing, motion character, illustrative CSS/tokens |

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
   physics/economics→`level`; actual build→`process`→`dev`/`roblox-engineering`).
4. **DIRECT section** — method + canon + critique output format.
5. **PRODUCE section** — how it emits the artifact + a self-critique gate before delivery.
6. **honesty law** — what this seat forbids.
7. `references/` — the discipline's canon.

---

## 7. Buro ⇄ Engineering handoff (in-house)

For any task that needs a real build (code — sites, game code), `buro:process` is the
switchman. It hands off to the **engineering department**, chosen by platform:

**`buro:dev`** — the general, engine-agnostic spine: understand the contract → design the
smallest correct boundary → tests first → implement → review (the twelve lenses) → verify
(run this session) → ship. Covers web, backend, CLI, library, and infra-as-code, in any
language.

**`buro:roblox-engineering`** — the Roblox/Luau platform spine: server authority,
DataStore/remote/shard safety, terrain and physics quirks, AnalyticsService wiring — on top
of the same general discipline, which it dispatches to `buro:dev`.

Routing rule of thumb:
- **Roblox/Luau** → `buro:roblox-engineering` (which still leans on `buro:dev` for the
  general TDD/review layer).
- **Everything else** → `buro:dev` directly.
- `buro:detective` sends *code* regressions to `buro:dev`.

**Return leg (always):** the finished artifact comes back to Buro seats for a taste and
usability critique pass (`usability`, `dataviz`, `a11y`, `motion`, `copy` …) and, on a
multi-seat production, to `creative-director` for coherence.

The engineering department owns build safety and code quality; the rest of Buro owns intent
and the taste critique. Neither re-implements the other.

---

## 8. "Make anything" — medium → seats map

| Medium | Seats engaged |
|---|---|
| Websites | buro (design) + dev (build) + analyst/pm/process |
| Games | gamedesign/narrative/level + buro (HUD) + coder/roblox-engineering (code) + sound/art |
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

**Every name is Latin.** The studio is `Buro` — never transliterated into Cyrillic. So is
everyone credited: `Gorbunov's method` (never transliterated into Cyrillic), `Lebedev Studio`,
Ilyahov, Birman, Tufte.
A name is a label; transliterating it costs the reader nothing and spares them a script they
may not read.

**Terms keep their original form, with an English gloss** — Kovodstvo, info-style /
информационный стиль, ФФФ/FFF, понимание задачи, внутреннее ≤ внешнее, мордоворот. A term
carries knowledge that the English gloss only approximates, so the original stays as the
precise handle and the gloss does the explaining. Translate the term and the precision is
gone; keep the name in Cyrillic and nothing is gained.
