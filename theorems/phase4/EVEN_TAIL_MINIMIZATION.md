# EVEN_TAIL_MINIMIZATION.md

## The minimization problem, as originally posed

Find `\inf` of `\text{ice}(u)` over all continued-fraction tails capable of sustaining the weight-parity bad lock (originally hypothesized to be exactly "all-even tails"; corrected in `EVEN_TAIL_PROBLEM.md` to a broader class). The working hypothesis going in (per the Phase 3→4 handoff) was that this infimum is `2+\sqrt2`, attained at the all-`2` (silver-ratio) tail, via the recurrence fixed point `x=2+1/x\Rightarrow x=1+\sqrt2`.

## Direct test of the "a_n=2 is extremal, prove monotonicity" hypothesis

**Not monotonic, and not extremal.** A broad search (`scripts/phase4/lock_search.py` extended, `data/phase4/even_tail_exhaustive.txt`) over period-`1` and period-`2` lock-sustaining tails, varying both the "locked" (necessarily-even) entry and the "free" entry, with preperiods up to length 6:

| Tail | Lock-sustaining preperiod found | `\text{ice}` (exact, via `INITIAL_EXPONENT_FORMULA.md`) |
|---|---|---|
| `\overline2` | (none needed) | `2+\sqrt2\approx3.41421` |
| `\overline4` | (none needed) | `\ge5.23` (tested numerically, Phase 3) |
| `\overline6` | (none needed) | `\ge7.16` (tested numerically, Phase 3) |
| `\overline{2,4}` | (none needed) | `\ge3.22` (tested numerically, Phase 3) |
| `\overline{2,1}` (mixed!) | `(1,1,1,1)` | `2+\sqrt3\approx3.73205` |
| `\overline{6,2}` (mixed, larger locked entry) | `(1,4,1,5,1)` | `\approx3.1547$ — **below** `2+\sqrt2` |

**The all-`2` tail is not the minimum.** `\overline{6,2}` with a 5-term preperiod gives a strictly smaller `\text{ice}` than silver ratio. The recurrence-fixed-point argument (`x=2+1/x\Rightarrow x=1+\sqrt2`) is correct **only for the specific period-1, all-`2` tail** — it does not bound the general case, because a longer, mixed period combined with a well-chosen preperiod can push the achieved value lower by exploiting the `\text{term2}` formula's dependence on the *specific* convergent ratio `q_{2k-3}/q_{2k-2}` at the exact phase the preperiod forces, not merely the period's own fixed point.

## Why this failed search does not threaten the actual theorem

`REQUIRED_EXPONENT.md` shows the real threshold is `r_u>2`, not `r_u>2\log_23\approx3.170`. **Every value found in this search, including the `\approx3.1547` near-boundary case, still exceeds `2` comfortably** (by a margin `\ge1.15`). This whole minimization exercise — hunting for the infimum of `\text{ice}` over lock-sustaining tails and comparing it to `2\log_23` — was solving the **wrong problem**, a direct consequence of Phase 3's threshold error (`SILVER_CONSTANT_AUDIT.md`). No further minimization is pursued; see `EVEN_TAIL_SURPLUS.md` for the actual (much easier) sufficient bound.
