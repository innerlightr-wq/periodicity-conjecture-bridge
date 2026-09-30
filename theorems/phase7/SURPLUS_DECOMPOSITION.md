> **CORRECTED BY PHASE 8 — see [`theorems/phase7/PHASE7_CORRECTIONS.md`](PHASE7_CORRECTIONS.md)
> item C4.** The displayed inequality `S_k >= A*E_k - C_A*D_k - O_A(log ell_k)` is dimensionally
> incomplete; the leading term is `ell_k * E_k`. Conclusions drawn from it are unaffected.
> Retained verbatim as the historical record.

# SURPLUS_DECOMPOSITION.md

## The key structural simplification for this phase

Every downstream ingredient after "a Sturmian witness `W_k` with exponent `r_k` exists" is **already proved intercept-agnostic**:

- **Rote transfer** (`theorems/phase5/TRANSFER_REDERIVATION.md`): pure algebra on `v_{n+1}=v_n\oplus u_n`, uses no property of `u` beyond being a fixed binary sequence. Applies verbatim to a general-intercept `u`.
- **Density `1/2`** (odd branch, `R=V\bar V`): pure algebra, `|R|_1=|V|_1+|\bar V|_1=|V|`. Intercept-independent by construction.
- **Discrepancy `D(W)=O_A(\log\ell)$** (`theorems/phase5/ROTE_DISCREPANCY_AUDIT.md`): the three-distance/Koksma mechanism bounds the discrepancy of `\{i\beta\bmod1\}$ for the rotation itself — this is a statement about the **rotation's equidistribution rate**, which does not depend on which point `\rho` the orbit starts at. Re-confirmed here: the classical bound `ND_N^*(\beta)=O(\sum_{i\le k}a_i)` governs the whole orbit uniformly, any starting phase.

**So the entire surplus decomposition collapses to one open factor:**

```
S_k >= A*E_k - C_A*D_k - O_A(log ell_k)
```
where `E_k` is the **repetition excess supplied by the Ostrowski digits at this intercept** — the only genuinely intercept-dependent quantity — and `A,C_A` are the same fixed constants (density-`1/2`-derived, `A`-derived) used throughout Phases 4–6.

## Decomposition, four contributions, as requested

**A. Repetition contribution.** `r_k\cdot\ell_k$ (even branch) or `r_k\cdot\ell_k/2` (odd branch, via `\tau=1/2$) — governed entirely by `\max(x'(k),y(k))` from `OSTROWSKI_WITNESS_MAP.md`.

**B. Density/drift contribution.** `\max(1,\gamma_k\log_23)\cdot\ell_k$ (even branch) or `1\cdot\ell_k` exactly (odd branch, density forced to `1/2`) — **unchanged from the intercept-`0` case**, since this is a fact about the *transferred root*, not the source word.

**C. Discrepancy penalty.** `\lceil D(W_k)\rceil\log_23=O_A(\log\ell_k)` — unchanged, intercept-agnostic (above).

**D. Logarithmic/polynomial height penalty.** `\log_2\ell_k=O(\log\ell_k)` — unchanged, universal.

## `E_k` identified

`E_k = \max(r'_k,r_k) - 2` (odd branch, the binding one per `theorems/phase4/REQUIRED_EXPONENT.md`), where `r'_k,r_k` are `OSTROWSKI_WITNESS_MAP.md`'s two competing exponents. **This is exactly `\text{ice}$-type excess above `2`**, and the entire remaining question of this phase is: for which `(c_k)` does `\limsup_kE_k\cdot\ell_k=+\infty` after accounting for `C_AD_k+O_A(\log\ell_k)=O_A(\log\ell_k)`?
