> **CORRECTED BY PHASE 8 — see [`theorems/phase7/PHASE7_CORRECTIONS.md`](PHASE7_CORRECTIONS.md).**
> Item 13's "remaining lemma" is BHZ 2006 Prop. 5.1/5.2 (**C1**), and the countable-exceptional-set
> reduction is refuted (**C2**). Retained verbatim as the historical record.

# INTERCEPT_OBSTRUCTION_MAP.md

## 1. What exactly changes when intercept `0` is removed?

The Ostrowski digit sequence `(c_k)` becomes a free parameter (any admissible sequence) instead of the fixed pattern encoding `\omega(-\gamma)`. This changes which closed-form BHZ formula applies (the general `x'(k),y(k)` of Corollary 3.5, not the two-term `\omega(-\alpha)`-specialized reduction), and hence changes the exact value and structure of the repetition margin above `2`.

## 2. Which proof ingredients remain unchanged?

All of them except the margin-source: exact XOR transfer, density-`1/2` odd branch, discrepancy `O_A(\log\ell)`, the abstract surplus criterion itself. Re-confirmed intercept-agnostic in `SURPLUS_DECOMPOSITION.md`.

## 3. Which quantities become Ostrowski-digit dependent?

Only the witness margin `E_k=\max(x'(k),y(k))-2` and the witness's root length/depth/density (`OSTROWSKI_WITNESS_MAP.md`).

## 4. What is the exact general witness surplus formula/bound?

`S_k\ge E_k\cdot\ell_k-C_AD_k-O_A(\log\ell_k)`, `E_k` from BHZ's general Corollary 3.5 formula (`SURPLUS_DECOMPOSITION.md`, `INTERCEPT_EXCESS.md`).

## 5. Which digit patterns provably certify?

Intercept `0` itself and countably many "return" intercepts `\{j\gamma\bmod1\}` reduce to already-proved cases (`BHZ_GENERAL_INTERCEPT_MAP.md`'s exceptional-orbit analysis); **none of the general (non-exceptional) patterns are proved** — every positive result for them in this phase is computational, not a closed proof.

## 6. Which patterns are computationally promising?

All 36 tested structured families (`STRUCTURED_INTERCEPTS.md`) plus 4 directly-tested genuine nonzero intercepts using the fully-verified exact pipeline (`data/phase7/nonzero_intercept_direct.txt` — **the strongest evidence in this phase**, since it bypasses the disclosed BHZ-word-reconstruction gap entirely and uses the same exact-arithmetic machinery already proved correct in Phases 4–6).

## 7. Which patterns are borderline?

None found at borderline (`\text{Class C}`, `theorems/phase7/FLEXIBLE_MARGIN_BOUNDARY.md`'s decaying-margin regime). The "eventually maximal admissible" family is the closest to a boundary case found, with margin shrinking like `\sim1/A^2` as `A\to\infty` but never observed to reach `0`.

## 8. Did any bounded-type intercept defeat all tested witnesses?

**No.** Zero configurations, across 36 structured `(c_k)` families and 4 direct-verification nonzero intercepts, failed to certify.

## 9. Does the intrinsic-square route bypass the obstruction?

**No — precisely located in `INTRINSIC_SQUARE_ROUTE.md`.** Bare squares (`r=2`) bypass it for the even-weight branch unconditionally, but give exactly zero margin for the odd-weight (density-`1/2`) branch, which is the binding one. Strict excess above `2` (the BHZ-margin route) remains necessary.

## 10. Is drift `R` useful technically, or only expositorily?

**Only expositorily, on the evidence gathered.** `DRIFT_VS_DIGITS.md`: no tested pattern showed drift materially helping or hurting; it is a re-coordinatization of the existing density variable (`DRIFT_COORDINATES.md`), not a new lever.

## 11. Does resonance amplification ever materially improve the bound?

**Not observed.** No tested witness came near the resonance line; the mechanism was not needed to explain any certifying case found.

## 12. What is the weakest sufficient intercept condition found?

None derived in closed algebraic form (`INTERCEPT_SUFFICIENT_CONDITION.md`, classified CONJECTURAL). The flexible asymptotic boundary (`FLEXIBLE_MARGIN_BOUNDARY.md`, `\epsilon_k\ell_k\gg\log\ell_k`) is proved as a *sufficient criterion*, but no specific digit-pattern condition guaranteeing it in general was proved.

## 13. What exact lemma would prove all bounded-type intercepts?

> For any admissible `(c_k)` of a bounded-partial-quotient slope, `\limsup_k\max(x'(k),y(k))>2` with a margin depending only on `A=\sup a_n`.

This is `INTERCEPT_SUFFICIENT_CONDITION.md`'s candidate, unproved. A proof would most plausibly proceed by the same reversed-continued-fraction elementary bound used for `\omega(-\alpha)`, generalized to track `\sum(a_j-c_j)q_{j-1}` under the admissibility constraint directly — not attempted to completion here.

## 14. Is an all-intercepts theorem plausible with the current bridge?

**Yes, plausible — strong, broad, exact-arithmetic evidence, no counterexample found anywhere searched.** Not yet proved.

## 15. What should Phase 8 target, if anything?

Either (a) complete the missing lemma (item 13) via the elementary reversed-CF argument, generalized properly to arbitrary admissible `(c_k)`, or (b) independently re-derive BHZ's Section-3 word-length construction correctly (closing this phase's own disclosed reconstruction gap) so that the *exact* surplus machinery, not just the abstract `\text{ice}` ratio, can be run directly on BHZ-predicted witnesses at scale. Given `nonzero_intercept_direct.py` already supplies the exact-machinery route without needing that reconstruction, **(a) is the higher-value target.**
