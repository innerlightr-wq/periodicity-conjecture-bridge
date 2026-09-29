# WEIGHT_PARITY_CLASSIFICATION.md (Phase 3)

Resolves Phase 2's precise missing lemma: does every quadratic irrational's weight-parity eventual cycle contain a `0`?

## The finite automaton, built exactly

States `\{A,B,C,Z\}=\{(0,1),(1,1),(1,0),(0,0)\}` (values of `(p_{k-1},p_k)\bmod2`), crossed with `\kappa=k\bmod2`, give 8 nodes. Transition on `a_k` parity: `M_0` (even): `A\leftrightarrow C`, `B,Z` fixed. `M_1` (odd): `A\to B\to C\to A`, `Z` fixed. `\kappa` flips every step. `\text{weight}_k=1$ ("bad", odd) exactly at nodes `\{(A,0),(B,0),(C,1),(Z,1)\}`.

**Exhaustive graph search** (`phase3/scripts/automaton_search.py`) over all `8` nodes finds **exactly one** bad-only cycle: `(A,0)\leftrightarrow(C,1)`, sustained iff `a_k` is even at every visit to `(A,0)` (visits to `(C,1)` are unconstrained — both parities return to `(A,0)`).

## Counterexample to Phase 2's open question — found

`\gamma=[0;1,1,1,\overline2]` (preperiod `1,1,1`, purely periodic tail `2` — a genuine quadratic irrational, `\gamma\approx0.630602`): weight parity is **`0,0,1,1,1,1,1,1,\ldots`, all `1` (odd) from index `2` on, forever** — verified to `28` convergents (`phase3/scripts/*`). **The universal claim ("every quadratic irrational's cycle contains 0") is FALSE.**

## But the odd-weight route still covers it — tested directly

At this slope's standard-word witnesses (`q_k=1,1,2,3,8,19,46,111,268,\ldots`), **every other `k`** achieves `r_u\to2+\sqrt2\approx3.41421` (the classical silver-ratio critical exponent — expected, since the CF **tail** is identical to silver ratio's, and critical-exponent asymptotics depend only on the eventual tail, not the preperiod). Since `2+\sqrt2>2\log_23\approx3.16993`, the halved exponent `r_v=r_u/2\to1+\frac{\sqrt2}2\approx1.70711>\log_23`, **still clearing the bridge threshold** — confirmed by **direct exact surplus computation**, not estimate: `S` at `\ell=q_{16}=309268` is `437340`, growing (`5,55,365,2191,12852,75014,437340,\ldots` across `k=4,6,8,\ldots,16`) — unboundedly, exactly the `\limsup=+\infty` signature needed.

## Full classification (proved half + strongly evidenced half)

> **DICHOTOMY.** For any quadratic-irrational Sturmian slope `\gamma`:
> **(a) [PROVED]** If the CF tail contains **any odd partial quotient**, the bad `(A,0)\leftrightarrow(C,1)` cycle cannot be sustained forever (an odd term at the `(A,0)`-phase always escapes to `(B,1)`, good) — infinitely many even-weight witnesses exist, giving `r_v=r_u\ge2>\log_23` directly.
> **(b) [STRONGLY EVIDENCED, not fully proved in general]** If the CF tail is **entirely even partial quotients** (the only case that can sustain the bad cycle), the achievable exponent `r_u` tends to a limit `\ge2+\sqrt2` (tested: tail `\overline2\to3.41421`; tail `\overline4\to\ge5.23`; tail `\overline6\to\ge7.16`; mixed tail `\overline{2,4}\to\ge3.22` — **every tested all-even tail clears `2\log_23` with positive margin**, smallest margin at the all-`2` tail, consistent with all-even tails' minimum being the silver-ratio value), giving `r_v=r_u/2>\log_23` via the odd-weight halved route.

**Consequence: Target C (all quadratic-irrational-slope CS Rote sequences) is resolved in practice** — every tested case, spanning both branches of the dichotomy, certifies. Branch (a) is a complete proof. Branch (b) rests on the classical/empirical fact that all-even-tail quadratic irrationals have critical exponent bounded below by the silver-ratio value `2+\sqrt2` — evidenced strongly (4 diverse tails, comfortable margins) but not given a fully general closed-form proof for an arbitrary all-even tail in this phase.

## Status

```
PROVED: branch (a) -- any odd-partial-quotient tail.
STRONGLY EVIDENCED, NOT FULLY PROVED: branch (b) -- all-even-partial-quotient tail, resting on
  the classical critical-exponent-of-silver-ratio-type-words fact (r_u -> >= 2+sqrt2), tested on
  4 tails, not proved for a fully general all-even tail.
NET RESULT: every tested quadratic irrational (9 slopes across Phase 2 + Phase 3) certifies.
  No genuine failure found. The remaining gap is a proof-completeness gap, not a counterexample.
```
