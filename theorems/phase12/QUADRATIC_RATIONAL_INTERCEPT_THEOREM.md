**PROVED — EVERY QUADRATIC SLOPE, EVERY RATIONAL INTERCEPT, `ρ = 0` INCLUDED**

# QUADRATIC_RATIONAL_INTERCEPT_THEOREM.md

Phase 12 / item 3. Attempted only after the item-1 audit passed.
Verification: `scripts/phase12/general_quadratic.py`, `data/phase12/general_quadratic_output.txt`
(5 slopes × up to 5 intercepts, `ρ = 0` in every block).

## 1. The theorem

> **THEOREM 12.** Let `α ∈ (0,1)` be a quadratic irrational, let `ρ ∈ ℚ` (reduce mod `1`, so
> `ρ = p/q` in lowest terms with `0 ≤ p < q`, `q ≥ 1`; **`ρ = 0` is allowed**), let
> `β = ln2/ln3 = log₃2`, `χ = 1_{[0,β)}`, and define
> ```
> s_n = 1  <=>  { n*alpha + rho }  in  [0, beta) ,    n = 0, 1, 2, ...
> ```
> Then `s` is aperiodic, has ones-density exactly `β`, has `p_s(n) = 2n`, and
> **`Φ(s) ∉ ℚ`**, with the effectivity of `THEOREM11_INDEPENDENT_AUDIT.md` §7.

Theorem 11 is the case `α = (√5−1)/2`, `ρ = 1/7`.

**Quantifier order, explicitly.** For every quadratic irrational `α ∈ (0,1)` and every `ρ ∈ ℚ` there
exist constants `A = A(α)`, `K = K(α,ρ)`, `c₁ = c₁(α,ρ,κ)`, `C = C(α)`, `C₀ = C(α)` such that for
every `M ≥ 2` there is a convergent denominator `ℓ(M)` of `α` with
`S(s[0:ℓ(M)]) ≥ M − (Cc₁/ln2)(log(M+2))^κ − C₀`; the right side `→ +∞` in `M`, so
`limsup_ℓ S(s[0:ℓ]) = +∞` and `Φ(s) ∉ ℚ`.

## 2. Notation and the constants

`α` quadratic ⟹ its continued fraction is eventually periodic ⟹ the partial quotients are bounded;
put `A := max_i a_i(α)`. Convergent denominators `q_k`; `δ(ℓ) := ℓα − round(ℓα)`, `|δ(ℓ)| = ‖ℓα‖`.

```
A  := max partial quotient of alpha            (finite: alpha is quadratic)
K  := (A+2) q^2                                 (q = reduced denominator of rho)
```

For `α = (√5−1)/2`, `ρ = 1/7`: `A = 1`, `q = 7`, `K = 3·49 = 147` — Theorem 11's constant, recovered.

## 3. The proof, step by step, with every qualification

**(P1) Aperiodicity.** A period `p ≥ 1` would make the proper arc `[0,β)` invariant under rotation by
`pα ≢ 0 (mod 1)`. Impossible. *No hypothesis on `ρ`.*

**(P2) Density exactly `β`.** Weyl equidistribution for irrational `α`; the limit exists, so
`liminf = limsup = β`. *No hypothesis on `ρ`.*

**(P3) Complexity `2n`.** `β = log₃2` is transcendental (Gelfond–Schneider) and `α` is algebraic, so
`ℤα + ℤ` consists of algebraic numbers and **`β ∉ ℤα+ℤ`** — automatically, for every quadratic `α`.
By Rote (1994) / Berstel–Vuillon (2001) the two-interval coding then has `p(n) = 2n`.
Verified at `n = 6, 12, 20` for all 10 tested `(α,ρ)` pairs including `ρ = 0`: `12, 24, 40`.
**(P3) is used only for the coverage claim, never in the proof of `Φ(s) ∉ ℚ`.** Stated separately so
that no reader takes the irrationality conclusion to depend on a cited complexity value.

**(P4) The mismatch set.** `{x + ℓα} = {x + δ(ℓ)}`, and

```
delta > 0 :  M(delta) = [beta-delta, beta) u [1-delta, 1)
delta < 0 :  M(delta) = [0, |delta|)       u [beta, beta+|delta|)
```

**valid under `|δ| ≤ min(β, 1−β) = 0.3690702464`** (the no-wrap hypothesis; see §5 for why the
construction satisfies it automatically). Hence `L(ℓ) − ℓ = m*(ℓ) := min{m ≥ 0 : {mα+ρ} ∈ M(δ(ℓ))}`.
Checked over 5 slopes × 2 intercepts × 10 shifts × 400 points: **0 disagreements with the definition**.

