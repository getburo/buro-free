# Game-dev craft — named-source research (2026-07-22)

Deep-research pass (111 agents, 28 sources fetched, 122 claims → 25 verified under a 2/3-vote
adversarial-refutation gate: 23 confirmed, 2 refuted). Purpose: raw named-source material to
distill into Buro seats (lenses + canon), prioritized for a Days Gone-style open-world
survival-action game. Confidence tags are the harness's, not editorial.

> **Source strength is uneven.** STRONG (first-party GDC talks / postmortems / textbooks):
> combat design, open-world horde & traversal, camera, systems/economy. WEAK: engine choice
> (one promotional anecdote, two supporting claims refuted). THIN: VFX (texture-authoring only),
> audio (one encyclopedic source).

---

## 1. Combat design & game feel — STRONG (build priority 1 → `buro:combat-design`)

- **Steve Swink, *Game Feel* (Morgan Kaufmann, 2008)** — *confidence: high.* Feel is a
  **definable, teachable "hidden language,"** not ineffable — reusable building blocks that recur
  across games like chord progressions, arising from the measurable real-time relationship of
  **input → response → polish** under a ~100 ms correction cycle. Gives a systematic vocabulary
  for the feel lens.
- **Mihir Sheth, "Evolving Combat in God of War for a New Perspective" (GDC 2019, Santa Monica
  Studio)** — *high.* The 2018 intimate, player-controlled over-the-shoulder camera **invalidated
  the prior decade's combat-readability tricks and forced a full combat redesign.** Anchor lesson:
  **camera and combat feel are inseparable — one system.** (⚠️ commonly misattributed to Vince
  Napoli; the verified presenter is **Mihir Sheth**.)
