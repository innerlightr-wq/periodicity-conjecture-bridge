**Classification: IRRELEVANT AFTER SHARPER ANALYSIS** (and, separately, the silver-ratio-extremality reading of it is **FALSE**, see `SILVER_EXTREMALITY.md`)

# SILVER_CONSTANT_AUDIT.md

## Where `2+\sqrt2` actually came from

Answering the six audit questions directly:

1. **Is it the initial critical exponent of the silver-ratio Sturmian word?** Yes — confirmed exactly via the Berthé–Holton–Zamboni closed form (`INITIAL_EXPONENT_FORMULA.md`): for `\gamma=[0;\overline2]`, `\text{ice}(\omega(-\gamma))=1+x` where `x=[2;2,2,\ldots]` solves `x=2+1/x`, giving `x=1+\sqrt2`, `\text{ice}=2+\sqrt2`. Exact, not approximate.
2. **Is it the minimum of a family?** **No** — `EVEN_TAIL_MINIMIZATION.md`/`SILVER_EXTREMALITY.md` find a tail (`\overline{6,2}` with a specific preperiod) with `\text{ice}\approx3.1547<2+\sqrt2\approx3.4142`. Silver ratio is **not** extremal among lock-sustaining tails.
3. **Is it associated specifically with tail `\overline2`?** Yes, exactly — it is the closed-form value for that one specific periodic tail, no more general than that.
4. **Is it a consequence of a recurrence eigenvalue?** Yes, incidentally — `x=1+\sqrt2` is the dominant eigenvalue-type fixed point of the period-1 all-`2` continued-fraction recurrence (`SPECTRAL_BRIDGE.md`), but this is specific to that one tail, not a general spectral bound.
5. **Is it merely a numerical observation from four tested tails?** **Yes — this is the operative answer.** Phase 3 tested exactly four tails (`\overline2,\overline4,\overline6,\overline{2,4}`), all `\ge2+\sqrt2`, and the smallest was promoted to a working hypothesis ("all-even tails have `\text{ice}\ge2+\sqrt2`") without a proof or a broad enough search. This phase's stress test (section 12, `COUNTEREXAMPLE_AUDIT.md`) found a counterexample to that specific numeric threshold within a modest search.
6. **Does the literature already contain the exact formula?** Yes — Berthé–Holton–Zamboni (Acta Arithmetica 122, 2006), Corollary 3.5 and Theorem 1.2, give the general closed form; Damanik–Lenz (2003) give the related critical-exponent (not initial-critical-exponent) formula. Neither paper singles out `2+\sqrt2` as any kind of universal lower bound for even/lock-sustaining tails — that specific claim was this project's own (Phase 3's) unproven extrapolation.

## Why it doesn't matter after `REQUIRED_EXPONENT.md`

The real required threshold, derived in this phase, is `r_u>2` (not `r_u>2\log_23\approx3.170`) — because the odd-weight route's transferred root `R=V\bar V` has **automatically** density `1/2`, dropping the threshold from the worst-case `\log_23\approx1.585` down to `\max(1,\tfrac12\log_23)=1`. Since `2+\sqrt2\approx3.414\gg2`, silver ratio was never remotely close to the boundary that actually matters — it was solving the wrong (too-hard) problem. **`2+\sqrt2` is a correct, exact, citable fact about one specific slope, but it is not the threshold this project needs, and promoting it to a general lower bound was an error this phase corrects.**
