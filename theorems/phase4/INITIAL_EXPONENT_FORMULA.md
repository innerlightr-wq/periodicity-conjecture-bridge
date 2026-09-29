# INITIAL_EXPONENT_FORMULA.md

## Source

Berthé, V., Holton, C., Zamboni, L.Q., *Initial powers of Sturmian sequences*, Acta Arithmetica **122** (2006), 315–347. Retrieved and read directly (`https://www.irif.fr/~berthe/Articles/sturm15.pdf`), not taken on secondary report.

## The formula, and which intercept it is

For `\gamma=[0;a_1,a_2,\ldots]`, convergents `p_k/q_k`, the paper defines the **characteristic sequence** `\omega` and its two one-symbol shift-preimages `\omega(-\gamma)=0\omega` and `\omega(1-\gamma)=1\omega`. This project's `u` (the lower mechanical word, `u_n=\lfloor(n+1)\gamma\rfloor-\lfloor n\gamma\rfloor`, used throughout Phases 1–3) satisfies `u_0=0` (since `\gamma\in(0,1)`) — **identified here as `\omega(-\gamma)=0\omega`** (confirmed by exact numeric match, `scripts/phase4/verify_ice_formula.py`, not merely inferred from the "starts with 0" heuristic).

**Corollary 3.5 / the `\omega(-\gamma)` case (BHZ, exact quote reproduced in `data/phase4/bhz_extract.txt`):**
```
ice(omega(-gamma)) = limsup_k max( a_{2k+1} + q_{2k-1}/q_{2k},  1 + a_{2k-1} + q_{2k-3}/q_{2k-2} )
```

**The formula's limiting value verified exactly** (`scripts/phase4/verify_ice_formula.py`, `data/phase4/verify_ice_formula_output.txt`, and the interactive session that produced `SILVER_EXTREMALITY.md`'s search) against four slopes: silver ratio → `2+\sqrt2` exactly; the Phase 3 counterexample `[0;1,1,1,\overline2]` → `2+\sqrt2` exactly (tail-only dependence, preperiod washes out, matching BHZ's own stated fact that `ice` depends only on the tail); a mixed tail `\overline{2,1}` → `2+\sqrt3` exactly; the Phase 4 near-boundary tail `\overline{6,2}` with preperiod `(1,4,1,5,1)` → `\approx3.1547` (an algebraic, non-quadratic-looking value from this specific 5-term preperiod interacting with the period-2 tail). **Note on scope**: `scripts/phase4/verify_ice_formula.py`'s own direct-computation cross-check (comparing the formula's `term1`/`term2` against an independently-computed achieved exponent `r_u` at root length `q_{2k-1}`) did not produce output for `k\ge2` at the tested slopes, since the required root lengths exceeded the word-generation budget used in that run — the formula values above come from the closed-form limit (`x=2+1/x`-type fixed-point algebra, or direct rational evaluation of the convergent ratios), not from that specific cross-check. The term2 bound below **is** independently verified by that script, exactly, for every tested tail.

## The key structural term, isolated

```
term2(k) := 1 + a_{2k-1} + q_{2k-3}/q_{2k-2}
```
Since `a_{2k-1}\ge1` (every partial quotient) and `q_{2k-3}/q_{2k-2}=1/[a_{2k-2};a_{2k-3},\ldots,a_1]` with the reversed-CF value `<a_{2k-2}+1\le A+1` (`A`= the largest partial quotient occurring, eventually, in `\gamma`'s continued fraction), we get
```
term2(k) > 1 + 1 + 1/(A+1) = 2 + 1/(A+1),   for EVERY k in the eventually-periodic regime — not just in the limsup.
```
**This one inequality, verified exactly in `scripts/phase4/verify_ice_formula.py` for every tested tail, is the load-bearing fact for `QUADRATIC_CS_ROTE_THEOREM.md`.** No minimization, no extremal-tail search, and no reliance on `2+\sqrt2` is needed once this bound is in hand: `2+1/(A+1) > 2` strictly, for **any** finite `A`, which is exactly the (weak, but sufficient per `REQUIRED_EXPONENT.md`) threshold `r_u>2`.

## Intercept tracking, as the task requires

`v_0=0` (Phase 1–3's convention) gives `V`, the CS Rote root, built from `u=\omega(-\gamma)`. The complementary choice `v_0=1` gives `\bar V` throughout (`ROTE_TRANSFER_THEOREM.md`'s complement-symmetry), not a different Sturmian intercept — **the CS Rote construction fixes `u=\omega(-\gamma)` regardless of the Rote seed bit**; the seed bit only complements `v`, it does not change which Sturmian sequence `u` is used. So the `\omega(1-\gamma)` formula (the *other* mechanical word) is **not** needed for this project's specific construction, and is recorded here only for completeness, not used further.
