# Roblox — Platform Truth

Open this for Roblox projects. Source — [Roblox Creator Docs](https://create.roblox.com/docs/production/game-design) (CC-BY 4.0 on the prose) plus verified observations. Roblox is not "just a platform": its algorithm and audience impose design constraints harder than any genre canon.

---

## Audience

The core is ages 9–15, but **44% of DAU are already 17+**, and the 18+ layer is growing >50% YoY and spends ~40% more per session. Designing "for kids" means choosing the worst-ARPU layer — that's a legitimate choice, but it has to be a conscious one.

Design consequences:
- **Value must read visually, not through cultural context.** A "vintage Fender" doesn't work — a "sparkling gold guitar with sparks" does.
- **The decision to leave is made in 60–120 seconds.** Not in the first hour.
- **Text is read reluctantly.** The rule "the game teaches itself" here isn't philosophy, it's physics.

---

## The Recommendation Algorithm — the Main and Often the Only Channel

Roblox publishes Recommended For You signals. Knowing them isn't marketing, it's a design constraint: **the algorithm ranks what you designed.**

Signals: playtime · play days · qualified play sessions · **intentional co-play days** · spend days · Robux spent · play-through rate · **first play bounce**.

**Three consequences that break naive design decisions:**

1. **Co-play days** — deliberately joining with friends. A game designed so that a second live player isn't needed ("works fine with 1 online", "bots fill the quorum") **crosses itself off the main signal**. Filler bots should be checked against this question: do they kill the reason to bring a friend?

2. **The retention window was extended from 7 to 28 days** (June 2026). Games with "exciting thumbnails but no long-term value" are pushed out by more retentive ones. A release that in writing forgoes retention gets not a "slow start" but **zero impressions**.

3. **First play bounce** — the entry point of the funnel. A first session that starts with losses or waiting hits the algorithm harder than everything else combined.

**Paid traffic:** the entry threshold is deceptively low (minimum ~$35, $1 daily minimum). But with cosmetics-only monetization on a kid audience, LTV ≈ $0.05–0.15, CPI ≈ $0.20–0.50. **LTV < CAC** — the paid channel is closed by arithmetic. The only justified use of budget is creative testing (icon/thumbnail) for the sake of play-through rate, which is itself a signal.

This is `buro:growth` territory — only what changes **design** is carried here.

---

## Core Loop — the Roblox Model

Three-part:
1. **Minute-to-minute interaction**
2. **Defining mechanic** — the most repeated set of actions
3. **Progression engine**

> «Without a progression system, a game becomes repetitive, boring, and shallow.»

⚠️ Honest caveat: the page is declarative — no questions or checklist there. The model is useful as a framework — pull the questions from the lenses in SKILL.md.

---

## D1 / D7 / D30 — Three Different Levers

This is **not one metric with different windows**, but three different problems. Each is fixed by its own means.

**D1** — the core loop is balanced (no frustration, no boredom) + **FTUE under 5 minutes** + contextual tooltips + a reward for the first loop completion + performance (crashes, FPS across devices).

**D7** — progression: clear short- and long-term goals, content variety, difficulty calibration (neither blowing through it nor getting stuck).

**D30** — **updates every 2–4 weeks** to existing mechanics, **major features every 2–3 months** + social (trading, guilds, PvP, leaderboards).

**Platform benchmarks** (median): D1 10–15%, D7 3–5%, D30 1–2%. A good game: 25–30 / 8–12 / 4–6.

⚠️ The thresholds "D1 ≥ 20% / D7 ≥ 8%" circulate in community guides — Roblox publishes signals and their relative importance, but not thresholds. A reference point, not a fact.

---

## Onboarding

Success metrics: D1 + reaching onboarding goals.

Techniques from the documentation:
- Low progress thresholds on early levels
- Starter items/currency with A/B-tuned "sweet spot"
- **Layered goals** (short / mid / long)
- Celebration moments at milestones

The funnel narrows — the task is to find and plug drop-off points **with data, not guesses**.

**Genre-leader practice:** the tutorial shows **every beat of the loop in a single pass** — before letting the player go. Not "explaining the mechanic" but running the whole loop.

---

## Prototyping

Paper and studio prototypes. A prototype is **fast and dirty**, it hits one specific aspect rather than building the whole feature. **Test the core loop first** — not graphics, not progression.

---

## Sharding — the Trap Everyone Forgets

Roblox shards its servers. "One event per day for all players" physically becomes **its own instance per server**. Design that relies on a shared event ("everyone's talking about the same drop") has to account for this: one legend for the whole game, its own instance per server, a global leaderboard.

Same with "live" multiplayer: check a competitor's `maxPlayers` before trusting their marketing. An 8-slot game with NPC opponents is a single-player game with a chat backdrop, whatever it's called.

---

## Monetization — the Line Where Law Begins

Roblox's policy on [paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items) is triggered by a purchase with Robux **or with in-game currency bought with Robux**, and explicitly covers pity systems and **luck boosts**. Since June 2026 the Korean odds-disclosure requirements have rolled out globally, with regional compliance handled through PolicyService.

**The trap almost everyone falls into:** an "earnings booster for Robux" looks like harmless convenience. But it's an indirect purchase of currency that buys random content — that is, **exactly paid randomness**. If the design rests on "we don't sell randomness", the ban on **"Robux → game currency by any route"** has to live at the core level, not in the monetization chapter.

Speeding up time (restoration, crafting) is not chance, it's time. That's allowed.

Economy and pricing are `buro:analyst` territory. Here, only the part that **forbids a mechanic**.

---

## Exploiters — a Design Constraint, Not a Programmer's Concern

The client is hostile by default. Any hidden information that reaches the client **will be read by a script** — usually within a week of the game becoming noticeable.

Design consequence: if the core of the game is incomplete information (see source of uncertainty #7), then **the truth never leaves the server**. Not "we'll filter it on the client" but "the client never received it at all." A silhouette, a hint, a shadow — is a **separate server-side entity**, not filtered real loot.

The sign that a mechanic feels like work rather than play: **auto-scripts appear**. People pay so they don't have to press your button — that's a diagnosis of the button.

---

## Links

[Game design docs](https://create.roblox.com/docs/production/game-design) · [Core loops](https://create.roblox.com/docs/production/game-design/core-loops) · [Onboarding](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/onboarding.md) · [Retention](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/retention.md) · [Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items) · [Optimizing Discovery (Newsroom, June 2026)](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox) · [Recommended For You — DevForum](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575)