**(P5) Relaxation, in two forms.**
- *two-sided, unconditional:* `M(δ) ⊆ B(0,|δ|) ∪ B(β,|δ|)`, so `m* ≥ min(t₀, t_β)`.
- *signed, under the no-wrap hypothesis:* for `δ > 0`, `M(δ) = [β−δ,β) ∪ [1−δ,1)` and in particular
  **`0 ∉ M(δ)`**. (Rule: `0 ∈ M(δ) ⟺ δ < 0`; 0 violations in 50 tested shifts satisfying the
  hypothesis.) This is what carries `ρ = 0`.

**(P6) The arc at `0`.** Two facts. For quadratic `α` with max partial quotient `A`,
`‖nα‖ > 1/((A+2)n)` for every `n ≥ 1`. And `‖x‖ ≥ ‖qx‖/q` with `q(mα + p/q) = qmα + p`:

```
|| m*alpha + p/q ||  >=  || q m alpha ||/q  >  1/( (A+2) q^2 m )  =  1/(K m)        (m >= 1).
```

Verified: `min_{1≤m<20000} K·m·‖mα+ρ‖ > 1` in **all 25** `(α,ρ)` cases (smallest observed `1.0718`).
So `t₀ > 1/(K|δ|)` **for the `m ≥ 1` part**. The `m = 0` orbit point is `{ρ}`:

- **`ρ ≠ 0`:** `‖ρ‖ ≥ 1/q`. Since `K = (A+2)q² ≥ 3q²` and `M ≥ 2`, `|δ| < 1/(KM) ≤ 1/(6q²) < 1/q`,
  so `m = 0` is outside `B(0,|δ|)`. No extra hypothesis is needed — the two-sided form suffices.
- **`ρ = 0`:** `‖0‖ = 0`, so `m = 0` **is** in `B(0,|δ|)` and the two-sided form collapses
  (`t₀ = 0`). This is the one genuinely different case, and it is handled in §4.

**(P7) The arc at `β`, and the `β`-boundary.** `c_m := ‖mα+ρ−β‖ = |A_m − β|` with
`A_m := mα + p/q − j_m`, `j_m` the nearest integer to `mα+ρ−β`.

- **The `β`-boundary is never hit:** `mα+ρ ≡ β (mod 1)` would give `β = mα + p/q − j`, algebraic,
  contradicting the transcendence of `log₃2`. So `c_m > 0` for **every** `m ≥ 0`, every `α`, every `ρ`.
- **Nonvanishing, uniformly:** `|A_m − β| ≤ 1/2` and `β > 1/2` give `A_m > β − 1/2 = 0.13092975 > 0`
  for every `m ≥ 0`. Verified across 25 `(α,ρ)` pairs × `m ≤ 3000`: minimum `0.13094`. **So Baker's
  "`β_j` non-zero" hypothesis holds with no case analysis, `m = 0` included.**
- **Degree and height.** Write `α = (u + v√D)/w` with `u,v,w ∈ ℤ`, `w > 0`, `v ≠ 0`, `D > 0`
  squarefree. With `g := wq`, `a_m := muq + wp − j_mwq`, `b_m := mvq`:
  `A_m = (a_m + b_m√D)/g`, `|j_m| ≤ m+2`, so `|a_m|, |b_m| = O(m)` with constants in `α, ρ`, and the
  primitive minimal polynomial divides `g²x² − 2g a_m x + (a_m² − D b_m²)`. Hence `d = 2` for every
  `m ≥ 1` and
  ```
  H(A_m) = O(m^2),   log H(A_m) = 2 log m + O(1).
  ```
  Measured `H(A_m)/m²` maxima: `1.00` (`√5`, `ρ=0`) up to `539` (`(√29−5)/2`, `ρ=3/11`) — always
  bounded. `d = 2` and `A_m ≠ 0` held in every one of the 45 000 sampled cases.
- **Baker.** `n=2`, `α₁=3`, `α₂=2` non-zero algebraic; `β₁ = A_m ≠ 0`, `β₂ = −1 ≠ 0` algebraic;
  `log 3, log 2` linearly independent over `ℚ` (first branch of the disjunction). `d = 2`, `C` depends
  on `d` and not on `H`. Fix any `κ > 2`. Then for `m ≥ 1`
  ```
  c_m = |A_m log 3 - log 2| / log 3  >=  exp( -c_1 (log(m+2))^kappa ) ,
  ```
  `c₁ = c₁(α,ρ,κ)` effective. `m = 0` needs no theorem: `c₀ = ‖ρ−β‖` is one explicit positive number
  (`1−β = 0.3690702464` when `ρ = 0`). Hence
  ```
  C_M := min_{0 <= m < M} c_m  >=  exp( -c_1' (log(M+2))^kappa ) .
  ```

**(P8) The witnesses.** Set `t(M) := min( C_M , 1/(K M) )` and

