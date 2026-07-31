# Freshness, rot, and the discipline that prevents it

> **Documentation rot** is the gradual divergence between documented behaviour and actual
> behaviour — code moves, configuration shifts, an API contract changes, and the document stays
> where it was. Its cost is not embarrassment: it is onboarding friction, support load, review
> confusion, and decisions taken on false information by exactly the people least able to check.

A stale document is worse than a missing one. A missing document sends the reader to ask someone.
A stale document sends them confidently in the wrong direction.

---

## Freshness is evidence, not a feeling

Three stamps make a document checkable. Without them it is a claim about the past written in the
present tense.

- **Date of last verification** — not last edit. Fixing a typo does not re-verify a procedure.
- **What it was verified against** — a version, a build, a commit, an environment.
- **An owner** — a named person or team. "The team" owns nothing; ownership that isn't assigned
  isn't ownership.

Optional and valuable: **what was checked**. "Steps 1–6 executed on a clean checkout" is evidence.
"Reviewed" is not.

## Execute the documentation

The strongest practice in the literature is also the simplest: **run the document against the real
system.** For runbooks and procedures this is a drill — execute against staging on a schedule, so
rot is found by you rather than by an incident.

This is the seat's gate 6. A procedure that has not been executed since the last release is
folklore that happens to be typed. When execution is impossible (no access, no environment), the
document says so, in the document, where the reader can see it: *"last verified against 2026.05
by @name; not re-run since."* An honest stale marker is a working document. A silent stale
document is a trap.

## Docs-as-code

The workflow consensus, and the reason it works is governance rather than tooling:

- Plain-text markup (Markdown, reStructuredText, AsciiDoc) in **the same repository as the code**.
- **Reviewed like code** — the docs change ships in the pull request that caused it, and the
  reviewer of the code reviews the doc.
- Built and published by **CI**; automated checks for broken links and style.
- Versioned and rollback-able, so a document can be true *for a release* rather than true in the
  abstract.

The mechanism that actually stops rot is the first one: **proximity plus the same review cycle.**
A document in another system, reviewed on another cadence, by other people, will drift no matter
how good the tooling is. The second mechanism is **one home per fact** — duplication is rot the
tooling cannot catch, since both copies build, lint and pass the link check (`structure.md`).

## Documentation is reviewed and tested

ISO/IEC/IEEE **26513** exists specifically for testers and reviewers of user documentation — an
official statement that documentation is a product that gets tested, not prose that gets proofread.
The rest of the family splits the same work by role: **26511** managers and planning, **26512**
acquirers and suppliers, **26514** designers and developers (structure, content, format), **26515**
documentation in an agile environment.

What to take from it, without ceremony:

- Review asks **"is this true and does it work"** before it asks "is this well written".
- Someone other than the author executes the procedure. The author cannot see their own assumed
  context — that is not a discipline failure, it is how knowledge works.
- Documentation has a plan and an owner like any other deliverable, not a slot at the end.

## The decision record — the one document that must not be updated

Every other document should be corrected when reality moves. A decision record must not be.

- It records **why**, in the moment, with the context and constraints that were true then.
- When the decision changes, write a **new** record that supersedes the old one, and link them.
- Editing an old record to match today's opinion destroys exactly the thing it exists for: the
  ability to see that a past decision was reasonable given what was known. Without that, teams
  re-litigate settled questions and undo decisions whose reasons are invisible.
- Keep it small — one decision, its context, the options, the choice, the consequences. The teams
  that get value from these are the ones that resist expanding them into design documents.

## Bloat prevention — the 80/20 of a technical document set

> **Goal: high confidence, low maintenance.** Every page is a liability that must be kept true; a
> set that documents everything is a set that is true about nothing. The same discipline a good test
> suite uses against itself applies here, and for the same reason — **coverage is not the metric,
> caught failures are.**

**The priority ladder — what earns documentation at all, in order:**

1. **What loses money, data or access** — auth and session handling, permissions, migrations,
   anything irreversible. A wrong belief here costs the most and is recovered from the slowest.
2. **Non-obvious business logic and its invariants** — the rules a reader cannot re-derive from the
   code in a minute: why this ordering, what must always hold, which case looks wrong and is not.
3. **Operational recovery** — the runbook, the rollback, the thing you read at 3am (`templates.md`).
4. **Interfaces others build against** — contracts, formats, limits, versions.
5. Everything else, which is usually nothing.

**Document behaviour, not implementation.** State what the thing *does*, what it *guarantees*, and
what happens when it fails — never how it loops internally. Implementation changes on every
refactor, so a document written against it rots on a schedule; behaviour changes when a decision
changes, and that is exactly when a document *should* be edited.

**Zero trivial coverage. Never write:**
- what the signature already says (parameters restated in prose, a getter, a DTO's fields);
- framework or library defaults the reader can look up at the source (`@Cacheable`, an ORM's save);
- a pass-through layer that adds no rule ("the service calls the repository");
- a second telling of the same rule in a different mode's document — link across, never restate
  (§one home per fact);
- a diagram of what one screen of code says plainly.

**One path, one document.** If a rule is stated in the reference, the tutorial links it and the
how-to assumes it. The same validation explained in three modes is three pages to keep true and two
that will silently disagree.

**Prefer the cheapest form that carries it** — three lines in a README over a page; a table over
prose; a worked example over a description of an example.

**Examples come from the source, not from a keyboard.** A pasted JSON blob, a hand-typed config, an
invented response — each is a copy that goes stale silently. Generate them, or execute them
(gate 6), or mark them illustrative.

**Fail fast, and prune.** A page that failed its execution check is fixed or deleted the same day —
`TODO: update this` shipped in a document is a page announcing it is lying. And once a round, ask of
each page: **would its absence cause a real error, or a question someone actually asks?** If not,
delete it; the deletion is the maintenance you are buying.

⚠ **Two bounds, so this does not become an excuse to cut.** Never prune **error-recovery** content
or **the one page a real reader depends on** — the Skeptic's guard in the seat cuts ceremony, never
the way out of a failure.

## Deprecation and deletion

Cutting documentation is real work and it has a failure mode: deleting the one page someone
depended on.

- **Redirect, don't vanish.** A deleted page with no forwarding address turns every old link, every
  bookmark, and every search result into a dead end.
- **Mark, then remove.** Deprecated with a date and a replacement, then deleted after it has been
  visibly dying for a while.
- The archive is not the same as the live set — but it is not the bin either. (Where the archive
  lives and how it stays findable is the queued `librarian` seat's subject, not this one's.)
- Before deleting: **who was relying on this?** If the answer is nobody, it should never have been
  written, and that is the lesson worth carrying to the next document.
