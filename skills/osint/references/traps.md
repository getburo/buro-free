# Traps — the failure catalogue

Each trap: how it looks, why it works, and the before/after.

---

## 1. Circular reporting

Several outlets carry the same figure. Each looks like independent corroboration. All of them cite
one origin — a press release, a wire story, one analyst's estimate.

It works because **counting is easier than tracing**, and four URLs feel like four sources.

> **Before:** "Widely reported at 40% — four independent trade outlets confirm it." — CONFIRMED
>
> **After:** "All four cite Vendor X's 2025 launch deck, p.11. One source, four echoes." — REPORTED

**The check:** for every source, name its origin before counting it. Independence is a property of
origins, not of domains.

---

## 2. Citation laundering

A claim acquires authority by being cited, then re-cited. Each hop looks like sourcing. Follow the
chain and it terminates in nothing — or in a source that was explicitly speculating.

> **Before:** "Per [analysis], citing [report], the figure is 2.1M."
>
> **After:** "[analysis] cites [report]; [report] cites a 2019 blog post that describes 2.1M as
> 'a rough guess for illustration'." — REPORTED, origin: speculative

**The check:** Lens 2. Keep walking until the trail ends at a document, a register, a dataset, or a
person who saw it. Record where it actually ended, even when that is embarrassing.

---

## 3. False context — true material, wrong caption

The commonest failure in open-source work, and the one people look for last. Nothing is fabricated;
the image, quote or chart is real. It is simply about something else.

> **Before:** "Photograph of the queues at their launch event last month."
>
> **After:** "Reverse image search: first appearance 2019, a different company's event in another
> city. Authentic photograph, false caption." — FALSE (as captioned)

**The check:** provenance before content, every time (`verifying.md` check 1). Also the shape of it in
text: a real quote with the qualifying sentence removed.

---

## 4. The press-release statistic

A number with no method, no sample, no denominator, published by the party it flatters — then
repeated until it reads like a measurement.

> **Before:** "40% of studios use it."
>
> **After:** "Vendor's own deck. No method, no sample, no denominator. The sector body's published
> survey (n=212, method stated) says 11%." — CONTRADICTED

**The check:** demand the denominator. "40% of what, measured how, by whom?" A percentage with no
denominator is a claim about nothing.

---

## 5. Survivorship in a dataset

The dataset is real, the arithmetic correct, and the population is wrong — because whatever removed
cases from it also removed the answer.

> **Before:** "Average lifespan of studios in this space: 11 years (n=340, active studios)."
>
> **After:** "The sample is *active* studios. Every studio that closed is absent — the exact
> population the question is about." — the finding is uninterpretable, not merely imprecise

**The check:** ask **who is missing** from the dataset, not who is in it. Then: who collected it,
when, from whom, and what was excluded.

---

## 6. The convenient find

The research stops the moment it agrees with what was wanted. No single step is wrong; the *effort*
was asymmetric.

> **Before:** three sources supporting the preferred answer, found in ten minutes, verdict written.
>
> **After:** "I spent ten minutes confirming and none disconfirming. Searched the negation: the
> sector body's survey disagrees, and was on page 1." — the bias was in the stopping rule

**The check:** Lens 4 — *would I have looked this hard for the opposite answer?* Formally: search the
negation before writing the verdict, and record that you did.

---

## 7. Name collision

Two records joined on a shared name, written up as one entity.

> **Before:** "The vendor was sued in 2021 [docket ref]."
>
> **After:** "The defendant is a same-named company, different registration number, different
> jurisdiction. No identifier links them." — the original claim was two facts, not one

**The check:** pivot only on identifiers (`finding.md`). If a name is the only link, the finding is
*"a same-named entity appears in X; unconfirmed."*

---

## 8. The dead citation

Cited live, never archived. Months later the page is gone, and a real finding is now
indistinguishable from a fabricated one.

> **Before:** "Source: https://… (accessed earlier)."
>
> **After:** "Archived at web.archive.org/… , retrieved 2026-08-05, sha256:… "

**The check:** archive at collection, before analysis. The record is the capture.

---

## 9. Metadata as proof

EXIF says the date and place, so the date and place are settled. Metadata is trivially editable and
routinely stripped by platforms: **present metadata is weak positive evidence; absent metadata is
almost no evidence at all.**

> **Before:** "EXIF confirms 2026-07-02, coordinates match." — CONFIRMED
>
> **After:** "EXIF is consistent with the claim and editable. Corroborated independently by shadow
> direction and historical weather; geolocated on two fixed features." — CONFIRMED, on the
> corroboration rather than the metadata

**The check:** metadata corroborates; it never establishes.

---

## 10. Confidence inflation across the write-up

Every finding is labelled honestly. The summary is not — because summarising drops the labels.

> **Before:** findings say `SUPPORTED`, `REPORTED`, `UNVERIFIED`; the summary says "the data shows".
>
> **After:** "One primary source, uncorroborated; the market-share figure is unverified."

**The check:** the summary inherits the **weakest** label it summarises. Read the verdict against the
findings list as the last act before shipping — this is the self-critique gate.

---

## 11. The generated artifact treated as a forensics problem

Time goes into inspecting pixels for tells; the tells are unreliable in both directions.

> **Before:** "No visible artifacts, hands look correct — likely authentic."
>
> **After:** "No provenance: no earlier posting, no camera, no source who will account for it.
> Treated as UNVERIFIED regardless of appearance."

**The check:** provenance, not pixels. Absence of history is the actionable signal (Lens 9).

---

## 12. The screenshot as the thing it depicts

> **Before:** "Their pricing page said $49 — screenshot attached." — CONFIRMED
>
> **After:** "Screenshot is unverified. The archived pricing page for that date says $49." —
> CONFIRMED, on the archive; the screenshot is not the evidence

**The check:** find and archive the original the screenshot depicts. If you can't, the finding is
`UNVERIFIED` and the artifact is described as an unverified screenshot.