```
ell(M) := the least ADMISSIBLE convergent denominator q_k of alpha with  || q_k alpha || < t(M) ,
```

where *admissible* means "all of them" if `ρ ≠ 0`, and "those with `δ(q_k) > 0`" if `ρ = 0`.

- *No-wrap is automatic:* `t(M) ≤ 1/(KM) ≤ 1/(2·3q²) ≤ 1/6 < 0.369`. ✓
- *`ℓ(M) < ∞`:* `‖q_kα‖ → 0`, and for `ρ = 0` the sign of `δ(q_k) = q_kα − p_k` alternates with `k`,
  so infinitely many convergents are admissible (verified: 10 of `q_2…q_20` in every slope tested).
- *Upper bound.* `ρ ≠ 0`: minimality gives `‖q_{k−1}α‖ ≥ t(M)`, and `‖q_{k−1}α‖ < 1/q_k`, so
  `ℓ(M) < 1/t(M)`. `ρ = 0`: the previous admissible denominator is `q_{k−2}`, giving
  `q_{k−1} < 1/t(M)` and then `ℓ(M) = q_k ≤ (A+1)q_{k−1} < (A+1)/t(M)` — **this is where bounded
  consecutive convergent-denominator ratios are used, and they are available exactly because `α` is
  quadratic** (eventually periodic CF ⟹ `a_i ≤ A` ⟹ `q_{k+1} = a_{k+1}q_k + q_{k−1} ≤ (A+1)q_k`;
  verified `max q_{k+1}/q_k ≤ A+1` on all 5 slopes). Either way
  ```
  log ell(M)  <=  c_1' (log(M+2))^kappa + O(1)  =  O( (log(M+2))^kappa ) .
  ```
- *Lower bound.* `‖q_kα‖ > 1/(q_{k+1}+q_k) ≥ 1/((A+2)q_k)`, so `t(M) > 1/((A+2)ℓ(M))` and
  `ℓ(M) > KM/(A+2) = q²M → ∞`.

**(P9) Agreement excess `≥ M`.** For `0 ≤ m < M`: `c_m ≥ C_M > |δ|` puts `m` outside `B(β,|δ|)`; and
`‖mα+ρ‖ > 1/(Km) ≥ 1/(KM) > |δ|` for `1 ≤ m < M` puts it outside `B(0,|δ|)`; `m = 0` is handled by
(P6) (`ρ ≠ 0`) or (P5)-signed (`ρ = 0`). So `m*(ℓ(M)) ≥ M`, i.e.

> `L(ℓ(M)) − ℓ(M) ≥ M`.

Verified end to end for `M = 2,4,8,16,32` over 10 `(α,ρ)` blocks: `L−ℓ ≥ M` in every one of the 50
rows, `ρ = 0` included.

**(P10) Drift and discrepancy, uniformly in `ρ`.** By Kuipers–Niederreiter, *Uniform Distribution of
Sequences*, Ch. 2 Thm 3.4, `N·D_N({mα}) ≤ c₁'Σ_{i≤k+1}a_i + c₂' ≤ c₁'A(k+1) + c₂'` for `q_k ≤ N`; and
`q_k ≥ 2^{(k−1)/2}` gives `k = O(log N)`. Shifting the orbit by `ρ` replaces one interval by at most
two, so `D_N({mα+ρ}) ≤ 2D_N({mα})` — **the bound is uniform in `ρ`**, which is what the theorem needs
since `ρ` is arbitrary. Hence with `e_ℓ := k_ℓ − ℓβ` and `D(W) := max_{i≤ℓ}|k_i − iβ|`,

```
|e_ell| <= C_D log2(ell) + C_D' ,     D(W) <= 2 C_D log2(ell) + 2 C_D' ,
```

`C_D, C_D'` depending on `α` only. Measured `max_{N≤20000}|k_N − Nβ|/log₂N ≤ 0.74` over all 15 tested
`(α,ρ)` pairs — a consistency check, not the proof.

**(P11) The height inequality and the conclusion.** Since `β·log₂3 = 1` exactly,

```
S(W) >= (L - ell) - log2(3) max(0, e_ell) - ceil(D(W)) log2(3) - log2(2 ell)
     >= (L - ell) - C log2(ell) - C_0 ,     C := 1 + 3 C_D log2 3,  C_0 := 1 + log2(3)(3C_D' + 1).
```

At `ℓ = ℓ(M)`, using (P8) and (P9),

```
S( s[0:ell(M)] )  >=  M  -  (C c_1'/ln 2) ( log(M+2) )^kappa  -  C_0'  ->  +infinity
```

