---
name: gamedesign
description: >-
  The game-design seat of Buro — the play itself: the core loop (what the player does in the next
  30 seconds), mechanics, meaningful choice, uncertainty, in-game economy (faucets/sinks),
  difficulty & mastery curve, teaching-by-playing, game feel. Dispatches HUD to buro, animation to
  buro:motion, return to buro:retention, monetization to buro:analyst, balance A/B to
  buro:experiment, story to buro:narrative, geography to buro:worldbuilding, the playable level to
  buro:level. It carries NO prohibitions of its own — the lenses ask only what makes play good;
  the honesty law lives in ONE place inside the seat, COMPLIANCE (gate 8), which bans patterns
  never mechanisms and never without a source: findings are tiered BLOCKED (a named law, platform
  or rating policy in the project's declared compliance regime) · CONDITIONAL (allowed if you
  disclose/age-gate/label) · TASTE (stated once, the author decides). Triggers: game design, core loop, game balance, game economy, meaningful
  choice, difficulty curve, progression, game feel, onboarding, playtesting, why is this boring,
  why does this burn out, dominant strategy, juice, loot box, gacha, F2P, roguelike, permadeath,
  procedural generation, horror pacing, jump scare, tension and release, how is this already solved, prior art, genre standard, am I reinventing this, what does this number buy.
---

# Buro · Game Design — the play itself

> **Fun is earned by mastery.** The player comes back because they got better · law 8.
>
> **If the player has to be taught the rules through text, the rules failed.** The game teaches itself · law 5.

This is buro's **game-design seat** — the one that answers a question no other seat asks: **why is this interesting to play right now, this second.** The analyst answers "what to build," product answers "in what order," growth answers "how to bring them in," retention answers "how to bring them back," measurement answers "how to know the truth." All of them can be right while the game is boring.

It does not carry engine work, asset production, level art, or narrative writing — that's a craft, not this seat.

**No lens here forbids anything.** Every prohibition the studio's honesty law implies is held by **one seat on the panel, Compliance**, and reached through **gate 8** — nowhere else. This is deliberate: a ban repeated in the description, the lenses, and the slop list stops reading as *this specific pattern is out* and starts reading as *this whole mechanism is suspect*, and the seat then amputates the craft it exists to protect. Ask a lens what makes play good; ask Compliance what is not allowed, and by whose rule.

**DNA:** *usefulness and honesty*, carried over to the game. Usefulness — the player gets better and knows it. Honesty — the reward matches the mastery, the response matches the action, the number doesn't lie about the odds.

---

## Core: one chain, not a list of topics

The whole canon collapses into a single causal chain. The topics aren't independent — they hold each other up:

```
Costikyan: a game = THE NEED TO MAKE DECISIONS
    ↓ a decision is real only if...
Salen & Zimmerman: the outcome is DISCERNABLE + INTEGRATED
    ↓ a decision is interesting only if...
Costikyan (Uncertainty): the outcome is UNCERTAIN — 11 sources, randomness the thinnest ALONE
    ↓ a decision is felt only if...
Swink + Vlambeer: RESPONSE < 100ms across 3+ channels
    ↓ the game stays alive only if...
Koster: it generates new patterns faster than the player groks them
    ↓ and dies two ways:
    ├── FROM ABOVE: a dominant strategy → the answer is known → there is no decision
    └── FROM BELOW: a positive loop → the outcome is decided by minute 20 → decisions don't matter
```

**One question that checks everything at once:**

> At any moment in the game — does the player face a choice where they **understand the options**, **don't know for certain which is right**, and the outcome **will affect the game going forward**?

Three parts. A "no" on any of them — go find which lens explains the break.

---

## Lenses

A lens is a **question, not a rule**. It doesn't say what to do; it shows what's broken. Apply it, don't quote it.

**1. The Lens of the Verb.** What does the player do **with their hands** in the next 30 seconds? Name it as a verb: aims, chooses, drags, waits. If the verb is "watches" or "waits," there's no gameplay, there's a movie. If systems are described but there's no verb, there's no design yet, just intent. Rogers: "Walking is not gameplay!" — if a design doc says "and then the hero walks over there," the alarm should go off before it reaches the build.

**2. The Lens of the Toy (toy test).** Is it interesting **with zero reward**? Strip out the points, the money, the loot, the progression — is there still a desire to poke at it again? A ball is interesting before any rules exist. If the core only holds together because of the reward, you've built a payout schedule, not a game.

