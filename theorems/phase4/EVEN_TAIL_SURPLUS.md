# EVEN_TAIL_SURPLUS.md

## Setup

`A` = the largest partial quotient occurring in the eventual period of `\gamma`'s continued fraction (finite, for any quadratic irrational — indeed for any bounded-partial-quotient slope). `INITIAL_EXPONENT_FORMULA.md`: at the standard-word witnesses `W_k=u[0{:}q_{2k-1}]$ in the eventually-periodic regime,
```
r_u(k) > 2 + 1/(A+1),     for EVERY k (not merely in the limsup).
```

## Odd-weight case (the binding one, per `REQUIRED_EXPONENT.md`)

`r_v=r_u/2 > 1+\tfrac1{2(A+1)}`, root length `2\ell_k` (`\ell_k=q_{2k-1}`), density `\gamma_R=1/2` exactly (`REQUIRED_EXPONENT.md`). Discrepancy of `R`: `O(\log\ell_k)` (`theorems/phase2/ROTE_ROOT_DISCREPANCY.md`'s bound applies to `V`, and the argument there — equidistribution rate `O(\log\ell/\ell)` for bounded partial quotients — transfers to `R=V\bar V` directly, since `|k_i(R)-i/2|\le D(V)+O(\log\ell)` by the same telescoping used for `V` itself, both terms `O(\log\ell)`).

Surplus, using `2\ell_k` as the root length in `REPETITION_SURPLUS_THEOREM.md`'s asymptotic form:
```
S_k ≥ [r_v - max(1, (1/2)log2(3))] · 2*ell_k - O(log ell_k)
    = [r_v - 1] · 2*ell_k - O(log ell_k)
    > [1/(2(A+1))] · 2*ell_k - O(log ell_k)
    = ell_k/(A+1) - O(log ell_k).
```

## Even-weight case (comfortable margin, not binding)

`r_v=r_u>2+1/(A+1)>\log_23`, root length `\ell_k`, density `\gamma_V` arbitrary but `\max(1,\gamma_V\log_23)<\log_23<2` always. Margin `>2+1/(A+1)-\log_23 > 2-\log_23\approx0.415$, uniformly — no `A`-dependence needed at all for this branch (Theorem 10.2's bare `r_u\ge2` already clears `\log_23` with the same margin `REPETITION_HEIGHT_CRITERION.md` established in Phase 1).

## The uniform margin

```
delta_even(A) = 1/(A+1)     [binding, odd-weight case; even-weight case has the larger, A-independent margin (2-log2(3))]
```

**Worst `\gamma`**: not `\gamma\to1` (density is fixed at exactly `1/2` for the binding case, so density extremes are irrelevant) — the worst case is **large `A`** (large partial quotients weaken the margin, `\delta_even(A)\to0` as `A\to\infty`). This is a **fixed, positive** constant for every individual quadratic irrational (finite `A`), but **not uniform across the whole class** of bounded-partial-quotient slopes as `A\to\infty` — consistent with `REQUIRED_EXPONENT.md`'s scope (Target C: quadratic irrationals, each with its own finite `A`; not Target B's fully general bounded-but-unbounded-sup case).

## The bound

```
S_k ≥ [ell_k / (A+1)] - O(log ell_k)  →  +∞  as  k→∞,  for every fixed quadratic-irrational gamma (finite A).
```

`\limsup_k S_k=+\infty$, so by `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`, `\Phi(v)\notin\mathbb Q`.
