# FINAL_PROOF_CHAIN.md

Shortest architecture actually used by `QUADRATIC_CS_ROTE_THEOREM.md` — the spectral route (`SPECTRAL_BRIDGE.md`) and the extremal-tail search (`SILVER_EXTREMALITY.md`, `EVEN_TAIL_MINIMIZATION.md`) were explored but are **not** part of the final chain; they are corroboration and a documented dead end, respectively.

```
quadratic slope gamma, bounded partial quotients, max value A
 |
Theorem 10.2 (cited, ADQZ 2001): arbitrarily long initial squares in u
 |
BHZ Corollary 3.5, omega(-gamma) case (cited, verified): term2(k) = 1+a_{2k-1}+q_{2k-3}/q_{2k-2}
 |
term2(k) > 2 + 1/(A+1), for EVERY k in the periodic regime (elementary CF bound, this phase)
 |
Rote transfer theorem (exact, Phase 2): depth preserved exactly (L+1); root -> V (even weight) or R=V-Vbar (odd weight)
 |
KEY FACT (this phase): R = V-Vbar has density EXACTLY 1/2, unconditionally
 |
required threshold collapses: tau=1 needs r_u>log2(3)<2; tau=1/2 needs r_u>2*max(1,0.5*log2(3))=2
 |          <- both branches need only r_u > 2, which the bound above supplies with margin 1/(A+1)
O(log ell) discrepancy of V and R (Phase 2 three-distance-theorem reduction, extends unchanged)
 |
S_k >= ell_k/(A+1) - O(log ell_k)  ->  +infinity
 |
abstract irrationality criterion (Phase 2, every subtlety resolved)
 |
Phi(v) not in Q
```

**What was dropped from the exploratory machinery, and why**: the weight-parity automaton (Phase 3) and its "all-even tail" classification are **not** in this chain — `TRANSFER_EFFICIENCY.md` shows the theorem needs no parity classification at all, only the observation that *whichever* case applies, the resulting threshold is `\le2`. The silver-ratio critical exponent `2+\sqrt2` is **not** in this chain — it was a special-case numeric fact mistaken for a general bound (`SILVER_CONSTANT_AUDIT.md`). Both remain in the historical record (`theorems/phase3/`, this phase's own audit files) but are not load-bearing for the final result.
