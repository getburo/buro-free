# Documentation & organisation craft — named-source research (2026-07-24)

Research pass for the queued `buro:docs` seat. Eight searches, four primary sources fetched.
Purpose: raw named-source material to distil into a seat (lenses + canon), across the four
domains the brief named — **software docs, game-dev docs, an undifferentiated pile, and
organising a library**.

> **The brief spans two crafts, not one.** Domains 1–2 are about **authoring a document**
> (what to write, in which mode, and how to keep it true). Domains 3–4 are about **organising a
> corpus** (where a thing lives, how it is addressed, how it is found again). They share an
> arbiter — *can the right person find and trust the right thing at the moment they need it* —
> but they produce different artifacts: prose versus a scheme. See §5 for the seat question.

> **Source strength is uneven.** STRONG (named authors, primary sites, books): Diátaxis,
> Carroll's minimalism, Nygard's ADRs, Ranganathan, Johnny.Decimal, Matuschak. MEDIUM
> (practitioner consensus, no single canonical source): docs-as-code, documentation rot, DAM
> taxonomy. WEAK (vendor blogs and SEO content, mutually copying): game-dev documentation —
> see §2's warning.

---

## 1. Software documentation — STRONG

- **Daniele Procida, *Diátaxis* (2020, diataxis.fr)** — *confidence: high.* Four distinct user
  needs produce **four distinct forms**: **tutorial** (learning, practical), **how-to guide**
  (working, practical), **reference** (working, theoretical), **explanation** (learning,
  theoretical). Organised on two axes — *studying vs working* and *practical vs theoretical*.
  The name is Greek: *diá* "across" + *táxis* "arrangement". Its own claim is that it addresses
  three things at once: **content** (what to write), **style** (how to write it) and
  **architecture** (how to organise it). Origin: Django CMS docs, where topic-based structure
  proved arbitrary — "a list of features doesn't show someone how to solve a problem". Adopted
  by Django, Canonical, Cloudflare, Gatsby.
  **The lens it gives:** *which of the four is this document trying to be?* The dominant failure
  is a single page attempting all four and serving none — a tutorial interrupted by reference
  tables, a reference padded with rationale.
  ⚠️ The primary site does **not** explicitly warn against mixing modes; the "never mix" rule is
  a practitioner reading of it, widely repeated. Treat the separation as the framework's
  structure, and the prohibition as the seat's own position.

- **John M. Carroll, *The Nurnberg Funnel* (MIT Press, 1990) and *Minimalism Beyond the Nurnberg
  Funnel* (MIT Press, 1998)** — *high.* **Minimalism** as an action- and task-oriented doctrine:
  explicit instruction is *severely reduced*, learners proceed by guided exploration on realistic
  tasks. Measured result cited across the literature: minimal manuals average **~3 pages per
  chapter** against the systems-approach manuals they replaced. **Error recovery is a first-class
  subject**, not an appendix — documentation anticipates the errors a real user will make and
  says how to get out. The title is a joke at the expense of the mythical Nuremberg funnel that
  pours knowledge into a head.
  **The lens it gives:** *what did the reader want to DO?* Prose that delays the first real action
  is not thoroughness, it is a toll.

- **Michael Nygard, "Documenting Architecture Decisions" (2011) → ADRs (adr.github.io)** — *high.*
  Deliberately **lightweight**, one record per architecturally significant decision, answering one
  question: **why did we do it this way?** Nygard's argument is двойной: **nobody reads large
  documents**, and **not knowing the rationale causes later decisions that defeat earlier ones**.
  "Architecturally significant" is defined as affecting structure, non-functional characteristics,
  dependencies, interfaces, or construction techniques. Practitioner consensus in the sources:
  the teams that get value are the ones that **resist expanding an ADR into something grander**.
  **The lens it gives:** the decision record is the only document whose value *increases* with
  age — and the only one that must never be edited to match a later opinion.

- **Docs-as-code (Write the Docs; broad practitioner consensus)** — *medium; no single canonical
  author.* Docs in plain-text markup (Markdown / reStructuredText / AsciiDoc), in Git, reviewed
  like code, built and published by CI, with automated link and style checks.

