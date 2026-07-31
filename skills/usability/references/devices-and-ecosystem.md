# Devices & ecosystem — one method, many embodiments

A product may live on one device or many, and the "many" may be a loose set or a
tight **ecosystem** acting as one product. The usability method is the same
everywhere; the *embodiment* changes with the device's input, distance, posture,
attention, and environment. The cardinal sin is **shrinking** one device's design
onto another instead of **re-authoring** for it.

Two jobs in this file:
1. **Embody per device** — fit the device's nature.
2. **Design the ecosystem** — when several devices are one product, design the
   continuity between them.

> Decide per device which **job** belongs there (the watch's job is a glance, not the
> spreadsheet) and let the system carry state across them (Tesler) so the user never
> re-does work when they switch.

---

## What changes per device (the variables)

For any device, characterize it before designing:
- **Input** — touch, precise pointer, keyboard, voice, remote/d-pad, rotary
  crown/dial, gaze/gesture, physical buttons.
- **Distance & target size** — 10 cm (watch), 30 cm (phone), 50 cm (laptop), 3 m (TV).
  Closer/coarser input → bigger targets.
- **Attention & session length** — a glance (watch), a focused session (desktop), a
  shared lean-back (TV), an interrupted one (car, kiosk queue).
- **Posture & hands** — one thumb, two hands, eyes-off (voice/car), gloved, standing
  in public.
- **Environment** — glare, noise, motion, privacy (an ATM is public; a phone is
  personal), connectivity.
- **Stakes & dwell** — a kiosk/ATM user won't read; a pro at a desktop will learn.

---

## Per-device embodiment

**Watch (small, glance, crown/touch/voice).** One primary thing per screen; the job
is a *glance or a single action*, never data entry. Huge targets, terse text,
complications/widgets for the at-a-glance value, voice for input. Hand off anything
deep to the phone. Don't port the phone UI — pick the one job that belongs on the
wrist.

**Phone (thumb, on the move, interrupted).** Mobile-first thinking (Wroblewski):
primary actions in the thumb zone (Fitts), forms minimized and forgiving, defaults
from sensors/context (location, contacts, camera). Assume interruption — preserve
state so a return resumes exactly. One-handed where possible.

**Tablet (touch, larger, lean-back or productive).** Not a big phone nor a small
desktop — use the canvas for side-by-side context (list + detail), direct
manipulation, and optional pointer/keyboard. Decide whether this instance is
lean-back consumption or real production and embody accordingly.

**Web / desktop (precise pointer + keyboard, focused, large).** Density is welcome
for experts (see `complexity.md`): keyboard shortcuts, command palette, multi-pane,
stable positions for muscle memory. This is where the most capability can sit on one
surface — reduce *noise*, not power.

**TV / 10-foot (remote/d-pad, 3 m, lean-back, shared).** Spatial focus navigation
with a clearly visible focus state; few, large, well-spaced targets; minimal text
entry (offer phone/voice instead); content-first, chrome minimal. Designed for
across-the-room legibility and a shared audience.

**Voice / conversational (eyes-off, hands-off, no screen).** No recall of menus —
the system must offer and confirm. Short turns, confirm destructive actions, always
let the user bail or hand off to a screen for anything complex. Design for
mishearing: graceful re-prompts, not dead ends.

**Car / automotive (eyes mostly off, safety-critical, interrupted).** Minimize
glances; voice-first; huge, few targets; never require precise aim while moving;
resumable after interruptions; comply with driver-distraction limits. The job is the
*minimum* to keep the driver safe and informed.

**Kiosk / ATM (public, standing, first-time, low dwell, no manual).** Maximum
forgiveness and guidance; very large targets; no jargon; assume the user never read
anything and won't. Privacy-aware (shoulder-surfing, masked entry), timeout with
graceful reset for the next person, accessible height/contrast/audio. One clear path,
strong "start over".

**Embedded / appliance (physical controls, constrained display, single-purpose).**
Map controls to real-world referents; make state physically obvious; forgiving of
the one or two things that can go wrong; assume no docs. Constrain inputs so wrong
states can't be reached (poka-yoke).

---

## The ecosystem — several devices as one product

When devices form one product, usability includes the *seams between them*.

- **Same mental model & language across devices (Birman, Apple consistency).** The
  same thing is named the same, behaves the same, and sits in a recognizable place
  everywhere. Switching devices should feel like the same product in a new shape, not
  a new product.
- **State follows the user (continuity / handoff).** What they started on the phone
  continues on the web at the same point; a cart, a draft, a position, a setting syncs
  without re-entry (Tesler — the system carries it). Model this on Apple
  Handoff/Continuity: pick up exactly where you left off.
- **Right job on the right device.** Don't replicate the whole product on each device
  — assign each the job it does best (watch = glance/notify; phone = capture/act on
  the go; tablet/desktop = create/manage; TV = consume; kiosk = a public subset) and
  let them complement, not duplicate.
- **Honest cross-device feedback.** An action on one device is reflected on the others
  promptly; the user is never left wondering whether it "took". Show sync state
  honestly when it lags.
- **Graceful degradation & escalation.** When a device can't do something, it offers
  the right hand-off ("continue on your phone", "open on web") rather than a dead end.

**Ecosystem failures the consilium hunts:** phone and web that feel like different
products; settings that don't sync; a watch that makes you do phone-sized work; a
kiosk that can't hand a half-finished task to your phone; an action on one device
that silently fails to reflect on another; the same word meaning different things on
different devices.
