# Open-World Systems — Reference

Depth behind SKILL.md's Lens 15 (Reactivity) and Lens 16 (Ambient Life). Open this when the design is an open world that has to feel *alive* — where the value isn't a single loop but a place that behaves on its own.

⚠️ **Synthesis, not citation.** These are best practices distilled from four studios' shipped open worlds, not a single theorist's framework. The named games are the evidence; the principles are this seat's reading of what they do well. Three seats split this material and must not duplicate it:
- **`buro:gamedesign` (here)** — how the world *behaves*: reactivity, emergent systems, ecology-as-mechanics.
- **`buro:worldbuilding`** — the *distribution*: who and what populates the map, and why (its "Populating a World" canon section).
- **`buro:narrative`** — the *content*: each point of interest as an authored story (its "Hand-Authored Point of Interest" canon section).

**Table of contents:**
- [Reactivity — the world registers you](#reactivity--the-world-registers-you-rockstar)
- [Ambient Life — the world runs on its own](#ambient-life--the-world-runs-on-its-own-rockstar)
- [Ecology as Mechanics](#ecology-as-mechanics-guerrilla--horizon)
- [The Emergent-Threat System](#the-emergent-threat-system-bend--days-gone)
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

The transferable principle: when the things that populate your world are **systems with legible roles and legible weak points**, the world's population and its mechanics reinforce each other instead of competing for the player's attention. (The *placement* of that ecology across the map — who lives where and why — is `buro:worldbuilding`'s Lens of the Living System; how each creature *fights* is here.)

---

## The Emergent-Threat System (Bend — *Days Gone*)

*Days Gone*'s horde is the cleanest example of an **emergent-threat system**: a large, dynamic population of enemies whose behavior — pathing, swarming, splitting, funneling through chokepoints — is a real-time system, not a scripted set-piece. Drawing a horde is a self-set challenge with dynamic difficulty: the player chooses when and where to engage, uses the terrain (chokepoints, explosives, traps), and the encounter plays out differently every time because the swarm *reacts*.

Why it works as game design:
- **The threat has a place in the world** (it migrates between feeding and nesting sites — see `buro:worldbuilding`), so encountering it feels like meeting the world's own logic, not a trigger.
- **The player authors the encounter.** When and how to fight the horde is a meaningful choice with a real tradeoff (Lens 3) — engage unprepared and it's lethal; prepare the ground and it's a triumph of mastery (Lens 7), not a scripted win.
- **Uncertainty from an opponent, not a die roll** (Lens 4). The swarm's exact behavior is unknown but *systemic*, so the player can read and outplay it — the best source of uncertainty, not the worst.

The transferable principle: a single well-tuned emergent-threat system can carry more felt content than a dozen scripted encounters, because it generates a new story each time the player chooses to engage. This is the systemic spine a *Days Gone*–style survival world is built on.

---

## The honesty line

Everything here still passes Compliance (gate 8). A reactive, living world earns the player's return through **mastery and discovery** — I got better at reading the ecology, I want to see what the world does next — not through anxiety, timers, or FOMO. The dark-pattern version is a "living world" whose systems exist to manufacture missable events the player feels guilty for skipping. Emergence in service of *the player's* curiosity: honest. Emergence in service of *retention metrics* at the player's expense: `buro:retention`'s honesty law vetoes it, same as any other extraction.

---

## Sources

Synthesis — the shipped games are the evidence, not a single cited framework:

- **Rockstar Games / Take-Two Interactive** — *Red Dead Redemption 2* (2018), *Grand Theft Auto V* (2013): systemic reactivity, NPC schedules, ambient/emergent life, diegetic density.
- **Guerrilla Games** — *Horizon Zero Dawn* (2017): machine ecology as mechanics, weak-point/resource loops, ecology-as-difficulty-signposting.
- **Bend Studio** — *Days Gone* (2019): the horde as an emergent-threat system, player-authored encounters, systemic swarm AI.
- **CD Projekt Red** — *The Witcher 3* (2015), *Cyberpunk 2077* (2020): the no-filler content philosophy that the *narrative* seat owns; cited here for the reactivity of its choice-consequence webs.

For the placement/distribution half of this material, see `buro:worldbuilding` → `references/canon.md`, "Populating a World." For the authored-content half, see `buro:narrative` → `references/canon.md`, "The Hand-Authored Point of Interest."
