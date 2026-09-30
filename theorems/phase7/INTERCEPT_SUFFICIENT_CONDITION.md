> **SUPERSEDED BY PHASE 8 — see [`theorems/phase7/PHASE7_CORRECTIONS.md`](PHASE7_CORRECTIONS.md)
> item C1.** The condition classified `CONJECTURAL` below is a **published theorem**: BHZ 2006
> Propositions 5.1 and 5.2. The computational findings in this file are correct and confirmed.
> Retained verbatim as the historical record.

**CONJECTURAL**

# INTERCEPT_SUFFICIENT_CONDITION.md

## Candidate condition

> For any admissible Ostrowski digit sequence `(c_k)` of a bounded-partial-quotient slope (`\sup a_n=A<\infty`), `\limsup_k\max(x'(k),y(k))>2` strictly, with a margin depending only on `A` (not on `(c_k)`'s specific pattern beyond admissibility).

## Evidence for it

- **36/36 tested configurations** (`STRUCTURED_INTERCEPTS.md`, 9 structured families × 4 slopes) give strictly positive margin, no exceptions.
- The empirically worst family found — `c_k` alternating between maximal (`c_k=a_k`) and near-maximal (`c_k=a_k-1`), the only pattern respecting admissibility while keeping `(a_j-c_j)` small at nearly every step — still gives margin `>0` at every tested `A\in\{2,3,4,\ldots,32\}`, decaying empirically like `\sim1/A^2`, never crossing `0` (`data/phase7/intercept_adversary.txt`, and the earlier `A`-scan reproduced in `theorems/phase7/DRIFT_VS_DIGITS.md`).
- A structurally *worse*-looking alternative (`c_k$ alternating maximal/`0`, rather than maximal/near-maximal) was tested and found to give a substantially **larger**, not smaller, margin — so the near-maximal family is a genuine local extremum among the patterns tried, not an artifact of an arbitrary choice.

## Why this is not proved

A general proof would require redoing the `\text{term2}(k)>2+1/(A+1)` style algebraic argument (`theorems/phase4/INITIAL_EXPONENT_FORMULA.md`) for BHZ's **general** `x'(k),y(k)` formula under an arbitrary admissible `(c_k)`, not the specific `c_k\equiv0` (characteristic) or the specific `\omega(-\alpha)` pattern those bounds were derived for. The general formula's sums `\sum_{j\le k}(a_j-c_j)q_{j-1}` do not obviously reduce to a two-term expression the way the `\omega(-\alpha)` case did (that reduction used a *specific*, simple `(c_k)` structure, per BHZ's own §4.1 derivation) — for a **general** `(c_k)`, no such reduction was found or attempted to completion in this phase.

## Status

```
CONJECTURAL. Strong, broad computational evidence (36/36 configurations, including the
identified worst-case family, across a range of A). No general algebraic proof attempted
to completion. This is the exact remaining lemma for a full all-intercepts theorem
(see theorems/phase7/INTERCEPT_OBSTRUCTION_MAP.md, item 13).
```
