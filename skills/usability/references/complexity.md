# Usable ≠ amputated — taming complexity without cutting it

This is the heart of the skill. When a product genuinely needs a lot — many
functions, much data, several roles, all at once — the lazy answer is to "simplify"
by removing features, hiding things, or dumbing down. **That fails the task:** the
user came *for* that power. The craft is to make "a lot, all together" feel
manageable and understandable **while keeping it whole**.

> **You never destroy the complexity. You decide who carries it and where it lives
> (Tesler).** The system carries as much as possible; what's left lives where the
> user expects it, surfaced exactly when needed.

So the structuring question is not "what do I cut?" but **"what structure makes all
of this both complete and comprehensible — for *this* user, at *this* frequency, in
*this* context?"** That is a judgement the skill makes and must justify. Below are
the techniques and the decision rules.

---

## The techniques (the toolbox)

Each keeps capability intact; they differ in *where* the complexity goes.

1. **Smart defaults & automation (Tesler).** The system makes the correct choice;
   the user overrides only if needed. Removes a decision *without removing the
   option*. First resort — always ask "can the system just do this?"

2. **Progressive disclosure.** Show the common 80% up front; put the advanced 20%
   behind a clearly-labelled, obviously-reachable door ("Advanced", "More options",
   a disclosure triangle). The power is *there*, one obvious step away — not gone.
   *Risk:* hiding an **essential** or frequent control to look clean. Only the rare
   and the advanced get hidden.

3. **Separate pages / screens / steps.** Split when the work is *sequential* (a
   wizard for a genuinely multi-stage task), when contexts are *distinct* (compose vs
   browse), or when one surface would force constant mode-switching. Each page has one
   job and a clear next/back. *Risk:* chopping one continuous task into needless
   pages, adding navigation tax — don't split what the user does in one thought.

4. **Modes / layers / roles.** Offer a simple view and an expert view of the *same*
   product (a "basic/advanced" toggle, a beginner vs pro mode, role-based surfaces).
   Everyone gets the depth they need; nobody is forced through the other's. *Risk:*
   modes you're in but can't see or leave — make the current mode visible and the
   switch one obvious move.

5. **Search / command palette.** For high-dimensionality (hundreds of commands,
   objects, settings), a good search or command palette beats deep menus: the user
   *recalls intent*, types it, and jumps straight there — full breadth, near-zero
   depth. Pair with browsable structure for discovery.

6. **Grouping & chunking (Miller).** Don't reduce the count — organize it. Cluster by
   the user's task, label the clusters, use spatial structure so the eye narrows fast.
   Twenty controls in five labelled groups read easier than eight controls in a heap.

7. **Spatial density done right (Tufte / the expert console).** Sometimes the *most*
   usable answer is to show it all on one dense surface — a trading terminal, a mixer,
   a dashboard. The expert wants everything visible and stable (muscle memory). Here
   you reduce *noise*, not *data*: kill borders, redundant labels, decoration; keep
   every control. (See `buro`'s dense-data and expert-console guidance.)

8. **Progressive engagement / staged onboarding.** Reveal capability as the user
   grows into the product — defaults and a narrow path on day one, more surface as
   they return. The depth was always there; you metered the *exposure*, not the power.

---

## The decision framework (which technique, when)

Choose by the user's reality, not by reflex. Ask, in order:

1. **Can the system carry it?** → default / automation / inference. Always first.
2. **How frequent is this control/path for this user?**
   - Frequent → keep it **up front, big, near** (Fitts); never hide it.
   - Rare/advanced → progressive disclosure or a mode.
3. **How expert is the user, and is there a split?**
   - One audience, mixed depth → progressive disclosure within one surface.
   - Two clear audiences (novice vs pro) → modes/layers, or even separate surfaces.
4. **Is the task one continuous thought or genuinely staged?**
   - One thought → one surface (splitting adds nav tax).
   - Staged/sequential → steps/pages with clear progress.
5. **How high is the dimensionality?**
   - Dozens+ of commands/objects → add search / command palette on top of structure.
6. **Does the expert need everything at once (muscle memory, monitoring)?**
   - Yes → one dense surface, noise removed, nothing hidden.
7. **Context & device?** A watch or an ATM forces aggressive staging and defaults; a
   pro desktop tool can hold far more on one surface. Decide per device
   (`devices-and-ecosystem.md`).

Then **state the choice and the reason** in the verdict: "one dense surface, because
this is a monitoring task for an expert who needs all values at a glance and stable
positions" — not just "we put it all on one screen."

---

## Red flags (getting it wrong in both directions)

**Over-cutting (amputation):**
- A feature removed because it was "too advanced", when its users needed it.
- Defaults with no override — the system decided and locked the user out.
- A flow that only handles the happy 80% and abandons the 20% who need the rest.

**Under-structuring (overwhelm):**
- Everything on one screen with no grouping, defaults, or hierarchy — "complete" but
  unreadable.
- A 40-field form where 35 could be defaulted or derived.
- Deep menu trees where search would jump straight to intent.

**Mis-hiding:**
- An **essential/frequent** control behind progressive disclosure (clean-looking,
  unusable).
- A mode with no visible indicator or exit.
- Splitting one continuous task into a multi-page wizard that adds clicks for nothing.

The target is the narrow band between these: **complete, and comprehensible.** If you
can't have both with the current structure, you've picked the wrong structure — not
too much capability.

---

## Worked micro-examples

**Pro photo editor — 200 adjustments.**
Wrong: hide most adjustments to "keep it simple" → pros leave. Right: a stable
panel of grouped adjustments (chunking), smart auto-defaults per photo (Tesler), an
"Auto" that does 90% then lets you refine, and a command/search to jump to any tool.
Nothing cut; depth on tap.

**Tax-filing app — huge, scary, mandatory.**
Wrong: one giant form. Right: staged steps with visible progress (goal-gradient),
each step prefilled from prior data and documents (Tesler, recognition over recall),
advanced/edge cases behind "My situation is more complex" (progressive disclosure),
every value reversible. Full power; staged so it never overwhelms.

**Smart-home app — dozens of devices, scenes, automations.**
Wrong: bury automations because they're "advanced". Right: a simple home view for
the daily 3 actions (Fitts — big, near), all devices one tap away, automations in a
clearly-labelled section, and search for "turn off everything downstairs". Complete,
not amputated; layered by frequency.
