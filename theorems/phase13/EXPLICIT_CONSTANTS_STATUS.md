**AN EXPLICIT ALGEBRAIC-COEFFICIENT ESTIMATE EXISTS AND IS APPLICABLE — `c₁ ≈ 2.4·10^13`**

# EXPLICIT_CONSTANTS_STATUS.md

Phase 13 / item 5. **Kept separate from the qualitative proof**: the stretched-exponential estimate
of Baker already suffices for Theorem 13, and nothing below is needed for it. Computation:
`scripts/phase13/explicit_constants.py`, `data/phase13/explicit_constants_output.txt`.

## 1. The estimate, read first-hand

> **Waldschmidt, Theorem 10.1** (*Linear independence of logarithms of algebraic numbers*; the book
> version is *Diophantine Approximation on Linear Algebraic Groups*, Grundlehren **326**, Springer
> 2000). Let `ℓ₁,…,ℓ_m` be logarithms of algebraic numbers, `α_i = exp(ℓ_i)`, let `β₁,…,β_m` be
> **algebraic numbers**, let `D` be the degree of `ℚ(α₁,…,α_m,β₁,…,β_m)` over `ℚ`, and let
> `A₁,…,A_m, B` be real numbers `≥ e` satisfying
> ```
> log A_i >= h(alpha_i),    D log A_i >= e |l_i|,   (1 <= i <= m)
> log B   >= h(1 : beta_1 : ... : beta_m),          B >= (50 m D log A)^{3m},   A = max A_i.
> ```
> If `Λ = β₁ℓ₁ + ⋯ + β_mℓ_m` does not vanish, then
> ```
> |Lambda|  >  exp{ -(50m)^{3m} D^{m+2} (log B)^2 log A_1 ... log A_m } .
> ```

`h` is the absolute logarithmic Weil height. **The coefficients are algebraic, which is what this
application requires**; the exponent on `log B` is **exactly 2**.

## 2. Hypotheses verified for our form

`Λ_m = A_m log 3 − log 2`, so `m = 2`, `α₁ = 3`, `α₂ = 2`, `β₁ = A_m`, `β₂ = −1`.

| hypothesis | check |
|---|---|
| `α₁, α₂` non-zero algebraic, `ℓ_i = log α_i` | rational integers `3, 2`; principal logarithms, real positive |
| `β₁ = A_m` non-zero algebraic | **`A_m > β − 1/2 = 0.1309297536 > 0`** for every `m`, every `α`, every `ρ` (Phase 12 M4) |
| `β₂ = −1` non-zero algebraic | trivial |
| `Λ_m ≠ 0` | else `log₃2 = A_m` algebraic, contra Gelfond–Schneider |
| `D = [ℚ(3,2,A_m,−1):ℚ]` | `= [ℚ(A_m):ℚ] ≤ [ℚ(α,ρ):ℚ]`; `2, 3` are rational and contribute nothing |
| `h(α₁) = log 3`, `h(α₂) = log 2` | Weil height of a rational integer `n` is `log n` |
| `log A_i ≥ h(α_i)` and `D log A_i ≥ e|ℓ_i|`, `A_i ≥ e` | `log A₁ = max(1, log3, e·log3/D)`, `log A₂ = max(1, log2, e·log2/D)` |
| `log B ≥ h(1:A_m:−1)` | take `log B ≥ log H(A_m) + 2`, `H` the classical height; safe since `h(A_m) ≤ log H(A_m) + log 2` and the projective height adds at most `log 2` |
| `B ≥ (50mD log A)^{3m}` | a floor on `B`, tabulated below; satisfied by taking `log B ≥ log B_min` |

