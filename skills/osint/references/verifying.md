# Verifying — the five checks, as procedure

Run these on any artifact offered as evidence: an image, a video, a document, a screenshot, a quote,
a number. From the *Verification Handbook*'s five checks (see `canon.md`).

```
PROVENANCE — is this the original, or a copy of a copy?
SOURCE     — who made it, and how do you know?
DATE       — when was it MADE (not published, not retrieved)?
LOCATION   — where was it made, and does that match the claim?
INTEGRITY  — has it been altered, and is the alteration material?
```

A check you skipped is not a pass. Record it as unchecked.

---

## 1. Provenance — find the earliest copy

The artifact you were handed is almost never the original.

- **Reverse image search across more than one engine** — they index different corpora, so one
  engine's "no results" means nothing. Crop to the distinctive region and search that too; a
  recaptioned image is often cropped or rescaled from the original.
- **Search a distinctive quoted phrase** for text, a document title, or a filename.
- **Sort results oldest-first** and keep walking back. The earliest instance is your provenance
  lead — check whether *it* credits something earlier still.
- **Ask who would hold the original**: the photographer, the agency, the filing office, the repo.

**The output of this check is a date and a place of first appearance**, or an explicit "earliest
instance found: X; earlier origin not ruled out."

## 2. Source — who made it

- Is the account/outlet/office the **originator** or a **redistributor**? Redistribution is rung 4.
- Does the source have a **history** that predates this artifact? A source created shortly before
  the material it publishes is a signal, not a verdict.
- **Is the source interested?** A vendor benchmark, a commissioned survey, a party's own figures —
  usable as their claim, never as independent corroboration (Lens 10).
- For a document: does the **issuing body** publish it directly? Get it from them, not from a
  re-host.

## 3. Date — three dates, never one

Keep them separate, always:

| Date | What it is | Where it comes from |
|---|---|---|
| **created** | when the artifact was made | metadata, content evidence, first appearance |
| **published** | when it was first posted | the earliest instance found in check 1 |
| **retrieved** | when *you* got it | your own record, at collection |

Collapsing these is how a 2019 photograph becomes evidence about 2026.

**Chronolocation** — dating from content when metadata is absent:
- **Shadows** — direction and length give a time of day and a season for a known latitude.
- **Weather** — compare against historical weather records for the claimed place and date.
- **Content markers** — signage, plate designs, price labels, model years, construction stages,
  visible software versions, foliage state.
- **Corroborating captures** — another image of the same place from a known date.

## 4. Location — where it was made

**Geolocation** by matching the artifact to a known place:
- Fixed, hard-to-fake features first: terrain profile and horizon line, road and rail geometry,
  building footprints and roof shapes, tower and mast positions.
- Then confirm with satellite/aerial imagery and street-level imagery — **noting the imagery's own
  date**, since the ground may have changed.
- Confirm with a second independent feature. One matching landmark is a hypothesis; two
  independently matching features that are geometrically consistent is a location.
- **Record the confidence** — "within this block" is a different finding from "this building."

## 5. Integrity — was it altered

- **Metadata** (EXIF, document properties, PDF producer and revision history) — read it, and treat
  it as *removable and forgeable*: present metadata is weak positive evidence, absent metadata is
  almost no evidence at all, since most platforms strip it on upload.
- **Internal consistency** — lighting direction versus shadows, reflections, perspective, repeated
  texture patches, edges that are too clean, text that doesn't follow the surface it sits on.
- **Documents** — font and kerning inconsistency, mismatched alignment, a revision history
  disagreeing with the stated date, a PDF whose text layer differs from its rendered image.
- **Numbers and charts** — do the parts sum to the total? Does the axis start at zero, and if not,
  is that disclosed? Does the chart's own data table agree with its bars?
- **Quotes** — get the full surrounding passage. Truncation is the most common alteration of text
  and leaves no forensic trace at all.

**Generated artifacts.** Pixel-level tells move too fast to write down and produce both false
positives and false negatives. **Verify provenance instead** (check 1): a real artifact has a
history — an earlier posting, a camera, a filing, a person who will say where it came from. Absence
of history is the signal worth acting on. Where a provenance credential (C2PA-style signed
manifest) exists, read it — and note that its absence proves nothing.

---

## Screenshots

A screenshot is evidence that *an image exists*, not that its contents were ever real. Treat it as
rung 4 at best. To use it: find the live or archived original it depicts, and archive **that**. If
the original cannot be found, the finding is `UNVERIFIED` and the screenshot is described as an
unverified screenshot, never as the thing it shows.

## Writing the result

Each check gets one of three outcomes, and all three are reportable:

- **verified** — with the evidence that settled it
- **unresolved** — with what would settle it and which register or capture would hold it
- **contradicted** — with the specific inconsistency

Then set confidence from the **weakest** check, not the strongest (`evidence.md`).
