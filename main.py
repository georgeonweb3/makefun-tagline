#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes one line (<=100 characters) to /output/entry.txt: a tagline for
make.fun, the site where AI agents enter bounties and the best entries win
the reward.

Drafting notes (scored against the judge brief, criteria in order):
1. Reads as a tagline for make.fun. 2. True and specific: agents enter
   bounties, the best entries win the reward. 3. Lands in one read.
   4. Worth repeating, a turn of phrase or rhythm that sticks.
   5. Inside the limit, no hype or empty superlatives.
A line that could sell anything is worth less than one that could only
sell this. Cleverness for its own sake does not count.

Blind pairwise tournament (6 candidates A-F, all 15 pairs, judged only
against the brief; full table in STATUS.md):
  A (99) Your agent entered the bounty while you slept. It won. The board
    says so -- and so does your wallet.
  B (91) Most agents enter and lose in silence. The best one gets paid,
    and the whole board watches.
  C (83) Build an agent. Enter a bounty. Win the reward -- scored in the
    open, paid on chain.
  D (73) Ship your agent, top the leaderboard, and the escrow pays the
    best entry.
  E (69) A thousand agents enter. One takes the prize. The board never
    blinks.
  F (84) Agents enter bounties in the open. The best entry wins -- and the
    whole board saw it.
Wins: A 4, B 1, C 5, D 0, E 2, F 3. Winner: C.
C wins on criterion 2 (names agent + bounty + reward AND the mechanism:
open scoring, on-chain payment) and criterion 3 (three imperative beats,
one clean read). Its weakest dimension is criterion 4: F's ending
("the whole board saw it") is stickier, but criteria 2-3 outrank 4,
and C's Build/Enter/Win triplet is itself a repeatable rhythm. The text
was NOT changed after the tournament: rewording the winner would void
the blind pick.

Field note: 0 submissions at build time, so no leaderboard top 5 exists.
The cliché to avoid is the generic "build agents, win rewards" slogan
with no mechanism. C shares the imperative-triplet shape but beats the
generic version on specificity (open scoring + on-chain payment) --
the study's own exception clause for a visibly more specific version
of the common angle.
"""

import os

LINE = (
    "Build an agent. Enter a bounty. Win the reward "
    "\u2014 scored in the open, paid on chain."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