because `(log M)^κ = o(M)` for every fixed `κ`. `s` is aperiodic so `s ≠ W^∞` for every `W`, and the
abstract criterion (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`) gives `Φ(s) ∉ ℚ`. ∎

## 4. `ρ = 0`: no finite shift, no separate argument — a sign restriction

The task asked whether `ρ = 0` needs a finite shift or a separate argument. Neither.

- **A finite shift does not work and must not be used.** `σ^1 s` is the coding at intercept
  `{α}`, which is *irrational*; that destroys the rationality of the intercept, which is precisely
  what (P6) needs. Shifting trades the one difficulty for a worse one.
- **What `ρ = 0` actually breaks** is only the two-sided relaxation at `m = 0`: `‖0‖ = 0 ≤ |δ|`, so
  `t₀ = 0` and `m* ≥ min(t₀,t_β)` becomes vacuous.
- **The fix is the signed form (P5).** For `δ > 0`, `M(δ) = [β−δ,β) ∪ [1−δ,1)`, and `0` lies in
  neither: `0 ∉ [1−δ,1)` since `δ < 1`, and `0 ∉ [β−δ,β)` since `δ < β`. So restrict `ℓ(M)` to the
  convergents with `δ(q_k) > 0`; since `δ(q_k)` alternates in sign, infinitely many qualify, and
  bounded ratios `q_{k+1} ≤ (A+1)q_k` absorb the cost of skipping every other one (P8).
- **`m = 0` is otherwise unexceptional.** The `β`-arc never contains it (`c₀ = 1−β = 0.36907 > |δ|`),
  and `A_0 = 1 ≠ 0` — indeed `A_0 = 1` exactly, because `j_0 = round(−β) = −1`, which is why the
  `A_m > β − 1/2` bound is the right way to see nonvanishing.
- `ρ = 0` is also exactly the case `ρ ∈ ℤα + ℤ` among rational intercepts (`ρ = mα+n` with `ρ ∈ ℚ`
  forces `m = 0`), so it is the only rational intercept whose orbit meets a discontinuity. Verified
  that it nonetheless has `p(n) = 2n` at `n = 6,12,20` for all five slopes.

**Can a rational intercept land exactly on the boundary at `0`?** Only at `m = 0`, and only for
`ρ = 0`: `mα + p/q ∈ ℤ` with `m ≥ 1` forces `α ∈ ℚ`. So the complete answer is: finitely many boundary
hits (exactly one, at `m = 0`), occurring for exactly one rational intercept, handled by (P5)-signed.

## 5. What the theorem does **not** cover, and why

| widening | status |
|---|---|
| `ρ` irrational | **OPEN, and the real boundary.** (P6) collapses: the orbit still misses `0`, but with no effective rate. `‖mα+ρ‖` can be as small as one likes along a subsequence |
| `α` algebraic of degree `≥ 3` | **conditionally covered.** The proof needs only: `α` algebraic (for Baker) *and* bounded partial quotients (for (P6) and (P8)). So Theorem 12 holds verbatim for every **algebraic `α` with bounded partial quotients**. Whether any of degree `≥ 3` exists is a well-known open problem, so the extra generality is currently vacuous — which is why the theorem is stated for quadratics |
| `α` transcendental | **NO.** `A_m` is then transcendental and Baker gives nothing; `c_m` is uncontrolled |
| interval `[0,γ)` with `γ ≠ β` | **already covered elsewhere**, and by easier means: density `γ ≠ β` is reached by T1 (for `γ < β`) — see `CRITICAL_ROTATION_PRIOR_RESULTS.md` |
| interval `[u, u+β)` with `u ≠ 0` | **plausible but unwritten.** Both discontinuities move; the arc at `u` needs `‖mα+ρ−u‖` bounded below, which for algebraic `u` is another Baker application and for transcendental `u` is nothing. Not attempted |

## 6. Quantitative content of the general theorem

Exact height floors, each an integer comparison `2^L > F(W)·2^S`, at `M = 32`:

```
alpha             rho    ell    k      L       H >=
(sqrt5-1)/2       0      89     56     233     2^140
(sqrt5-1)/2       1/7    2584   1630   5062    2^2469
sqrt2-1           0      169    107    354     2^179
sqrt2-1           1/7    2378   1500   4523    2^2136
sqrt3-1           0      153    97     285     2^125
sqrt3-1           1/7    2911   1836   3622    2^701
(sqrt13-3)/2      0      1189   750    5116    2^3919
(sqrt13-3)/2      1/7    3927   2477   5580    2^1643
(sqrt29-5)/2      0      701    443    1317    2^608
(sqrt29-5)/2      1/7    3640   2296   11717   2^8069
```

These are Baker-free. The asymptotic continuation is Baker-dependent and effective in principle but
not numerically explicit — the distinction of `THEOREM11_INDEPENDENT_AUDIT.md` §7 applies verbatim.
