**THE POLYNOMIAL BOUND IS WITHDRAWN — THE SOURCE GIVES A STRETCHED EXPONENTIAL**

# BAKER_SOURCE_AND_APPLICATION.md

## 1. What Phase 11 claimed, and why it is wrong

Phase 11 (`theorems/phase11/ROTATION_REPETITION_LEMMA.md` R4) asserted

> ~~`c_m ≥ C₂·m^{−κ}`, citing Baker, *Transcendental Number Theory* (1975), Theorem 3.1.~~

**Withdrawn.** For **algebraic** coefficients the source does not give a polynomial bound. A
polynomial bound `|Λ| > C·B^{−κ}` is what the later sharpenings give for **rational integer**
coefficients; substituting that theorem here would be exactly the error the audit was asked to look
for, and it is not done.

## 2. The theorem actually available, read first-hand

> **Baker, A., *Linear forms in the logarithms of algebraic numbers III*, Mathematika **14** (1967).
> Theorem 2.** Let `α₁,…,α_n` and `β₁,…,β_n` denote non-zero algebraic numbers. Suppose that either
> `log α₁,…,log α_n` or `β₁,…,β_n` are linearly independent over the rationals. Suppose further that
> `κ > n`, and let `d` and `B` denote respectively the maximum of the degrees and heights of
> `β₁,…,β_n`. Then
> ```
> | beta_1 log alpha_1 + ... + beta_n log alpha_n |  >  C e^{-(log B)^kappa}
> ```
> for some effectively computable number `C = C(n, α₁,…,α_n, κ, d) > 0`.

(Theorem 1 of the same paper is the inhomogeneous case `β₀ ≠ 0`, with `κ > n+1` and the same shape
of bound. The height is the **classical** height.)

**The three notions the audit asks to separate:**

| notion | status here |
|---|---|
| **nonvanishing** of `Λ_m` | available independently of Baker: `Λ_m = 0` would give `log₃2 = A_m` algebraic, contradicting Gelfond–Schneider |
| **effective lower bound** | **yes** — `C` is effectively computable |
| **polynomial lower bound** | **no** — the bound is `C·e^{−(log B)^κ}`, a *stretched exponential in `log B`*, strictly weaker than any `B^{−κ'}` |

## 3. Application to the actual coefficients

`α = (√5−1)/2`, `ρ = 1/7`, `β = log₃2`. For `m ≥ 0` let `j_m` be the nearest integer to
`mα + 1/7 − β` and put

```
A_m := m*alpha + 1/7 - j_m ,        c_m := || m*alpha + 1/7 - beta ||  =  | A_m - beta | .
```

**Explicit form and uniform degree/height bounds.** Over the common denominator `14`,

```
A_m = ( a_m + 7m*sqrt5 ) / 14 ,        a_m = -7m + 2 - 14 j_m ,
```

with `|j_m| ≤ m+2` (since `0<α<1`, `0<β<1`), hence `|a_m| ≤ 21m + 30`. For `m ≥ 1`, `A_m` is
irrational, so `deg A_m = 2` with minimal polynomial `196x² − 28a_m x + (a_m² − 245m²)`; for `m = 0`,
`A_0 = 1/7 − j_0` is rational, `deg A_0 = 1`. In both cases `d ≤ 2` and the classical height is

```
H(A_m) = max( 196, 28|a_m|, |a_m^2 - 245 m^2| )  =  O(m^2) ,      log H(A_m) = 2 log m + O(1).
```

Verified: `H(A_m)/m² ≤ 220` on a sample from `m = 0` to `m = 10⁴`.

**Nonvanishing.** `A_m ≠ 0` for every `m ≥ 0` (for `m ≥ 1` because `α ∉ ℚ`; for `m = 0` because
`1/7 ∉ ℤ`). And `Λ_m := A_m log 3 − log 2 ≠ 0`, else `log₃2 = A_m` would be algebraic. **`m = 0` is
therefore not a special case**, but it does require the minimum defining `C_M` to start at `m = 0`,
which it does.

**Hypotheses of Theorem 2, checked.** `n = 2`; `α₁ = 3`, `α₂ = 2` non-zero algebraic; `β₁ = A_m ≠ 0`,
`β₂ = −1 ≠ 0` algebraic; `log 3` and `log 2` are linearly independent over `ℚ` (a rational relation
`a log2 + b log3 = 0` with `(a,b) ≠ 0` gives `2^a = 3^{−b}`, contradicting unique factorisation).
This is the **homogeneous** case, so `κ > n = 2` suffices. Hence, for any fixed `κ > 2`,

> **`c_m = |Λ_m| / log 3 ≥ exp( −c₁ ( log(m+2) )^κ )`** for an effective `c₁ = c₁(κ)`.

This is the strongest bound the source supports, and it is what the repaired proof uses.

## 4. Consequence for `C_M`

```
C_M := min_{0 <= m < M} c_m  >=  exp( -c_1 ( log(M+2) )^kappa ) .
```

Uniform over the whole range, with `c₁` effective. `REPAIRED_WITNESS_GROWTH.md` shows this is
sufficient — a polynomial bound on `C_M` is **not** needed.
