# Evidence — custody, the record line, and the confidence ladder

## Archive before you cite

**The record is the archived copy. The live URL is a convenience.** A citation to a live page is an
assertion with a link attached: pages change and vanish, and a dead citation cannot be
distinguished from a fabricated one.

At collection, in this order:

1. **Capture** — a web archive with a public timestamp (Wayback, archive.today), and where the page
   resists capture, your own saved copy plus a note saying why the public capture failed.
2. **Record the retrieval date** — the date *you* got it, separate from creation and publication.
3. **Hash it** when the artifact is a file (a PDF, a dataset, an image): a SHA-256 in the record line
   makes later tampering — including your own accidental re-saving — detectable.
4. **Note the method** — how you reached it, in one clause. This is what makes a finding re-runnable
   by someone who doubts it, which is the whole point.

Capture **before** analysis, not after. Analysis that changes what you are looking at has destroyed
the thing you were looking at.

## The record line

One line per fact. Not per source, and not per paragraph — **per fact**, because confidence attaches
to facts and a source can carry several at different strengths.

```
<fact, stated flatly> — <CONFIDENCE> · <source, named> · origin: <primary|registry|secondary|interested>
  · archived <URL> · retrieved <YYYY-MM-DD> · <sha256:… if a file> · method: <how you reached it>
```

Worked:

```
Vendor X's engine shipped v2.0 on 2024-03-14. — CONFIRMED · vendor repo tag v2.0.0 (signed) ·
  origin: primary · archived https://web.archive.org/… · retrieved 2026-08-05 · method: repo
  releases page, tag date cross-checked against the commit it points at.
```

**Inferences are written differently and kept out of the findings list.** An inference gets its own
labelled section, states which findings it rests on, and names what would break it. Mixing the two
in one list is the failure the Berkeley Protocol names as separating observed from inferred — and
the reason a reader ends up believing your reasoning at the confidence of your documents.

## The confidence ladder

Exact words, so that a fast reader cannot upgrade a finding by skimming it.

| Level | Means | Requires |
|---|---|---|
| `CONFIRMED` | established | **two independent** primary or registry sources, independence checked by **origin** |
| `SUPPORTED` | one good source, uncorroborated | one primary or registry source |
| `REPORTED` | someone says so, and you traced who | secondary only, provenance traced to its origin |
| `UNVERIFIED` | not established | no primary source reached — **name the register that would hold it** |
| `CONTRADICTED` | the evidence points the other way | a source of equal or better standing disagrees |
| `FALSE` | disproved | a primary source establishes the negative |

Three rules that do the actual work:

1. **Confidence is set by the weakest supporting check, never the strongest.** A finding with a
   verified source and an unresolved date is not `CONFIRMED`.
2. **Independence is counted by origin, never by URL.** Four articles citing one deck are one
   source. State independence as something you checked, not as an absence of doubt.
3. **`UNVERIFIED` is a valid, publishable answer.** It is a finding: *we looked, here is where the
   answer lives, we could not reach it.* Softening it into a hedge — "seems to be around 40%" —
   converts an honest gap into a fabricated number, and is the failure this seat exists to prevent.

An **interested** origin never reaches `CONFIRMED` on its own, however primary it is. A vendor is a
primary source for *what the vendor claims*, and that is the fact you may record.

## The falsifier

Every verdict carries **one line naming what would change it.** Not a list of caveats — the
specific, findable thing.

- Good: *"an audited restatement of the 40% with a stated denominator."*
- Good: *"the sector body's 2026 survey, due in November."*
- Useless: *"more research would be needed."*

A verdict with no falsifier is a belief with a citation. The falsifier is also the handover: it tells
whoever picks this up what to go and get.

## Absence records

When a record that *should* exist does not, that is a finding and it gets a record line of its own:

```
No third-party audit of the 40% figure exists. — ABSENCE · searched: vendor site, filings 2024–2026,
  sector body publications · retrieved 2026-08-05 · method: … · what would falsify: any audit or
  filing-level restatement.
```

State **what you searched**, or the absence is indistinguishable from not having looked.

## Minimisation, at the end

Before the file leaves your hands, strip incidental personal data the claim does not need
(`perimeter.md`, Gate 7). The file you keep is part of what you did — including the parts nobody
asked to see.
