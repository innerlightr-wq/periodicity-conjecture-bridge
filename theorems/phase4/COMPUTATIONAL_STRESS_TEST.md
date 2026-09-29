# COMPUTATIONAL_STRESS_TEST.md

`scripts/phase4/even_tail_exhaustive.py`, output `data/phase4/even_tail_exhaustive.txt`. Exact `Fraction`/big-integer arithmetic decides every reported pass/fail (`bridge_surplus_exact`, the same exact-integer-comparison routine used throughout Phases 1–3); no floating point enters any decision, only display.

## Configurations tested

7 all-even tails (period 1: `\overline2,\overline4,\overline6`; period 2: `\overline{2,4},\overline{2,6},\overline{4,6}`; period 3: `\overline{2,2,4}`) and 4 mixed lock-sustaining tails with explicit locking preperiods found by search (`\overline{2,1}`, `\overline{6,2}`, `\overline{4,3}`, `\overline{2,3}`).

## Results

| Tail | Preperiod | `A` | `r_u` (achieved) | bound `2+1/(A+1)` | exceeds? | exact `S` | `S>0`? |
|---|---|---|---|---|---|---|---|
| `\overline2` | — | 2 | 3.4142 | 2.3333 | Yes | 80755 | Yes |
| `\overline4` | — | 4 | 5.0000 | 2.2000 | Yes | 1203 | Yes |
| `\overline6` | — | 6 | 5.0000 | 2.1429 | Yes | 5598 | Yes |
| `\overline{2,4}` | — | 4 | 3.2247 | 2.2000 | Yes | 192034 | Yes |
| `\overline{2,6}` | — | 6 | 3.1547 | 2.1429 | Yes | 75634 | Yes |
| `\overline{4,6}` | — | 6 | 5.0000 | 2.1429 | Yes | 2578 | Yes |
| `\overline{2,2,4}` | — | 4 | 5.0000 | 2.2000 | Yes | 11518 | Yes |
| `\overline{2,1}` (mixed) | `(1,1,1,1)` | 2 | 3.7310 | 2.3333 | Yes | 1600 | Yes |
| `\overline{6,2}` (mixed) | `(1,1,1)` | 6 | 3.1547 | 2.1429 | Yes | 62237 | Yes |
| `\overline{4,3}` (mixed) | `(1,1,1,1)` | 4 | 5.0000 | 2.2000 | Yes | 13 | Yes |
| `\overline{2,3}` (mixed) | `(1,1,1,1)` | 2 | 3.4000 | 2.3333 | Yes | 3 | Yes |

**11/11 configurations: `r_u` exceeds the theoretical bound, and the actual exact surplus `S` is positive.** Smallest observed `r_u-2` margin: `1.15467` (`\overline{2,3}` — still comfortably positive, an order of magnitude above `0`). No counterexample to `r_u>2` was found in this pass (in contrast to the earlier `r_u>2+\sqrt2`-style search, which did find a near-miss — `SILVER_EXTREMALITY.md` — precisely because that was testing the wrong, unnecessarily strong threshold).

## What was not exhaustive

Period lengths beyond `3`, entries beyond `6`, and preperiod lengths beyond `5` were not searched — per `INITIAL_EXPONENT_FORMULA.md`, this is not needed: the bound `r_u>2+1/(A+1)` is proved **unconditionally** for any finite `A`, not merely observed in this sample. This stress test corroborates the proof; it is not the proof's basis.