- **Documentation rot** — *medium, consensus.* Defined as **the gradual divergence between
  documented behaviour and actual behaviour**, arising when code, configuration or API contracts
  move and the docs don't. Named costs: onboarding friction, support overhead, review confusion.
  The consensus prescription is **not** a cleanup project but a maintenance regime: docs reviewed
  in the same cycle as code; one source recommends **executing the documentation against staging**
  (runbook drills) "to find rot before incidents find it".
  **The lens it gives:** *what is the freshness evidence?* An undated, unowned, never-executed
  document is a claim about the past.

## 2. Game-development documentation — WEAK sourcing, useful shape

⚠️ **Sourcing warning.** Unlike §1, this domain produced **no primary-author canon**: the results
are vendor blogs (Nuclino, Document360, Tekrevol), tutorial sites, and a secondhand summary of a
talk. Claims below are practitioner *consensus shape*, not verified doctrine. Do not present them
in a seat as named canon; either find primary sources (GDC vault, studio postmortems) or mark
them as synthesis.

- **The GDD's death is misreported.** Consensus across sources: the **rigid 100-page static
  document** is gone — "hardly ever read", expensive to maintain — but design documentation as
  such is not. It moved to **living, collaborative, wiki-shaped** artifacts.
- **The one-pager is the load-bearing artifact early on.** Carries the pitch, the design pillars,
  the core loop, the key mechanic, the look, the platform — nothing more. The stated reason it
  works is economic: **cheapest to write and cheapest to throw away**, which matters precisely
  when ideas still move fast.
- **A game studio's document set is plural, not one bible.** Recurring across sources: **GDD**
  (the design vision), **TDD / technical design document** (stack, tools, architecture), **art
  bible** (the visual vision — and often the *technical* art constraints so assets survive the
  engine), **pipeline docs** (how to actually make content: set up a level, author a weapon, add
  a spell), and an onboarding knowledge base.
- **The stated purpose of pipeline and onboarding docs is knowledge-loss defence** — getting a new
  team member productive, and surviving turnover.
  **Seam note:** the art bible already belongs to `buro:art-director`, and the GDD's *content*
  belongs to `buro:gamedesign`. What a docs seat owns here is the **document**, not the design:
  its mode, its size, its freshness, whether it is the cheap one-pager or the expensive bible.

## 3. The undifferentiated pile — STRONG

- **Andy Matuschak, "Evergreen notes" (notes.andymatuschak.org)** — *high.* Notes that **"evolve,
  contribute, and accumulate over time, across projects"**. Five stated properties: **atomic**,
  **concept-oriented**, **densely linked**, **preferring associative ontologies over
  hierarchies**, **written in your own voice for yourself**. The central argument is a rebuke to
  the whole genre: **"'Better note-taking' misses the point; what matters is better thinking."**
  Names the failure mode directly — scattered notes in many places mean "you rely heavily on your
  brain to remember where and when these notes were written down", which is the one job the
  system was supposed to do.
- **Zettelkasten (Luhmann tradition)** — *medium-high.* Emergent structure from **explicit links
  that carry meaning** — the link says *why* two things connect. Suited to research writing.
- **PARA (Tiago Forte)** — *medium.* **Projects / Areas / Resources / Archive**: ranks material by
  **action-need**, from "needs action now" to "store for later". The sources' honest assessment:
  PARA fits **active project work**, and fits recall or brainstorming badly.
- **Comparative finding worth keeping:** these systems are **not rivals but layers** — the
  practitioner pattern is Johnny.Decimal for *address*, PARA for *action-status*, Zettelkasten /
  evergreen for *meaning*. A seat that picks one and forbids the others would be picking a
  religion, not a method.

## 4. Organising a library — STRONG

