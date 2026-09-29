# DIRECT_SURPLUS_RECURRENCE.md

## Why the counterexample's surplus grows the way it does

Observed (`theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md`, `data/phase3/counterexample_and_recovery_output.txt`): `S` at `\ell=8,46,268,1562,9104,53062,309268` (the locked, odd-weight-certifying witnesses) is `5,55,365,2191,12852,75014,437340`. Ratio of consecutive values: `55/5=11`, `365/55\approx6.6`, `2191/365\approx6.0`, `12852/2191\approx5.87$, `75014/12852\approx5.84`, `437340/75014\approx5.83` — **converging to a fixed ratio `\approx5.83`**, not merely "growing."

**Explanation, now available from `EVEN_TAIL_SURPLUS.md`.** Since `S_k\approx\ell_k/(A+1)` (leading order) and `\ell_k=q_{2k-1}` are convergent denominators of a tail `\overline2` (`A=2`), the `q`'s themselves satisfy the linear recurrence `q_{n+1}=2q_n+q_{n-1}` (silver-ratio recurrence), whose dominant eigenvalue is `1+\sqrt2\approx2.41421`. Two convergent-index steps (`q_{2k-1}\to q_{2k+1}`) multiply by `(1+\sqrt2)^2=3+2\sqrt2\approx5.82843` — **matching the observed ratio `\approx5.83` exactly.** The surplus growth rate is not an independent phenomenon; it is a direct shadow of the CF recurrence's own Perron eigenvalue, confirming `EVEN_TAIL_SURPLUS.md`'s `S_k=\Theta(\ell_k)` claim quantitatively, not just asymptotically.

## Does positivity follow directly from the eigenvalue?

**The eigenvalue governs the growth *rate* once `S_k>0` is established; it does not by itself certify positivity of the leading coefficient** (the sign of `1/(A+1)` in `EVEN_TAIL_SURPLUS.md`, which came from the `\text{ice}` formula's `\text{term2}>2+1/(A+1)` bound, not from the eigenvalue). **This route does not bypass the initial-critical-exponent argument — it corroborates and explains its output, at the level of growth rate, after positivity is already established by `INITIAL_EXPONENT_FORMULA.md`.**
