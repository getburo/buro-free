# Priority filter — scoring examples

Product-agnostic calibration examples. The filter works for **any** product; below are three gaps
across different product types, scored the same way. Use them to calibrate new scores.

Dimensions: **Pain · North-star fit · Timing · Worth it · Execution** (1–10 each, total /50).

---

## Example (DO) — "Show the goal before the user commits" (a SaaS onboarding)

> The user lands on a signup wall with no idea what they get on the other side.

| Dimension | Score | Argument |
|-----------|-------|----------|
| Pain | 9 | The user doesn't know why to sign up — high risk they bounce. |
| North-star fit | 8 | The north-star is activated users; a blind wall kills activation. |
| Timing | 10 | It's the first screen — without it onboarding doesn't start. |
| Worth it | 8 | Delete it and first contact breaks; it carries its weight. |
| Execution | 10 | One value line + a preview above the wall. An afternoon. |
| **Total** | **45/50** | **→ DO** — a blocker on the primary funnel |

---

## Example (SKIP) — "Real-time multiplayer" (a solo mobile game, pre-launch)

> Add live co-op so two players can play together.

| Dimension | Score | Argument |
|-----------|-------|----------|
| Pain | 4 | No one asked; it doesn't block the single-player goal. |
| North-star fit | 3 | The north-star is a fun 30-second loop; netcode is off-mission now. |
| Timing | 2 | We don't have one retained player yet — too early for two. |
| Worth it | 2 | Delete it — nothing breaks; the game is complete without it. |
| Execution | 2 | Netcode, sync, servers — months. |
| **Total** | **13/50** | **→ SKIP** — good idea, wrong time |

---

## Example (WAIT) — "Bring your own content" (a content / learning product)

> Let the user import their own material instead of only the built-in catalog.

| Dimension | Score | Argument |
|-----------|-------|----------|
| Pain | 8 | "Anything you want" is the promise; the catalog caps it. |
| North-star fit | 9 | It bends the product to the user's actual goal — squarely on-mission. |
| Timing | 6 | Not day one, but the small catalog means users hit the wall soon. |
| Worth it | 9 | Delete it and "anything" becomes "from our list" — a broken promise. |
| Execution | 5 | Import + processing is non-trivial but the APIs exist. A medium cycle. |
| **Total** | **37/50** | **→ WAIT** — high priority, not day one |

---

## Calibrating "Pain"

| Score | What it means |
|-------|---------------|
| 9–10 | The user cannot reach their goal without this |
| 7–8 | The user reaches the goal, but with difficulty or a workaround |
| 5–6 | Inconvenient, but tolerable |
| 3–4 | They notice, but it doesn't get in the way |
| 1–2 | Nice to have, rarely think about it |

## Calibrating "North-star fit"

Score against **the product's own** north-star — whatever success actually is for that product —
never a borrowed one.

| Score | What it means |
|-------|---------------|
| 9–10 | Directly moves the product's north-star |
| 7–8 | Supports it, doesn't get in the way |
| 5–6 | Neutral |
| 3–4 | Drifts off-mission |
| 1–2 | Contradicts the north-star |