- **S. R. Ranganathan, *Colon Classification* (1933) and *The Five Laws of Library Science*
  (1931)** — *high.* **Faceted classification**: instead of one enumerated hierarchy, a subject is
  decomposed into fundamental categories — **PMEST: Personality, Matter, Energy, Space, Time** —
  and classes are *constructed* rather than looked up. The stated advantage over enumerative
  schemes is that facets accommodate **several points of view on the same subject**. The Five Laws
  supply the ethics: user-centred service and — the one that matters most here — **the library is
  a growing organism**, i.e. the scheme must be designed to be extended, not sealed.
  **The lens it gives:** *is this one hierarchy pretending a thing has one nature?* Most folder
  trees fail because an item honestly belongs in three places at once; facets say that is not an
  error to resolve but a fact to encode.
- **Johnny.Decimal (johnnydecimal.com)** — *high, primary.* Hard structural limits, and the limits
  *are* the method: **no more than 10 areas; no more than 10 categories per area; no more than 100
  IDs per category.** Address form is fixed — two digits, a decimal, two digits (`21.34`); the
  digits before the decimal are the category. Stated problem: information scattered "across
  disparate systems" (mail, SharePoint, Teams), so the ID travels **without requiring
  centralisation**. Stated mechanism: at every step you choose among **no more than ten** things.
  ⚠️ The homepage does not state the limits; they are in the concepts documentation. Cite the
  documentation, not the landing page.
- **DAM taxonomy practice** — *medium, vendor-sourced but consistent.* Three components recur:
  **controlled vocabulary** (a standardised term list, so everyone uses the same words),
  **naming conventions**, and a taxonomy that is either **nested** (hierarchy) or **flat**.
  The governance finding is the useful one: **metadata only works if applied consistently**, so a
  scheme must name required vs optional fields **and who owns tagging quality** — an untended
  vocabulary decays into synonyms.

## 4b. The official layer — standards and house style guides — STRONG

Missed on the first pass because the search was aimed at practice, not at standards. This is the
layer that gives the seat a *process* canon, not only a form canon.

- **ISO/IEC/IEEE 2651x series — "information for users"** — *high.* A role-split family of
  standards covering user documentation across the software life cycle:
  **26511** (managers — documentation plans and management), **26512** (acquirers and suppliers),
  **26513** (testers and reviewers), **26514** (designers and developers — specifies **structure,
  content and format**, with informative style guidance), **26515** (developing user documentation
  **in an agile environment**). The series positions itself against ISO/IEC 12207 / 15288 life
  cycle processes.
  **The lens it gives — and the reason this matters most:** the existence of **26513** is the
  official statement that documentation is **reviewed and tested**, not merely written. That is
  the same claim the rot literature makes from practice, with a standards body behind it.
- **Google developer documentation style guide** (developers.google.com/style) — *high.* Public,
  actively maintained (last updated December 2025); editorial guidance curated for ease of
  understanding, accessibility, localization and globalization.
- **Microsoft Writing Style Guide** — *high.* The other industry de-facto; covers documentation,
  apps, websites and whitepapers, and is explicitly usable for non-Microsoft material.

**Consequence for the seat:** the canon now has three layers — **process** (ISO 2651x: roles,
planning, review and test), **form** (Diátaxis: the four modes), **manner** (Carroll's minimalism;
Google / Microsoft for style). It also sharpens §2's gap: software documentation has an ISO
standard; game-development documentation has not one named primary work.

**Nothing official exists inside Claude Code for this craft.** Checked on 2026-07-24: the bundled
skill set contains exactly one skill (`dataviz`), and the official plugin marketplace's 22 skills
(superpowers, skill-creator, frontend-design, mcp-server-dev, claude-md-management, playground…)
include nothing on documentation or on organising a corpus. Unlike `buro:dataviz`, this seat has
no adjacent official implementation to adapt — and correspondingly no provenance question.

## 5. The seat question this research forces

The four domains do not divide the way the brief's phrasing suggests. They split into:

- **Authoring** (§1, §2) — mode (Diátaxis), size and delay-to-action (Carroll), rationale that
  must not be rewritten (Nygard), freshness (rot), and the game-dev document set. Produces
  **prose**.
