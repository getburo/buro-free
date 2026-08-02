# Open-World Systems — Reference

Depth behind SKILL.md's Lens 15 (Reactivity) and Lens 16 (Ambient Life). Open this when the design is an open world that has to feel *alive* — where the value isn't a single loop but a place that behaves on its own.

⚠️ **Synthesis, not citation.** These are best practices distilled from four studios' shipped open worlds, not a single theorist's framework. The named games are the evidence; the principles are this seat's reading of what they do well. Three seats split this material and must not duplicate it:
- **`buro:gamedesign` (here)** — how the world *behaves*: reactivity, emergent systems, ecology-as-mechanics.
- **`buro:level`** — the *distribution*: who and what populates the map, and why (its "Populating a World" canon section).
- **`buro:narrative`** — the *content*: each point of interest as an authored story (its "Hand-Authored Point of Interest" canon section).

**Table of contents:**
- [Reactivity — the world registers you](#reactivity--the-world-registers-you-rockstar)
- [Ambient Life — the world runs on its own](#ambient-life--the-world-runs-on-its-own-rockstar)
- [Ecology as Mechanics](#ecology-as-mechanics-guerrilla--horizon)
- [The Emergent-Threat System](#the-emergent-threat-system-bend--days-gone)
- [The Same Systems at Solo-Dev Scale](#the-same-systems-at-solo-dev-scale-isocore)
- [The honesty line](#the-honesty-line) · [Sources](#sources)

---

## Reactivity — the world registers you (Rockstar / Take-Two, *RDR2*, *GTA V*)

The defining property of a Rockstar world: **almost every action the player takes gets an acknowledgment.** Draw a weapon in a town and pedestrians flee and a lawman reacts; commit a crime and a wanted state escalates with a real cost; treat an NPC well or badly and the honor/reputation system remembers. None of these is deep in isolation — the *density* of them is the point. The player learns, within minutes, that **the world is listening**, and that belief is what makes every subsequent action feel weighted.

The inverse is the dead open world: a beautiful map where the player can do anything and the world responds to nothing. The mechanic is technically present (you *can* fire the gun) but the world is inert around it, and the player quickly concludes — correctly — that their actions don't matter here.

**Design test (Lens of Reactivity):** name three things the player can do *to* the world, and what the world does back within five seconds. Fewer than three concrete answers → you have scenery with a skin of interactivity, not a reactive system. The fix is rarely "add a bigger system" — it's usually "acknowledge the small actions the player already takes."

**Cost note:** reactivity is expensive because it's *broad, not deep* — many small acknowledgments, each cheap alone, adding up to a felt whole. Budget it as breadth. One deep reactive system (a full faction-reputation web) impresses less than ten shallow ones (NPCs flinch, weather reacts, animals scatter, lawmen escalate) because the player samples breadth constantly and depth rarely.

---

## Ambient Life — the world runs on its own (Rockstar, *RDR2*)

Reactivity is the world responding *to* the player. **Ambient life is the world doing things whether or not the player is there.** NPCs in *RDR2* keep schedules — they wake, work, drink, sleep; weather rolls through on its own clock; animals hunt and are hunted; a random encounter on the road wasn't placed for *this* player at *this* moment, it emerged from systems running in the background.

The test that separates a living world from a stage set: **have the player stand still and do nothing for two minutes.** In a living world, a story happens anyway — a stranger passes, a storm breaks, a predator takes a deer. In a stage set, nothing moves until the player pulls a lever, and the illusion collapses.

**Emergence, not triggers.** A scripted event fires the same way every time from a fixed trigger; an emergent event is the *intersection* of independent systems (an NPC's schedule + weather + the player's location) and is different each time. Emergent encounters are cheaper per-hour-of-content than scripted ones *and* feel more alive — but only if the underlying systems are legible enough that the player reads the emergence as a world, not as randomness. If the player can't tell why something happened, emergence reads as noise.

---

## Ecology as Mechanics (Guerrilla — *Horizon Zero Dawn*)

*Horizon* fuses the living-world idea with the core combat loop: the machines aren't a spawn table, they're an **ecology that is also the mechanics.**

- **Niches.** Grazers harvest resources and move in herds; mid-tier machines patrol and defend; apex machines hunt. Each occupies a role, and the player reads the landscape like a habitat — herd here, predator there.
- **The distribution is the telegraph.** You know a region is dangerous before a fight starts, because of *what lives there*. The world's population doubles as its difficulty signposting — no UI needed.
- **Weak points and resource loops.** Each machine is a puzzle of exposed components; hitting the right part both wins the fight faster and *harvests the resource* that part represents. Combat, economy, and ecology are one system, not three bolted together.

The transferable principle: when the things that populate your world are **systems with legible roles and legible weak points**, the world's population and its mechanics reinforce each other instead of competing for the player's attention. (The *placement* of that ecology across the map — who lives where and why — is `buro:level`'s Lens of the Living System; how each creature *fights* is here.)

---

## The Emergent-Threat System (Bend — *Days Gone*)

*Days Gone*'s horde is the cleanest example of an **emergent-threat system**: a large, dynamic population of enemies whose behavior — pathing, swarming, splitting, funneling through chokepoints — is a real-time system, not a scripted set-piece. Drawing a horde is a self-set challenge with dynamic difficulty: the player chooses when and where to engage, uses the terrain (chokepoints, explosives, traps), and the encounter plays out differently every time because the swarm *reacts*.

Why it works as game design:
- **The threat has a place in the world** (it migrates between feeding and nesting sites — see `buro:level`), so encountering it feels like meeting the world's own logic, not a trigger.
- **The player authors the encounter.** When and how to fight the horde is a meaningful choice with a real tradeoff (Lens 3) — engage unprepared and it's lethal; prepare the ground and it's a triumph of mastery (Lens 7), not a scripted win.
- **Uncertainty from an opponent, not a die roll** (Lens 4). The swarm's exact behavior is unknown but *systemic*, so the player can read and outplay it — the best source of uncertainty, not the worst.

The transferable principle: a single well-tuned emergent-threat system can carry more felt content than a dozen scripted encounters, because it generates a new story each time the player chooses to engage. This is the systemic spine a *Days Gone*–style survival world is built on.

---

## The Same Systems at Solo-Dev Scale (Isocore)

Everything above is drawn from AAA teams of dozens to hundreds. The same *shape* of system —
population that runs itself instead of being hand-placed — is achievable by a single developer,
just built smaller and cheaper. *Isocore*, a solo-developed 2D open-world survival game, is a
useful reference precisely because its population system is legible at a scale one person can
actually reason about end to end:

- **One shared base class, many derived creatures.** A single "mob" base class carries the
  behaviour every creature needs (movement, basic AI, animation, event handling); each specific
  creature is a small derived class on top of it. This is what makes a varied population
  affordable for one developer — the shared 80% is written once.
- **Per-region population caps as homeostasis, not hand-placement.** Rather than placing
  creatures by hand, a spawner tracks a friendly-population and hostile-population count per
  region and tops each up toward a target when it's under, with no manual authoring per spawn.
  This is the solo-scale version of Rockstar-style ambient life above: cheap to build, and it
  keeps a hand-built world from feeling over- or under-populated as the player moves through it.
- **Every creature earns a resource role, not just a cosmetic one.** A creature added purely for
  atmosphere (ambient insects, frogs) is legitimate, but the ones tied to player-facing systems
  (a resource only obtainable from a specific animal) do double duty — population *and* economy
  from one asset, which matters when every asset is expensive to make alone.
- **Soft difficulty layers over the population, not just harder enemies.** An energy meter that
  degrades a player's effectiveness rather than killing them outright, and a biome-linked
  temperature hazard mitigated by the environment itself (water cools, shelter warms), are both
  ways of adding pressure to an open world without requiring more hand-built content — the
  systems create the tension, not new areas.

**Criterion:** for a solo or small-team open world, is population handled by a system with a
shared base and a target-driven spawner, or is every instance hand-placed? Hand-placement caps
how large and varied a world can afford to be for one person; a homeostatic spawner scales past
that ceiling at a fixed, one-time cost.

## The honesty line

Everything here still passes Compliance (gate 8). A reactive, living world earns the player's return through **mastery and discovery** — I got better at reading the ecology, I want to see what the world does next — not through anxiety, timers, or FOMO. The dark-pattern version is a "living world" whose systems exist to manufacture missable events the player feels guilty for skipping. Emergence in service of *the player's* curiosity: honest. Emergence in service of *retention metrics* at the player's expense: `buro:retention`'s honesty law vetoes it, same as any other extraction.

---

## Sources

Synthesis — the shipped games are the evidence, not a single cited framework:

- **Rockstar Games / Take-Two Interactive** — *Red Dead Redemption 2* (2018), *Grand Theft Auto V* (2013): systemic reactivity, NPC schedules, ambient/emergent life, diegetic density.
- **Guerrilla Games** — *Horizon Zero Dawn* (2017): machine ecology as mechanics, weak-point/resource loops, ecology-as-difficulty-signposting.
- **Bend Studio** — *Days Gone* (2019): the horde as an emergent-threat system, player-authored encounters, systemic swarm AI.
- **CD Projekt Red** — *The Witcher 3* (2015), *Cyberpunk 2077* (2020): the no-filler content philosophy that the *narrative* seat owns; cited here for the reactivity of its choice-consequence webs.
- **Isocore** (solo-developed, in progress) — the same population-system shape (shared base class, target-driven per-region spawner, resource-tied creatures, soft difficulty layers) built and documented at a one-person scale; cited via the developer's own devlog.

For the placement/distribution half of this material, see `buro:level` → `references/canon.md`, "Populating a World." For the authored-content half, see `buro:narrative` → `references/canon.md`, "The Hand-Authored Point of Interest."
