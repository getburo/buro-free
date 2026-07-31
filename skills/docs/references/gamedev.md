# The game-development document set

> ⚠️ **This file is synthesis, not canon.** Unlike the rest of this seat — which rests on named
> work (Procida, Carroll, Nygard, ISO/IEC/IEEE 2651x) — game-development documentation produced
> **no primary-author sources** in research (see `docs/research/2026-07-24-documentation-craft-
> sources.md` §2). What follows is practitioner consensus: a useful shape, repeatedly described,
> with nobody's name on it. Present it as such. Do not cite it as doctrine, and if a primary
> source turns up, this file gets rewritten around it.

---

## The misreported death

"The GDD is dead" is a misreading. What died is the **rigid hundred-page static document** written
up front and read by nobody — expensive to write, more expensive to maintain, obsolete by the time
it was bound. Design documentation itself did not die; it became **living, collaborative, and
plural**, usually wiki-shaped.

The correction matters because both errors are common and both are expensive: teams that keep
writing the bible waste months on a document that ages faster than the build, and teams that
conclude documentation is obsolete lose the knowledge when a person leaves.

## The one-pager, and why it is load-bearing

Early on, the one-pager is the right artifact, and the reason is economic rather than aesthetic:
**it is the cheapest thing to write and the cheapest thing to throw away.** That combination is
exactly what a phase of fast-moving ideas needs — a document you cannot bear to discard will
distort the design to stay true.

Carries, and nothing more: the pitch, the design pillars, the core loop, the key mechanic, the
look and feel, the platform.

## The set, and who owns what

A studio does not have "the document". It has a set, each with a different reader:

| Document | Reader | Owns the **content** | This seat owns |
|---|---|---|---|
| **One-pager** | everyone, at the start | `buro:gamedesign` | its size and its ruthlessness |
| **GDD** (living) | the team, continuously | `buro:gamedesign` | its mode, shape, freshness |
| **Technical design doc** | engineers | the engineering seat | structure, decisions recorded |
| **Art bible** | artists, outsourcers | `buro:art-director` | that it is usable as a reference |
| **Pipeline docs** | whoever makes content | the discipline lead | that the steps were executed |
| **Onboarding / knowledge base** | the person who joined Monday | shared | the whole thing |

**The seam that keeps this seat honest:** the *design* is not this seat's. The core loop belongs
to `buro:gamedesign`, the visual language to `buro:art-director`. This seat owns the **document** —
which mode it is, how big it is, whether it is the cheap one-pager or the expensive bible, whether
it is still true, and whether the person who joined on Monday can use it.

## Pipeline docs are how-tos, and they rot fastest

"How to set up a level", "how to author a weapon", "how to add a spell" are **how-to guides** in
the strict sense: a competent reader, a specific goal, an interrupted task. Everything in
`modes.md` applies — goal-shaped title, prerequisites as a checklist, numbered steps, error
recovery inline.

Their skeletons — one-pager, GDD, TDD, pipeline doc, onboarding path — are in `templates.md`.

They also rot faster than anything else in a studio, because tools and engine versions move
weekly. They are the strongest candidate for the execute-it discipline in `maintenance.md`:
someone who did not write the doc makes the thing by following it, on the current build.

## The stated purpose of onboarding docs is knowledge-loss defence

Not tidiness, not process. Games are made by teams with turnover, on tools that only a few people
understand deeply, over years. Pipeline and onboarding documentation exists so that a departure
is a scheduling problem instead of a capability loss.

The test is therefore behavioural, not editorial: **someone who joined last week, whose mentor
has left, ships something real by Friday using only what is written.** A document set that passes
that is good regardless of its prose; one that fails it is decorative regardless of its polish.

## Patch notes and release notes

Player-facing patch notes are a **document** and belong here: what changed, in plain language,
where players will see it. The reader is a player who wants to know whether their build, their
strategy, or their bug got touched.

- Plain language over jargon. A changelog nobody can parse is a note that did not communicate.
- **"Bug fixes and improvements" is not an entry.** It is the absence of one.
- Say what changed *for the player*, then what changed underneath — not the reverse.
- Nerfs and removals get named, not buried. Hiding them costs more trust than the change does.

Seams: the **cadence** of updates, the event calendar and the incident comms are `buro:live-ops`;
the in-product "what's new" panel is a **string** and belongs to `buro:copy`; the launch narrative
and press angle are `buro:launch-pr`. The document itself is this seat's.
