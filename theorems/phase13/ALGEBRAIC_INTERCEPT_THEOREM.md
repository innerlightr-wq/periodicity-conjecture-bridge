**PROVED — EVERY REAL ALGEBRAIC INTERCEPT, BOUNDARY HITS INCLUDED**

# ALGEBRAIC_INTERCEPT_THEOREM.md

Phase 13 / items 3–4. Verification: `scripts/phase13/{numfield,algebraic_intercept}.py`,
`data/phase13/algebraic_intercept_output.txt` — 7 cases spanning field degrees `D = 2, 4, 6`,
including two with an exact `0`-boundary hit (at `m₀ = 5` and `m₀ = 0`).

## 1. The theorem

> **THEOREM 13.** Let `α ∈ (0,1)` be a quadratic irrational, let `ρ ∈ ℝ` be **any real algebraic
> number** (interpreted mod 1), let `β = ln2/ln3 = log₃2`, `χ = 1_{[0,β)}`, and
> ```
> s_n = 1  <=>  { n*alpha + rho }  in  [0, beta) ,     n = 0, 1, 2, ...
> ```
> Then `s` is aperiodic, has ones-density exactly `β`, has `p_s(n) = 2n`, and **`Φ(s) ∉ ℚ`**.

Theorem 12 (`theorems/phase12/`) is the case `ρ ∈ ℚ`; Theorem 11 is `α = (√5−1)/2, ρ = 1/7`.

**Quantifiers.** For every quadratic irrational `α ∈ (0,1)` and every real algebraic `ρ` there are
constants `A = A(α)`, `D = [ℚ(α,ρ):ℚ]`, `c_L = c_L(α,ρ)`, `c₁ = c₁(α,ρ,κ)`, `C = C(α)`, `C₀ = C(α)`
such that for every `M ≥ 2` there is a convergent denominator `ℓ(M)` of `α` with
`L(ℓ(M)) − ℓ(M) ≥ M` and `S(s[0:ℓ(M)]) ≥ M − (C/ln2)·max(c₁(log(M+2))^κ, D²log M + O(1)) − C₀`,
which tends to `+∞`.

## 2. What is genuinely new versus Phase 12, in one line

Phase 12 needed `ρ` rational because the arc-at-`0` bound used `‖x‖ ≥ ‖qx‖/q` with `qρ ∈ ℤ`. For
algebraic `ρ` that identity is unavailable — and is **not needed**: `mα + ρ − j` is itself an
algebraic number of bounded degree and polynomially bounded height, so **Liouville's inequality
alone** bounds it below. No transcendence theory enters the `0`-boundary at all.

## 3. The `0`-boundary

Let `θ_m := mα + ρ − j_m^{(0)}` where `j_m^{(0)}` is the nearest integer to `mα + ρ`, so
`‖mα+ρ‖ = |θ_m|`.

**(a) Degree and height, uniform in `m`.** `θ_m ∈ K := ℚ(α,ρ)`, `D := [K:ℚ] ≤ 2·deg ρ`, so
`deg θ_m ≤ D` for every `m`. Each conjugate of `θ_m` is `mα^{(i)} + ρ^{(i)} − j_m^{(0)}` with
`|j_m^{(0)}| ≤ m+1`, hence `O(m)`; the coefficients of the characteristic polynomial of
multiplication by `θ_m` are the elementary symmetric functions of the `D` conjugates, each therefore
`O(m^D)`, and the fixed denominators of `α, ρ` clear once and for all. So

> **`H(θ_m) ≤ C_h(α,ρ)·m^D`**, with `H` the classical height (largest `|coefficient|` of the
> primitive integer polynomial).

Verified: `max_{1≤m≤400} H(θ_m)/m^D` is `27, 133, 8, 3, 855, 1620, 1.75·10⁶` across the seven cases.

**(b) Exact zero classification.** `θ_m = 0 ⟺ mα + ρ ∈ ℤ ⟺ ρ ∈ ℤα + ℤ`, and then the index `m` is
**unique**, because two solutions `m ≠ m'` would give `α = (j−j')/(m'−m) ∈ ℚ`. So:

> **either `ρ ∉ ℤα+ℤ` and the orbit never hits `0`, or `ρ ∈ ℤα+ℤ` and it hits `0` at exactly one
> index `m₀ ≥ 0`** (or at none, if the unique solution has `m < 0`).

For rational `ρ` this degenerates to `ρ ≡ 0, m₀ = 0` — Phase 12's case. For algebraic `ρ` the hit can
sit at **any** index: `ρ = 3 − 5α` gives `m₀ = 5`. Both were tested; the test is an exact zero test
on a coefficient vector, with no numerics.

**(c) Effective separation — Liouville, no transcendence input.** If `θ ≠ 0` is a root of the
primitive integer polynomial `P(t) = Σ_{i≤d} a_i t^i` of degree `d ≤ D` and height `H`, then
`a₀ ≠ 0`, `|a₀/a_d| = Π|roots| ≥ 1/H`, and every root has modulus `≤ 1 + H/|a_d|`; hence

```
| theta |  >=  (1 + H)^{-D} .
```

Combining with (a):

> **`‖mα+ρ‖ ≥ c_L(α,ρ)·m^{−D²}` for every `m ≥ 1` with `θ_m ≠ 0`** — a **polynomial** lower bound.

Verified: `min_{1≤m≤400} m^{D²}‖mα+ρ‖` is positive in all seven cases (smallest `0.0894`), and the
Liouville inequality itself held at every sampled `m`.

Consequently `t₀ := min{m : ‖mα+ρ‖ ≤ |δ|} > (c_L/|δ|)^{1/D²}` on the indices where `θ_m ≠ 0` — which
diverges as `|δ| → 0`, and that is all the construction needs. For rational `ρ` this recovers a
weaker constant than Phase 12's `1/(K|δ|)`; the weakening is harmless.

**(d) The exact hit does not defeat the proof.** Two independent treatments, both verified:

- *Signed relaxation (self-contained).* For `δ > 0`, `M(δ) = [β−δ,β) ∪ [1−δ,1)`, and `0` lies in
  neither (`δ < 1` and `δ < β`). So restricting `ℓ(M)` to convergent denominators with `δ(q_k) > 0`
  removes the hit whatever its index `m₀`. The sign of `δ(q_k) = q_kα − p_k` alternates with `k`, so
  infinitely many qualify, and `q_{k+1} ≤ (A+1)q_k` absorbs the cost of skipping every other one.
  This is exactly the Phase 12 `ρ = 0` device, and it is insensitive to `m₀`.
- *Reduction by a finite shift.* `ρ ∈ ℤα+ℤ` means `ρ = j₀ − m₀α`, whence `{nα+ρ} = {(n−m₀)α}` for
  **all** `n`: the word is the `ρ = 0` coding read from index `−m₀`. Since `Φ∘S = T∘Φ`, and both `T`
  and its two branches `y ↦ 2y`, `y ↦ (2y−1)/3` preserve rationality, `Φ(s) ∈ ℚ ⟺ Φ(σ^{m₀}s) ∈ ℚ`.
  So the case **reduces to Theorem 12 at `ρ = 0`**. Verified: `s_n = t_{n−5}` for `5 ≤ n < 600` in the
  `ρ = 3−5α` case.

So these intercepts are not discarded, and they need no new analysis beyond the sign restriction.

## 4. The `β`-boundary

Let `A_m := mα + ρ − j_m` with `j_m` the nearest integer to `mα + ρ − β`, so `c_m := ‖mα+ρ−β‖ =
|A_m − β|` and

```
c_m = | A_m ln 3 - ln 2 | / ln 3  =  | Lambda_m | / ln 3 .
```

**(a) The boundary is never hit.** `mα+ρ ≡ β (mod 1)` would make `β = mα+ρ−j` algebraic,
contradicting Gelfond–Schneider. **Uniform in `α`, `ρ`, `m`; this is where the algebraicity of `ρ` is
used a second time.** So `c_m > 0` for every `m`, with no exceptions and no index conditions.