Note this is the **homogeneous** case, so no `β₀` condition arises, and unlike Baker III Theorem 2
there is **no "either … or" disjunction to discharge** — Waldschmidt's Theorem 10.1 assumes no linear
independence among the `β_j` at all (its stated novelty: "an argument which enables us to avoid any
assumption of linear dependence between the coefficients `β₁,…,β_m`"). That removes the one place in
`THEOREM11_INDEPENDENT_AUDIT.md` §4 where `m = 0` fell outside a branch of the hypothesis.

## 3. The constant, evaluated

With `m = 2`, `(50m)^{3m} = 100^6 = 10^{12}`, `D^{m+2} = D^4`:

```
D    log A_1     log A_2   c_1 = 10^12 * D^4 * logA_1 * logA_2     B_min            log B_min
2    1.493169    1.000000  2.38907e+13                            7.093e+14        34.195
3    1.098612    1.000000  8.89876e+13                            1.282e+15        34.787
4    1.098612    1.000000  2.81245e+14                            7.202e+15        36.513
6    1.098612    1.000000  1.42380e+15                            8.203e+16        38.946
```

> **`c_m = |Λ_m|/log 3 > exp(−c₁(log B_m)²)/log 3` with `log B_m = max(log B_min, log H(A_m)+2)` and
> `H(A_m) ≤ C_h m^D` — every constant on the right numerically supplied.**

This **discharges the analytic half** of the *effective in principle / numerically supplied*
distinction introduced in Phase 12. It is also **sharper than Baker III Theorem 2**, whose exponent is
any `κ > 2`; here it is exactly `2`.

## 4. What it costs, and what it does not buy

Feeding `c₁` through `log ℓ(M) ≤ c₁(log B_M)²` and `S ≥ M − (C/ln2)log ℓ(M) − C₀`, and taking `C = 1`
(optimistic — the true `C` also needs the unevaluated Kuipers–Niederreiter constants), the surplus
first turns positive at roughly:

```
D    c_1          M_0 (surplus > 0)     log10 ell(M_0)
2    2.39e+13     2.65e+17              7.95e+16
3    8.90e+13     2.32e+18              6.96e+17
4    2.81e+14     1.37e+19              4.12e+18
6    1.42e+15     1.70e+20              5.09e+19
```

> The first `M` at which the **effective** argument yields a positive surplus is about `10^17`, at a
> witness length of about `10^{8·10^16}`. Utterly beyond computation.

So the explicit route produces a **written-down** bound where before there was only "effectively
computable in principle" — a real gain in rigour and none in usable numbers. **The five finite
certificates (`H ≥ 2^462 … 2^15998`) remain the only numerically useful height floors, and they are
Baker-free.** Nobody should read the table above as an improvement on them.

## 5. The polynomial hope is withdrawn

Phase 12 §8 suggested that at fixed degree these measures might be *polynomial* in the height, which
would restore Phase 11's `c_m ≥ C₂m^{−κ}` and `ℓ(M) = O(M^κ)`. **That suggestion is withdrawn.**

| shape | source | status |
|---|---|---|
| `exp(−C(log B)^κ)`, `κ > 2`, `C` not supplied | Baker, Mathematika 14 (1967), III, Thm 2 | available |
| `exp(−c₁(log B)²)`, `c₁` supplied | Waldschmidt Thm 10.1 | **available — best explicit shape known** |
| `B^{−C}` (polynomial), i.e. `κ = 1` | — | **exactly Baker's own conjecture.** MR0220680: *"It is conjectured that Theorems 3.1 and 3.2 essentially hold with `k = 1`."* **Not available.** |

The orientation offered in Phase 12 — Waldschmidt's 1978 transcendence measure for `|log α − ξ|`,
which at fixed degree `N = 2` has the polynomial shape `H^{−C}` — does **not** transfer: that is an
**inhomogeneous form in one logarithm** (`ξ·1 − log α`), and ours is **homogeneous in two logarithms
with an algebraic coefficient**. Different theorem, different shape. Phase 12 flagged the risk; Phase
13 settles it against the hope.

## 6. No valid reduction to integer coefficients exists

The prohibition on substituting Laurent–Mignotte–Nesterenko or Baker–Wüstholz is not merely
procedural — **no reduction exists**. Clearing denominators for `ρ = p/q`:

```
q * Lambda_m  =  (q m) * (alpha * log 3)  +  (p - q j_m) * log 3  -  q * log 2 ,
```

which has **rational integer** coefficients `qm`, `p−q j_m`, `−q`. But its first "logarithm" is
`α·log 3 = log(3^α)`, and **`3^α` is transcendental** by Gelfond–Schneider, `α` being algebraic
irrational. Linear-forms-in-logarithms theorems require algebraic arguments. So the integer-coefficient
theorems do not apply, with or without clearing denominators, and the algebraic-coefficient theory is
the only route. For algebraic `ρ` of degree `> 1` the same computation leaves `ρ·log 3 = log(3^ρ)`
with `3^ρ` transcendental as well.

## 7. What remains for a fully numerical theorem

One item: **`C` and `C₀`**, i.e. numerical values for the Kuipers–Niederreiter constants `c₁', c₂'` in
`N·D_N ≤ c₁'Σ_{i≤k+1}a_i + c₂'`, specialised to `[0,β)` and to `α` of bounded type. This is
elementary bookkeeping in a classical estimate — no new theorem is needed — and it is the last step to
an explicit `H ≥ 2^{f(M)}` valid at every `M`. It is recorded as the next action in
`PHASE13_VERDICT.md` §8.