- **Eric Williams, "Combat Canceled: God of War & Action Game Design" (Game Developer)** + **"7
  Combat Systems Every Game Designer Should Study"** — *high.* Three transferable, cross-studio
  principles: **(1) hit stop / hit pause / hit slowdown** on impact simulates resistance and weight
  (GoW holds attacker + target on the first hit frame; the axe impact "lingers for a moment");
  **(2) universal cancellation** — any action cancelable into a dodge or jump — makes combat feel
  responsive (Bayonetta; GoW's canceling windows); **(3) animation masks a generous input window**
  so combat reads responsive to experts yet stays accessible (Batman: Arkham's cape animation
  covering a ~40–50-frame counter window).
- **Jan Willem Nijman (Vlambeer), "The Art of Screenshake" (INDIGO 2013)** — *surfaced in search,
  not separately verified this pass; already cited in `buro:gamedesign` sources.* The origin text
  for action **"juice"** (screenshake, kickback, bigger bullets, impact frames). Seam: the juice
  **art** is `buro:gamedesign`/`buro:art-director`; here it's the feel-amplifier on an honest loop.

## 2. Open-world survival-action — STRONG (build priority 2 → genre playbook in `buro:gamedesign`)

- **Sony Bend, "The Freak-O-System: The Dynamic Open World of Days Gone" (GDC 2018 AI Summit —
  Darren Chisum & Tobias Karlsson)** — *high.* The **horde as an emergent-threat systemic spine**:
  hundreds of freakers on PS4 without perf collapse, AI unit spawning, streaming, horde
  behaviour/interaction. Direct primary source for the horde/density lens. (Composes with the
  existing `buro:gamedesign` → `references/open-world.md` emergent-threat section.)
- **Techland, "Game Design Deep Dive: Dying Light's Natural Movement" (Game Developer — Bartosz
  Kulon & Maciej Binkowski)** — *high.* Traversal-as-survival: **(1)** real-time geometry scan
  auto-selects the parkour animation (replacing 50,000+ hand-placed hook points); **(2) anything
  that looks climbable must actually be climbable** — kill artificial barriers; **(3) evasive
  traversal must be as valid a survival strategy as direct combat** ("should I fight or avoid?").
- **Naughty Dog, "The Last of Us: Human Enemy AI" (GDC)** — *surfaced (primary), companion/enemy
  AI for grounded survival encounters.*
- **Gap (open question):** the survival **resource economy** primary sources (fuel/scarcity, the
  bike/vehicle-as-resource, population density beyond the horde talk; State of Decay / DayZ / The
  Long Dark) did **not** produce verified claims — treat that layer as synthesis until researched.

## 3. Systems & economy — STRONG (queued → future `buro:systems`/economy seat)

- **Vili Lehdonvirta, "Economic Balancing and Improved Monetization Through Clever Sink Design"
  (GDC)** — *high.* **Sinks** (mechanisms that remove resources) are essential to long-term
  balance and sustained value; a concrete taxonomy of **6 currency sinks + 11 item sinks**.
  Author co-wrote *Virtual Economies: Design and Analysis*.
- **Daniel Cook (lostgarden), "Value Chains" & "Designing Game Content Architectures"** —
  *surfaced (blog, high-relevance).* The faucet → pool → sink economy model.
- **Josh Bycer, "How Power Curves Work in Video Games"** — *surfaced.* Progression/power curves.

## 4. Game camera / the 3 C's — STRONG (queued → future `buro:camera` seat)

- **Mark Haigh-Hutchinson, *Real-Time Cameras* (Morgan Kaufmann/Elsevier, 2009; ISBN
  9780123116345)** — *high.* Book-length, cinematographic **and** technical/algorithmic, by the
  Metroid Prime camera lead. Thesis: **camera quality is decisive** (a bad camera disrupts, a good
  one lifts a good game to great); the defining hardness is responding to **unscripted** player
  events.
- **Haigh-Hutchinson, "Fundamentals of Real-Time Camera Design" (GDC 2005)** — *high.* Three
  citable third-person rules: **4.1** always keep the player in view (total occlusion disorients;
  partial is fine); **4.2** prevent the near-plane from intersecting geometry — fade/remove
  offending geometry as the camera nears; **4.3** auto-select the best view; the player must
  **never be required** to manipulate the camera merely to play (optional manual is fine) — unlike
  first-person, where camera control *is* the gameplay.

## 5. Technical art / VFX — THIN (queued)

- **Simon Trümpler (simonschreibt), "How to (Not) Create Textures for VFX" (GDC 2022 VFX
  Summit)** — *high, but narrow.* VFX texture types (diffuse, LUT, erosion, flow) × four authoring
  methods (hand-paint, photobash, procedural, simulation). **Caveat:** texture authoring only — does
  not reach particles, shaders, hit-VFX, or screenshake. The RealTimeVFX community is the named hub.

## 6. Audio implementation / adaptive audio — MEDIUM (queued)

- **Winifred Phillips, *A Composer's Guide to Game Music* (MIT Press, 2014)** — *medium
  (encyclopedic/publisher source).* Covers the two core adaptive techniques — **horizontal
  resequencing** vs **vertical layering** — as dynamic-music constructs. Middleware specifics
  (Wwise/FMOD) not separately sourced.

## 7. Engine choice — WEAK / mostly REFUTED (do NOT treat as decided)

- The only surviving UE5-solo-viability evidence is a **single promotional interview** (80.lv,
  Unifiq Games; a ~5-person unreleased game) — *confidence: low, 2-1 split.* **Two companion claims
  were refuted:** "5-person team proves small-team viability" (0-3) and "World Partition used &
  highly optimized" (1-2).
- Grounded facts that *did* surface (blogs, medium confidence): **UE** — free until $1M gross,
  then 5% royalty; **World Partition server streaming** (`wp.Runtime.EnableServerStreaming=1`) can
  cut dedicated-server RAM dramatically; **Godot** — no royalties/fees, open-source. Comparisons
  (wayline, dev.to) note UE as the AAA-visuals/open-world choice, Godot as the lightweight/free one.
- **Honest recommendation:** engine choice is **not settled by this research.** Before committing,
  run a dedicated, current (2026) eval of UE5 vs Unity vs Godot for *this* game — World
  Partition/Nanite/Lumen maturity, networking, licensing, and solo-dev viability — because the
  engine-tradeoff landscape moves fast and this pass did not credibly capture it. Hold the engine
  **seat** until then.

---

## What Buro builds from this (and what waits)

- **Now:** `buro:combat-design` (§1, strongly sourced) + an **open-world survival-action** genre
  playbook in `buro:gamedesign` canon (§2). Both rest on first-party GDC/postmortem canon.
- **Next (canon captured here, seat not yet built):** `buro:camera` (§4, textbook + 3 rules ready),
  a systems/economy seat (§3, Lehdonvirta + Cook + Bycer), then VFX (§5) and audio-implementation
  (§6) once their sources are deepened.
- **Blocked on a fresh eval:** the engine decision and its seat (§7).

## Open questions carried forward

1. Current (2026) honest UE5 vs Unity vs Godot tradeoffs for a solo/small-team open-world
   survival-action game — the engine evidence here was weak/refuted.
2. Primary-source canon for the survival **resource economy** (fuel/scarcity, vehicle-as-resource,
   density) — Days Gone beyond the horde talk, plus State of Decay / DayZ / The Long Dark.
3. Citable sources for the **juice/screenshake** side (Vlambeer/Nijman, GMTK, particle/shader/hit-
   VFX craft) beyond Trümpler's texture talk.
4. Systems/economy at scale — what Cook, Bycer, and Koster contribute as named lenses (surfaced but
   not deeply verified this pass).
