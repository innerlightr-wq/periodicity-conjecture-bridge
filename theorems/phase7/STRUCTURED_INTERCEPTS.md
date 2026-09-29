# STRUCTURED_INTERCEPTS.md

`scripts/phase7/intercept_adversary.py`, output `data/phase7/intercept_adversary.txt`. Exact `Fraction` arithmetic (BHZ's general formula, `bhz_general_witness.py`) throughout.

## Families tested, 4 slopes (golden `A=1`, silver `A=2`, two non-periodic bounded-type slopes `A=2,3` reused from Phase 6's style)

1. **Intercept `0`** (positive control, `c_k\equiv0`): reproduces known values exactly (`2.618` golden, `3.414` silver — matching Phases 4–6).
2. **Shift-probe / eventually-zero prefixes**: essentially identical to intercept `0`'s asymptotic value (the finite prefix washes out, as expected — matches the theory's own prediction that only the eventual behavior of `(c_k)` matters).
3. **Eventually maximal admissible** (`c_k=a_k` whenever the admissibility rule permits): **consistently the worst (smallest-margin) family across every slope tested** — margins `0.21`–`0.68`, still strictly positive.
4. **Periodic `(c_k)` patterns, alternating sparse/dense, long zero/near-maximal blocks**: all give margins **larger** than intercept `0`'s own, several substantially so (up to `+2.7`).

## Finding

**Every structured family tested, on every slope tested, gives strictly positive margin above `2`.** The "eventually maximal admissible" family is the natural adversarial candidate (confirmed the worst in every test) — consistent with the intuition that maximizing `c_k$ minimizes the `(a_j-c_j)` terms driving both `x'(k)` and `y(k)` upward. No structured family found defeats the bridge.
