# Game Design Canon — Reference

Depth beyond the lenses in SKILL.md — theory, criteria, and primary sources. Genre playbooks are in `applied.md`.

**Table of contents:**
- [Order of Application](#order-of-application) — by cost of error
- [The Lens of the Toy](#the-lens-of-the-toy) · [Triangularity](#triangularity) · [Sid Meier's Criteria](#sid-meiers-criteria) · [Meaningful Choice](#meaningful-choice-and-dominant-strategy)
- [Sirlin — Yomi/Scrub/Bans](#sirlin--yomi-the-scrub-and-what-actually-warrants-a-ban) · [Bartle's Player Types](#bartles-player-types) · [MDA](#mda--mechanics-dynamics-aesthetics) · [Meaningful play](#meaningful-play) · [Costikyan](#costikyan--decisions-resources-struggle)
- [Uncertainty](#uncertainty--11-sources) · [Damage Roll Probability](#damage-roll-probability--controlling-variance-on-purpose) · [Koster](#koster--fun-as-learning)
- [Verbs](#verbs) · [Loops](#loops--micromezzomacro) · [Feedback Loops](#feedback-loops) · [Crafting Systems](#five-approaches-to-crafting-systems) · [Response](#response--game-feel-and-juice) · [Onboarding](#onboarding-the-first-60-seconds)
- [Design's Three Pillars (Rogers)](#designs-three-pillars-rogers-character-camera-controls) · [Level Design (Rogers) → buro:level](#level-design-rogers--owned-by-burolevel) · [Enemies and Bosses (Rogers)](#enemy-and-boss-design-rogers)
- [Sources](#sources)
- **Genre playbooks live in `applied.md`** — auctions, loot/unboxing, bots, soulslike, roguelike, F2P ethics, horror, open-world survival. Don't load them for a lens.

⚠️ **Trap:** Schell's lens numbers differ between editions. Rely on the **name**, not the number.

---

## Order of Application

Don't run the lenses as a checklist. The order reflects the **cost of the error**.

**Phase 1 — kills the project (a day):**
1. Toy (turn off the goals — is it fun for 30 sec?)
2. Triangularity (is there risk/reward in 30 sec?)
3. Pattern inventory (<5–7 → it'll burn out)
4. Time to grok (this is the ceiling of the game's lifespan)

**Phase 2 — kills the game (a week):**
5. Uncertainty audit (<2–3 sources → bland)
6. Dominant strategy
7. Feedback loops (30% test)
8. Endogeneity

**Phase 3 — kills the feel (ongoing):**
9. Response channels (<3 = dry), frames to response (>6 = fix this first)
10. Loop: all 4 arrows, feedback tied to a concrete pixel
11. Verb (physical, not "interacts")
12. Onboarding (60 seconds, the text test)

---

## The Lens of the Toy

Don't ask whether it's fun **to play** the game. Ask whether it's fun **to play with**.

> If my game had no goal, would it be fun at all? If not, how can I change that?
> When people see my game, do they want to start interacting with it, even before they know what to do?

**Criterion:** turn off the goals, the points, winning, progression. Is anything left that's pleasant to fiddle with for 30 seconds? **No → the goals and rewards are masking a boring core. No meta-progression fixes that.**

A falsifiable test that kills a project in a day, not six months.

🚩 "It'll be fun once we add progression."

---

## Triangularity

The choice: play safe for a small reward, or risk it for a big one. The single most valuable empirical claim in the whole of Schell's book:

> **"Eight times out of ten, when someone comes to me with a prototype that's 'somehow not fun,' the game is missing exactly this choice."**

> Do I have triangularity now? If not, how can I get it?
> Is my attempt at triangularity balanced? Are the rewards commensurate with the risks?

**Criterion:** take any 30-second window. Can the player, **right now**, choose between "slow and safe" and "fast and risky"? If every 30-second window says "no" — **that's why it's not fun.**

Balance via expected value: EV(risky) ≈ EV(safe) → triangularity is alive. One path dominates → the choice is an illusion.

---

## Sid Meier's Criteria

"A game is a series of interesting decisions" (GDC '89). At GDC 2012 he explained what that actually means. The method is **by contradiction**:

> "It's easier to look at what **isn't** an interesting decision. If the player always picks the first of three options, that's probably not an interesting choice. Neither is a random one."

**Two failure tests:** (a) they always pick the same thing → no choice; (b) they pick at random → no information.

**Five types of interesting decisions:**

| Type | What it is | Example |
|---|---|---|
| **Trade-off** | Price or opportunity cost | A sword for 500 gold; speed vs. handling |
| **Situational** | Interacts with the current state | "Good decisions are situational" |
| **Style-expressive** | Expresses personal style | Aggression vs. turtling |
| **Risk/reward** | Penalty against reward | "In almost any kind of game you'll find opportunities" |
| **Short vs. long term** | Planning horizon | A wonder vs. a chariot in Civ |

**The information rule (counterintuitive):**
> "You should almost err on the side of too much information — or at least enough of it that the player is confident they understand the choice."

This runs directly against the instinct toward "intrigue through vagueness." **Uncertainty belongs in the outcome, not in the rules.**

**Criterion:** for every decision, name which of the five types it is. **Fits none of them → it's not a decision, it's a ritual.**

---

## Meaningful Choice and Dominant Strategy

> What choices am I asking the player to make? Are they meaningful? How?
> Am I giving the player the right number of choices?
> **Are there any dominant strategies in my game?**

Strategy A **dominates** B if A is always better, no matter what everyone else does. A dominant strategy doesn't kill balance — it kills the **decision**: there's no choice, only a test of whether you know the right answer.

**Three conditions for an interesting choice (all of them at once):**
1. No option is obviously better than the rest.
2. Options are **not equally attractive** either (otherwise the choice is indifferent — also a failure).
3. There's enough information to decide consciously, not to guess.

**Dominance test:** for every pair of options A and B — **is there a situation where B beats A?** Never → B is dead. Cut it or give it a niche.

**The "no free power" rule:** every strong option has a price — a cost, a cooldown, a risk, a vulnerability, or giving up some alternative.

🚩 >40–50% win rate on a single build. That's dominance, not "meta." A healthy meta is a rotating rock-paper-scissors.

---

## Sirlin — Yomi, the Scrub, and What Actually Warrants a Ban

David Sirlin, *Playing to Win* (free web edition, sirlin.net). Written for competitive players, but every claim in it is a direct test of a designer's own balance work — from the other side of the table.

**The scrub — a diagnostic for reading your own playtest feedback, not a player insult.** "A scrub is a player who is handicapped by self-imposed rules that the game knows nothing about. A scrub does not play to win." The game "only knows winning and losing" — it doesn't know that a throw "should" be blockable, or that repeating one move is "cheap." Sirlin's examples of self-imposed rules: rejecting throws because blocking should feel "totally impervious," rejecting projectile spam, rejecting a single move repeated, rejecting a defensive turtle who "does nothing" for fifty seconds.

**Why this matters for balance work, not just player psychology:** when a playtester calls a mechanic "cheap," check whether they're reporting a real dominant strategy (see the lens above) or just a self-imposed rule the mechanic was specifically built to break. "The entire purpose of the throw is to be able to damage an opponent who sits and blocks." A counter to a strategy is not evidence the counter is broken — it's evidence the counter is doing its job. Nerf the number, not the complaint.

**Yomi — the actual source of "legitimate" depth**, and a sharper, more mechanical restatement of the dominant-strategy lens. Layer 0: a player finds and repeats a strong move. Layer 1: the opponent learns and plays a specific counter. Layer 2: the first player reads that and plays a counter to the counter. Layer 3: the opponent reads *that*. "Yomi layer 4 loops back around to layer 0" — depth doesn't need infinite layers, it needs the loop to hold for at least two or three reads before repeating. Worked example (Virtua Fighter 3, Akira vs. Pai after a knockdown): throw → escape → an unthrowable slow power move → block (which beats the slow move) → loop. "Strategic depth [is] defined almost entirely on its ability to support and reward yomi." A game can have enormous option count and still have none of it — Sirlin's own contrast case is tic-tac-toe, which offers "no room for yomi at all" regardless of how many squares are on the board, because there's no read that can itself be read.

**The yomi test, applied to a design:** does the best-known response to the current best strategy have its own counter that a skilled opponent can find? If the first counter is unconditionally final — no further read beats it — there's no yomi here, no matter how many buttons the game has.

**What actually warrants a ban.** Three conditions, all required: **enforceable** (can you reliably detect it?), **discrete** (can you define it with zero ambiguity — his camping-ban example: define it as "3 minutes in one zone" and sitting there for 2:59 becomes the new optimal tactic, which is worse, not better), and **warranted**. The third one does almost all the work: "the great lesson of competitive games is that hardly anything warrants a ban." His default assumption for an apparently broken tactic: it doesn't destroy the game, keep playing, because 99% of the time a counter or a better tactic gets discovered. A ban is only justified when a tactic "completely dominates the entire game, to the exclusion of other tactics," demonstrated over real, extended competitive play — not a day-one impression.

**Criteria:**
- **The scrub-complaint test:** is "this feels cheap" backed by an actual win-rate number, or is it a self-imposed rule the mechanic exists specifically to violate? Check the number before you nerf the complaint.
- **The yomi test:** does the current best answer to the current best strategy have its own counter a skilled opponent can find? No further read beats it → there's no depth here yet, regardless of option count.
- **The ban test:** is the tactic enforceable, discretely definable, and does it dominate to the exclusion of nearly everything else over real extended play — not just a strong first impression?

🚩 Nerfing a mechanic because testers called it "cheap" without checking whether it's actually winning at a dominant rate. · A written ban rule vague enough that gaming its exact boundary (2:59 vs. 3:00) becomes the new best play — that's a sign the fix belongs in the mechanic, not a rule. · Banning on day-one impressions instead of watching whether a counter gets discovered. · Mistaking a large option count for yomi — depth requires that a read can itself be read, not just that there are many buttons.

---

## Bartle's Player Types

Richard Bartle's four-quadrant taxonomy (from his 1996 MUD player-type research, later expanded in *Designing Virtual Worlds*), crossing two axes: **acting on the world vs. acting on players**, and **acting vs. interacting**.

- **Achievers** — acting on the world. Want points, levels, gear, status through accumulation. The largest group in most player bases.
- **Explorers** — interacting with the world. Want to understand the game's systems and map its space; reward them with knowledge and content variety, not loot.
- **Socializers** — interacting with players. Want relationships, guilds, chat; retained by who else is online, largely indifferent to content.
- **Killers** — acting on players. Want to impose themselves on other players directly (PvP, griefing at the edge); the smallest group by headcount but often the most vocal and the most willing to pay for status that only means something in front of other players.

**The point of the model isn't to sort players into boxes — no player is purely one type.** It's a lens for reading a specific complaint or a specific metric: a churn spike among Explorers usually means content variety dried up; a churn spike among Socializers usually means the friend group left first. A design that only feeds Achievers (numbers going up) will retain them while quietly starving the other three — worth checking against the boredom/burnout lens above, since "the same thing with bigger numbers" is exactly what Achiever-only design produces.

**Where the axes clash on purpose:** Killers and Socializers actively work against each other — one group's fun is the other group's reason to quit. A design that puts both in the same unwalled space without a separation mechanism (ranked matchmaking, a PvP-flagged zone, an opt-in) is quietly choosing Killers over everyone else, whether or not that was the intent.

**Criterion:** for a churn or complaint pattern, name which quadrant is actually affected before proposing a system-wide fix. "Players are leaving" is not a diagnosis; "Explorers are leaving because there's nothing left to find" is.

🚩 Content that only ever expands the Achiever axis (bigger numbers, more grind tiers) while Explorer and Socializer needs go unaddressed. · Killers and Socializers sharing an unflagged space by default. · Treating "engagement" as one undifferentiated number when a churn spike is actually concentrated in a single quadrant.

---

## MDA — Mechanics, Dynamics, Aesthetics

Hunicke, LeBlanc, Zubek, "MDA: A Formal Approach to Game Design and Game Research" (GDC Game Design and Tuning Workshop, 2001–2004; AAAI, 2004). The paper that names why a designer and a player are looking at the same game through opposite ends of the telescope.

**Three layers, one causal chain, read in opposite directions by the two people who touch it:**

> **Designer's perspective:** Mechanics → Dynamics → Aesthetics — rules give rise to system behavior, which gives rise to the felt experience.
> **Player's perspective:** Aesthetics → Dynamics → Mechanics — the felt tone comes first, born out in observed behavior, and only then (if ever) in the rules underneath.

- **Mechanics** — the components at the level of data and algorithms: shuffling, trick-taking, betting, spawn points, ammunition, sand traps.
- **Dynamics** — the run-time behavior of mechanics acting on player input and each other's output over time: bluffing, camping, sniping, a broken club.
- **Aesthetics** — the desirable emotional responses the system evokes when the player interacts with it. Deliberately **not** the word "fun" — the paper's whole point is that "fun" is too blunt an instrument to design with.

**The eight kinds of fun — a vocabulary to replace "make it more fun":**

| # | Kind | Framed as |
|---|---|---|
| 1 | Sensation | Game as sense-pleasure |
| 2 | Fantasy | Game as make-believe |
| 3 | Narrative | Game as drama |
| 4 | Challenge | Game as obstacle course |
| 5 | Fellowship | Game as social framework |
| 6 | Discovery | Game as uncharted territory |
| 7 | Expression | Game as self-discovery |
| 8 | Submission | Game as pastime |

Every real game pursues **several of these at once, in different proportions** — that's the diagnostic use, not a single-label taxonomy. The paper's own worked comparison: *Charades* — Fellowship, Expression, Challenge. *Quake* — Challenge, Sensation, Competition, Fantasy. *The Sims* — Discovery, Fantasy, Expression, Narrative. *Final Fantasy* — Fantasy, Narrative, Expression, Discovery, Challenge, Submission. Naming the two or three a design is actually chasing turns "make it more fun" into a checkable claim: *Charades* emphasizes Fellowship **over** Challenge — a specific, arguable proportion, not a mood.

**The paper's own Monopoly diagnosis — dynamics before mechanics, every time.** As one player's lead grows, they can punish opponents with increasing effectiveness (a positive feedback loop — the runaway-loop lens, independently named here in 2004): "as the gap widens, only a few (and sometimes only one) of the players is really invested. Dramatic tension and agency are lost." The fix is proposed at the **mechanics** layer only after the **dynamics** layer names the actual failure: subsidize the losing players, tax the leaders, or add time pressure so the game ends before the gap calcifies. Tuning numbers before naming which dynamic is broken is solving the wrong layer.

**Worked example from the paper — the same "tag" mechanic, three aesthetic targets, three different mechanical designs:**
1. **Babysitting game, ages 3–7:** aesthetic goal is Discovery, not Challenge. Dynamics optimize for a baby expressing surprise and fear, not for winning. Mechanics: manual hiding spots, hard-coded paths, minimal AI.
2. **Same tag mechanic, "Rugrats"-style, ages 7–12:** aesthetic goal adds Narrative and mild Challenge. Dynamics add time pressure and multi-character tracking. Mechanics now need babies who choose their own hiding places and track internal state — static paths no longer suffice.
3. **Same tag mechanic again, military-stealth, ages 14–35:** aesthetic goal is Fantasy bordering on Submission. Dynamics add earnable equipment and deceptive-movement tactics. Mechanics now need full tech trees, unit-type variety, and sensor-realistic AI.

The mechanic ("find and don't be found") never changed. The aesthetic target did, and that's what determined every layer under it — not the other way around. "There are no 'AI mechanics' as such — intelligence or coherence comes from the interaction of AI logic with gameplay logic." The paper's own conclusion: reason from aesthetic goals down to dynamics down to mechanics, not the reverse.

**Criteria:**
- **The vocabulary test:** can you name which 2–3 of the eight kinds of fun this design is actually chasing, in what proportion? "Make it more fun" with no answer here is not yet a design goal.
- **The direction test:** when a design is broken, are you naming the broken **dynamic** first (a feedback loop, a dead choice, an unreadable signal) before reaching for a **mechanics**-layer number tweak? Tuning the wrong layer treats the symptom.
- **The reuse test:** could the same underlying mechanic serve a completely different aesthetic target for a different audience, the way "tag" serves Discovery for a 5-year-old and Fantasy/Submission for a 25-year-old? If a mechanic only ever supports one aesthetic reading, that's a fact worth stating explicitly, not assuming.

🚩 Reaching for a mechanics-layer fix (add a number, add an item) before naming which dynamic is actually broken. · Describing a design goal only as "fun" or "engaging" with no aesthetic vocabulary underneath it — not falsifiable, can't be checked against the shipped game. · Assuming a mechanic's aesthetic reading is fixed and universal rather than audience-dependent.

---

## Meaningful play

Salen & Zimmerman, "Rules of Play":

> "**Meaningful play occurs when the relationships between actions and outcomes in a game are both discernable and integrated into the larger context of the game.**"
> "**The meaning of an action in a game resides in the relationship between action and outcome.**"

| Criterion | Player's question | What failure looks like |
|---|---|---|
| **Discernable** | "What just happened?" | Pressed it — didn't understand. The action vanished into nothing |
| **Integrated** | "How will this affect the game?" | Clear what happened, but it changes nothing. A decorative move |

Both are needed. Discernable without integrated = clear but empty actions. Integrated without discernable = everything matters, but the player doesn't understand what they're doing.

**Criterion** for every action: (a) does the player perceive the result right away? (b) will the result change the course of the game 5 minutes from now?
"No" on (a) → it needs feedback (not a mechanic — a **message**).
"No" on (b) → **cut the action.** It's stealing time.

**The hard test:** can the player tell whether their choice **moved them closer to winning or further from it**? No → there's no choice, just a click.

---

## Costikyan — Decisions, Resources, Struggle

"I Have No Words & I Must Design" (1994/2002). The only source with **direct directives**.

> «**A light switch is not a game.** Interaction has no game value in itself. **Interaction must have a purpose.**» → «**What makes a thing into a game is the need to make decisions.**»

Chess is his proof by subtraction: no simulation, no roleplaying, almost no colour — nearly every quality games are praised for is absent. **What it's got is the need to make decisions.**

**2002 definition:** «An interactive structure of **endogenous meaning** that requires players to **struggle** toward a **goal**.»

**Endogenous meaning.** His illustration: handed $100 of Monopoly money on the street, you have been handed nothing. Inside a game of Monopoly the same paper has value — **the value is manufactured by the game and exists nowhere else.** His counter-example is the stock market, whose meaning is *not* endogenous: the things traded there would still mean something if the market evaporated tomorrow.

**The economic analogy — his directive:** treat a game's structure as an **economy or ecosystem** — a complex system that **doesn't dictate outcomes, it steers behaviour**. Expect players to respond to whatever incentives the structure provides, and to **exploit that structure** to reach their goals. A dominant strategy is not cheating; it is the system answering honestly.

**Checklist:**
- **Light-switch test:** does every interaction have a purpose?
- **Resource test:** what is the player managing? Name it explicitly. Name the **tokens** through which they manage it.
- **Struggle test:** *what resists the player?* "Nothing" → a toy, not a game.
- **Endogeneity test (the strongest one):** *"If the game vanished tomorrow — would its objects keep their meaning?"* Yes → it's a tool/market, not a game.
- **Incentive test:** write down what the game **rewards**. Players will do **that**, not whatever you intended.

---

## Uncertainty — 11 Sources

"Uncertainty in Games" (MIT Press, 2013).

> «**Games require uncertainty to hold our interest, and the struggle to master uncertainty is central to their appeal.**»
> «**Games thrive on uncertainty, whereas other interactive entities do their best to minimize it.**»

**Randomness is just one of 11, and usually the worst one:**

| # | Source | Player's question | Example |
|---|---|---|---|
| 1 | **Performative** | "Can I physically pull it off?" | Mario, Tetris |
| 2 | **Solver's** | "Can I solve it?" | Puzzles; better when emergent |
| 3 | **Player unpredictability** | "What will the others do?" | Diplomacy; strong AI as a surrogate |
| 4 | **Analytic complexity** | "What do I choose given this tree?" | Chess. **Deterministic**, yet beyond calculation |
| 5 | **Algorithmic complexity** | "What's actually under the hood?" | RollerCoaster Tycoon |
| 6 | **Randomness** | "What will fortune give me?" | Poker, roguelikes |
| 7 | **Hidden information** | "What's in their hand?" | Poker |
| 8 | **Perception** | "Can I make it out?" | Guitar Hero |
| 9 | **Narrative anticipation** | "How will it end?" | Suspense |
| 10 | **Schedule** | "When do I come back?" | FarmVille |
| 11 | **Development anticipation** | "What's coming in the patch?" | DLC |

**Criteria:**
- **Audit:** mark which sources are present. **<2–3 → the game is bland.**
- **Death test:** *"If the player knew everything — what would be left?"* "Nothing" → the game gets solved, then dies.
- **Boredom diagnosis:** players are leaving → **which source of uncertainty collapsed?**

🚩 **"Everything on randomness":** if the only source present is #6, the game feels unfair and skill never grows. Randomness is cheap, which is exactly why it's tempting. **Replace it with 3, 4, or 7 — the same uncertainty, but rewarding skill.**

🚩 **The F2P trap:** #10 and #11 drive retention, but they're **external** to the gameplay. Relying on them alone means death the moment the content pipeline stops. That's retention extracted, not earned · law 8.

---

## Damage Roll Probability — Controlling Variance on Purpose

Amit Patel, redblobgames.com, "Damage Rolls" — a practical, interactive-tool companion to the "randomness is source #6, the worst one" point above: even when you've decided a mechanic *should* use randomness, the exact numeric model you pick changes the felt experience far more than most designers expect.

**A single die is not the same shape as multiple dice, even at the same average.** `1 + random(12)` is a flat distribution — 2 and 12 come up exactly as often as 7. Rolling 2d6 for the same range produces a peaked, bell-shaped distribution centered on 7 — extreme outcomes get rarer, not because you nerfed them, but because of how many ways there are to reach the middle versus the edges.

**Dice count controls variance directly, independent of the average.** 2d6, 3d4, 4d3, and 6d2 all reach the same 2–12 range with the same average, but the distribution goes from wide to narrow as dice count goes up and individual die size goes down. **More dice, smaller each = lower variance, more predictable outcomes clustering near the average. Fewer, bigger dice = wider swings, more room for a lucky or unlucky extreme.** This is a direct dial: want a mechanic where skill dominates and luck rarely swings the outcome? More, smaller dice. Want a mechanic where a single roll can swing a match? Fewer, bigger dice.

**Asymmetry is a deliberate technique, not an accident of the dice you happened to pick.** Taking the higher of two rolls (or dropping the lowest of three) skews the result upward — useful for player-favoring rolls (attribute generation, a "best of" mechanic). Taking the minimum skews it downward — useful for damage-against-the-player rolls where you want the occasional big hit to actually land as a real spike, not get averaged away. Critical hits are the same technique named differently: a bonus applied with some probability, deliberately reintroducing the spike that averaging dice removes.

**When dice constrain you too much, drop them — a weighted lookup table gives total control.** Rather than reverse-engineering a dice formula to hit a specific distribution shape, define the exact outcome weights you want directly in a table. "Nonparametric distributions give you a great deal of flexibility, and using data tables instead of code allows quick iteration" — this is the same principle as Costikyan's uncertainty sources above: the shape of the randomness is a design choice, not a side effect of whichever formula was easiest to code.

**Criteria:**
- **The variance-intent test:** does the number of dice (or the table shape) actually match how much you want a single roll to matter? A "high-skill, low-luck" combat system built on 1d20 is fighting its own dice.
- **The asymmetry test:** is the skew (toward big hits, toward reliable averages) something you chose on purpose, or just whatever the first formula that hit the right average happened to produce?
- **The iteration test:** can you retune the distribution shape without touching code — a data table, not a hardcoded formula? If not, every balance pass costs an engineer, not just a spreadsheet edit.

🚩 A flat single-die roll used where a peaked, predictable distribution was actually wanted (or vice versa) — nobody checked which shape the mechanic needed. · Hardcoding a dice formula for a distribution shape that a weighted table would let you iterate on in minutes instead of a rebuild.

---

## Koster — Fun as Learning

> «That's what games are, in the end. **Teachers. Fun is just another word for learning.**»
> The brain — **a voracious consumer of patterns, a soft pudgy gray Pac-Man of concepts**.
> **Noise is any pattern we don't understand** — and Koster puts the blame on the observer, not the world: perceiving something as noise is usually our failure to read it, not its failure to have structure.
> «**The destiny of games is to become boring, not to be fun.**»

**Three states — fun lives only in the middle window:**

| What the brain sees | Reaction |
|---|---|
| A pattern it **doesn't understand** (noise) | "Too hard" → leaves |
| A pattern it's **mastering** | **FUN** |
| A pattern it's **mastered** (grokked) | "Boring" → leaves |

Noise is **the observer's failure, not the universe's**. For the designer: when players call a system "random" — **you failed to make the pattern legible.**

**Six reasons players leave:**

| Player says | The real reason | What to fix |
|---|---|---|
| "Too easy" | Grokked instantly | Deepen the decision space |
| "Too hard" | Can't see the patterns — it's noise | Legibility, one input at a time |
| "Repetitive" | Patterns arrive **too slowly** | Speed up the novelty |
| "Got hard too fast" | Patterns arrive **too fast** | Add rungs |
| "I beat it" | Pattern mastered | Generate new problems |
| "Fun, but not worth the time" | Mastered, but demands repetition | Reconsider the loop's value |

**The core question:** does the game manage to teach everything it has before the player gets bored?

**Three tests:**
1. **Pattern inventory.** List **what the player learns** — not the content. **<5–7 → it'll burn out regardless of content volume.** 50 levels of the same pattern is one pattern.
2. **Time to grok.** After how many minutes is the player acting **automatically**? **That's the upper bound on the game's lifespan.**
3. **New pattern vs. burnout.** Every grok should be met with a new pattern. A gap = a churn window.

**Law:** a game survives only if it **generates new problems faster than the player grokks them.** Authored content is finite → burnout on schedule. Systemic generation (opponents, emergence, triangularity) → burnout deferred.

Countermeasure: build around **one deep** core lesson. A pattern that can never be fully grokked (chess, playing against people) doesn't burn out.

---

## Verbs

Design starts with a **verb** — a concrete action of the hands. Anthropy & Clark, "A Game Design Vocabulary": rules are a **vocabulary**. Structure: **subject (the player) — verb — object**. "Mario **jumps** over a fire flower."

Objects set the context: "shoot" means something different depending on what you're shooting. Robert Yang pushes this to the extreme: a game built around **one** unusual, bodily verb.

**Criteria:**
- **One-sentence test:** "The player [VERB]s [OBJECT] in order to [GOAL]." **A verb like "controls," "interacts," "explores" isn't a verb — it's a dodge.** You need something physical: jumps, cuts, pulls, hides, **outbids.**
- **Vocabulary inventory:** the core should have **3–5** verbs. 15 → smeared thin. 1, and it's boring → there's no game.
- **Verb × object matrix:** does every cell produce a meaningful result? Empty ones are missed design.
- **The question:** "What do the hands do? Describe it **without a single noun from the setting**." Sounds identical for your game and ten others → the verb isn't yours.

A direct analog of "interface as language" and "internal ≤ external": the verb is the minimal honest unit.

---

## Loops — Micro/Mezzo/Macro

| Level | Horizon | Benchmark |
|---|---|---|
| **Micro** | seconds | the cycle closes in **1–5 sec**; ~60% of the player's time |
| **Mezzo** | minutes | completes in **2–10 min** |
| **Macro** | hours/sessions | days–weeks |

**The first reward comes in the first 30–60 seconds.**

**Skill atom (Daniel Cook)** — four parts:
**Action** → **Simulation** → **Feedback** → **Modeling** (the player updates their mental model). Atoms link into **skill chains**.

> Cook's framing: chemistry became a science when it built testable models of physical atoms. A science of game design would do the same with **testable models of human psychology** — which is the whole claim behind the skill atom.

**Loops vs Arcs:** > «**An arc is a broken loop you exit immediately.**»

**Diagnosing a broken loop:**
- **Missing feedback** — didn't understand whether it worked. *The most common break.*
- **Unclear modeling** — cause and effect are blurred.
- **Burnout** — the atom is mastered, but the game keeps forcing repetition.
- **Frustration** — an atom without its prerequisite mastered (a hole in the chain).
- **Boredom** — feeding an experienced player something they've already learned.

**Criteria:**
- Draw the loop, **all 4 arrows**. **Can't name the feedback as a concrete pixel and sound → there's no loop, only an arc.**
- Name the timer for every level **in numbers**. No macro → boredom. No micro → dryness.
- "What does the player learn about the system on the **10th** repeat?" Nothing → grind.
- **The arc test:** "Do it a second time — same value?" No → it can't go in the core.

---

## Feedback Loops

A positive loop **amplifies** deviation ("the rich get richer"). A negative one **dampens** it ("the leader gets slowed down"). Neither is inherently "bad" — an **unbalanced** one is.

**Runaway leader.** The gap becomes a chasm → **emotional stakes disappear**: the leader is bored, the trailing players are bitter. The game is effectively over an hour before its formal end.
- **Monopoly** — the canonical death spiral. Worse: the loser **isn't eliminated**, they die slowly for an hour and a half.
- **Catan** — "productive settlements generate more resources, enabling more settlements."

**Catch-up:**
- **Mario Kart** — the blue shell. "Rubber-banding."
- **Power Grid** — elegant: whoever has more power plants **buys fuel last**; pays a markup just to keep the lights on.
- **Catan** — players are reluctant to trade with the leader. **The loop works through the players, not through a rule — the highest craft.**

**Overcorrecting breaks skill.** Mario Kart Wii: outcome "fairly random."
> «**Effective game balance requires carefully calibrated feedback, not eliminated feedback entirely.**»

The ideal is **oscillation**: "reputation raises your score, but the higher the score, the faster reputation falls" → **the timing of the oscillation itself becomes the strategy.**

**Criteria:**
- **Draw every loop:** "X grows → what grows next? → does it loop back to X?"
- **The 30% test:** the leader has pulled 30% ahead — can a trailing player still win by playing well? No → the game is de facto over.
- **Leader-boredom test:** does the leader still have interesting decisions, or are they just coasting?
- **Catch-up honesty test:** does it reward **skill** or **falling behind**? 🚩 A player deliberately loses to bank the bonus.

**Hierarchy by elegance:**
1. Friction through the **market** (Power Grid)
2. Friction through the **players** (Catan)
3. Friction through a **rule** (a tax on the leader)
4. **Direct handouts** to trailing players (blue shell) ← the crudest of all

Runaway leader is often cured not by a loop but by an **end condition**: the game should end right when the loop starts to accelerate.

---

## Five Approaches to Crafting Systems

A crafting mechanic is a faucet-and-sink design in a costume — the same lens above applies, but the five shapes below (Jason Wishnov, Tuts+, "5 Approaches to Crafting Systems in Games") are where most crafting mechanics actually go wrong, since each shape has a different failure mode.

1. **Money by another name** — raw materials swapped for items at a fixed rate, functionally a shop with extra flavor ("hand over units of wood to a workbench, and it hands you back a wooden shield"). Cheapest to build, easiest to understand, but adds nothing beyond a reskinned purchase — and too many parallel resource currencies makes it a chore rather than flavor.
2. **Find the recipe** — the player must discover a recipe/blueprint before an item becomes craftable at all. Adds narrative/exploration reward without inflating item count, but the schematic drop rate itself becomes a second economy to balance against the item's actual value — the same random-item-math problem as the Roguelike section above, one layer up.
3. **Guess and see what sticks** — no known recipes; combinations are found by trial and error. Genuine discovery when it works (Minecraft, Skyrim alchemy); becomes either "punitive to experiment with" or "solved by a wiki in week one" when it doesn't — there's no stable middle state for this shape.
4. **Made-to-order customization** — the player picks from known modular components (casing, fuse, contents) to build genuinely different outcomes with real tradeoffs. Closest of the five to the meaningful-choice lens directly — but the option count that makes this rewarding is the same option count that makes balancing it against every other way to acquire power expensive.
5. **Anything is possible** — many input variables, a combinatorial output space (Vagrant Story, Morrowind spellcrafting). Maximum agency and replay value, resists a single dominant recipe simply by being too large to fully map — but is the most expensive of the five to develop, balance, and QA, and the one most likely to produce an unintended game-breaking combination nobody playtested.

**Criterion:** which of the five did you actually pick, and does its specific failure mode show up in your design? Shape 1 dying to currency bloat, shape 3 dying to a wiki, shape 5 dying to an unplaytested combo are different diagnoses that call for different fixes — "the crafting system feels bad" isn't specific enough to act on.

🚩 Shape 3 or 5 shipped without enough playtesting to catch the combinatorial edge cases — these two shapes have the largest gap between "looks fine in the design doc" and "breaks in players' hands." · Treating all five shapes as equally cheap to balance — shape 5 costs an order of magnitude more QA than shape 1 for the same shipped feature name ("crafting").

---

## Response — Game Feel and Juice

**Swink.** Three mandatory blocks:
- **Real-time control** — input changes the world faster than the player can consciously register it
- **Simulated space** — movement, collisions, weight, inertia
- **Polish** — amplifies perception **without changing the simulation**

Control without space = a slider; space without polish = debug cubes; polish without control = a cutscene.

**Numbers — feel is measurable:**
- Correction cycle **<100 ms**
- **1–2 frames** at 60 fps (16–33 ms) = "instant"
- 50–100 ms = "has weight"
- **>100 ms = perceived as broken**

**The ADSR envelope:** any response = Attack / Decay / Sustain / Release. It makes "feel" something you can discuss in numbers.
- "Slippery" = a long release · "Wooden" = instant attack + release · "Sluggish" = a long attack

**The Lens of Juiciness (Schell):**
> Is my interface giving the player continuous feedback for their actions?
> Is **second-order motion** created by the actions of the player?
> Juicy systems reward the player **many ways at once**.

**Second-order motion** — motion **caused** by an action: not "the crate moved," but "the crate moved → hit the tower → the tower rocked → sparks."

**"The Art of Screenshake" (Nijman, Vlambeer).** 27 techniques in 25 minutes. The lesson is in the **method**: the techniques are cheap, they stack in layers, the effect is **cumulative**.

The order is **not accidental**: simulation first (less HP, higher fire rate, bigger bullets), effects **after**. **He balances the game before he polishes it.**

Three underrated ones:
- **Sleep / hitstop** — 2–4 frames of **total freeze** deliver more "weight" than any amount of particles. The cheapest trick there is.
- **Screenshake — three magnitudes.** As the impulse grows, add **rotation** — fractions of a degree read as force.
- **Permanence** — trails and shell casings turn "I shot" into "**I was here**."

**Animation-specific craft (Dave Bleja, Volnaiskra — developer of *Spryke*):**
- **Quantity is a quality of its own.** A single bubble is nothing; a dozen bubbles with slightly different transparency, size, wobble, and trajectory read as *alive* purely from the accumulated small variations — the mind stops tracking each one individually and perceives the whole. The same principle scales down to a single character: idle animation reads as alive when several small things happen at once (blinking, weight-shifting, breathing), not because any one of them is impressive.
- **An ugly frame, in isolation, can make the whole sequence better.** A single exaggerated or "broken-looking" pose — held for exactly one frame in the middle of a fast motion — reads as nothing but noise in isolation, but at full speed it sells impact the surrounding clean frames can't sell alone. Don't judge a frame by freezing on it; judge the sequence.
- **A blurred middle frame buys back milliseconds an animator doesn't have.** Compress a fast transition into two clean keyframes plus one deliberately blurred frame between them, and the eye reads continuous fast motion in far fewer frames than drawing the whole thing out — the technique that most benefits from it is exactly the transition a fast-paced game can't afford to spend real frames on.
- **Anticipation fights responsiveness, and the fix is to split them, not pick one.** The 12-principles-of-animation "anticipation" beat (wind up before a throw, inhale before a shout) looks better with a few lead-in frames — but a jump that visibly winds up before it fires reads as unresponsive input, because the player pressed the button *now* and expects the character to leave the ground *now*. Rayman Legends resolves this by dropping anticipation entirely on the jump specifically, while keeping it on landings and NPC jumps. Prince of Persia (1989) kept full anticipation on every jump and paid for it in perceived control lag, which was the right tradeoff for its era and the wrong one for how players expect a platformer to feel today. The general fix: fire the mechanic on the exact input frame, and put the anticipation entirely in the animation's *visual* weight transfer (a bounce, antennae lagging behind, an eye that moves first) rather than in a delay before the character actually leaves the ground.

**Criteria:**
- **Count the response channels:** sound, animation, particles, shake, a number, color, a state change. **<3 = dry. 5+ = juicy.**
- How many frames until the **first visible pixel**? **>6 at 60 fps → fix this first.**
- **Strip all the polish — does the control still read?** No → the problem is in the simulation. 🚩 **The classic mistake: fixing broken controls with particles.**
- **The one-layer rule:** add one technique at a time. Can't feel the difference → double it or throw it out.

---

## Onboarding: The First 60 Seconds

Good onboarding doesn't explain — it **constructs a situation where the only sensible action is exactly the skill you need**. The term is **conveyance**.

**Nintendo's method — 4 steps (Kishōtenketsu)**, a level as a showcase for **one** idea:
1. **Ki / Introduce** — the mechanic in a **safe environment**, where you can't lose.
2. **Shō / Develop** — the same, but now **dangerous**.
3. **Ten / Twist** — an **unexpected angle**.
4. **Ketsu / Conclude** — the final test.

Critically: **after step 4, the idea gets discarded.** This is how burnout is killed — a direct implementation of Koster's law.

**Mega Man X.** The vocabulary is small: **five buttons**. Falling debris teaches that the world is dangerous; a wall teaches wall-sliding; **the boss demonstrates the dash instead of explaining it.** Not a single text box.

**Valve:**
- **The Cabal (Half-Life)** worked this out explicitly: for **every** monster/weapon introduced, **what skills are expected of the player and how the game will teach them**. Teaching isn't a mode — it's **a schedule for the entire project**.
- **Portal — a cautionary tale.** A year in, playtesters would clear ~14 puzzles and say "great tutorial, can't wait for the real game" — **but that was the game**. The takeaway: **pedagogy alone isn't enough — you need an antagonist.** That's how GLaDOS came to exist.
- The sterile white walls are a **result of playtesting**: in a cluttered environment, players failed to recognize the puzzle elements. Style is subordinate to legibility.
- Scale: the first **20–30** playtests produced the understanding of what was fun; **200+** sessions in total.

**Criteria:**
- **The safe-room rule:** for every mechanic, is there a place to try it and **not lose**? If the first encounter punishes, that's an exam, not an introduction.
- **Walk each level through the 4 steps out loud.** A mechanic drags on for 5 levels with no twist → burnout.
- **The text test:** remove every hint. Will the player figure it out? No → **fix the level, not the hint. A hint is an admission that the design didn't work.**
- **The 60-second test:** did the player manage to (a) act, (b) get a response, (c) feel that it was good? **All three.**
- **Skill schedule:** a table of "skill → where it's introduced → where it's developed → where it's tested." **Gaps = frustration, duplicates = boredom.**
- **The Portal test:** "Will the player say, 15 minutes in, 'can't wait for the real game'?" Yes → they're missing **conflict/stakes**, not mechanics.

---

## Design's Three Pillars (Rogers): Character, Camera, Controls

Scott Rogers, "Level Up!" (2nd ed., 2023): three interdependent systems that every action game rests on — character, camera, controls. A failure in one breaks the other two, even if they're each designed perfectly.

⚠️ The Rogers quotes in this section and the two that follow (Level Design, Enemy and Boss Design) were extracted from the Russian translation and rendered back into English — they're not verified against Rogers' original English wording. Treat them as faithful in substance, not as citable verbatim English.

**Character.** Form follows function — three adjectives describe the hero (Mario: brave, bouncy, fun), body shape reads as character (round = friendly, square = strong). The player learns a **character's metrics** (height, speed, jump distance) intuitively through practice — the way a fencer learns the length of their own blade, not as numbers in a UI.

> "WALKING IS NOT GAMEPLAY!" — if the phrase "and then the hero walks over here" turns up in a design document, an alarm should go off in your head.

The same thing as the verb lens in SKILL.md, but framed as a test **for documentation**, not for a finished game: hunt for the verb "walks" in the design doc's text before it ever reaches the build.

**Camera.** It holds **one** frame of reference for the entire game — camera-relative or character-relative, never mixed mid-game.

> "Game designers often fall into this trap: they alternate between controls anchored to the camera and controls anchored to the character. It's incredibly annoying."

Example of failure: in a survival-horror game, after the camera flips inside a room, pushing the stick "left" sends the hero right, straight into the enemy's arms — the player isn't physically at fault, but feels clumsy.

Framing rules: the camera is **always** aimed at the target; the character must never vanish from frame; **don't let the player get backed into corners** — block them with visual geometry (bushes, fences), not invisible walls — corners cause camera flipping, and an invisible wall reads as a cheat.

**Controls.** An action should happen **on the button press** — the only exception is an explicit risk/reward window with a visible charge-up (example: charged attacks in The Mark of Kri). Vibration and gestures — the language must be **consistent**, not a constant hum: the two actuators at different frequencies in Silent Hill simulate a heartbeat only when it's a meaningful signal, not background noise.

**Criteria:**
- **Reference-point test:** take a combat moment with a camera flip — does pushing the stick "left" always produce the same on-screen movement direction for the character? No → camera and character are tangled up; fix this before any other change.
- **Document-walking test:** does the design doc, or a note on a screen, say "the hero walks over there"? Replace it with a verb — runs, climbs, takes cover, pulls up — or admit it's a transition, not gameplay.
- **Corner test:** is there a spot on the level where the camera is guaranteed to "flip" against a wall? Replace the invisible barrier with a visible one.

🚩 Inverted flight controls with no explicit toggle · a camera the player can neither control nor predict · a long animation with no instant response to a button press outside an explicit risk/reward window.

---

## Level Design (Rogers) — owned by `buro:level`

Rogers' level-design material lives with the seat that uses it: **`skills/level/references/canon.md`
§Rogers** — the beat chart, cliché themes and the "Mexican pizza", reuse-of-reuse and the
three-repeat test, alleyway vs island, weenies, illusory narrative, graybox pacing, puzzles as
player-vs-puzzle. Two of its rules bear on *mechanics* rather than space and stay in this seat's
scope, cross-referenced there: the **three-repeat test** for whether a system earns its place at all,
and **teaching is the whole game, not the first level** (see §Onboarding above).

---

## Enemy and Boss Design (Rogers)

**Form follows function for enemies too.** Parameters: size, behavior, speed, movement type, attacks, aggression, health. The "bottom-up" rule: attacks match size — a small enemy gets hit with a crouch or a leg sweep, a huge one only while jumping.

**Ten behavioral archetypes** — an axis orthogonal to the Grunt/Veteran/Elite difficulty taxonomy from the "Soulslike" section below (that one asks "how dangerous," this one asks "what exactly it does"): patroller, chaser, shooter, guard, flyer, bomber, burrower, teleporter, shield-bearer, mimic. Effective pairings: a shooter behind a shield-bearer · a big grappler + flyers · a teleporter + a grappler · a guard + a bomber.

**Speed is inversely proportional to strength.** If an enemy is simultaneously the fastest AND the strongest, the player will feel it as unfair, not as difficulty. The same principle as the dominant-strategy test, just applied to the opponent instead of the player's build.

**Telegraphing is mandatory** — a warning animation before an attack (a wind-up, a roar, aiming, a charge). Without it, damage feels like cheating rather than a lost exchange.

> "Enemies should be fought, not avoided" — a critique of the cliché "exploding charging enemy," which a first- or third-person camera simply doesn't let you see and react to in time.

**Bosses.** Three villain archetypes (per the Bond formula): the brute (beaten by cunning, not force), the intellectual (the climactic encounter), the global threat (a timer or a force of nature, not a character). The camera always focuses on the boss; extreme high angles diminish the drama, extreme low angles make attack distance hard to judge.

> "The player must land the final blow" — not a cutscene. The **"fake kill"** technique, for bosses who need to escape: let the player still feel like they won, even though the enemy got away.

**A contrarian twist — not every boss needs scale.** Designer Paul Girao's case (Dead to Rights): the hero spends years training in arm-wrestling for prison cigarettes; at the climax, that skill literally deflects the killer's knife bearing down on the villain's eye. The lesson has three parts: **the emphasis is on drama, not scale** (the camera stays on faces and hands, not the wide shot) · **the fight itself tells the story**, not a cutscene laid over it · **not a single new asset** — all the material had been introduced long before, the boss just found a use for what was already there.

**Criteria:**
- **The telegraphing test:** does every enemy attack have a recognizable warning animation, with at least one frame to react? No → the damage feels unfair regardless of the number balance.
- **The speed/strength test:** is the enemy simultaneously the fastest and the strongest in its category? Split those axes across different enemies — don't give one enemy everything at once.
- **The final-blow test:** does the player land the boss's last hit with a button press, or does a cutscene steal the victory? The latter robs the player of mastery they just earned.
- **The scale-vs.-drama test:** before inflating a boss with numbers and size — could the scene be made personal instead, hinging on a skill the player has already mastered? Often cheaper and stronger.

🚩 An enemy that's simultaneously fast and powerful feels unfair, not hard · an attack with zero frames of telegraph · a cutscene lands the final blow instead of the player · a stock "oversized brute" where a personal scene would have hit cheaper and harder.

---

## Sources

**Decisions:** [Sid Meier, GDC 2012](https://www.gamedeveloper.com/design/gdc-2012-sid-meier-on-how-to-see-games-as-sets-of-interesting-decisions) · [video](https://www.youtube.com/watch?v=WggIdtrqgKg) · [Costikyan, "I Have No Words" 2002 (PDF)](http://www.costik.com/nowords2002.pdf)

**Frameworks:** [MDA — AAAI (full PDF)](https://cdn.aaai.org/Workshops/2004/WS-04-04/WS04-04-001.pdf) · [Rules of Play (MIT Press)](https://mitpress.mit.edu/9780262240451/rules-of-play/)

**Lenses:** [Art of Game Design, 1st ed. PDF](https://www.inventoridigiochi.it/wp-content/uploads/2020/07/art-of-game-design.pdf) *(source of the verbatim quotes)* · [Table of Lenses, 3rd ed.](https://www.oreilly.com/library/view/the-art-of/9781351803632/xhtml/C02b_tol.xhtml)

**Koster:** [Theory of Fun: 10 Years Later, GDC Online 2012 (PDF)](https://www.raphkoster.com/gaming/gdco12/Koster_Raph_Theory_Fun_10.pdf)

**Uncertainty:** [Uncertainty in Games (MIT Press)](https://mitpress.mit.edu/9780262527538/uncertainty-in-games/) · [a review listing the types](https://lizengland.com/blog/2016/10/review-uncertainty-in-games-by-greg-costikyan/)

**Game feel:** [Designing Game Feel: A Survey (arXiv)](https://arxiv.org/pdf/2011.09201) · [The Art of Screenshake](https://www.youtube.com/watch?v=AJdEqssNZ-U) · [transcript](https://theengineeringofconsciousexperience.com/jan-willem-nijman-vlambeer-the-art-of-screenshake/) · [Juice it or lose it](https://www.youtube.com/watch?v=Fy0aCDmgnxg)

**Loops:** [The Chemistry of Game Design — Lostgarden](https://lostgarden.com/2007/07/19/the-chemistry-of-game-design/) · [Loops and Arcs](https://lostgarden.com/2012/04/30/loops-and-arcs/) · [Runaway Leader & Rubber Banding](https://oakleafgames.wordpress.com/2014/02/13/game-theory-runaway-leader-rubber-banding-and-feedback/)

**Degeneracy:** [Sirlin, Playing to Win — full text](https://www.sirlin.net/ptw) · [What is a degenerate game state?](https://www.skeletoncodemachine.com/p/degenerate-game)

**Verbs:** [A Game Design Vocabulary](https://books.google.com/books/about/A_Game_Design_Vocabulary.html?id=sZTlAgAAQBAJ) · [Robert Yang](https://debacle.us/)

**Onboarding:** [Mario 3D World 4-Step Design — GMTK](https://archive.org/details/SuperMario3DWorlds4StepLevelDesignGameMakersToolkit) · [Sequelitis — Mega Man X](https://www.youtube.com/watch?v=8FpigqfcvlM) · [The Cabal: Valve's Design Process](https://www.gamedeveloper.com/design/the-cabal-valve-s-design-process-for-creating-i-half-life-i-) · [Valve's Secret Weapon](https://gmtk.substack.com/p/valves-secret-weapon)

**Auctions:** [Auctions as a Game Balancing Tool](http://gamedesignaspect.blogspot.com/2013/12/auctions-as-game-balancing-tool.html) · [Cornell, Networks ch. 9 "Auctions" (PDF)](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch09.pdf) · [Medici Review](https://rolltoreview.com/medici-review/) · [GDC 2013: D3 auction house "really hurt the game"](https://www.pcgamer.com/diablo-3-auction-house-jay-wilson/) · ["it was on the box"](https://kotaku.com/diablo-3-real-money-auction-house-box-blizzard-1849700971)

**Loot:** [Psychology and Destiny's Loot System](https://www.gamedeveloper.com/design/psychology-and-destiny-s-loot-system) · [Loot 2.0](https://www.diablowiki.net/Loot_2.0) · [Legendary Pity Timer](https://www.diablowiki.net/Legendary_Pity_Timer) · [Belgium's Ineffective Regulation](https://online.ucpress.edu/collabra/article/9/1/57641/195100/Breaking-Ban-Belgium-s-Ineffective-Gambling-Law)

**Bots:** [Combat Dialogue in F.E.A.R. — Game AI Pro 2, ch. 2 (PDF)](https://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter02_Combat_Dialogue_in_FEAR_The_Illusion_of_Communication.pdf) *(read in full)* · [Three States and a Plan: The AI of F.E.A.R. (PDF)](https://www.gamedevs.org/uploads/three-states-plan-ai-of-fear.pdf) · [Handling Complexity in the Halo 2 AI](https://www.gamedeveloper.com/programming/gdc-2005-proceeding-handling-complexity-in-the-i-halo-2-i-ai) · [Sid Meier, The Psychology of Game Design (GDC Vault)](https://gdcvault.com/play/1012186/The-Psychology-of-Game-Design) · [notes](https://www.adachen.com/gdc10-notes-sid-meier-on-why-everything-you-know-is-wrong/)

**Soulslike:** Joshua Bycer, *Game Design Deep Dive: Soulslike* (CRC Press, 2024) · the Miyazaki quote — The New Yorker interview, 2022 (quoted via Bycer, p. 95)

**Three Pillars / Enemies and Bosses:** Scott Rogers, *Level Up! The Guide to Great Video Game Design*, 2nd ed. (cited via the Russian translation by A. Golubeva, Eksmo, 2023) — the same book's level-design chapters are credited in `skills/level/references/canon.md`

**Roguelikes:** Joshua Bycer, *Game Design Deep Dive: Roguelikes* (CRC Press, 2021)

**Free-to-Play Ethics:** Joshua Bycer, *Game Design Deep Dive: Free-to-Play* (CRC Press, 2022)

**Horror:** Joshua Bycer, *Game Design Deep Dive: Horror* (CRC Press, 2021)

**Yomi / Scrub / Bans:** [Sirlin, *Playing to Win* — full web edition](https://www.sirlin.net/ptw) · [Introducing... the Scrub](https://www.sirlin.net/ptw-book/introducingthe-scrub) · [Spies of the Mind (Yomi)](https://www.sirlin.net/ptw-book/7-spies-of-the-mind) · [What Should Be Banned?](https://www.sirlin.net/ptw-book/what-should-be-banned)

**Player Types:** Richard Bartle, *Designing Virtual Worlds* (New Riders, 2003); original taxonomy from "Hearts, Clubs, Diamonds, Spades: Players Who Suit MUDs" (1996)

**Damage Roll Probability:** [Amit Patel, redblobgames.com — Damage Rolls](https://www.redblobgames.com/articles/probability/damage-rolls.html)

**Crafting Systems:** [Jason Wishnov, Tuts+ — 5 Approaches to Crafting Systems in Games](https://code.tutsplus.com/5-approaches-to-crafting-systems-in-games-and-where-to-use-them--cms-22628a)

**MDA (full text):** Hunicke, LeBlanc, Zubek — see the Frameworks entry above.

**Practitioner notes (procedural generation, drop systems):** Anatoly Karlov, ant-karlov.ru — "Генерация уровней" (Wave Function Collapse experiments) · "Система дропа случайных вещей" (Zombotron/Knighttron rarity-tier drop algorithm)

**Animation craft:** Dave Bleja (Volnaiskra, developer of *Spryke*) — "5 Tricks That Will Make Your Animation Better," cited via the Russian translation on ant-karlov.ru