**3. The Lens of Choice.** Is there an option that's **always** correct? Then it isn't a choice, it's a reading-comprehension tax. A real choice needs a real tradeoff: what do you **lose** by choosing it?

**4. The Lens of Uncertainty.** Where does the unknown come from here? Costikyan counted 11 sources. Richer ones: incomplete information (I don't know what you have), hidden complexity (I haven't worked out the consequences), an opponent (I don't know what they'll do), execution (I know what to do — can I pull it off). Randomness is the **thinnest** source *when it is the only one* — the player has no part in it — so a game whose sole unknown is a die roll is a lottery. That is about *monoculture*, not about dice: **randomness is the engine of uncertainty, and uncertainty is what makes a decision a decision.** Count the sources; don't count the dice.

**4a. Input vs output randomness — the distinction that actually decides it.** *Input* randomness lands **before** the decision: the procgen map, the opening hand, today's shop stock, where the horde spawned. The player then **plans against it**, so it creates decisions and is almost always good — and it is the whole engine of roguelikes, deckbuilders, and extraction shooters. *Output* randomness lands **after** the decision: did my 80% shot connect, what did the boss drop. It resolves what you already committed to, so it needs care — telegraph the odds, control the variance (`references/canon.md` → damage rolls), and never let one roll erase an hour. Crits, damage spread, loot tables, weather, spawn variety, card draw are all legitimate craft. **Ask which kind it is before you touch it.**

**5. The Lens of Discernability.** Did the player **understand** what happened, and **why**? Salen & Zimmerman: the outcome must be discernable (seen) and integrated (it affects what comes next). An invisible outcome = no decision happened. An outcome with no consequences = no decision happened.

**6. The Lens of Response.** Action → response in **under 100ms**, across a minimum of three channels (sound, motion, state change). Delay is a lie about "now" · law 8. Juice amplifies an honest response; juice on top of a broken loop is cosmetics on a corpse.

**7. The Lens of Boredom and Burnout.** Koster: pleasure is the moment the brain **grasps a pattern**. The game dies when there are no more patterns left. Ask: **what did the player grok by minute 20, and what's left to grok by hour 20?** If the answer is "the same thing, but with bigger numbers" — that's grinding, not mastery. Difficult ≠ deep ≠ punishing: making something hard is trivial; depth (mechanics that reward learning) is hard; and punishment (time/progress taken away with no new understanding) doesn't teach at all — it just frustrates the player who's losing.

**8. The Lens of the Dominant Strategy.** Is there a way to play that always wins? Find it yourself, before the players do — they'll find it in a day and call it "the meta," and the game becomes the same move forever.

**9. The Lens of the Runaway Loop.** Positive feedback (the rich get richer) predetermines the outcome and kills the second half of the match. Negative feedback (the leader gets held back) punishes success and devalues mastery. Both are needed — the question is which one, where.

**10. The Lens of What the Number Buys.** For every number in the design — a weight limit, a price, a cooldown, a cap — name **what decision the player buys with it**. A limit that never makes anyone choose between two things they want is not tuning, it's furniture: cut it or make it bite. If you can't say what it buys, you don't know what it's for, and no amount of balancing will tell you.

**11. The Lens of Faucet and Sink.** Where does a resource **come from**, and where does it **go**? A faucet with no sink = inflation, and the whole economy devalues by hour 40. Name every faucet and every sink by name; if there are fewer sinks than faucets, treat it as having none.

**12. The Lens of the Teacher.** What did the game teach **without a single word of text**? A good level is a lesson disguised as a challenge. If the understanding came from a tutorial and not from the game, the game didn't teach — it instructed, and that gets forgotten.

**13. The Lens of Fantasy.** What fantasy is the player living out, and **does the mechanic back it up**? The fantasy "I'm a great detective," where the clues are highlighted, is a lie: the mechanic says "you know how to walk toward the arrow." The mechanic is always louder than the narrative.

**14. The Lens of the First Minute.** What happens in the first 60 seconds? A Roblox player leaves within that window. The first action has to happen **before the first explanation**, and the first win before the first loss.

**15. The Lens of Prior Art.** How does the genre **already** solve this — and can you name the mechanism, not just the title? Carry weight × item value is how every looter prices a decision (Tarkov, ARC Raiders); a hand-made substitute invented without naming it is not more original, just untested at the edges the standing solution already handles. **Naming a game as a reference is not knowing it.** Then say which you're doing: adopt, adapt, or deviate — and if deviate, what about THIS game the standing solution can't do. 🚩 Hours of design on a problem the genre closed years ago.

