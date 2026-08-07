# Dev Canon — Reference

Depth beyond the rules in SKILL.md — the general software-engineering practices this seat's
method draws its lenses from. Open this when you need the reasoning behind a gate, not just the
gate itself.

**Table of contents:**
- [Test-First Development](#test-first-development) · [Refactoring & Code Smells](#refactoring--code-smells)
- [Deep vs Shallow Modules](#deep-vs-shallow-modules) · [Small, Fast Reviews](#small-fast-reviews)
- [The Standard Vulnerability Classes](#the-standard-vulnerability-classes)
- [Confidence Scoring & False Positives](#confidence-scoring--false-positives)
- [Layering, Init Order, and Implicit Loads](#layering-init-order-and-implicit-loads) · [Sources](#sources)

---

## Test-First Development

Write the test before the code it tests. The discipline has a short cycle: **red** (a failing
test that names the behaviour you want) → **green** (the smallest change that passes it) →
**refactor** (clean up with the safety net of a passing suite). The point isn't ritual — it's that
a test written after the code tends to describe what the code already does, not what it must do;
a test written first is the only kind that can actually fail.

**Criterion:** for any new behaviour, did a test exist and fail *before* the implementation did?
If the test was written after, ask whether it would have caught the bug the implementation
originally had — if it can't answer that, it isn't a regression test, it's decoration.

---

## Refactoring & Code Smells

Refactoring changes the internal structure of code without changing its observable behaviour —
which only means anything if a test suite is what proves the behaviour didn't change. A **code
smell** is a surface signal of a deeper problem, not the problem itself: duplicated logic, a
function or class doing two unrelated things, a parameter list that keeps growing, a chain of
conditionals that mirrors a type the language should be expressing instead, a comment explaining
what the code does rather than why.

**The rule that keeps refactoring honest:** never refactor and change behaviour in the same diff.
A reviewer (or a future bisect) needs to be able to tell "this changed what it does" from "this
changed how it's shaped" at a glance.

**Simplification has a failure mode of its own, and it looks like virtue.** Clarity beats brevity:
a nested ternary that packs three conditions into one expression is not simpler than an if/else
chain, it's denser — the reader now decodes precedence instead of reading intent. "Fewer lines"
is not the goal; a one-liner that takes three reads to parse is a regression dressed as a
refactor. Consolidating logic can go too far the same way abstraction can — combining unrelated
concerns into one function to save a few lines, or removing an abstraction that was genuinely
carrying complexity somewhere a caller didn't have to think about it, both make the code harder to
change later while looking like progress today.

**Criterion:** after a simplification pass, would a reader unfamiliar with the diff take *longer*
to understand any single line than before? If yes on even one line, that line got denser, not
simpler — revert just that line, even if the rest of the pass is good.

**Criterion:** does this diff do exactly one of {change behaviour, change shape}? If both, split
it — the second diff will be trivial to review precisely because the first one already passed.

**Four smells worth naming precisely, because the fix depends on telling them apart:**

- **Divergent Change vs. Shotgun Surgery** are mirror images of the same misplaced boundary, and
  the fix runs opposite directions. Divergent Change: one module has to change for many unrelated
  reasons ("I touch these three functions for a new database, these four for a new instrument") —
  split the module along those reasons. Shotgun Surgery: one reason to change forces edits across
  many modules — pull the scattered pieces into one. Diagnose by asking which direction the pain
  points: too many reasons converging on one file, or one reason scattering across many.
- **Feature Envy.** A function that calls another module's getters more than it touches its own
  module's data is homesick — move it to where the data lives, not the other way around.
- **Data Clumps.** The same three or four values keep appearing together as fields or parameters.
  Litmus test: delete one of them — if the rest stop making sense on their own, they were already
  one object and just hadn't been named yet.
- **Primitive Obsession.** A domain concept (money, a range, a phone number) represented as a bare
  number or string loses the invariant that made it that concept — money added across currencies,
  inches added to millimetres. If the type doesn't exist, the compiler can't catch the mix-up; a
  small wrapper type earns its keep the moment two unrelated primitives can be swapped by mistake
  and nothing complains.

---

## Deep vs Shallow Modules

A module's cost isn't its size, it's its **interface** — what a caller has to learn to use it
correctly. A **deep module** hides substantial complexity behind a small, simple interface (a
good compression library, a well-designed file API). A **shallow module** exposes almost as much
complexity as it hides — a thin wrapper whose interface is nearly as complicated as just doing the
thing directly. Shallow modules accumulate as a codebase grows and are individually cheap to add,
which is exactly why they're dangerous: each one adds a small tax that a caller pays forever.

**Complexity is not eliminated by adding a layer — it's moved.** The only question worth asking is
whether the new layer moved it somewhere a caller has to think about it less, or just relocated it
behind a name.

**Criterion:** could a caller use this module correctly from its interface alone, without reading
the implementation? If not, the interface is lying about what it costs to use.

---

## Small, Fast Reviews

A change is easier to review correctly the smaller it is — past a certain size, reviewers stop
finding bugs and start rubber-stamping, because holding the whole diff in working memory becomes
the bottleneck, not understanding it. The standard a reviewer should hold a change to isn't
"perfect," it's **"does this leave the codebase healthier than it found it"** — a change that
improves things without being ideal is still worth approving, provided it doesn't introduce a new
problem to fix later.

**Criterion:** could this diff be split into two independently-reviewable, independently-shippable
pieces? If yes, and neither piece depends on unshipped context from the other, split it.

---

## The Standard Vulnerability Classes

The recurring categories a security pass checks first, in the order untrusted input actually
travels through a system: **injection** (SQL, shell, template — untrusted data interpreted as
code or query structure), **broken access control** (an authorization check assumed by the UI but
not enforced at the API/data layer), **cryptographic failures** (secrets in plaintext, weak or
missing encryption at rest/in transit), **insecure design** (a missing threat model — the flaw is
architectural, no patch fixes it), **security misconfiguration** (default credentials, verbose
errors leaking internals, unnecessary features left on), **vulnerable dependencies** (a library
with a known CVE, unpinned or unpatched), **identification/auth failures** (session fixation, weak
password/reset flows, missing rate limits on login), **software/data integrity failures**
(unsigned updates, deserializing untrusted data), **logging/monitoring gaps** (an attack that
leaves no trace to detect it by), and **server-side request forgery** (a server fetching a
URL an attacker controls).

**Criterion:** for any input crossing a trust boundary — where does it get validated, and is that
validation on the server side of that boundary, not merely in the client that happens to be
well-behaved today?

---

## Confidence Scoring & False Positives

A review's value comes from what it filters out, not from how much it lists. Every candidate
finding should get an honest confidence score before it's reported — not as bureaucracy, but
because an unfiltered list trains the reader to skim past all of it, including the one finding
that mattered. A workable scale: **0** not confident (false positive, doesn't survive scrutiny,
or pre-existing) · **25** plausible but unverified (if stylistic, no stated convention requires it)
· **50** real but minor, a nitpick relative to the change · **75** verified, will be hit in
practice, the current approach is genuinely insufficient · **100** certain, directly confirmed.
Reporting only the top band (roughly ≥80) is not being lenient — it's the same subtraction
discipline applied to the review itself as to the code: a finding that doesn't clear the bar is
decoration, not rigor.

**The standard false-positive categories, checked before anything is reported:** a pre-existing
issue the diff didn't introduce · something a linter, typechecker, or compiler would already catch
in CI · an issue explicitly silenced on purpose (a lint-ignore, a documented exception) · a real
issue, but on a line the diff didn't actually touch · a change that looks surprising in isolation
but is an intentional, clearly-related part of the broader diff · a pattern the code's own history
(git blame, a prior accepted review) already explains and settled.

**Criterion:** before reporting a finding, can you point to the specific evidence that puts it at
or above the reporting threshold — the exact line, the exact input, the exact prior context
checked and ruled out? If the honest answer is "it seems like it probably," that's a 25–50, and it
stays off the report.

---

## Layering, Init Order, and Implicit Loads

Three structural rules, generalized from how large game engines organize dozens of interdependent
subsystems — but none of them are game-specific; they apply just as directly to a web backend or an
admin panel with several services (auth, cache, DB pool, feature flags) that depend on each other.

**Dependencies point one way.** A lower layer (a utility, a data-access module) never reaches back
up to call a higher one (a request handler, a UI component) to get something it needs — if it seems
to need to, the shared thing belongs in the lower layer instead. A cycle between two modules means
neither can be tested, deployed, or even fully understood alone, regardless of how clean each one
looks read in isolation; a cycle is a design defect, not a style preference.

**Startup order should be explicit, not inherited from language mechanics.** A language's own
static/module-initialization order across files is often unspecified or fragile — two interdependent
services (a cache that needs a config service, a config service that needs a secrets client) can end
up constructed in the wrong order purely by accident of import order or file layout, and the bug only
shows up in the environment where the accident goes the other way. The fix: give shared services a
do-nothing constructor and an explicit `startUp()` (and its mirrored `shutDown()`), called in a
hand-written, human-readable order at the entry point — never left to whatever order the runtime
happens to resolve today.

**A cache-miss is either an explicit failure or an explicit load — never a silent one.** An accessor
that looks like a free read (a getter, a cached property, a `get()`) but hides a synchronous fetch on
miss turns an ordinary cache miss into an unpredictable latency spike, landing on whichever caller
happens to hit it first. Callers can only reason about cost if the expensive path is visible at the
call site, not buried behind an interface that promises it's cheap.

**Criterion:** for a set of interdependent services, is the startup order stated somewhere a reader
can see it in one place, or does it depend on import order, file order, or a DI container's own
resolution algorithm? For a cache or lookup, is a miss's cost visible at the call site, or hidden
behind an accessor that looks the same whether it hits or misses?

---

## Sources

Kent Beck, *Test-Driven Development: By Example* — the red/green/refactor cycle.
Martin Fowler, *Refactoring: Improving the Design of Existing Code* — behaviour-preserving
transformation; the code-smell catalogue chapter is credited jointly to Kent Beck and Fowler.
John Ousterhout, *A Philosophy of Software Design* — deep vs shallow modules, complexity as the
enemy, where complexity actually lives.
Google engineering practices (`google.github.io/eng-practices`) — the "leaves the codebase
healthier" standard of code review, small-CL discipline.
OWASP Top 10 (`owasp.org/Top10`) — the standard web-application vulnerability categories.
Jason Gregory, *Game Engine Architecture* (4th ed., CRC Press) — strict subsystem layering with no
circular dependencies, explicit `startUp()`/`shutDown()` over implicit static-initialization order,
and treating a resource's cache-miss path as an explicit load rather than a hidden implicit one;
generalized here past its engine-specific origin to any layered service architecture.