**(b) Zero coefficients and small indices, handled explicitly.** `β₁ = A_m` and `β₂ = −1` must be
non-zero for the theorem quoted below. `β₂` is trivial. For `β₁`:

> `j_m` is the **nearest** integer to `mα+ρ−β`, so `|A_m − β| ≤ 1/2`; and `β = 0.63093 > 1/2`.
> Hence **`A_m > β − 1/2 = 0.1309297536 > 0` for every `m ≥ 0`, every `α`, every `ρ`.**

No case analysis, no exception at `m = 0`, and none at an exact `0`-boundary index either. Verified
across all seven cases for `0 ≤ m ≤ 400`: the observed minimum of `A_m` is `0.13147`, always above
`β − 1/2`. And `Λ_m ≠ 0`, else `log₃2 = A_m` would be algebraic.

**(c) Degree and height, tracking the dependence on `ρ`.** Exactly as in §3(a) with `j_m` in place of
`j_m^{(0)}`: `deg A_m ≤ D = [ℚ(α,ρ):ℚ]` and `H(A_m) ≤ C_h'(α,ρ)·m^D`, so
`log H(A_m) = D log m + O(1)`. Verified: `max H(A_m)/m^D` ranges over `2 … 1.42·10⁵` across the seven
cases — bounded in every one, growing with `D` as the estimate predicts.