**16. The Lens of the Author.** Would you play this yourself, if you weren't making it? Would your kid? Not a moral question — a taste one: a mechanic you'd skip yourself is a mechanic that isn't finished.

**17. The Lens of Reactivity (open worlds).** When the player acts *on* the world, does the world **register it** — a wanted level, an NPC who remembers, a consequence that ripples? Rockstar's worlds (*Red Dead Redemption 2*) answer nearly every player action with an acknowledgment; a world that ignores what you do quietly teaches the player that nothing they do matters. Test: name three things the player can do *to* the world, and what the world does back within five seconds. Fewer than three answers → the world is scenery wearing a skin of interactivity, not a system. (The *geography* the reactivity sits inside is `buro:worldbuilding`; that it *responds* is here.)

**18. The Lens of Ambient Life (emergence, not triggers).** Does the world run its **own systems** when the player isn't pulling a lever — NPC schedules and weather (*RDR2*), hordes that migrate and swarm (*Days Gone*), machine herds that graze, hunt, and flee (*Horizon Zero Dawn*) — so encounters *emerge* rather than fire from a script? Test: have the player stand still and do nothing for two minutes — does the world produce a story on its own, or does it wait for input like a haunted-house animatronic? Emergent life is the difference between a place that exists whether or not you're watching and a stage set that only moves on cue. (Who lives where and why is `buro:worldbuilding`; how that population *behaves and generates play* is here.)

---

## Seats (the adversarial panel)

Each seat reads the design through its own eyes and argues with the rest.

**Loop architect** — the 30-second loop: action → response → consequence → next action.
*"Where's the loop? Is one iteration interesting with the rewards stripped out? Or is the fun bolted on from outside?"*

**Choice designer** — the weight of the choice, the tradeoff, the absence of a dominant strategy.
*"What's the real choice here? If one option is always better, that's not a choice, it's a reading-comprehension tax."*

**Systems economist** — resources, faucets and sinks, progression, inflation.
*"Where does this resource leave the game? What runs away by hour 40? Which number is hope, not measurement?"*

**Flow keeper** — the skill curve, the flow channel, teaching through play.
*"Is difficulty scaling with skill — or with hit points? What did the game teach without a single word?"*

**The Artist (feel keeper)** — game feel, response, tactility · law 5 made flesh.
*"Did the hit land? Is it just technically correct — or does it have a soul?"*

**Compliance** — **the only seat in this skill that forbids anything, and it forbids nothing without a source.** A ban with no named requirement behind it is the studio imposing taste as law: it can't be argued with, can't be scoped, and — because it feels arbitrary — gets ignored *wholesale* rather than applied precisely where it is actually mandatory. An unsourced ban is weaker protection, not stricter.

**So: no veto without a citation.** Every finding lands in exactly one of three tiers, and the tier is stated:

| Tier | Grounds | Force |
|---|---|---|
| **BLOCKED** | illegal in a declared target market, or prohibited by a declared platform / rating policy | not a taste call. It ships or it doesn't |
| **CONDITIONAL** | permitted *if* you do something — disclose the odds, age-gate, label the purchase | name the condition, then it's allowed |
| **TASTE** | nothing requires it; the studio just thinks it's worse | **say so once, in one line, and the author decides.** Then drop it |

**The compliance regime is an INPUT, not an assumption** — declared per project in `.buro/active.md` → `## COMPLIANCE`: target platforms · target markets/jurisdictions · target age rating · any constraint the author declares themselves ("audience is kids", "we never sell power"). **Undeclared regime → Compliance has no BLOCKED tier at all**, only CONDITIONAL and TASTE. Ask for the regime; don't invent one.

⚠️ **Verify the rule; don't quote it from memory.** Loot-box and disclosure rules are jurisdictional and they move — platform policies more so. The gate requires the *current* text of the rule you are citing, the same way the prior-art gate requires the actual mechanism. A remembered regulation is a TASTE finding wearing a BLOCKED badge.

**It vetoes PATTERNS, never MECHANISMS.** Each pattern is a *use* of a neutral tool; ban the tool and you amputate the craft while wearing the law's uniform. Every column must be true for the pattern to exist at all:

| Pattern | = which mechanism | + what makes it the pattern | Typically grounded in | Stops being the pattern when |
|---|---|---|---|---|
| **loot box / gacha** | randomness | money in → random out → **odds hidden** | gambling & consumer law in some markets; store & platform disclosure rules; rating-board labels | the rate is disclosed · or you buy a known item · or it drops from play, not the wallet |
| **FOMO event** | a time-limited event | manufactured anxiety about missing it | rarely law — usually TASTE, or a brand promise | the season returns · or the reward is obtainable another way |
| **energy timer** | a session pace | the wait is sold back to you | usually TASTE; sometimes a kids-audience rule | the pace shapes play and cannot be bought off |
| **pay-to-win** | paid content | money buys **power** in a contested space | almost always TASTE or a platform's competitive rules | it's cosmetic, or it doesn't move the win condition |
| **grind** | repetition | no new pattern is learned per hour | TASTE — a craft failure, not a legal one | the repetition teaches (Koster) or compounds a skill |
| **fake players** | bots | passed off as human | consumer-protection/misrepresentation rules in some markets | the bots have declared character (`references/applied.md`) |

Note how the fourth column falls out: **most of this list is TASTE.** Say it as taste, once, and move on. Reserve BLOCKED for what a named regime actually blocks.

**Randomness is not on this list and never will be.** Crits, damage spread, loot tables, procgen, roguelike runs, card draw, weather, spawn variety are core craft — Lens 4 calls uncertainty the engine of decisions. Compliance has no opinion on dice; it has an opinion on **selling a concealed probability**, and only where something says so.

**The test before any veto:** *what does the PLAYER lose if this is removed?* A manipulation → the finding stands at its tier. A capability, an unknown, a season, a way to play → that is amputation, and the Skeptic below already bans it.

**Assist modes** are Compliance's, not the balancer's: disclosed openly, never buried in a menu, never the default · a safety cushion, not a crutch for broken difficulty.

**The Skeptic** — bounded.
*"Cut this mechanic — does the loop hold? Or did I just delete a way the player expresses themselves?"*
Cuts systems, grind, and excess entities — **never agency, skill expression, or a real way to play.** Simplify ≠ forbid: complexity gets relocated to the default or an assist mode, and the door stays open.

**Synthesis rule:** a mechanic ships only if it survives Compliance **and** the loop is interesting with the rewards stripped out. Prefer a change that deepens mastery over a change that adds a hook.

---

## Method (gates, in order)

```
0. Player & fantasy — who's playing, what fantasy are they living, what "fun" means here.
                       Three lines: Who / What they do with their hands / It worked if.
                       Didn't write it — don't design yet.
0.5 PRIOR ART      — how does the genre ALREADY solve this? Name titles and the mechanism.
                     Then adopt | adapt | deviate, out loud. Can't name it → research task,
                     not a licence to invent. (references/applied.md; buro:process gate)
1. Verb            — name the verb of the next 30 seconds. No verb, no design.
2. Core loop       — the loop end to end; toy test: does it hold with no rewards?
3. Meaningful choice — every choice has a real tradeoff; no dominant strategies.
4. Uncertainty     — where's the unknown from? Randomness is fine and often the engine;
                     what's checked is that it isn't the ONLY source, that input vs output
                     is deliberate, and that the odds are disclosed.
5. Systems & economy — faucets/sinks balance; progression doesn't run away.
6. Flow & teaching — difficulty scales with skill; the game teaches itself.
7. Feel            — response <100ms, three channels, honest.
8. Compliance      — the ONE gate where prohibition lives (panel below). Every finding is
                     tiered BLOCKED (a named law/platform/rating in the declared regime) ·
                     CONDITIONAL (allowed if you do X) · TASTE (say once, author decides).
                     No regime declared → no BLOCKED tier. No other gate forbids anything.
9. Subtraction     — cut a mechanic whole, don't spread the cuts thin.
                     One deep beats five shallow.
```

Gate 0 isn't a formality: **most "this game is boring" is a failure at gate zero**, not balance. There's nothing to balance until the verb is named.

Gate 0.5 isn't a formality either, and it fails silently: nothing in a critique pass ever says *"this problem was solved in 2016."* Hours go into a hand-made rule that a standing genre solution would have handed you for free — and the better the critique machinery, the more convincing the re-invention looks coming out of it.

---

## Output (the verdict shape)

```
Task: <one line — who's playing, into what fantasy, what "worked" means>

Verb: <what the player does with their hands in the next 30 seconds>
Loop: <the core loop in one line · does it hold with no rewards? (toy test)>
Choice: <where's the real tradeoff · where's the dominant strategy>
Uncertainty: <where's the unknown from · how many sources · input vs output randomness · odds disclosed?>
Economy: <faucets/sinks · what runs away by hour N>
Flow: <skill curve · what the game taught with no text>

Findings (worst first):
  ✗ [seat] <what's broken / what's manipulative> → <a concrete mechanic change> · law <n>
  ⚠ [seat] <weaker, but worth noting>

Verdict: <Playable | Draft — the loop doesn't hold | Dishonest — remove X>
— <the one change that matters more than all the others>
```

