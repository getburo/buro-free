# Documentation · canon — the sources behind the lenses

Compressed reference for the `buro:docs` seat. Tools, not rules.

The canon here has three layers, and a seat that uses only one of them will be lopsided:
**form** (which document is this), **manner** (how it is written), **process** (how it is planned,
reviewed, tested and kept true).

## Procida — Diátaxis (form)

Daniele Procida, *Diátaxis* (2020, diataxis.fr). Four user needs produce four incompatible
documents — **tutorial** (studying + practical), **how-to** (working + practical), **reference**
(working + theoretical), **explanation** (studying + theoretical). Greek *diá* "across" + *táxis*
"arrangement". The framework claims to settle content, style **and** architecture at once. Born
from Django CMS documentation, where topic-based structure proved arbitrary: *"a list of features
doesn't show someone how to solve a problem."* Adopted by Django, Canonical, Cloudflare, Gatsby.

Worth knowing precisely: the framework's own material presents the four as distinct forms serving
distinct needs; the hard rule **"never blend them"** is this seat's position, argued from the
collisions in `modes.md`, not a quotation.

## Carroll — minimalism (manner)

John M. Carroll, *The Nurnberg Funnel* (MIT Press, 1990) and *Minimalism Beyond the Nurnberg
Funnel* (MIT Press, 1998). Action- and task-oriented instruction: explicit teaching is *severely
reduced*, the learner proceeds by **guided exploration** on realistic tasks. Minimal manuals
averaged roughly **three pages per chapter** against the systems-approach manuals they replaced.
**Error recognition and recovery are first-class** — documentation anticipates the errors a real
user will make and says how to get out of them.

The title mocks the mythical Nuremberg funnel that pours knowledge into a head — the assumption
that comprehensiveness transfers understanding. It does not; it transfers volume.

## Nygard — architecture decision records (process, and memory)

Michael Nygard, *Documenting Architecture Decisions* (2011); the practice now at adr.github.io.
One record per architecturally significant decision, answering one question: **why did we do it
this way?** The argument is two-sided and both halves matter: **nobody reads large documents**,
and **not knowing the rationale leads to later decisions that defeat earlier ones**.
"Architecturally significant" = affecting structure, non-functional characteristics, dependencies,
interfaces, or construction techniques. The consistent practitioner finding: value comes to the
teams that **resist expanding an ADR into something grander**.

The consequence this seat leans on: a decision record is the only document whose worth grows with
age, and the only one that must be **superseded rather than edited**.

## ISO/IEC/IEEE 2651x — information for users (process)

A role-split family of standards for user documentation across the software life cycle, aligned to
the ISO/IEC 12207 / 15288 process standards:

- **26511** — managers: documentation plans and documentation management.
- **26512** — acquirers and suppliers of documentation.
- **26513** — **testers and reviewers** of documentation.
- **26514** — designers and developers: specifies **structure, content and format**, with
  informative style guidance.
- **26515** — documentation in an **agile** environment.

The load-bearing fact for this seat is the existence of 26513: documentation is **tested and
reviewed**, officially, as a product — the same claim the rot literature makes from practice, with
a standards body behind it. Take the principle; leave the ceremony.

## Docs-as-code and documentation rot (process, practice)

No single canonical author; consistent practitioner consensus (Write the Docs and others).
Plain-text markup in version control, reviewed like code, built and published by CI, checked
automatically for links and style. **Rot** = the gradual divergence between documented and actual
behaviour; the prescription is a maintenance regime rather than a cleanup project — docs reviewed
on the code's cycle, and procedures **executed against a real environment** on a schedule, so rot
is found before an incident finds it.

## Google and Microsoft style guides (manner)

**Google developer documentation style guide** (developers.google.com/style) — public, actively
maintained, curated for ease of understanding, accessibility, localization and globalization.
**Microsoft Writing Style Guide** — the other industry de-facto, explicitly usable for non-Microsoft
material, with a warm, plain, help-first voice.

Both are house styles, not laws. Use them the way this studio uses any style authority: for
consistency decisions that are not worth re-deciding, and never against the reader's task.

## The Russian school, applied here

`buro:copy` carries **информационный стиль** (info-style, Ilyahov) — every word earns its place;
would a real person say this. It transfers to documentation almost unchanged, with one amendment
this seat insists on: **brevity serves the task, and error recovery is never the thing cut.** The
`buro:lebedev` laws that bite hardest are law 1 (one function — one document, one mode) and law 8
(honesty — describe behaviour, not intent).

## Where the canon does not reach

**Game-development documentation has no named primary source** found in research. `gamedev.md` is
flagged synthesis. Neither were researched: **API reference generation** (OpenAPI, docstring
extraction) and the generated/hand-written boundary · **repository doc layout and naming** ·
**diagram maintenance** · **documents written for a machine reader**. The working defaults for
those four live in `structure.md`, flagged there as consensus; the open questions are carried in
`docs/research/2026-07-24-documentation-craft-sources.md`.
