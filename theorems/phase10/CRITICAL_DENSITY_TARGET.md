**THE TARGET — ONE FAMILY, FOUR PROPERTIES ESTABLISHED, ONE PROOF OBLIGATION**

# CRITICAL_DENSITY_TARGET.md

## 1. The family

> **Definition (critical-density rotation coding `C(α, ρ)`).** Let
> `β := log₃2 = 0.6309297535714574…`, let `α ∈ (0,1)` be a **quadratic irrational**, and let
> `ρ ∈ [0,1)` with `ρ ∉ ℤα + ℤ`. Define `s = s(α,ρ) ∈ {0,1}^ℕ` by
>
> ```
> s_n = 1   <=>   { n*alpha + rho }  in  [0, beta) .
> ```

`scripts/phase10/critical_density_target.py`; output `data/phase10/critical_density_target_output.txt`.
All slope and intercept arithmetic is done in certified rational brackets (`β` from a 120-digit
`Decimal` logarithm, `α` from its convergents); every membership test is either decided by the
bracket or raises.

## 2. The four required properties — established, not inferred

| property | status | argument |
|---|---|---|
| **aperiodic** | **PROVED** | If `s` had period `p ≥ 1` then `{nα+ρ}` and `{(n+p)α+ρ}` would lie on the same side of the partition for every `n`, i.e. the arc `[0,β)` would be invariant under rotation by `pα ≠ 0 (mod 1)`. A proper arc is not invariant under a non-trivial rotation. |
| **lower ones-density exactly `β`** | **PROVED** | `k_n(s) = #{m < n : {mα+ρ} ∈ [0,β)}`, and `α` irrational, so by Weyl equidistribution `k_n/n → β`. The limit exists, so `liminf = limsup = β` — neither `< β` nor `> β`. |
| **complexity `p(n) = 2n`** | **CITED + verified** | `β` is transcendental and `α` is algebraic, so `β ∉ ℤα + ℤ`; for a two-interval rotation coding with the partition point outside the module the complexity is `2n` (Rote, *J. Number Th.* **46** (1994) 196–213; Berstel–Vuillon, *Coding rotations on intervals*, arXiv:math/0106217). **Verified exactly here** for `n = 6, 12, 20` on 5 slopes × 3 intercepts: `p = 12, 24, 40` in every case. The `2n` value for *all* `n` is quoted, not re-proved. |
| **outside T3 (Dubickas)** | **follows** | T3 needs `liminf p(L)/L < 1.70951129…`; here it is `2`. |
| **outside T4 (all-Sturmian)** | **follows** | T4 is the complexity-`(n+1)` line; `p(20) = 40 ≠ 21`. |
| **outside T1 and T2** | **follows** | T1 needs density `< β`, T2 needs `> β`; here it is `= β` exactly. |

So `C(α,ρ)` sits at `(d, c) = (β, 2)` — the uncovered ray of `DENSITY_COMPLEXITY_LADDER.md` §2.

## 3. This is a minimal change, not complexity inflation

`theorems/phase5/ROTE_DISCREPANCY_AUDIT.md` reduces a CS Rote sequence to **the coding of a rotation
against an interval of length `1/2`**. So the whole repository's headline class and this target are
the *same construction* with one parameter moved:

```
lambda = 1/2   ->  CS Rote                      density 1/2  <  beta   ->  covered by T1
lambda = 1/3   ->  the Phase 1/2 rotation example  density 1/3  <  beta   ->  covered by T1
lambda = beta  ->  THE PHASE 10 TARGET          density beta = beta   ->  UNCOVERED
lambda = 0.7   ->                               density 0.7  >  beta   ->  covered by T2 (preprint)
```

Complexity is `2n` for all four. The conclusion for `λ = β` is **not** obtainable from `λ = 1/2` by
a shift, a finite modification or any transformation the known results see, because the only thing
T1/T2 read is the density, and the density changes. Conversely nothing was inflated: the complexity
is unchanged and the construction is the one already in the repository.

`ρ ∉ ℤα + ℤ` is required, not cosmetic. At `ρ = 0` the orbit point `{0}` sits exactly on a
discontinuity of the partition, the period-`ℓ` agreement fails at the first step, and `L − ℓ = 0`;
every negative exact surplus in the run occurs there.

## 4. The exact bridge requirement at critical density

For a root `W = s[0:ℓ]` with `k := |W|_1`, the height bound
`log₂F(W) ≤ log₂ℓ + ⌈D(W)⌉log₂3 + max(ℓ, k log₂3)` splits on `k log₂3 ≷ ℓ`, i.e. on `k ≷ ℓβ`. Put

```
e_ell := k_ell - ell*beta          (the FINITE-root density deviation)
```

so that `max(ℓ, k log₂3) = ℓ + max(0, e_ℓ)·log₂3`. With `L := lcp(s, W^∞)`:

