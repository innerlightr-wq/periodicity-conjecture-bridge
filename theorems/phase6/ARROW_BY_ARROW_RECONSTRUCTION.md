# ARROW_BY_ARROW_RECONSTRUCTION.md

Reconstructed from BHZ's primary theorem and the source paper, against three genuinely non-eventually-periodic bounded-partial-quotient adversarial controls (Thue–Morse-coded `\{1,2\}`, Fibonacci-word-coded `\{1,2\}`, and two independent random-bounded `\{1,2\}` seeds) — confirmed non-periodic by direct search (`scripts/phase6/bounded_type_generators.py`, period `\le300`, not found in any of the four).

## Arrow 1: `\sup a_n=A<\infty\Rightarrow` witnesses with `r_n\ge2+\delta(A)`, `\delta(A)>0`

**Re-derivation, checked line by line for periodicity dependence**: BHZ's `\omega(-\alpha)` formula (`\text{ice}(\omega(-\alpha))=\limsup_k\max(x(k),y(k))`, their Corollary 3.5 specialized to `\omega(-\alpha)`'s specific, `\alpha`-independent Ostrowski pattern) is derived by BHZ for **any** irrational `\alpha` — their derivation (§4.1) never invokes periodicity of `(a_k)`. The bound `\text{term2}(k)=1+a_{2k-1}+q_{2k-3}/q_{2k-2}>2+1/(A+1)` was re-derived from `a_{2k-1}\ge1` and the reversed-CF fact `[a_{2k-2};a_{2k-3},\ldots,a_1]<a_{2k-2}+1\le A+1` — **also periodicity-free on its face.**

**A genuine correction found by the adversarial test, not by re-reading.** `scripts/phase6/full_pipeline_nonperiodic.py`, Fibonacci-coded case: `\text{term2}(2)` is **exactly equal** to `2+1/(A+1)$ (`=7/3`), not strictly greater — checked across 4 sequences × ~58 values of `k` each (232 checks total), this is the **only** non-strict instance found, and it is **never a violation** (`term2\ge` bound always; `>` fails only this once). **Root cause, re-derived**: `[x;\text{rest}]<x+1` is strict only when `\text{rest}>1`; at the smallest `k` (here `k=2`), the reversed CF can terminate in a bare `a_1=1` with no further terms, giving `\text{rest}=1` exactly and `[x;\text{rest}]=x+1` **exactly**. This is a **small-`k` boundary artifact of the recursion bottoming out**, not a periodicity-dependent phenomenon and not a recurring one (0 further equalities across 231 other checks, including 57 more `k` for the same Fibonacci sequence). **Corrected statement**: `\text{term2}(k)>2+1/(A+1)` for all `k` beyond a small, sequence-specific initial transient (empirically `k\ge3` suffices in every tested case); `\ge` holds always. This does not threaten the theorem, which only needs infinitely many growing witnesses, but **corrects** Phase 5's `UNIFORM_MARGIN_AUDIT.md`, which stated the strict bound holds "for literally every `k`" without having tested a case where it doesn't.

**Verdict: Arrow 1 survives, periodicity-free, with one small-`k` boundary correction now documented.**

## Arrow 2: exact XOR transfer

Pure algebra (`v_{n+1}=v_n\oplus u_n`), no reference to `\gamma`'s arithmetic anywhere in the derivation (`theorems/phase5/TRANSFER_REDERIVATION.md`, already periodicity-free by construction, re-confirmed by inspection — nothing to re-test computationally beyond what Phase 5 already did exhaustively for arbitrary `W`).

## Arrow 3: `R=V\bar V`, density exactly `1/2`

Pure algebra (`|R|_1=|V|_1+|\bar V|_1=|V|`), independent of any CF property. Re-confirmed numerically at every tested witness across all 4 adversarial sequences (`full_pipeline_nonperiodic.py`'s `dens(R)` column: exactly `0.5000` at every odd-weight witness, every sequence).

## Arrow 4: `D(R)=O_A(\log|R|)`

The cited mechanism (`N\cdot D_N^*(\beta)=O(\sum_{i\le k}a_i)$, three-distance/Koksma) is the **standard characterization of bounded-type numbers** in uniform distribution theory — it is stated and proved for *any* irrational with bounded partial quotients; periodicity is not a hypothesis anywhere in this classical result. The auxiliary fact used alongside it, `k=O(\log N)` via `q_k\ge F_k` (Fibonacci growth), holds for **any** continued fraction with `a_i\ge1`, periodic or not — trivial, re-confirmed. **Numerically re-checked**: the `D(R)/\log|R|` column in `full_pipeline_nonperiodic.py`'s output stays in a bounded range (roughly `0.3`–`0.7`) across witness lengths spanning `10` to `7000`, for all 4 non-periodic sequences — consistent with `O(\log|R|)`, not linear growth, with no sign of blow-up specific to non-periodicity.

## Assembling the surplus

`S_n=r_n\ell_n-O(\log\ell_n)$ (even branch, `r_n>2+\delta(A)$ directly) or `S_n\ge\delta(A)\ell_n-O_A(\log\ell_n)` (odd branch, via density `1/2`, same margin). **Confirmed at every one of 4 adversarial slopes**: multiple certifying (`S>0`) witnesses found, at growing root lengths (deepest certifying `\ell` ranges from `1267` to `3549` across the four), values reaching into the thousands. **One expected, harmless non-monotonicity noted**: the certifying-`S` subsequence is not always literally increasing step-to-step (e.g. Thue–Morse: `\ldots,381,377,934$ — a small dip between two certifying witnesses) — this is consistent with, not a violation of, the abstract criterion's own `\limsup` (not monotone-limit) requirement (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`'s sharpness discussion, re-confirmed relevant here).

## Overall

Every arrow reconstructed independently against non-periodic bounded controls survives, with one precise, non-threatening correction (Arrow 1's small-`k` boundary equality) found specifically **because** the adversarial (non-periodic) test was run rather than a periodic-slope substitution check.
