**THE REPETITION LEMMA — PROVED, MODULO ONE CITED EFFECTIVE THEOREM (BAKER)**

# ROTATION_REPETITION_LEMMA.md

> **CORRECTION (Phase 11B).** R4's claim `c_m ≥ C₂m^{−κ}` is **WITHDRAWN**: read first-hand, the source (Baker, *Linear forms in the logarithms of algebraic numbers III*, Mathematika **14** (1967), Thm 2) gives a *stretched exponential* `C·e^{−(log B)^κ}`, not a polynomial bound. R5 is correspondingly replaced by `log ℓ(M) = O((log(M+2))^κ)`, which still suffices. A second, unstated hypothesis of the closed-form arc description (`|δ| ≤ min(β,1−β)`) is also identified there; the construction satisfies it with a factor ≈108 to spare. See `theorems/phase11b/PHASE11B_VERDICT.md` and `theorems/phase11b/BAKER_SOURCE_AND_APPLICATION.md`. **Theorem 11 itself stands**; only this justification changed.


Throughout: `α = (√5−1)/2`, `ρ = 1/7`, `β = log₃2`, `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)`,
`χ := 1_{[0,β)}`, `L(ℓ) := lcp(s, (s[0:ℓ])^∞)`. For `ℓ ≥ 1` let `δ(ℓ) := ℓα − round(ℓα)` (signed),
so `|δ(ℓ)| = ‖ℓα‖`. Verification: `scripts/phase11/rotation_repetition.py`,
`data/phase11/rotation_repetition_output.txt`.

## R1. First-mismatch characterisation — PROVED

`s_{m+ℓ} ≠ s_m ⟺ χ({mα+ρ}) ≠ χ({mα+ρ+δ(ℓ)})`, i.e. `{mα+ρ} ∈ M(δ(ℓ))` where

```
M(d) := { x in [0,1) : chi(x) != chi({x+d}) } .
```

Computing the symmetric difference of `[0,β)` with its translate:

```
d > 0 :  M(d) = [1-d, 1)  u  [beta-d, beta)
d < 0 :  M(d) = [0, |d|)  u  [beta, beta+|d|)
```

— two arcs of length `|d|`, one at `0` and one at `β`, on the side fixed by `sign(d)`. Since the
first mismatch of `s` against `(s[0:ℓ])^∞` occurs at index `ℓ + m` for the least such `m ≥ 0`,

> **`L(ℓ) − ℓ = m*(ℓ) := min{ m ≥ 0 : {mα+ρ} ∈ M(δ(ℓ)) }`.**

**The overshoot *is* a first hitting time.** Verified against the literal longest common prefix at
every convergent denominator `2 ≤ q ≤ 3000`, computing `m*` by the `M(δ)` route with exact `ℚ(√5)`
arithmetic and `L` by literal scanning — they agree in every case.

## R2. Two-ball relaxation — PROVED

From the explicit description, `[1−d,1) ⊆ B(0,d)`, `[0,|d|) ⊆ B(0,|d|)`, `[β−d,β) ⊆ B(β,d)`,
`[β,β+|d|) ⊆ B(β,|d|)`, where `B(y,r)` is the two-sided arc of radius `r`. Hence

```
M(delta)  subset  B(0,|delta|)  u  B(beta,|delta|) ,
```

so with `t₀ := min{m : ‖mα+ρ‖ ≤ |δ|}` and `t_β := min{m : ‖mα+ρ−β‖ ≤ |δ|}`,

> **`m*(ℓ) ≥ min(t₀, t_β)`.**

Checked on 16 shifts × 4000 orbit points: 0 containment violations.

## R3. The arc at `0` is harmless — PROVED, and this is where `ρ = 1/7` earns its keep

For the golden conjugate, `inf_{q≥1} q‖qα‖ = ‖α‖ = 0.38196… > 1/3`, so `‖qα‖ > 1/(3q)` for every
`q ≥ 1`. Using `‖x‖ ≥ ‖7x‖/7` and `7(mα + 1/7) = 7mα + 1`:

```
||m*alpha + 1/7||  >= ||7m*alpha + 1||/7  = ||7m*alpha||/7  >  1/(7 * 3 * 7m)  =  1/(147 m)   (m >= 1),
```

and `‖0·α + 1/7‖ = 1/7`. Therefore

> **`t₀ > 1/(147|δ(ℓ)|)`.**