> **The requirement.**
> ```
> S  >=  (L - ell)  -  ( ceil(D(W)) + max(0, e_ell) ) * log2 3  -  log2 ell .
> ```

Three things to note, all of them consequences of `β log₂3 = 1`:

1. **The threshold is not an exponent.** At every other density the leading term is
   `ℓ·[r − max(1, γ log₂3)]`; at `γ = β` the bracket is `r − 1` and the whole requirement collapses
   to the **overshoot** `L − ℓ`. An initial power of exponent `1 + o(1)` is enough, provided the
   overshoot is large.
2. **Limiting density is useless; the finite deviation `e_ℓ` is what enters.** `k_ℓ = ℓβ + e_ℓ`
   exactly, and `e_ℓ` appears *linearly and un-damped* in the height. A word could have density
   exactly `β` and still be unreachable if `e_ℓ` grew linearly.
3. **Both correction terms are already controlled here.** `theorems/phase2/ROTATION_EXAMPLE_THEOREM.md`
   proves — for **any** fixed interval and **any** bounded-partial-quotient rotation — that the
   interval-counting deviation is `O(log N)`; that is exactly `e_ℓ`, and `D(W)` is bounded by it plus
   `|e_ℓ|`. Measured across 15 (`α`,`ρ`) pairs and `ℓ` up to 3927: `max |e_ℓ| = 1.136`,
   `max D(W) = 3.51`, `max |e_ℓ|/log₂ℓ = 0.17`.

Substituting, the requirement becomes a single clean statement.

## 5. The smallest sufficient lemma

> **(L2)** For `s = s(α,ρ)` as above there are infinitely many `ℓ` with
> ```
> lcp(s, (s[0:ell])^inf)  -  ell   >>   log ell .
> ```

**(L2) ⟹ `Φ(s) ∉ ℚ`.** Everything else is in place: aperiodicity (§2), `e_ℓ, D(W) = O_α(log ℓ)`
(§4.3, already proved in the repository), and the abstract criterion
(`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`). No transfer, no weight parity, no
Ostrowski machinery — the criterion applies to `s` directly.

### What (L2) says geometrically

For `ℓ = q_k` (a convergent denominator of `α`), `s_n ≠ s_{n−ℓ}` exactly when `{(n−ℓ)α+ρ}` and its
translate by `θ := ‖q_kα‖ ≈ 1/q_{k+1}` straddle one of the **two** discontinuities `0` and `β`. So
`L − ℓ` is the **first entry time of the orbit into a union of two arcs of length `θ`**, and (L2)
asks that this entry time exceed `log ℓ` infinitely often. Generic behaviour is `≈ 1/(2θ) ≈ q_{k+1}/2`,
which is polynomial in `ℓ` — enormously more than `log ℓ`. The lemma can only fail if `ρ` is
pathologically close to the orbit of `0` or of `β` at *every* scale.

### Adversarial test

Ratio `(L − ℓ)/log₂ℓ` at `ℓ = q_k`, five slopes × three intercepts
(`data/phase10/critical_density_target_output.txt` §4):

```
alpha                rho     #ell   min ratio   max ratio   # with ratio > 1
golden [0;1bar]      1/7     17     0.463       5267.4      15/17
golden [0;1bar]      3/11    17     2.789       2872.3      17/17
silver [0;2bar]      1/7      9     1.235       1064.9       9/9
[0;3bar]             1/7      7    11.696       3663.5       7/7
[0;5bar]             1/7      5     4.255       5541.5       5/5
[0;1,2bar]           1/7     12     0.874       8702.4      11/12
golden [0;1bar]      0       17     0.000       1829.9       7/17     <- rho = 0, excluded
```

No `(α,ρ)` with `ρ ∉ ℤα+ℤ` failed to produce a large ratio at most scales; the occasional dip below
`1` is harmless because (L2) needs only *infinitely many* good `ℓ`. **The exact integer surplus** is
positive at 45 of 62 tested `(α,ρ,ℓ)`, and every failure is a `ρ = 0` row with `L − ℓ = 0`. Sample
(golden, `ρ = 1/7`): `ℓ = 233 → S = 230.3`; `ℓ = 987 → S = 1447.9`; `ℓ = 2584 → S = 2469.7`. The
derived inequality of §4 was **asserted** on every row, not merely observed.

## 6. The proof obligation, stated once

> Prove (L2): for a quadratic irrational `α` and `ρ ∉ ℤα+ℤ`, the first entry time of the orbit
> `({mα+ρ})_{m≥0}` into `(−θ_k, 0) ∪ (β−θ_k, β)`, where `θ_k = ‖q_kα‖`, exceeds `C log q_k` for
> infinitely many `k`.

This is a three-distance / inhomogeneous-approximation statement about **`ρ` and `β` jointly**, with
no arithmetic input. It is the one open step, and it is the only thing between the existing
machinery and a genuinely uncovered theorem.