**(d) The logarithmic-form theorem, with its hypotheses checked.** Applied in the verified form of
`theorems/phase12/THEOREM11_INDEPENDENT_AUDIT.md` §4 — **Baker, *Linear forms in the logarithms of
algebraic numbers III*, Mathematika 14 (1967), Theorem 2** (= MR0220680's Theorem 3.2): `n = 2`,
`α₁ = 3`, `α₂ = 2`, `β₁ = A_m`, `β₂ = −1`, all non-zero algebraic; `log 3, log 2` linearly independent
over `ℚ` (first branch of the disjunction — the second branch `A_m ∉ ℚ` can fail, e.g. `ρ ∈ ℚ` at
`m = 0`); `κ > n = 2`; `d = ` max degree `≤ D`; `B = ` max classical height `= H(A_m)`. Hence for any
fixed `κ > 2`

> **`c_m ≥ exp(−c₁(log(m+2))^κ)`**, `c₁ = c₁(α,ρ,κ)` effective, uniformly in `m ≥ 1`.

**A uniformity point specific to `D > 2`.** Baker III Theorem 2 fixes `d` as *the* maximum degree of
the `β_j`, so different `m` with different `deg A_m ≤ D` formally invoke different constants. Two
clean fixes, either sufficient: take `c₁ := max` over the finitely many `d ∈ {1,…,D}` (a maximum over
a finite set, still effective); or use **Baker Part I, Theorem 1.1**, which is stated "for all
algebraic `β₁,…,β_n`, not all `0`, **with degree at most `d`**" — a single constant for all degrees
`≤ D` — at the cost of `κ > n+1 = 3` and the extra hypothesis that `log α₁,…,log α_n` **and `2πi`** be
`ℚ`-independent (satisfied: a rational relation `a log2 + b log3 + c·2πi = 0` forces `c = 0` by taking
imaginary parts, then `a = b = 0` by unique factorisation). **For `D > 2` the Part I form is the
cleaner citation, and it is the one used here.**

`m = 0` needs no theorem at all: `c₀ = ‖ρ−β‖` is one explicit positive number.

## 5. The uniform bound on the minimum boundary distance over the first `M` points

Combining §3(c) and §4(d), with `m₀` the exceptional index if there is one:

> **`t(M) := min( min_{0≤m<M, m≠m₀} ‖mα+ρ‖ , min_{0≤m<M} c_m ) ≥ min( c_L M^{−D²},
> exp(−c₁(log(M+2))^κ) ) = exp(−O((log(M+2))^κ))`**, since `κ > 2 > 1`.

This is the inequality the construction consumes. Verified values of both minima are tabulated in
`data/phase13/algebraic_intercept_output.txt` (G).

## 6. Witness growth and unbounded surplus

`ℓ(M) := ` the least **admissible** convergent denominator `q_k` of `α` with `‖q_kα‖ < t(M)`, where
*admissible* means all of them when `ρ ∉ ℤα+ℤ`, and those with `δ(q_k) > 0` when `ρ ∈ ℤα+ℤ`.

- *No-wrap is automatic:* `t(M) ≤ min_{m<M} c_m ≤ c₀ < 1/2 < min(β,1−β)`, so §7's arc description is
  valid at every witness. (Verified: 0 disagreements between the closed form and the definition over
  all fields, 8 shifts each.)
- *Upper bound.* By minimality the previous admissible denominator `q` satisfies `‖qα‖ ≥ t(M)` and
  `‖qα‖ < 1/q'` for its successor `q'`, so `q' < 1/t(M)` and `ℓ(M) ≤ (A+1)q' < (A+1)/t(M)`. Hence
  ```
  log ell(M)  <=  max( c_1 (log(M+2))^kappa , D^2 log M + O(1) ) + O(1)  =  O( (log(M+2))^kappa ) .
  ```
  **Bounded consecutive convergent-denominator ratios are used here**, and they are available because
  `α` is quadratic: eventually periodic continued fraction ⟹ `a_i ≤ A` ⟹ `q_{k+1} ≤ (A+1)q_k`
  (verified `max q_{k+1}/q_k ≤ A+1` in all seven cases).
- *Lower bound.* `‖q_kα‖ > 1/(q_{k+1}+q_k) ≥ 1/((A+2)q_k)`, so `ℓ(M) > 1/((A+2)t(M)) → ∞`.
- *Agreement excess.* By the relaxation of §7 and the bound of §5, no `m < M` lies in
  `B(0,|δ|) ∪ B(β,|δ|)` (the exceptional `m₀`, if present, being excluded by `δ > 0`), so
  ```
  L(ell(M)) - ell(M) = m*(ell(M)) >= M .
  ```
  **Verified end to end at `M = 2,4,8,16,32` in all seven cases: 34 rows, `L−ℓ ≥ M` in every one.**
- *Drift and discrepancy.* Unchanged from Phase 12 (P10): Kuipers–Niederreiter Ch. 2 Thm 3.4 with
  `Σ_{i≤k+1}a_i ≤ A(k+1)` and `k = O(log N)`; a shift of the orbit turns one interval into at most
  two, so the bound is **uniform in `ρ` — including irrational and algebraic `ρ`**, since the
  discrepancy estimate never sees `ρ`. Hence `S(W) ≥ (L−ℓ) − C log₂ℓ − C₀` with `C, C₀` depending on
  `α` alone.
- *Conclusion.* `S(s[0:ℓ(M)]) ≥ M − (C/ln2)·O((log(M+2))^κ) − C₀ → +∞`, so `limsup S = +∞`, and the
  abstract criterion (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`) gives `Φ(s) ∉ ℚ`. ∎

## 7. The combinatorial layer, re-verified in every field

`M(δ) := {x : χ(x) ≠ χ({x+δ})}` equals `[β−δ,β) ∪ [1−δ,1)` for `δ > 0` and `[0,|δ|) ∪ [β,β+|δ|)` for
`δ < 0`, **provided `|δ| ≤ min(β,1−β) = 0.3690702464`** (the Phase 11B hypothesis), and then
`0 ∈ M(δ) ⟺ δ < 0`. `L(ℓ) − ℓ = m*(ℓ)`, the first hitting time — verified against the literal prefix
scan at four convergents in each of the seven cases.

## 8. Aperiodicity, density, complexity — for the actual coding

- **Aperiodic:** a period `p` would make the proper arc `[0,β)` invariant under rotation by
  `pα ≢ 0 (mod 1)`. No `p ≤ 120` is a period of the first 4000 symbols, in any case.
- **Density exactly `β`:** Weyl for irrational `α`; the limit exists. Measured `k_N/N` at `N = 4000`
  lies in `[0.63075, 0.63125]` in all seven cases against `β = 0.6309298`.
- **Complexity `2n`:** `β` is transcendental and `α` algebraic, so `β ∉ ℤα+ℤ` automatically; Rote
  (1994) / Berstel–Vuillon (2001) then give `p(n) = 2n`. Measured `p(6),p(12),p(20) = 12,24,40` in all
  seven cases, **including both exact-hit cases**. Used only for the coverage claim, never in the
  proof.

## 9. Exact height certificates for the family

Each an integer comparison `2^L > F(W)·2^S`, `F(W) = |2^ℓ−3^k| + c_W`, at `M = 32`:

```
case                             ell    k      L       H >=
Q(v5)   a=(v5-1)/2  r=v5/3       233    147    358     2^117
Q(v5)   a=(v5-1)/2  r=1/7        233    147    469     2^230
Q(v5)   a=(v5-1)/2  r=3-5a  EXC  89     56     238     2^144
Q(v5)   a=(v5-1)/2  r=0     EXC  89     56     233     2^140
Q(v2,v5) a=(v5-1)/2 r=v2/3       987    623    1593    2^598
Q(2^1/4) a=v2-1  r=2^1/4/3       70     44     143     2^68
Q(2^1/6) a=v2-1  r=2^1/6/5       70     44     141     2^67
```

Baker-free, like every finite certificate in this programme.

## 10. Translated intervals `[u, u+β)` — the equivalence, checked

For any `u` and any `x`, membership in the arc of length `β` starting at `u` satisfies

```
1_{[u, u+beta) mod 1}( x )  =  1_{[0,beta)}( { x - u } ) ,
```

an identity of arcs, valid **including when `u+β > 1` and the arc wraps** (both sides are the
indicator of the same arc). Hence

> **the coding at intercept `ρ` with interval `[u,u+β)` IS the coding at intercept `ρ−u` with
> interval `[0,β)`.**

Therefore Theorem 13 covers `[u,u+β)` **exactly when `ρ − u` is algebraic** — and this is strictly
more general than requiring `ρ` algebraic: `ρ` and `u` may **both be transcendental** as long as
their difference is algebraic (e.g. `ρ = π`, `u = π − 1/7`). What the theorem constrains is the
**offset between the intercept and the interval's left endpoint**, not the intercept.

Verified: 7 values of `u` (wrapping and non-wrapping) × 400 orbit points, 0 mismatches, 0 undecided.

**Corollary 13.1.** Let `α ∈ (0,1)` be a quadratic irrational and `u, ρ ∈ ℝ` with `ρ − u` algebraic.
If `s_n = 1 ⟺ {nα+ρ} ∈ [u, u+β) (mod 1)`, then `Φ(s) ∉ ℚ`.

## 11. What is still not covered

| widening | status |
|---|---|
| `ρ − u` **transcendental** | **OPEN, and the real boundary.** Both bounds fail: `‖mα+ρ‖` has no effective lower bound (Liouville needs algebraicity), and `‖mα+ρ−β‖` is no longer a logarithmic form in algebraic data. This is now the *only* obstruction on the intercept axis |
| interval length `≠ β` | covered elsewhere and more easily below `β` (Monks–Yazinski); see `FAMILY_THEOREM_PRIOR_COVERAGE.md` |
| **two** intervals of total length `β` at unrelated endpoints | not attempted; each endpoint needs its own bound, and a transcendental endpoint kills it |
| `α` algebraic of degree `≥ 3` with bounded partial quotients | covered verbatim by the same proof; whether such `α` exists is a well-known open problem, so the generality is currently vacuous |
| `α` transcendental | **impossible by this route.** `A_m` transcendental ⟹ no logarithmic-form input, and `‖mα+ρ‖` uncontrolled |