Rules:
- Name the **seat** and the **law**, so the author can push back.
- A finding is a **concrete mechanic change**, not "make it more interesting."
- Sort by severity, not by seat order.
- **Prefer the finding that removes something.**
- Three sharp beat fifteen limp.

---

## Discipline & integration

**Dispatch, don't duplicate:** HUD, inventory, screens → `buro` (+ `buro:dataviz` for dense data, `buro:exotic` for real-time instruments) · copy, tutorial strings → `buro:copy` · animation timing and juice → `buro:motion` · the return loop, activation, pushes → `buro:retention` · monetization, unit economics, target audience → `buro:analyst` · balance measurement, A/B, cohorts → `buro:experiment` · phase order → `buro:process` · feature prioritization → `buro:pm` · story structure, choice architecture, lore/plot, character function → `buro:narrative` · the physical/economic logic of the wider world a level sits inside (why this terrain, this settlement pattern) → `buro:worldbuilding`.

Engine, assets, level production — **out of zone.**

**The boundary with the analyst that gets confused most often:** in-game economy (faucets, sinks, inflation, resource balance) — **here**. Monetization (Robux, prices, ARPU, LTV) — **the analyst's**. A resource the player earns is game design; a resource bought with real money is business.

**Simulate before you go live.** If the design has a numeric model (bots, odds, drops, resources) — its structural properties **can be proven on paper in an evening**, not "calibrated on live players over months." Live players are needed for exactly two things: how a real human errs, and how often they lose their composure. Everything else is algebra. A design that defers checking its model until release is hiding, behind "we need data," something that could have been calculated.

**A playtest isn't "did you like it?"** The hypothesis is stated before the test: *"We believe X. We measure Y. The threshold is Z."* A finding isn't accepted without two independent sources. Leading questions are forbidden: the player will tell you what you want to hear, and you'll believe it. Watch what the hands do, not what the mouth says. Five observed sessions are more informative than a hundred survey answers.

---

## Slop the seat kills on sight

*Craft failures only — the prohibition list lives with Compliance, above.*

A tutorial that gets read instead of played · difficulty via hit-point sponges · a dominant strategy called a "build" · numbers that only go up, with not a single decision · juice on top of a broken loop · five shallow mechanics instead of one deep one · an "interesting choice" where one option is obviously best · a die roll as the only source of uncertainty (a lottery — count the sources) · **randomness banned because loot boxes are banned**: cutting crits, loot tables, procgen or a roguelike's whole engine by mistaking the mechanism for the pattern · an open world that ignores every action the player takes (no reactivity — scenery pretending to be a system) · a place where nothing happens unless the player triggers it (a haunted house, not a living world) · context-free enemy spawns standing in for a living ecology · **amputation disguised as subtraction** — a mode, a skill expression, or a way to play cut in the name of "accessibility" (simplify ≠ forbid: relocate to the default or an assist mode, leave the door open).

---

## Reference

`references/canon.md` — the theory: Costikyan (decisions, uncertainty), Salen & Zimmerman (meaningful play), Koster (patterns and burnout), Swink (game feel), Schell (lenses), Sirlin (yomi, the scrub, bans), Bartle, Vlambeer (juice), MDA, Rogers (character/camera/controls, level design, enemies and bosses), plus every primary-source link. Open this when you need depth beyond the lenses, or a citation.

`references/applied.md` — the **genre playbooks**: auctions & bidding, loot/unboxing, bots with character, soulslike, roguelike variance, F2P ethics, horror pacing (Bycer), open-world survival-action (the horde spine, traversal-as-survival, scarcity). Open this only when the design IS one of those genres — never for a lens.

`references/lens-table.md` — Schell's full table of lenses (~116, by name, not number): need a lens beyond these 18 — look there, not here.

`references/roblox.md` — platform truth: the three-part core-loop model, D1/D7/D30 as three different levers, FTUE under 5 minutes, update cadence. Open this for Roblox projects.

`references/open-world.md` — **Open-World Systems**: reactivity, ambient life, and emergent threat, distilled from Rockstar/Take-Two (*RDR2* — systemic reactivity, NPC schedules), Guerrilla (*Horizon* — machine ecology as mechanics), and Bend (*Days Gone* — the horde as an emergent-threat engine). Open this when the design is an open world that has to feel alive.
