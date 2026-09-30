**THE WITNESS-SIZE ARGUMENT, REPAIRED FOR THE STRETCHED-EXPONENTIAL BOUND**

# REPAIRED_WITNESS_GROWTH.md

Phase 11 R5 sized the witnesses using a polynomial `C_M`, giving `ℓ(M) = O(M^κ)`. With the bound
actually available (`BAKER_SOURCE_AND_APPLICATION.md` §3) that estimate is no longer justified.
This is the replacement.

## 1. Setup

`α = (√5−1)/2`; `q_k` the convergent denominators (Fibonacci); `‖·‖` distance to the nearest
integer. Fix `κ > 2` and let `c₁` be Baker's effective constant, so
`C_M ≥ exp(−c₁(log(M+2))^κ)`. For `M ≥ 2` set

```
t(M)  :=  min( C_M , 1/(147 M) ) ,
ell(M) := the LEAST convergent denominator q_k with || q_k * alpha ||  <  t(M) .
```

## 2. Two facts about the golden continued fraction, used explicitly

Since every partial quotient is `1`:

- **(F1) bounded consecutive ratio:** `q_{k+1} = q_k + q_{k−1} ≤ 2q_k`.
- **(F2) two-sided estimate:** `1/(q_{k+1} + q_k) < ‖q_kα‖ < 1/q_{k+1}`.

Both verified over 30 convergents.

## 3. The size of `ℓ(M)` — upper bound

Let `ℓ(M) = q_k`. By minimality `‖q_{k−1}α‖ ≥ t(M)`, and by (F2) `‖q_{k−1}α‖ < 1/q_k`. Hence

```
t(M)  <  1/q_k ,      i.e.      ell(M)  <  1 / t(M)  =  max( 1/C_M , 147 M ) .
```

Since `κ > 2`, `exp(c₁(log(M+2))^κ)` eventually exceeds `147M` (compare exponents:
`c₁(log M)^κ` versus `log M + log 147`). So for all large `M`

```
ell(M)  <  exp( c_1 ( log(M+2) )^kappa ) ,     hence
```

> **`log ℓ(M) ≤ c₁ (log(M+2))^κ`, i.e. `log ℓ(M) = O( (log(M+2))^κ )`.**

This is exactly the form the repair required.

## 4. `ℓ(M) → ∞` — lower bound

By (F2) and (F1), `‖q_kα‖ > 1/(q_{k+1}+q_k) ≥ 1/(3q_k)`, so `t(M) > 1/(3ℓ(M))`, i.e.

```
ell(M)  >  1/(3 t(M))  >=  147 M / 3  =  49 M   ->   +infinity .
```

So the witnesses do grow, and at least linearly in `M` — the upper bound of §3 is not vacuous.

## 5. Agreement excess

Unchanged from Phase 11 R5, and independent of which Baker bound is used: the two thresholds in
`t(M)` give `t_β ≥ M` (no `m < M` has `c_m ≤ |δ|`, since `c_m ≥ C_M > |δ|`) and `t₀ > M` (since
`t₀ > 1/(147|δ|) > M`), so by the two-ball relaxation

> **`L(ℓ(M)) − ℓ(M) = m*(ℓ(M)) ≥ M`.**

## 6. The height penalty is `o(M)`

`EXACT_HEIGHT_AND_SURPLUS.md` (H′), with the proved drift/discrepancy constants of
`THEOREM11_DEPENDENCY_AUDIT.md` §4:

```
S( s[0:ell(M)] )  >=  ( L - ell )  -  C log2( ell )  -  C_0
                  >=  M  -  (C c_1 / ln 2) ( log(M+2) )^kappa  -  C_0 .
```

For **any fixed** `κ`, `(log(M+2))^κ / M → 0`. So the penalty is `o(M)` and

> **`S( s[0:ℓ(M)] ) → +∞`.**

Illustrative (taking `κ = 3` and the constant `1`):

```
M        (log(M+2))^3    penalty / M      M - penalty
1e2       98.93           0.9893            1.07
1e3      329.9            0.3299          670.10
1e6     2637              0.002637      9.97e5
1e12    2.11e4            2.11e-08        1e12
1e100   1.221e7           1.221e-93       1e100
```

The second column is the whole content of "`o(M)`"; at `M = 100` the margin is already positive and
it widens without limit.

## 7. What this costs

Only the *rate*. Phase 11 claimed `ℓ(M)` polynomial in `M`; the truth available is
`ℓ(M) ≤ exp(c₁(log M)^κ)`, which is quasi-polynomial. The conclusion `S → ∞` is unaffected, because
it needs only `log ℓ(M) = o(M)` — an enormously weaker demand than either bound. **A polynomial
bound on `C_M` is unnecessary.**
