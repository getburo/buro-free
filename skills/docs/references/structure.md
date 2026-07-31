# One home per fact — the doc tree, names, links

> ⚠️ **Mostly synthesis.** The one-home rule and the mode-shaped tree follow from Diátaxis and the
> rot literature; the concrete layout, naming, generated-reference and machine-reader guidance below
> is practitioner consensus with nobody's name on it (see `canon.md` §"Where the canon does not
> reach"). Apply it as a default, not as doctrine.

---

## The rule

**A fact has exactly one home. Every other place that needs it links to that home.**

The reason is not tidiness, it is freshness. A fact in two files can only be *kept* true in one of
them — whoever changes the limit, the flag, the port, the price will find the copy they remember and
leave the other one standing. So the second copy is not redundancy. It is a **stale document entered
on purpose**, and it is more dangerous than an obviously old page, because it looks maintained: same
tone, same authority, same repo, no warning.

Two consequences worth stating separately:

- **Two owners is no owner.** Ownership per gate 7 is per-document; a fact split across two owned
  documents is owned by neither, because each owner reasonably believes the other one handles it.
- **The link is the mechanism, not a courtesy.** If duplication is banned, links carry the load — so
  a broken link is not cosmetic, it is the one-home rule failing. Link checking in CI is therefore
  part of the discipline (`maintenance.md` §docs-as-code), not polish.

## A quantity is a fact, and the rule bites hardest there

**Measured:** *"four numbers for one lane"* — one channel width had four values living in a document,
a builder, a check and a comment, each derived differently, and the project's top verdict rested on
which one you happened to read. Also *"a slot period is not a length fraction"* and *"the sixteen was
an instrument constant"*: same name, different unit, different subject.

- **A number lives once**, in the thing that consumes it — the config, the schema, the source of
  record. Documents cite it; they do not restate it.
- **A derived number names its derivation** beside it — *"47.5 studs = 3.0 s at walkspeed 16"* — so
  that when the input moves, the derived value is visibly stale rather than quietly wrong.
- **A unit is part of the name.** A quantity written without one will be read in whichever unit the
  reader is holding.
- ⛔ **Two numbers for one concept is not a discrepancy to average — it is a finding**, and the fix
  names which is canonical and deletes the other (`buro:experiment` §two instruments disagreeing).

## When a copy is allowed

Three cases, and they are narrow:

1. **A summary plus a pointer.** One line, in the reader's own mode, then the link — "runs on Node
   20 (full matrix: `reference/platforms.md`)". The test: if the canonical fact changes, is the
   summary still *true*? A version number fails that test; "Node 20+" often passes.
2. **A generated copy.** The same fact rendered from one source (an OpenAPI file, a docstring, a
   constant). One home still holds: the **source** is the home, and the rendered page is never
   hand-edited — an edit there is a copy with a countdown to the next build.
3. **A quoted example.** Fine, if it is illustration and marked as such. Not fine when readers start
   using it as the reference, which is what happens when the real reference is hard to find.

Everything else — "it's convenient to have it here too", "the onboarding page should be
self-contained" — is the failure. Self-contained pages are how a corpus goes stale in parallel.

## The tree

Diátaxis claims to settle architecture, not only content. Taken literally, the folder layout **is**
the mode discipline made visible: a document that cannot be filed has not chosen a mode.

```
README.md                  the entrance: what this is, one first success, four doors
CONTRIBUTING.md            how to work on it (a how-to, for a contributor)
CHANGELOG.md               what changed, per release
docs/
  README.md                the index — the map of the four, not a copy of any of them
  tutorials/               learn-by-doing, one path each, ordered
  how-to/                  goal-shaped tasks: restore-a-deleted-branch.md
  reference/               the product's own shape: api/, cli/, config/
  explanation/             why it is like this
  adr/                     0001-use-postgres.md … immutable, superseded not edited
  runbooks/                on-call procedures, drilled on a schedule
```

Local variations are fine (`guides/` for how-to, a docs site's own conventions). What is not fine:

- **`docs/misc/`, `docs/other/`, `docs/notes/`** — where mode collapse hides. A page with no mode
  gets filed here and is never read again.
- **A second docs system** for the same project — a wiki *and* `docs/`, drifting apart on different
  review cycles. Pick the home; make the other one point at it (`maintenance.md` §redirect).
- **A monorepo where every package README restates the root.** Each package README is an *entrance*
  to that package — what it is, how to use it, links out. Not a copy of the build instructions.

## Names

- **How-to and tutorial: the reader's goal, in the reader's words.** `deploy-a-preview-environment.md`,
  not `preview-env-subsystem.md`. The filename is a search result.
- **Reference: the thing's own name.** The endpoint, the flag, the class.
- **ADR: `NNNN-kebab-title.md`,** zero-padded, never renumbered — the number is a permanent address
  that other records cite.
- **No dates in filenames** except for records that are inherently dated (ADRs, post-mortems,
  research captures). A dated filename on a living document is a lie the moment it is edited.
- **Never** `final`, `new`, `v2`, `updated`, `copy`. Each one is a confession that the old file is
  still there, still findable, still wrong.
- Lowercase, hyphens, stable. A renamed file with no redirect breaks every link that was holding the
  corpus together.

## Generated vs hand-written

Reference is the mode most safely generated from source (`modes.md`). A healthy shape is **generated
reference + hand-written tutorials, how-tos and explanation**; generated *everything* is a corpus
with no way in, because nothing tells a newcomer where to start.

- The generated tree is separate and marked generated, with the source named at the top.
- Never hand-edit inside it. A fix belongs in the docstring or schema — that is the home.
- What generation cannot produce: the first success, the reason, the error the reader will actually
  hit. If those are missing, the docs are not "auto-generated", they are absent.

## Diagrams

One diagram often beats three paragraphs — and rots the same way, but invisibly, because nobody
diffs an image.

- **Text-source diagrams in the repo** (Mermaid, Graphviz, PlantUML), beside the document, rendered
  by the build. Reviewable in a pull request, editable by whoever changes the system.
- A binary export whose editable source lives in someone's private account is **unmaintainable by
  design** — when they leave, the diagram is frozen and slowly becomes fiction.
- Screenshots are the highest-rot content there is. Use them where the UI is the subject, date them,
  and expect to replace them every release.

## The machine reader

A repository's documents are now read by agents as well as people (`AGENTS.md`, `CLAUDE.md`, a tool
manifest, a docs site scraped into a model's context). This does not create a new craft — every rule
above holds — but two things change:

- **A machine reader cannot ask a colleague.** It will believe the stale copy and act on it, at
  speed, without the hesitation a human feels when a doc smells wrong. Duplication costs more here,
  not less.
- **An agent file is a document with a reader**: one mode (it is a how-to for building in this repo),
  one home, dated, owned. It must not become a drifting second copy of the README — it links to the
  README, or the README links to it, and the fact lives once.

Beyond that: the vocabulary, addressing and search of a corpus **across** projects is the queued
`librarian` seat's subject, not this one's. This file stops at the edge of one repository.
