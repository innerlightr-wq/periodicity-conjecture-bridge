# DRIFT_COORDINATES.md

**Diagnostic coordinate only — not a new invariant, not a new theorem.**

For finite `W`, `\ell=|W|`, `k=|W|_1`:
```
R(W) := ell - k*log_2(3)
```
Then `3^k/2^\ell=2^{k\log_23-\ell}=2^{-R(W)}`, so
```
2^ell - 3^k = 2^ell * (1 - 2^{-R(W)}).
```
Diagnostically, define the **resonance amplification**
```
A_res(W) := 1 / |1 - 2^{-R(W)}|.
```
Near `R=0`: `1-2^{-R}\approx(\ln2)R`, so `|2^\ell-3^k|\approx2^\ell(\ln2)|R|` and `A_\text{res}\sim1/((\ln2)|R|)`.

## This is the existing density margin, re-coordinatized — shown explicitly

`R(W)/\ell=1-\gamma\log_23` (`\gamma=k/\ell`). The quantity `\max(1,\gamma\log_23)` — the exact margin threshold in every surplus theorem since `theorems/phase1/REPETITION_HEIGHT_CRITERION.md` — equals `1-\min(0,R/\ell)$ restricted appropriately; concretely, `R/\ell>0\iff\gamma<1/\log_23\approx0.631$, exactly the branch split already used throughout. **No new information is encoded by `R` that `\gamma` did not already carry.** Its value is purely coordinate: `R=0` (resonance) is a more evocative way to talk about the density threshold than `\gamma=1/\log_23`, and it separates the exponential-dominance question (`2^\ell$ vs `3^k`) from the discrepancy/repetition question cleanly, which is useful for organizing Phase 7's tracking of witness families (`theorems/phase7/DRIFT_VS_DIGITS.md`).

## What `R` is used for in this phase, precisely

Not as a new sufficient condition. As a **bookkeeping coordinate** for tracking, across a sequence of general-intercept witnesses `W_k`, whether their density `\gamma_k=k_k/\ell_k` (equivalently `R_k/\ell_k`) is drifting toward, away from, or oscillating around the resonance line `R=0`, alongside the (separately tracked) repetition-exponent excess. The two are independent axes of the same witness — `theorems/phase7/ADMISSIBILITY_GEOMETRY.md` treats them as coordinates of one point, not as competing theories.