Exact check: `min_{1≤m<60000} 147·m·‖mα+1/7‖ = 1.341 > 1`. **The rationality of `ρ` is essential
here** — for irrational `ρ ∉ ℤα+ℤ` the orbit still misses `0`, but with no effective rate.

## R4. The arc at `β` — PROVED via an effective cited theorem

**[CORRECTED — see the Phase 11B banner above. The polynomial conclusion stated in this section is withdrawn; the corrected bound is `c_m ≥ exp(−c₁(log(m+2))^κ)` with `κ > 2`, and it still suffices.]**

Put `c_m := ‖mα + ρ − β‖`. Writing the nearest integer as `n`, `c_m = |A − β|` with
`A := mα + 1/7 − n ∈ ℚ(√5)` algebraic of degree `≤ 2` and height `O(m²)`. Since `β = ln2/ln3`,

```
c_m  = | A*ln3 - ln2 | / ln3 ,
```

a **nonzero** linear form in the logarithms of the algebraic numbers `3` and `2` with **algebraic**
coefficients (nonzero because `log₃2` is transcendental, so `A ≠ β`). Baker, *Transcendental Number
Theory* (1975), **Theorem 3.1** — the algebraic-coefficient form, `|β₀ + β₁log α₁ + … + β_n log α_n| > C·H^{−κ}`
with `C, κ` effective and `H` bounding the heights of the `β_j` — gives effective `C₂ > 0`, `κ > 0`:

> **`c_m ≥ C₂ · m^{−κ}` for all `m ≥ 1`.**

Only a **polynomial** lower bound is used; nothing sharper is needed anywhere below. Note this is
the sole external input of the whole argument, and it is effective, so the final height floors are
effective too. A consistency table of `c_m` for `m ≤ 5000` shows no super-exponential decay
(`c_m·m²` ranges over `0.13 … 8·10⁶`), as the bound requires.

## R5. The construction — PROVED

Fix `M ≥ 2`. Put `C_M := min_{0≤m<M} c_m > 0`; by R4, `C_M ≥ C₂M^{−κ}`. Let

```
ell(M) := least convergent denominator q of alpha with ||q*alpha||  <  min( C_M , 1/(147 M) ) .
```

**Both thresholds are needed.** The first gives, for every `m < M`, `c_m ≥ C_M > |δ|`, hence
`t_β ≥ M`. The second gives `1/(147|δ|) > M`, hence `t₀ > M` by R3. By R2, `m*(ℓ(M)) ≥ M`, so

> **`L(ℓ(M)) − ℓ(M) ≥ M`.**

*Recorded failure.* A first draft imposed only the `β`-threshold. At `M = 4` that returns `ℓ = 5`
with `|δ| = 0.0902`, `1/(147|δ|) = 0.075 < 1` — R3 certifies nothing — and indeed `m* = 3 < 4`. The
bug is kept on the record rather than silently repaired.

**Size of `ℓ(M)`.** `min(C_M, 1/(147M)) ≥ C₃M^{−κ''}` with `κ'' := max(κ,1)`, and for the golden
conjugate `‖q_kα‖ ≍ 1/(√5 q_k)` with `q_{k+1}/q_k → φ`, so the least qualifying denominator
satisfies `ℓ(M) ≤ C₄ M^{κ''}`, i.e.

> **`log₂ ℓ(M) ≤ κ'' log₂M + O(1)`.**

**Consequence, stated without `≫`.** Along the subsequence `ℓ(M)`, `M = 2,4,8,…`:

```
( L(ell(M)) - ell(M) ) / log2( ell(M) )   >=   M / ( kappa'' log2 M + O(1) )   ->   +infinity .
```

So `(L−ℓ)/log₂ℓ` is **unbounded** along an explicit subsequence — which is exactly the repetition
estimate `EXACT_HEIGHT_AND_SURPLUS.md` needs.

## Verified instances

```
 M    min(C_M, 1/147M)    ell(M) |delta(ell)|        m*(ell)    m* >= M
  4   1.7006802721e-03       377    1.1862412896e-03       469     True
  8   8.5034013605e-04       610    7.3313743587e-04       846     True
 16   4.2517006803e-04      1597    2.8003358216e-04       881     True
 32   2.1258503401e-04      2584    1.7307027156e-04      2478     True
 64   1.0629251701e-04      6765    6.6106960730e-05     16008     True
128   5.3146258503e-05     10946    4.0856350097e-05      5062     True
256   2.6573129252e-05     17711    2.5250610634e-05     16008     True
```

The table is a consistency check on a proved statement, not the evidence for it.
