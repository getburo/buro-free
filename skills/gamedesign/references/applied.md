# Game Design — Applied Genre Playbooks

Genre-specific application of the lenses. The theory they apply is `canon.md`; open this file
only when the design is one of these genres.

**Contents:** [Auctions](#applied-auctions-and-bidding) · [Loot and Unboxing](#applied-loot-and-unboxing) · [Bots with Character](#applied-bots-with-character) · [Soulslike](#applied-soulslike--reflex--abstracted-in-one-mechanic) · [Roguelike Variance](#applied-roguelike-variance-and-persistence) · [F2P Ethics](#applied-free-to-play-ethics--naming-the-mechanics) · [Horror](#applied-horror--tension-scarcity-and-the-one-chance) · [Open-World Survival-Action](#applied-open-world-survival-action--the-horde-spine-traversal-as-survival-and-scarcity)

Sources for every section: `canon.md` → Sources.

---

## APPLIED: Auctions and Bidding

An auction **shifts balancing from the designer onto the players**. The designer doesn't need to know what a lot is "worth" — the room sets the price. A self-balancing mechanic: a lot is strong → people overpay → the price eats the advantage. You play **against people, not against rules** — which is why simple rules produce deep play.

**Knizia's technique — Victory Points as a Resource.** In Medici, **money is the sole source of victory points, at a 1:1 conversion**. "All the tension comes from how much you're willing to **lose** in order to **win**." Every bid is literally spending victory points.

| Type | What it does to the game |
|---|---|
| **English** (open outcry) | Maximum drama **and maximum AP** |
| **Once-around** (exactly one bid each) | Kills stalling, sharpens the value of turn order. Medici's core |
| **Dutch** (descending price) | Fast, tense; rewards decisiveness, not calculation |
| **Sealed bid** (first-price) | Bluffing, reading the opponent, the "winner's curse" |
| **Vickrey** (pay the second price) | Removes the fear of overpaying. **Mathematically elegant, unintelligible to players, emotionally flat** |
| **Fixed price** | Not an auction of value, but an auction of the queue |

With **risk-averse** players, Dutch and sealed first-price auctions yield the seller more than Vickrey/English. Choice of auction type = a direct dial for tuning the economy.

**Known problems:**
1. **Analysis paralysis** — valuing a lot is an open-ended task with no upper bound on deliberation.
2. **"Auctions are merciless to newcomers"** — the genre's central complaint. Bidding meaningfully requires knowing the price metagame. A newcomer doesn't — and pays for it in money.
3. **Runaway leader / money-is-VP** — Knizia cures this by making money **finite** (in Ra you bid with a fixed set of "suns," which **pass to your opponent**).
4. **"Who bids first"** — a hidden, enormous advantage.
5. **Kingmaking** — a losing player jacks up the price out of spite.

**Diablo 3's failure.** Jay Wilson (GDC 2013): the auction houses "**really hurt the game**." Used by **>50% of players**. The reason: the auction **short-circuited the loot loop** — it "dampened the core motivation: playing through the story and killing Diablo." Why kill monsters for a chance at an item when you can just buy it?

A separate lesson: they couldn't remove it right away — **"legally, we didn't think we could, because it was listed on the box."**

**Counter-example — WoW's auction house** works: (a) it's an in-game currency, (b) there's a **gold sink** — a 5% fee fighting inflation, (c) it **doesn't replace looting** — it rewards market knowledge.

**Criteria:**
- **Self-balancing test:** if a lot is overpowered, does the price automatically eat the advantage? No → the auction is decorative.
- **Knizia pain test:** does the player spend what they need for victory? Bidding currency and victory currency are unlinked → the bid costs nothing.
- **Finiteness test:** can a wealthy player just keep outbidding forever? **Where's the faucet, and where's the sink, for the currency?**
- **Newcomer test:** can someone seeing a lot for the first time value it in 5 seconds? No → give them an **anchor** (a reference price, sale history).
- **Turn-order test:** win rate by first-bid position. A gap of more than a couple of percent → compensate for it.
- **Timer test:** **an auction with no timer = AP by construction.**
- **The Diablo test:** **does the auction short-circuit the core loop?** Buying beats looting → looting is dead.

🚩 Infinite money → a test of patience, not a decision · No sink → inflation, newcomers locked out permanently · English with no timer at 4+ players → AP · Vickrey "because it's mathematically correct" → the player won't understand what they paid for; **elegance ≠ emotion** · Real money → legal risk plus **a promise printed on the store box can physically forbid you from fixing the mechanic**.

---

## APPLIED: Loot and Unboxing

Loot feels good **not because of the item, but because of the uncertainty before the item**. Variable-ratio reinforcement (Skinner): a reward on an unpredictable schedule produces behavior **more resistant to extinction than a guaranteed reward**. The key shift: **anticipation itself becomes the reward**. That's why the opening ritual is **not decoration but the actual product**; the item is just the excuse for the pause.

> "When a reward arrives on a predictable schedule, it stops feeling special almost instantly. But when the timing and size of the reward are uncertain, **the anticipation itself becomes the reward**."

**Color tiers — Diablo's contribution.** Color = a value scale readable **in 100 ms, without reading a single stat**. This is what made "loot rain" possible.

**Diablo 3's "Loot 2.0" (2014) — a canonical breakdown of mistakes:**
- **Smart drops** — an item rolls its stats for the class that found it
- **Fewer, but better**
- **The moral: the problem wasn't rarity — it was that 99% of the drops were trash.** Frequent empty rewards devalue the ritual.

**Pity / protection from bad luck:**
- *Soft pity* — past a threshold (~75 pulls), the odds start climbing; by pull 89 they can be 50%+ against a base rate of 0.6%
- *Hard pity* — a guarantee after a fixed number of pulls
- Genshin: 90 wishes, plus "lost the 50/50 → the next one is guaranteed to be the banner unit." **Diablo 3: a hidden Legendary Pity Timer — no more than ~2 hours without a legendary.**
- Its honest purpose: pity "protects players from extreme bad luck, **and protects the publisher from rage, refunds, and regulator complaints**"

**The ethical line — three questions:** does the player pay **real money** for a random outcome → can the outcome be **cashed back out** into money → are the odds **disclosed**.

Belgium — a full ban on paid loot boxes (2018), yet **82% of the top-100 iPhone games kept them anyway**. China — mandatory odds disclosure.

**Criteria:**
- **The pause test:** is there a moment of uncertainty, ~0.5–2 sec, between the action and the result? An instant result → **you threw away the actual product**.
- **The 100-millisecond test:** is the value legible from color/silhouette/sound **before any text is read**?
- **The Loot 2.0 test:** what fraction of drops trigger a reaction? **<~30% → cut the quantity, raise the quality.**
- **The worst-case player test:** compute the **99th percentile of bad luck**. If the number is scary, you need pity.
- **The regulator test:** does the player pay real money for a random outcome? Yes → **you're in regulatory territory regardless of intent**.

🚩 Trash rain "for a sense of abundance" → D3's mistake · **An animation rigging a near-miss** → that's slot-machine mechanics, not design · No pity → guaranteed players with a catastrophic experience · Hidden odds plus real money → illegal in China · "We're just using variable ratio" as an excuse → that's **precisely** what the regulator is watching for.

**The line:** an honest near-miss (the outcome of an honest roll) is design. A **rigged** near-miss is a dark pattern. The difference is whether you're lying to the player about the state of the system · law 8.

**A working single-player counter-example — the same rarity vocabulary, used honestly.** Anatoly Karlov (indie developer, *Zombotron*/*Knighttron*) documents the exact weighted-roulette algorithm behind an honest, non-monetized drop system: four rarity tiers (Common/Rare/Epic/Legendary) each with a fixed probability weight (1.00 / 0.35 / 0.15 / 0.01); a "container" is defined not by a specific item but by an entity type, a count, and a drop chance ("8 random coins at 70%, 3 ammo packs at 60%, 1 boots at 40%"); rolling against a container sums the weights of every eligible candidate into one "roulette length" and picks a point along it — the same weighted-lookup-table technique named in the damage-roll section above, applied to items instead of numbers.

Two details worth stealing directly: **ammo drops are filtered to weapons the player actually owns**, so the roulette never wastes a slot on ammo for a gun that isn't in the inventory — and **item rarity is filtered by character level**, so a level-5 container's roulette only contains items that require level 5 or below, which is the concrete implementation-level fix for the Roguelike section's "random-item-math" problem above: it prevents a lucky early drop from trivializing the whole run, without banning anything or needing a hard "requires level 8" tag players carry around as an unusable trophy.

The same author also names a hidden anti-frustration adjustment: ammo drop probability quietly rises when the player is critically low across nearly every gun — but only then, and it never fully saves a player who consistently misses. Same principle as the "tilted RNG" example in the Roguelike section above (XCOM's creeping hit-chance), independently arrived at in a different genre.

---

## APPLIED: Bots with Character

Game AI isn't about intelligence — it's about **the illusion of intelligence**. The player never sees the algorithm; they see behavior and build the story themselves. Hence a conclusion confirmed by both canonical talks below: **it's cheaper and more effective to make the AI ANNOUNCE its intentions than to make the AI actually smart.**

**F.E.A.R., Jeff Orkin** — the single most valuable source here:

> **"If the AI didn't say it, it didn't happen. That was the AI design philosophy behind the squad behavior in F.E.A.R. There's no point spending significant effort implementing sophisticated AI if the player never notices it."**

> "Although developers remember F.E.A.R. for its GOAP, it's clear from the reviews that **what stood out to players was specifically the coordinated squad behavior**."

**The technique: replace a bark with dialogue (2–3 lines between squad members).**
> "Instead of the wounded guy just yelping in pain, someone else shouts, 'What's your status?' The wounded one answers, 'I'm hit!' This dialogue serves **several purposes at once**: it tells the player they landed a hit; **it reinforces the illusion that the AI is working as a squad**; and it hints at the enemy's health state."

**Dialogue as an excuse for inaction:**
> "If you shoot at someone and they don't move, they look like **dumb, broken AI**. But if you hear 'Get out of there!' — 'I've got nowhere to go!', you understand that the AI **is aware of the threat and wants to move, but can't find a better position**."

**And the main point:**
> **"From a production-budget standpoint, this might be the single most valuable line item. Dialogue can be used to create the illusion of behavior that was never actually implemented."**
> "The AI counted the dead: 'Man down!' The last one called out, 'We need backup!' In any shooter, the player will sooner or later see fresh enemies show up — and conclude that's who was called in. **We never wrote a single line of code for calling in reinforcements — but the reviews said we had it!**"

> "Don't underestimate the power of language. **Our perception of intelligence rises on a subconscious level when we see someone using language effectively.**"

**Halo 2, Damian Isla:**
> **"AI works best when the player believes they're fighting a living, breathing (malicious) creature."**

Complexity produces "**a murky experience, in which the AI seems to be acting 'randomly' rather than 'intentionally'**." Principle #2: **"Value legibility above all else."** The chief enemy of legibility is **dithering** (flickering between actions).

**Sid Meier — AI should feel fair, not be fair.** GDC 2010: a player complained about losing at **3:1 odds in their own favor**. **And didn't complain about winning at 3:1 against them.** They accepted a loss at 2:1, but not at 20:10 — the same odds, a different perception. He had to **shift the actual odds away from the true probability** to make the game feel fair.

**XCOM implements exactly this:** hidden aim assist above 50%; below 50% it's honest. On lower difficulties — **a stacking bonus for consecutive misses**.

⚠️ **The price:** players dug this up, and part of the audience took it as "the developers cheated" — with the observation that showing the adjusted numbers wouldn't have hurt. **Tilting things in the player's favor is fine. Get caught hiding it, and you pay in trust.**

**Criteria:**
- **The Orkin test (the main one):** take every piece of smart behavior. Does the player ever find out about it? **No → cut it and replace it with a line of dialogue.**
- **The Orkin inversion:** which behavior can you **only announce, and never actually implement**?
- **The inaction test:** when a bot makes a weak move, does it explain why? "I've got nowhere to go!" **turns a bug into character.**
- **The dialogue-vs.-bark test:** are the lines shouted into the void, or **addressed to each other**? Dialogue between two bots is incomparably more convincing.
- **The Isla test:** watch 2 minutes of footage with no code. "Intentional" or "random"? The latter → the problem is legibility, not intelligence.
- **The character test:** describe every bot with **one adjective**. A character = asymmetric parameters + lines that voice them.
- **The Meier test:** judge not "is it fair" but "**does it feel fair**."
- **The believable-loss test:** the bot should lose because of a **legible mistake**, not "a number dropped."
- **The getting-caught test:** if the tilt gets discovered, does it look like care or like deception?

🚩 Smart AI with no voicing → a budget spent on something nobody will ever see · **Difficulty = stat inflation** → that's a tax; difficulty should grow through **readable tells** · Dithering → illegible, and therefore characterless · Cheating **visibly** → wrecks trust instantly · Every bot is one archetype at a different power level → **a slider, not characters** · "Players just don't understand statistics" → **they DON'T, and that's your problem, not theirs.**

---

## APPLIED: Soulslike — Reflex + Abstracted in One Mechanic

The genre is hard not because it's hard for the player, but because the designer has to master **both** disciplines at once. Bycer, "Game Design Deep Dive: Soulslike" (2024): *reflex-driven design* (player skill decides the outcome — action) and *abstracted design* (character stats decide the outcome — RPG) are normally kept in separate genres. The Souls formula is their deliberate fusion.

> "Making a good soulslike is not about designing a great RPG with poor combat or vice versa but making both designs work in harmony together."

**Three genre qualifiers (Bycer's explicit definition):**
1. **Combat parity** — the player stays roughly at the enemies' level of power and pace, unlike DMC/DOOM/God of War, where the player is by design the stronger party.
2. **A viable multi-build** — different playstyles (melee, ranged, magic) aren't merely different, they're all **playable**, not just "different for the sake of variety."
3. **Shortcut-based level design** — dense, looping zones with a checkpoint (bonfire), rather than a linear start-middle-end corridor.

Missing even one of these, and it's not a soulslike — just a hard game with one good part and two weak ones.

**The bonfire loop.** The Estus Flask (a recharging resource, not a finite consumable) solved a problem in earlier games: finite healing chokes the pace for the whole run, while unlimited healing kills risk. The flask turned healing into a **separate risk mechanic** — you need to find a safe window to drink it, but long-term it doesn't punish the player. The price of resting at a checkpoint is that **every enemy in the zone respawns**: a checkpoint is a trade between safety and rolling back progress, not a free save.

**Sidegrade, not upgrade.** In a typical ARPG, a new weapon replaces the old one. In Souls, variants of the same weapon type are a **lateral choice**, not an upgrade: a heavy sword and a light sword of different classes don't outclass each other — they serve different styles. The test: if a new item is always strictly better than the old one, that's not a sidegrade — it's a timer counting down to your build's obsolescence.

**Difficulty ≠ depth ≠ punishment** — three different things that get confused constantly:

> «Depth, not difficulty» — to move the player through a game and learn its mechanics, there must be depth, not difficulty, to the gameplay.
> «Failure is not the same as punishment.»
> Miyazaki (New Yorker, 2022): «Hardship is what gives meaning to the experience... it's our identity.»

Making a game hard is trivial. Making it **deep** (mechanics that reward learning) is hard, and it's depth — not difficulty by itself — that carries the player through the game. **Punishment** (losing time/resources/progress after death) is different from both: it only lands on players who are already losing, and **doesn't make them any better** — it just piles on frustration weight with no new understanding. The canonical failure is **World Tendency** in Demon's Souls: the system secretly made a zone harder after a run of player deaths, punishing weaker players without them ever knowing it. Never repeated in any later game in the series.

The same point is independently stated by Scott Rogers in "Level Up!": "Hard emphasizes pain and loss. Challenging emphasizes mastery and improvement." Two different sources arriving at the same line — the coincidence is itself an argument that the distinction is real, not one author's personal taste.

**Accessibility ≠ Approachability ≠ Assist mode** — three more terms that get confused just as often:
- **Accessibility** — options that let someone with a specific limitation play at all (a colorblind mode, subtitles, disabling photosensitive effects).
- **Approachability** — QoL that makes the game easier **for everyone** (auto-equip, clear stat descriptions, legible menus).
- **Assist mode** — bypassing the challenge entirely, which is not the same thing as approachability.

> "Think of assist modes like an airbag in a car" — they should exist for when they're needed, but they shouldn't be the default experience. "They are not there to fix your game or ignore problems but to make what's there better."

An assist mode doesn't excuse an unbalanced game, and it must be **announced explicitly**, not buried in a menu (a failure example — Young Souls: players quit without ever learning the available options existed).

**Enemy taxonomy** (by increasing power): Grunt (weak, dangerous in a pack) → Veteran → Supporter (utility/ranged, rarely alone) → Elite (mid-boss, dangerous even solo) → Boss (unique, one-of-a-kind, its own pattern).

**Zone taxonomy**: Hub/base (safe, vendors) → Transitionary area (a connector, optional bosses) → The Stage (a full start-middle-boss arc).

**Criteria:**
- **The three-qualifier test:** parity + a viable multi-build + shortcut-based level design — all three at once, or it's not the Souls formula, just a hard game.
- **The difficulty/UX test:** is this moment hard because it challenges skill, or because it's unexplained and illegible? Speedrunners routinely prove that the "hardcore" games of the '80s–'90s were just poorly explained, not deep.
- **The punishment test:** after death, did the losing player understand what to change on the next attempt — or did they just lose time and resources with no new knowledge?
- **The assist-mode test:** is it explicitly announced and not the default (an airbag) — or is it hidden and implied as the "fix" for broken balance?
- **The input-reading test:** does the AI react to the **specific button** the player is pressing, predictably, every single time? That's not learned behavior — it's a pattern exploit; don't confuse it with genuinely difficult AI.
- **The dominant-defense test:** does one defensive move (a parry, a specific build) trivialize **every** encounter? See the dominant-strategy lens — same test, different mechanic.

🚩 **Escalation trap:** the only way to add content is raising numbers instead of designing a new pattern ("progression should be intrinsic — the player actually gets better, not just leveled-up"). · **Input reading** passed off as "smart AI" — that's an exploit, not learning. · One prevailing defensive move (a parry) is so strong it trivializes the entire fight — frustrating precisely because there's no reason left to take a risk. · Assist mode buried in a menu with no on-screen indicator — the Young Souls failure. · Copying the aesthetic of "Dark Souls of X" without all three pillars at once — a marketing trick, not a genre shift.

---

## APPLIED: Roguelike Variance and Persistence

Joshua Bycer, *Game Design Deep Dive: Roguelikes* (CRC Press, 2021): the genre's whole design problem is **variance**, not randomness. "Procedural generation is a powerful tool and a great way to ruin your game design" (Tanya Short, quoted p. 25). "Procedural generation will not save a bad game" (p. 27).

**Random generation ≠ procedural generation.** Random generation picks from a fixed list of developer-authored outcomes. Procedural generation mixes developer-defined pieces into new combinations. Neither one *is* variance — variance is a separate, harder property: **do different playthroughs actually feel different and stay balanced?**

**The Focal Points of Replayability — three things content generation must actually vary:**
1. **The goal** — position/type can shift, but the underlying purpose should stay legible.
2. **The player's tools** — new items/abilities must offer a genuinely new benefit, not a reskinned one, or variance is an illusion.
3. **What's in the way** — enemies/hazards/obstacles must scale in difficulty as the player masters the system, or they become window dressing.

A game can generate an enormous space and still fail this test — *Invisible, Inc.* had procedurally generated levels but only a handful of objective types and enemy factions, so strategies converged fast and exploration became "a chore." Contrast *The Binding of Isaac*: 300+ items with genuinely different effects, stacking unpredictably — McMillen told Bycer he deliberately gave up on "completely balancing" the game because unpredictable combinations were the point.

**Persistence — the honesty fork.** Two different uses of "stuff that carries over between runs":
- **Unlock-only persistence** (the purer form) — carryover unlocks new *content* (items, biomes, endings), but every fresh run starts from the same baseline strength. *Binding of Isaac*'s model.
- **Power-up persistence** — carryover *permanently strengthens the character*. This isn't a variant of the same design, it's a different balance philosophy: the game is no longer balanced run-by-run, and "almost every player should eventually be able to beat the game" just by grinding upgrades — which erodes the skill-based promise that makes a roguelike a roguelike in the first place.

**Fixed content invites a meta — the same failure as the dominant-strategy lens, on a different axis.** Any predictable anchor (a boss always at the same HP, an event that always triggers the same way) lets players over-prepare, and worse, can specifically counter certain builds no matter how well the run otherwise went — *Slay the Spire*'s third-map boss pool was tuned to hard-counter specific decks, punishing players "for something they could not have predicted." *FTL*'s fixed three-stage final boss is the book's worked fairness example: with 5 of 30 items providing healing, that's a 16.7% chance per run of getting one — and adding 30 more non-healing items via DLC drops that to 8.3%, making the game *less* fair while nominally "adding content."

**Progressive difficulty, done right — *Hades*'s "Pact of Punishment."** The player chooses *which specific modifiers* to enable (more trap damage, time limits, less healing), each with its own point value and reward. Contrast with blanket difficulty settings: every tier must stay independently winnable, buffing the player to survive a hard tier can break the easy one, and the margin for error shrinks sharply at the top — a build that worked at baseline can become nonviable.

**The roguelike/roguelite/action-roguelike/soulslike confusion is itself a design decision, not just marketing.** Roguelike = run-by-run, permadeath, procedural, no fixed endpoint that stops replayability. Roguelite = the same tools, but structured around a fixed endpoint and long-term persistence-driven progression toward a final win. Action roguelike = skill-first (the player's own reflexes matter more than RPG abstraction); persistent upgrades exist but are optional help. Soulslike = a separate genre entirely — no procedural generation, no run-based replay, a single continuous playthrough with persistence tied to the character, not the run (see the Soulslike section above). Getting this wrong in your own design doc means you're building toward the wrong promise.

**Criteria:**
- **The three-focal-points test:** does this run vary the goal, the tools, *and* what's in the way — or just reshuffle cosmetics while the actual path stays the same?
- **The persistence-fork test:** does what carries over unlock content, or does it permanently strengthen the character? The second one needs its own balance philosophy, not a patch on the first.
- **The fixed-content test:** is there any anchor point (boss HP, a scripted event) predictable enough that players will build a wiki page around it? That's where the meta will calcify.
- **The false-choice test (both directions):** is there an option that's never viable, or one so strong it's mandatory? Either one kills real variance — this is the same test as the dominant-strategy lens, applied to procedural balance.
- **The random-item-math test:** calculate the real odds of getting a critical item before shipping more content that dilutes the pool (his 30→60 item, 16.7%→8.3% example) — "adding content" can quietly make a run less fair.

**A practitioner's warning about procedural generation specifically, from outside the roguelike genre.** Anatoly Karlov, documenting his own Wave Function Collapse experiments for tile-based level generation: "when you study levels made by a level generator, you quickly realize they're all built on some basic algorithm, and the chance of finding something genuinely unique trends toward zero... you start seeing repeating patterns from level to level, and the game starts to feel monotonous." His example is Minecraft: infinite explorable world, but "you'll never find a village with unique houses, a city with inhabitants, a seaport" — a purely algorithmic world can produce endless *terrain*, but not a single hand-placed surprise, because it only ever follows the rules it was given. His own conclusion matches the Focal Points test above from the opposite direction: procedural generation works best as a *foundation* the player or in-game events build meaning on top of — not as the sole source of content, which is exactly the "Invisible, Inc." failure mode Bycer names above, independently arrived at from hands-on implementation rather than genre analysis.

🚩 Generating a large space that only reshuffles a handful of underlying elements — the illusion of freshness with none of the substance. · RNG the player has zero agency over losing to (a run lost turn one to bad luck, no choice involved). · Power-up persistence marketed as if it were unlock-only persistence — it isn't the same promise. · A "meta" build so dominant every run converges on it — the roguelike equivalent of the dominant-strategy lens. · "Infinite replayability" claimed for a game with a finite, small content pool — "long-lasting is not the same as infinite" (p. 85).

---

## APPLIED: Free-to-Play Ethics — Naming the Mechanics

Joshua Bycer, *Game Design Deep Dive: Free-to-Play* (CRC Press, 2022). This section exists so the Compliance seat has exact vocabulary for what it is tiering — not a monetization playbook. Every mechanic named here is named so it can be called out on sight, per the honesty law.

**The line itself, in Bycer's own words:** "Video games are addictive, and that is perfectly fine... The problem is when a game is designed to demand your time, force you to play it, and keep playing beyond what you feel is acceptable. When someone becomes conditioned to keep playing no matter what, and to spend money over their limit because they feel that they need to do it, that's when designers cross a dangerous line." That's the whole boundary in one paragraph.

**Named mechanics, named plainly:**
- **Loot box** — a randomized box whose contents are revealed on opening, sold before the player knows what's inside. "The hook of a loot box is that someone could spend very little and get something of tremendous value, much in the same way that casinos try to convince you that a jackpot is only a pull away." Regulated as gambling in several jurisdictions; drop-rate disclosure is now legally required in some markets.
- **Milling** — a duplicate pull auto-converts into a resource whose cost to reach a top-tier item is deliberately set so high it "can often require hundreds of loot box openings" — "a system that incentivizes mass spending."
- **Gacha** — a single pull against a banner, often with only a 50%+ chance of the advertised rate-up item even at the right rarity tier; limited-time banners plus a pity system (guaranteed item after ~100 pulls) soften the randomness without removing the underlying structure. Ten-pull mechanics are tuned to reward bigger simultaneous spending and implicitly punish small pulls.
- **Hero collector design** — "the culmination of loot box and gacha design": characters as the sellable content. "Hero collectors are always designed to capitalize on the phenomenon known as the 'Fear of Missing Out' (FOMO)... This is one of the shadier practices of gacha games and how they exploit this."
- **Energy/stamina systems** — a resource that runs out, and can be "purposely set up to have the player run out at an inopportune time" to push a paid refill. The canonical bad case: *Harry Potter: Hogwarts Mystery* runs the player out of energy at the exact moment a child character is shown being strangled on-screen — "designers have often relied on psychological manipulation, especially in games aimed at kids."
- **Intentional difficulty spikes** — you can tell one apart from honest difficulty because "the content before and after the spike is nowhere near as difficult" — it exists to push a paid shortcut.
- **VIP systems / beginner's purchase** — a cheap first purchase or subscription tier offered only briefly to new players, explicitly gambling-conditioning: "just like with gambling, it becomes natural [to keep spending]... there needs to be that feeling of investment."
- **Currency layering** — soft/hard currency plus game-specific sub-currencies that make one unlock path effectively require real money; premium currency is often gifted early "to get them conditioned to the advantages of spending it and normalizing it as a part of playing."
- **Monetization-integrated matchmaking** — a real, documented 2017 Activision patent for matching non-spenders against spenders "to show the nonpaying player what they're missing," and biasing paying players' matches so their purchase feels worth it.
- **Guild/social coercion** — top guilds impose spend/time quotas and expel non-paying members, turning peer pressure into a monetization lever independent of the game's own systems.
- **"Cosmetics are harmless" — rejected directly.** "Cosmetics *do* impact the experience and social aspect of these games," with default (free) skins deliberately made "drab or boring compared to the paid ones to incentivize spending," and documented real bullying of kids over default skins.

**Pay-to-Win, defined with a hard test (not the casual overuse of the label):** "A game is considered P2W when there is a noticeable, and often game-affecting, difference between those who spend money vs. those who don't." The test: "If it can take months to get the very same content that someone can spend money to achieve instantly, that is P2W." And the sharper ethical statement: "Putting a metaphorical wall between what nonpaying and paying players can access is an example of unethical game design... it removes any connection to the actual play or skill of the person involved."

**Whales exist — designing only for them doesn't.** "There will always be whales who will buy everything day one, no questions asked; however, building your game to only cater to them is both highly unethical and will ruin any chance of a fanbase developing."

**Dopamine, named as a mechanism, not a metaphor.** Gacha reveal animations and buildup sequences are explicitly engineered around dopamine anticipation: "a constant stimulation of it has been known to lead to health issues such as stress, problems sleeping, and more." Combined with sunk-cost framing — "once someone has spent either a long time or a large amount of money in a game, they have now invested something into this game... it will feel like they have 'lost' their investment" — this is the psychological engine behind every mechanic listed above.

**Criteria:**
- **The P2W test:** does paid content deliver in seconds what unpaid play delivers in months, for the *same* outcome? Yes → P2W, regardless of what the game calls itself.
- **The wall test:** is there a hard content wall separating payers from non-payers, disconnected from skill entirely? That's the sharpest form of unethical design named in this section.
- **The spike test:** is a difficulty spike disproportionate to the content immediately before and after it? That disproportion is the tell.
- **The FOMO test:** is a banner/event/skin deliberately time-boxed to manufacture urgency rather than reflecting a real production constraint?
- **The cosmetics-are-harmless test:** don't accept it at face value — check whether the default option is deliberately made worse to manufacture a social gap.
- **The dopamine/sunk-cost test:** is the reveal sequence engineered for anticipation buildup independent of the odds themselves? That's the same mechanism as a slot machine, named as such by the source.

🚩 Loot boxes / gacha pulls bought with real money, undisclosed odds. · An energy system tuned to run out at a manufactured emotional low point. · A "limited time" banner or skin with no real production reason for the deadline. · A content wall that separates payers from non-payers with zero connection to skill. · Guild/social quotas that punish non-payers through peer pressure instead of game systems. · Matchmaking that uses purchase history to manipulate perceived value. · A default (free) option deliberately made worse to manufacture envy. · Any of the above aimed at a child audience — treat as an aggravating factor, not a neutral fact.

---

## APPLIED: Horror — Tension, Scarcity, and the One Chance

Joshua Bycer, *Game Design Deep Dive: Horror* (CRC Press, 2021). "Horror isn't the same kind of genre as the other entries: there are no predefined mechanics... horror is about a certain kind of philosophy." Any system can be built horror-themed; the genre is intent, not a mechanic list — which is exactly why it needs its own applied section rather than folding into the lenses above.

**The central tension: games empower, horror must resist that.** Videogames are inherently about giving the player control (the whole premise of "the lens of the toy," "the lens of fantasy" above); horror has to fight this instinct on purpose, or it collapses into a power fantasy with monster skins.

**Resource scarcity is the actual differentiator, not monster count.** "Do I have enough ammo to fight? Is it worth it to risk fighting this thing?" Rule of thumb: "the stronger the weapon, the less ammo should be found for it." This is the genre's version of faucet/sink — except the sink is designed to feel dangerously close to zero on purpose.

**Survival horror requires both halves.** First defined by *Alone in the Dark* as adventure gameplay (puzzles, clues, exploration) **and** action gameplay (combat, staying alive) — remove either half and it becomes a different form of horror (pure walking-sim atmosphere, or pure action with horror skin).

**Alpha Antagonist (Bycer's own coined term).** An "ever-present threat that intersects with the rest of the game experience" and can't simply be avoided or killed the way a normal enemy can — Mr. X, Nemesis, the Xenomorph in *Alien: Isolation*. This is a distinct axis from Rogers' ten behavior archetypes and the Soulslike section's difficulty-tier taxonomy above: those describe *what an enemy does* and *how dangerous it is*; this describes an enemy that layers itself across the whole level as a standing condition, not an encounter. Three design questions define one: (1) what happens if it catches the player — damage, or instant restart? (2) can it be disabled or scared off, how early, at what cost? (3) how does it hunt — location-aware or general-area — and are there safe zones excluded from its reach?

The failure mode is fixed triggers: "interactions and appearances are fixed events, and can be easily countered by knowing when they show up" — the same fixed-content problem named in the Roguelike section above, applied to a stalker instead of a boss.

**Tension only moves one way at a time, and it must release.** Tension rises by keeping the player in the dark about what or when; it releases via a scare, a cutscene, reaching safety, or an upgrade. It cannot rise indefinitely without a release valve, or the player just calms down and stops being scared. H.P. Lovecraft, quoted as the genre's first principle: "The oldest and strongest emotion of mankind is fear, and the oldest and strongest kind of fear is fear of the unknown." Once a specific scare device is known, "it is not something that will come back" for that player.

**The One Chance principle — horror's unique design constraint.** "Horror is an unusual genre in that any example of it can only be truly experienced one time with fresh eyes." Practical consequence: "If your game is only 90% horror [by the end], do not consider that as a failure" — degrading fear across a long playthrough is normal, not a bug, and pacing should be planned around spending that one chance well rather than trying to sustain maximum dread for 15 hours straight (even *Alien: Isolation*, widely praised, is criticized for growing repetitive over its ~15-hour length).

**Jump scares are a tool, not the genre.** Craft rules: the scare must relate to the environment/situation, not be a random sting; it must be used sparingly and with randomized timing, or players learn the cue and it stops working; and critically, it should force the player to actually react afterward — "when the Cerberus jumped through the window for the first time, that was not a cutscene, that was an actual attack that the player had to respond to." A scare with no follow-through wastes the moment it bought.

**Stealth-enemy design — six variables to set explicitly for every enemy:** detection method (sight/sound), detection range, how it searches, how fast it responds, what happens on detection, and whether it can be killed at all.

**Puzzle design in horror has an extra failure mode beyond the level-design puzzle craft above:** puzzles that require outside real-world knowledge (chemistry, sheet music, period history) stop progression cold for players who don't have that knowledge — the horror-specific version of "no cat-hair whiskers" (see Level Design above), and it's compounded by placing active enemies in the same room, which removes the focus a puzzle needs.

**Approachability is more urgent here than anywhere else in this canon.** "The first part of your game should be the last part finished" — most players decide whether to keep playing within the first 30 minutes to an hour, and a rough or frustrating UI in that window kills the game's *one chance* regardless of how good everything after it is.

**Criteria:**
- **The both-halves test:** does the design have real adventure *and* real action components? Cutting either turns "survival horror" into a different, less demanding subgenre — that's a legitimate choice, but name it, don't accidentally drift there.
- **The alpha-antagonist test:** for any always-present threat, can you answer all three design questions above (consequence, disable-ability, hunt method)? Missing one usually means the threat feels either cheap or toothless.
- **The tension-release test:** after the last spike, did the player get an actual release (safety, reward, resolution) — or is tension just accumulating with no valve? Unreleased tension reads as fatigue, not dread.
- **The one-chance test:** is the design front-loading its scariest, freshest material, or spreading it evenly and hoping 15 hours of dread holds? It won't — plan degradation on purpose.
- **The jump-scare follow-through test:** after the scare, does the player have to actually do something in response? If not, it's a cosmetic shock, not a scare with teeth.
- **The outside-knowledge test:** does solving this puzzle require real-world knowledge the player might not have? If yes, that's a wall, not a puzzle.

🚩 A jump scare with no follow-through action required — a cosmetic shock, not a scare. · An alpha antagonist whose trigger conditions are fixed and learnable — the same problem as a predictable roguelike boss. · A power curve so generous by the endgame that no enemy, including the final boss, poses real threat — horror quietly became a power fantasy. · "Dead time" (forced waits with zero input) mistaken for tension. · A puzzle that requires knowledge outside the game world (real chemistry, real sheet music). · Copying another horror game's specific scares beat-for-beat — "repetition is the enemy of horror," and the player has already spent their one chance on the original.

---

## The Thread Connecting the Three Applied Topics

**Perceived matters more than actual.** The auction works because price is set by **player perception**, not a designer's table. Loot works because **anticipation matters more than the item**. The bot works because **the announced intent matters more than the algorithm**.

And all three share one common failure — **short-circuiting the loop**: the auction killed loot in D3 because buying became better than looting. **If a single game has an auction, loot, and bots all at once — that's the first risk to check.**

---

## APPLIED: Open-World Survival-Action — the Horde Spine, Traversal-as-Survival, and Scarcity

The genre playbook for a Days Gone-style world (grounded in first-party GDC/postmortem canon; the *fight* is `buro:combat-design`, the systemic-reactivity layer is `references/open-world.md`). Sourced from the 2026-07-22 research pass — see `docs/research/2026-07-22-game-dev-craft-sources.md`.

**The horde as the systemic spine** (Sony Bend, "The Freak-O-System: The Dynamic Open World of Days Gone," GDC 2018 AI Summit — Darren Chisum & Tobias Karlsson). The horde is not a scripted set-piece — it is a **living system**: hundreds of freakers simulated on PS4 without perf collapse, via unit spawning, streaming, and horde behaviour/interaction. Design consequences: the horde has a *place in the world* (it migrates between feeding/nesting sites — see `buro:worldbuilding`), the player *authors* the encounter (when and how to engage is a real tradeoff — the emergent-threat pattern in `references/open-world.md`), and the swarm is *systemic, not random*, so a skilled player can read and outplay it. One well-tuned horde carries more felt content than a dozen scripted fights.

**Traversal-as-survival** (Techland, "Game Design Deep Dive: Dying Light's Natural Movement," Game Developer — Bartosz Kulon & Maciej Binkowski). Three rules that make an open world worth *moving through* under threat:
1. **Real-time geometry scan, auto-selected animation.** The system scans the environment each frame and picks the right parkour move (climb/jump/slide) from the player's parameters — replacing an earlier manual system that needed **50,000+ hand-placed hook points**. Movement is systemic, not authored per-ledge.
2. **Anything that looks climbable IS climbable.** Kill artificial barriers (knee-high fences, boxes that stop you). A world that lies about what it can traverse breaks the trust the whole system runs on.
3. **Evasive traversal is a valid survival strategy, equal to combat.** Mobility ties into survival — "should I fight, or avoid this?" is a real choice. When running is as legitimate as fighting, the world's threats become a navigation puzzle, not just a damage check.

**Scarcity and the vehicle-as-resource** (⚠️ synthesis — flagged). The survival economy is what makes traversal *tense*: fuel, ammo, medical, and crafting materials are scarce, and the vehicle (Days Gone's bike) is itself a **resource to maintain and protect**, not just transport — running dry far from a safe zone is the survival loop biting. *This layer is reasoned design, not citation:* the research did **not** surface verified primary sources for the survival resource economy (Days Gone beyond the horde talk; State of Decay / DayZ / The Long Dark). Treat as synthesis until researched.

**Criteria:**
- **The horde-place test:** does the biggest threat have somewhere to *be* when the player isn't watching (migration/nesting logic), or does it only exist when triggered?
- **The climbable-honesty test:** can the player traverse everything that *looks* traversable? Every lie is a trust leak.
- **The fight-or-flee test:** is avoiding a threat by moving as valid as killing it? If not, traversal is decoration, not survival.

🚩 A "horde" that's a scripted spawn wave with no world-place or systemic behaviour. · Climbable-looking geometry blocked by invisible walls or knee-high fences. · A survival-sized world where running away is never a real option. · A survival economy so generous that scarcity never bites — the tension the genre runs on, defaulted away.

Cross-refs: the *fight* → `buro:combat-design` · systemic reactivity & ambient life → `references/open-world.md` · population density & living ecology → `buro:worldbuilding` · hand-authored points of interest → `buro:narrative` · the return loop → `buro:retention`.

