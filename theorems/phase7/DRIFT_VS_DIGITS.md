# DRIFT_VS_DIGITS.md

`R_k=\ell_k-\kappa_k\log_23` computed on the **actual** BHZ achieving witness words (`scripts/phase7/intercept_adversary.py`'s `build_witness_word`, the real substitution-image words, not an approximation), golden and silver slopes, intercept `0` vs. the "eventually maximal" adversarial family.

## Answers to the six questions

**1. Which digit patterns drive `R_k` toward `0`?** None observed drove it to exactly `0` — in every tested case `|R_k|/\ell_k` stabilizes to a fixed nonzero fraction (`\approx0.02` golden intercept-`0`, `\approx-0.12` silver intercept-`0`, `\approx0.07` silver eventually-maximal) rather than decaying. The digit pattern shifts the *word density* `\gamma_k` (e.g. silver: `0.707` at intercept `0` vs. `0.586` at eventually-maximal — a real, digit-driven change), which moves `R_k/\ell_k=1-\gamma_k\log_23` correspondingly, but no tested pattern pushed it near the resonance line `\gamma\approx0.631` (`R\approx0`).

**2. Which drive `|R_k|` linearly away from `0`?** All tested patterns give `|R_k|=\Theta(\ell_k)` (linear growth, confirmed at `k=4,8,12,16` for golden, `k=4,8,12` for silver — the `R/\ell$ column is stable, not shrinking) — this is the generic behavior; no sublinear-drift pattern was found or specifically sought.

**3. Can near-resonance rescue weak witnesses?** Not tested directly (no pattern found near `R=0`) — this remains open, flagged, not claimed either way.

**4. Can far-from-resonance destroy otherwise strong witnesses?** Not observed. Every tested pattern's `c_W` (via the exact discrepancy-height bound, unaffected by `R`'s sign or magnitude beyond the standard `\max(2^\ell,3^k)` packaging) stayed controlled; no case showed a strong repetition witness defeated by an unfavorable `R`.

**5. Is `R_k` predictable from a bounded digit window?** **No** — consistent with `INTERCEPT_STATE_MODEL.md`'s finding: `\gamma_k$ (hence `R_k$) is a cumulative statistic of the *entire* prefix `(c_1,\ldots,c_k)`, not a bounded-window function.

**6. Monotone or reciprocal relationship between repetition excess and resonance amplification?** No relationship found in the tested data — the two quantities (`\text{ice}$ margin from `OSTROWSKI_PATTERN_CLASSIFICATION.md`, and `R_k$ here) vary independently across the tested families; no correlation was found or expected, consistent with `DRIFT_COORDINATES.md`'s framing of `R` as an *independent* bookkeeping axis, not a competing mechanism.

## Bottom line

**Resonance did not materially help or hurt in any tested case** — every certifying witness certified through the standard repetition-margin route (`OSTROWSKI_PATTERN_CLASSIFICATION.md`), with drift staying a stable, unremarkable linear quantity throughout. `A_\text{res}` remained a diagnostic label in this phase's actual data, exactly as `DRIFT_COORDINATES.md` cautioned it might.
