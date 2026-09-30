> **CORRECTED BY PHASE 8 — see [`theorems/phase7/PHASE7_CORRECTIONS.md`](PHASE7_CORRECTIONS.md)
> items C3 and C5.** Root lengths here use `q_1 = a_1`; BHZ Prop. 2.7 sets `q_1 = a_1 + 1`.
> Retained verbatim as the historical record.

# OSTROWSKI_WITNESS_MAP.md

For general `(a_k),(c_k)`, BHZ's Corollary 3.5 (`BHZ_GENERAL_INTERCEPT_MAP.md`) produces **two competing witness families per `k`**, `x'(k)` and `y(k)` — not one. This project does not force them into a single scalar `r_k`; both are tracked.

## `y(k)`-type witness

- **conjectured** root length: `\ell_k = q_k - c_kq_{k-1}` (the denominator of `y(k)`'s fractional part — algebraically the natural candidate, since `y(k)=1+\text{num}/\text{denom}` reads as `(\text{depth})/(\text{root length})` with that denominator). **Correction, found by this phase's own verification (`scripts/phase7/verify_phase7.py`, §2)**: an independent reconstruction of BHZ's Section-3 achieving-word (`build_witness_word`, applying the stated substitutions `\tau_0^{a_1}\circ\tau_1^{a_2}\circ\cdots\circ\tau_{k-1}^{a_k-c_k}(i)`) does **not** produce a word of this conjectured length — checked at `k=3,5,7$, mismatched every time, not close. **This identification is not verified and is now flagged as open, not assumed.**
- agreement depth: same caveat — `L_k = \Big(\sum_{j=1}^k(a_j-c_j)q_{j-1}\Big) + \ell_k` is the algebraically natural reading of `y(k)`'s formula, **not independently confirmed against an actual reconstructed word.**
- exponent: `r_k=y(k)=L_k/\ell_k` — this ratio itself (the value of `y(k)`, an exact `Fraction` computed directly from BHZ's stated formula) **is** trustworthy, since it comes straight from Corollary 3.5's algebra, not from this phase's own word-reconstruction attempt. Only the *root-length/depth decomposition* of that ratio is unverified.

## `x'(k)`-type witness

- Same root length convention with `k+1` in place of `k$: root length `\ell'_k=q_k` (the denominator of `x'(k)`, **not** `q_{k+1}$ — BHZ's `x'(k)` is normalized by `q_k`, one index lower than the numerator's summation range, per the exact formula), depth `L'_k=q_k\cdot x'(k)=\sum_{j=1}^{k+1}(a_j-c_j)q_{j-1}` directly.
- exponent: `r'_k=x'(k)=L'_k/\ell'_k`.

## Density and drift, per witness

For either family, root weight `\kappa_k$, density `\gamma_k=\kappa_k/\ell_k`, drift `R_k=\ell_k-\kappa_k\log_23` (`theorems/phase7/DRIFT_COORDINATES.md`). **Not derived in closed form here** — `\kappa_k` (the number of `1`s in the specific achieving substitution image) is not extracted from BHZ's text explicitly; `scripts/phase7/bhz_general_witness.py`'s companion word-builder (below) computes it directly by generating the actual word.

## Not forced into one statistic

BHZ's own Corollary 3.5 proof (`\S3`) shows the limsup alternates which of `x'(k),y(k)` dominates depending on the digit pattern (their own case analysis: "if `c_k=a_k` then `y(k)=x'(k-2)`", etc.) — **this project follows that discipline**: `theorems/phase7/OSTROWSKI_PATTERN_CLASSIFICATION.md` and `scripts/phase7/bhz_general_witness.py` track both `x'(k)` and `y(k)` at every `k` and take whichever is larger, never assuming one family alone suffices.
