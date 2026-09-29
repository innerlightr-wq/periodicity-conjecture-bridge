# REPETITION_SURPLUS_THEOREM.md

## Setup

`\text{lcp}(s,W_n^\infty)\ge r_n\ell_n` (i.e. `s` begins with a power of exponent `\ge r_n` on root `W_n`). `k_n/\ell_n=\gamma_n`, `D(W_n)=o(\ell_n)` (the weakest clean-threshold condition from `DISCREPANCY_HEIGHT_PROOF.md`).

## The asymptotic surplus, error terms tracked exactly

From `DISCREPANCY_HEIGHT_PROOF.md`: `\log_2F(W_n) \le \log_2\ell_n + \lceil D(W_n)\rceil\log_23 + \max(\ell_n,k_n\log_23)`, i.e. `= \max(\ell_n,\gamma_n\ell_n\log_23) + o(\ell_n)` (the `\lceil D\rceil\log_23` term is `o(\ell_n)` exactly because `D(W_n)=o(\ell_n)`, and `\log_2\ell_n=o(\ell_n)` trivially). Hence
```
S_s(W_n) \ge r_n\ell_n - \max(\ell_n,\gamma_n\ell_n\log_23) - o(\ell_n) = \big[r_n-\max(1,\gamma_n\log_23)\big]\ell_n - o(\ell_n).
```
**This is exactly the asymptotic form the task specifies, with the error term identified precisely: it is `o(\ell_n)`, coming entirely from the discrepancy correction `\lceil D(W_n)\rceil\log_23` (negligible by hypothesis `D=o(\ell)`) and the universal `\log_2\ell_n` term (negligible unconditionally).** No other error source exists — the `2-adic` side `(★)` is exact with zero error, and the archimedean triangle-inequality step `(†)` is a one-shot inequality with no accumulated error across `n`.

## Density-convergent criterion

> **THEOREM.** If `\gamma_n\to\gamma_\infty` and `\liminf_n r_n > \max(1,\gamma_\infty\log_23)`, then `\Phi(s)\notin\mathbb Q`.

**Proof.** Immediate from the displayed asymptotic surplus: the bracket's `\liminf` is strictly positive by hypothesis, so `S_s(W_n)=\Theta(\ell_n)-o(\ell_n)\to+\infty`. `\blacksquare`

## Density-free criterion (no limit on `\gamma_n` assumed)

> **THEOREM (uniform over density).** If `D(W_n)=o(\ell_n)`, `\ell_n\to\infty`, and
> ```
> \liminf_n r_n > \log_23,
> ```
> with **no assumption that `\gamma_n` converges, or is bounded away from `0` or `1`, or behaves in any controlled way**, then `\Phi(s)\notin\mathbb Q`.

**Proof.** `\max(1,\gamma\log_23) < \log_23` strictly for every `\gamma\in(0,1)$ (since `1<\log_23` and `\gamma\log_23<\log_23` for `\gamma<1`), so `\sup_{\gamma\in(0,1)}\max(1,\gamma\log_23)=\log_23` (approached, not attained, as `\gamma\to1`). Set `\varepsilon_0:=\liminf r_n-\log_23>0`. For all large `n`, `r_n-\max(1,\gamma_n\log_23) \ge r_n - \log_23 \ge \varepsilon_0 - o(1) > \varepsilon_0/2`, uniformly regardless of `\gamma_n`'s actual value. Hence `S_s(W_n)\ge(\varepsilon_0/2)\ell_n - o(\ell_n)\to+\infty`. `\blacksquare`

**This is genuinely density-free**: no hypothesis whatsoever on the sequence `(\gamma_n)` beyond its being a valid sequence of densities in `(0,1)`. Reproduces `REPETITION_HEIGHT_CRITERION.md`'s uniform theorem exactly, now derived with the error terms made fully explicit as requested.

## Why `\log_23<2` is the structural reason initial squares work for the `3x+1` multiplier

`\log_23=1.58496\ldots<2$, so `r=2` (squares) clears the density-free threshold with margin `2-\log_23=0.41503\ldots`, **whether or not** the discrepancy of the roots vanishes — because (independently, `PHASE1_FREEZE.md` §2) discrepancy is combinatorially capped at `\gamma(1-\gamma)\ell\le\ell/4`, and even substituting this *worst possible* rate `\theta=\gamma(1-\gamma)` into the general theorem of `DISCREPANCY_HEIGHT_PROOF.md` still leaves the threshold at `\sup_\gamma[\max(1,\gamma\log_23)+\gamma(1-\gamma)\log_23]=\log_23<2` (Phase 1's `DISCREPANCY_HEIGHT_THEOREM.md`, re-verified). **This is the exact numerical fact — `\log_2 3 < 2` — that this phase treats as the load-bearing constant for every theorem downstream.**

## Status

**PROVED**, in both the density-convergent and density-free forms, with the asymptotic error term traced to its exact two sources (discrepancy correction, `\log_2\ell` term) rather than left as an unspecified `o(\ell)`.
