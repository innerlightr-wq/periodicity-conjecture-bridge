# ROTE_DIRECT_HEIGHT.md

## Not needed — discrepancy control succeeded

`ROTE_ROOT_DISCREPANCY.md` proves `D(V_n)=O(\log\ell_n)` directly, for bounded-partial-quotient slopes — the strongest row of `DISCREPANCY_HEIGHT_PROOF.md`'s ladder, well beyond merely `o(\ell_n)`. The discrepancy route did not fail, so the fallback direct-height-bound approach this section was reserved for is **not required** for Target B/C.

## Brief sketch of why it would likely also work (recorded for completeness, not pursued)

Had discrepancy control failed, `c_V` could in principle be bounded directly using the Rote root's own structure: `V_i=\lfloor i\gamma\rfloor\bmod2` has a closed combinatorial form via the Ostrowski expansion of `i`, and `c_V=\sum_{i:V_i=1}3^{k(V)-k_{i+1}(V)}2^i` could be estimated by substituting the Ostrowski-digit bound on `k_{i+1}(V)` directly (the same mechanism used in `ROTE_ROOT_DISCREPANCY.md`'s Step 2, one level earlier in the derivation, before packaging it as a discrepancy statement). This would very likely reproduce the same `O(\log\ell)`-type correction, since it is the identical underlying three-distance/Ostrowski combinatorics — not an independent verification, just a different packaging of the same argument. **Not pursued, since it would not add new information beyond `ROTE_ROOT_DISCREPANCY.md`.**

## Status

**N/A — superseded by §9's success.** Retained as a placeholder file per the task's numbered structure, with the reasoning for why it is unnecessary made explicit rather than silently omitted.