- **Organising** (§3, §4) — address (Johnny.Decimal), facets vs hierarchy (Ranganathan), meaning
  through links (Matuschak/Zettelkasten), action-status (PARA), controlled vocabulary and
  tagging ownership (DAM). Produces **a scheme**.

They share one arbiter — *the right person finds and trusts the right thing at the moment of
need* — and they fail in mirror ways: authoring fails by writing what nobody needed; organising
fails by filing where nobody looks.

**Settled 2026-07-24: two seats.** `buro:docs` (authoring — built first, its canon is complete)
and a queued **`librarian`** seat (the corpus: address, facets, links, vocabulary and its
governance). Named by role, like `curator` and `producer` — the studio names *craft* seats after
the subject and *stewardship* seats after the role, and organising a corpus is stewardship. The
librarian seat is decided but **not built**: it needs its own seam against `buro:usability`
(which already owns product information architecture) and against `buro:asset-sourcing` (which
procures assets but does not shelve them).

Existing seams either way: product IA and navigation → `buro:usability`; the *design* inside a
GDD → `buro:gamedesign`; the art bible's *content* → `buro:art-director`; UI strings →
`buro:copy`; editing existing text → `buro:editor`; narrative non-fiction → `buro:prose`;
asset procurement and vetting (not shelving) → `buro:asset-sourcing`.

## Open questions carried forward

- **Game-dev documentation has no verified primary canon** (§2). Either mine the GDC vault and
  studio postmortems for named sources, or the seat marks that section synthesis and says so.
- **Release notes / changelogs** were not researched this pass. `buro:live-ops` currently sends
  patch notes to `buro:copy`; whether they land in a docs seat is undecided and unsourced.
- **API reference generation** (OpenAPI, docstring extraction) was not researched — the boundary
  between generated and written reference is unexamined.
- **Whether "one seat or two"** (§5) can be settled by the seams checklist alone, or needs a
  `buro:curator` pass like the dataviz decision did.

## Sources

Diátaxis — https://diataxis.fr/ · https://simonwillison.net/2021/Aug/21/diataxis/ ·
https://idratherbewriting.com/blog/what-is-diataxis-documentation-framework
Carroll, minimalism — https://mitpress.mit.edu/9780262512954/minimalism-beyond-the-nurnberg-funnel/ ·
https://www.researchgate.net/publication/3229757_John_Carroll's_The_Nurnberg_Funnel_and_Minimalist_Documentation
ADRs — https://adr.github.io/ · https://www.redhat.com/en/blog/architecture-decision-records ·
https://github.com/peter-evans/lightweight-architecture-decision-records
Docs-as-code & rot — https://www.writethedocs.org/guide/docs-as-code/ ·
https://docsalot.dev/blog/documentation-rots-heres-how-to-stop-it · https://www.stew.so/blog/documentation-rot-devops
Game-dev docs (weak) — https://www.nuclino.com/articles/write-game-design-document ·
https://kreonit.com/idea-generation-and-game-design/9-essential-types-of-game-design-documents-insights-from-alexey-savchenko/ ·
https://en.wikipedia.org/wiki/Game_design_document · https://www.gamedevpensieve.com/design/design_documents
Evergreen notes / PKM — https://notes.andymatuschak.org/Evergreen_notes ·
https://en.wikipedia.org/wiki/Zettelkasten · https://www.atlasworkspace.ai/blog/note-taking-systems-compared
Ranganathan — https://www.librarianshipstudies.com/2019/02/s-r-ranganathan.html ·
https://www.redalyc.org/journal/3843/384357586006/html/ · https://grokipedia.com/page/Faceted_classification
Johnny.Decimal — https://johnnydecimal.com/ · https://johnnydecimal.com/documentation/philosophy ·
https://www.dsebastien.net/2022-04-29-johnny-decimal/
DAM taxonomy — https://www.bynder.com/en/blog/building-digital-asset-library-taxonomy/ ·
https://www.assetbank.co.uk/blog/taxonomies-metadata-for-digital-asset-management ·
https://www.orangelogic.com/blog/digital-asset-taxonomy-best-practices
