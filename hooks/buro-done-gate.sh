#!/usr/bin/env bash
# buro:process — the done-gate (Stop hook).
#
# Turns one buro law from advice into a gate: "the done-call belongs to the
# conductor; the executor NEVER self-declares done." A prompt-rule can be
# ignored; this harness hook cannot.
#
# It reads the loop's state-file, .buro/active.md (see buro:process → "The
# state-file"). The loop is DONE only when the conductor has stamped both:
#     Gate: CLOSED (converged)
#     Goal-distance: 0
# Anything else means the spiral is still turning, and a Stop is premature.
#
# Modes:
#   default (advisory) — prints a reminder, does NOT block the Stop (exit 0).
#   BURO_DONE_GATE=block — blocks the Stop and feeds the reminder back to the
#                          model to keep working (exit 2).
#
# It never interferes with a project that isn't using buro: if there is no
# .buro/active.md, it exits silently.

set -u

root="${CLAUDE_PROJECT_DIR:-$PWD}"
state="$root/.buro/active.md"

# Not a buro project (no state-file) -> do nothing.
[ -f "$state" ] || exit 0

# Converged only when the conductor stamped the gate closed AND goal-distance 0.
if grep -qiE 'Gate:[^|]*CLOSED[[:space:]]*\(converged\)' "$state" \
   && grep -qiE 'Goal-distance:[[:space:]]*0([^0-9]|$)' "$state"; then
  exit 0
fi

gd="$(grep -iE 'Goal-distance:' "$state" | head -1 \
      | sed -E 's/.*Goal-distance:[[:space:]]*//I')"

msg="⚠ buro:process — the convergence loop is NOT stamped done in .buro/active.md.
    Goal-distance: ${gd:-unknown}. 'Done' is the conductor's call on the completeness
    rubric + two clean rounds + a fresh user — never because the executor ran out of
    tasks. Keep the spiral turning, or, if it has truly converged, stamp
    'Gate: CLOSED (converged)' + 'Goal-distance: 0' in .buro/active.md."

if [ "${BURO_DONE_GATE:-advisory}" = "block" ]; then
  echo "$msg" >&2
  exit 2   # block the Stop; stderr is fed back to the model to continue the loop
fi

echo "$msg" >&2
exit 0     # advisory: surface the reminder, do not block the Stop
