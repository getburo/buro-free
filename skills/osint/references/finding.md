# Finding — the source ladder, and which register holds which fact

## The ladder, and why the direction matters

Always walk **down** toward the document, never sideways toward more coverage.

```
1. THE PRIMARY DOCUMENT      the filing, the dataset, the spec, the commit, the patch note
2. THE REGISTER THAT HOLDS IT  the registry/court/office/repository whose job is to keep it
3. AN ARCHIVE OF IT          a timestamped capture, when the live original is gone or may go
4. SECONDARY REPORTING       an article about it — a pointer to a source, never a source
```

Reporting is a **finding aid**. Use it to learn that a document exists and where, then go get the
document. A claim that never gets below rung 4 is `REPORTED`, whatever its confidence felt like.

**The failure this ordering prevents:** starting at rung 4 and collecting more of rung 4. Five
articles agreeing is one source with four echoes until you check their origins.

## Which register holds which kind of fact

The useful question is never "where do I search" but **"whose job is it to keep a record of this?"**

| The claim is about… | The register that would hold it |
|---|---|
| a company existing, its officers, filings, accounts | the national company register of its jurisdiction |
| ownership, a group structure, a beneficial owner | company registers + consolidated accounts; aggregators (OCCRP Aleph) as an index, not a source |
| a lawsuit, a judgment, a bankruptcy | the court's own docket system for that jurisdiction |
| a trademark, a patent, a design right | the patent/trademark office (national, EPO, WIPO) |
| a technical claim about a standard | the standards body's published spec, by version |
| a software claim — when a feature shipped, what changed | the repository, its tags, its release notes, its commit history |
| a public contract, a supplier, a price paid | the procurement portal / tender database |
| a regulated firm's status or sanction | the sector regulator's public register |
| a property, a licence, a permit | the land registry / licensing authority |
| a dataset's numbers | the statistical agency or the dataset's own repository, **with its method document** |
| a domain, a service, an IP-level fact | WHOIS/RDAP, certificate transparency logs, DNS history |
| a page that has changed or vanished | web archives (Wayback, archive.today), and your own capture |
| an academic claim | the paper itself, its data availability statement, and its retraction status |
| a market size or share | **no register holds this.** It is always someone's estimate — find whose, and their method |

That last row is the one that matters most in this studio. **A market number has an author.** Find
the author and the method, or label it `REPORTED`.

## Query construction

The move that changes results is not a clever operator — it is choosing the string the *document*
would contain rather than the string a *description of it* would contain.

- **Search the document's own language.** A filing says "principal activities", not "what the
  company does". A patch note says "fixed", not "they fixed a bug where".
- **Search a quoted distinctive phrase** from any text you already hold — it finds every copy, and
  the earliest copy is your provenance lead (Lens 2).
- **Constrain to the register**, not the whole web: `site:` the registry, the court, the repo host.
- **Constrain by filetype** when the target is a document: `filetype:pdf`, `filetype:xlsx`.
- **Constrain by date** to separate creation from republication — and remember search-engine date
  filters report *indexing*, which is a third date again (Lens 7).
- **Exclude the echo.** Once you know the press-release phrasing, subtract it to see what remains.
- **Search the number itself**, formatted the way its author would have written it (`1.4bn`,
  `1,400,000,000`, `1.4 billion`). Its earliest appearance is usually its origin.
- **Search the negation.** If nothing anywhere disputes a widely repeated claim, that is either
  strong support or a monoculture — Lens 4 says find out which.

## Pivoting: identifiers, never names

A pivot is how you get from one record to another. It is only sound on an identifier that means
exactly one thing.

**Sound pivots:** a company registration number · a filing or docket ID · a domain · a file hash ·
a DOI · a commit SHA · a patent number · a certificate fingerprint.

**Unsound pivots:** a person's or company's *name* · a job title · a city · a logo · a photograph
of a building · "the same wording".

Two records joined on a name are **two records**, and writing them up as one is the most common way
an open-source finding turns out to be false. If a name is the only link you have, that is a
finding of its own: *"a same-named entity appears in X; the link is unconfirmed."*

## Datasets

Before using a number from a dataset, get four things or say you couldn't: **who collected it**,
**when**, **from whom (the sample and the denominator)**, and **what was excluded**. A dataset with
no published method is an opinion in a table. See `traps.md` on survivorship.

## Stopping

Stop when one of these is true, and say which:

1. You reached a primary source and verified it (Gate 4). → `CONFIRMED` / `SUPPORTED`
2. You traced the trail to its origin and the origin is secondary or interested. → `REPORTED`
3. You identified the register that would hold the answer and could not reach it. → `UNVERIFIED`,
   **naming the register** — an unresolved with an address is worth far more than a blank.
4. The record that should exist does not. → an **absence finding** (Lens 6), recorded explicitly.

Running out of time is not a fifth option. It changes how far you got, never how you label it.
