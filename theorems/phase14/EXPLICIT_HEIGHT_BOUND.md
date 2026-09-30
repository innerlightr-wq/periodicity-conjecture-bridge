**`H ≥ 2^{f(M)}` WITH `f` WRITTEN DOWN — AND `f(M) > 0` ONLY BEYOND `M₀ ≈ 1.78·10^18`**

# EXPLICIT_HEIGHT_BOUND.md

Phase 14 / item 3, second half. `α = (√5−1)/2`, `ρ = 1/7`, `β = ln2/ln3`,
`s_n = 1 ⟺ {nα+ρ} ∈ [0,β)`. Computation: `scripts/phase14/explicit_constants.py`.

## 1. Audit of the analytic estimate before it is used

The `β`-boundary bound rests on **Waldschmidt, Theorem 10.1** (algebraic coefficients; see
`theorems/phase13/EXPLICIT_CONSTANTS_STATUS.md` for the statement). Three points were checked here
that Phase 13 stated loosely or not at all.

**(a) Coefficient hypotheses.** `Λ_m = A_m log3 − log2`, so `n = 2`, `α₁ = 3`, `α₂ = 2`, `b₁ = A_m`,
`b₂ = −1`. All four are non-zero algebraic: `A_m > β − 1/2 = 0.13093 > 0` for every `m ≥ 0` because
`j_m` is the *nearest* integer to `mα+ρ−β` and `β > 1/2`. `Λ_m ≠ 0`, else `log₃2 = A_m` is algebraic.
`D = [ℚ(3,2,A_m,−1):ℚ] = [ℚ(A_m):ℚ] = 2` for `m ≥ 1`. Waldschmidt's theorem imposes **no** linear
independence condition on the coefficients, so unlike Baker's Theorem 2 there is no disjunction to
discharge and no exceptional index.

**(b) Height convention — corrected.** Waldschmidt's hypothesis is
`log B ≥ h(1 : b₁ : ⋯ : b_n)` with `h` the **absolute logarithmic Weil height**, whereas `H(A_m)`
below is the **classical height** (largest `|coefficient|` of the primitive minimal polynomial).
Phase 13 wrote `log B = log H(A_m) + 2` without saying which height was meant. The relation is
`h(a) = (1/d)log M(P)` with `M(P) ≤ ‖P‖₂ ≤ √(d+1)·H`, so for `d = 2`,
`h(A_m) ≤ (log H(A_m) + log√3)/2`; and `h(−1) = 0` with `h(1:b₁:b₂) ≤ h(b₁)+h(b₂)`. Hence

```
h(1 : A_m : -1)  <=  (log H(A_m))/2 + 0.275 .
```

Phase 13's choice is *larger*, hence still admissible — both hypotheses on `B` are lower bounds and
the conclusion is monotone decreasing in `B`, so overestimating `B` is safe — but it is wasteful by
about a factor of 4 in the exponent. The sharper form is used from here on.

**(c) The height bound must be proved, not measured.** With `A_m = (a_m + 7m√5)/14`,
`a_m = −7m+2−14j_m`, `|j_m| ≤ m+2` hence `|a_m| ≤ 21m+30`, and minimal polynomial dividing
`196x² − 28a_m x + (a_m²−245m²)`:

```
196 <= 196 m^2,   28|a_m| <= 588m + 840 <= 1428 m^2, |a_m^2 - 245 m^2| <= 2601 m^2   (m >= 1),
```

so **`H(A_m) ≤ 2601 m²` for every `m ≥ 1`**. The measured maximum of `H(A_m)/m²` over `m ≤ 20000` is
`55`; the proved constant is `2601`. **The measured value is not substituted for the proved one**,
though it shows how much slack the transparent argument gives away.

**(d) The constant.** `log A₁ = max(1, ln3, e·ln3/2) = 1.493169`, `log A₂ = max(1, ln2, e·ln2/2) = 1`,
so

```
c_1 = (50n)^{3n} D^{n+2} log A_1 log A_2 = 100^6 * 2^4 * 1.493169 = 2.38907 * 10^13 ,
B >= (50 n D log A)^{3n} = 7.09306 * 10^14,   log B_min = 34.1953 .
```

This reproduces the Phase 13 figure. Its derivation is now checked line by line.

## 2. Starting-index restrictions, in full

- `M ≥ 2`; the construction quantifies over integers `M ≥ 2`.
- `ℓ(M)` is a convergent denominator `q_k` with **`k ≥ 2`**. This is what makes
  `|δ| ≤ min(β,1−β) = 0.3690702464` hold, which the closed form of the mismatch set requires; it
  fails at `q₁ = 1`, where `|δ| = 0.3819660 > 0.3690702`.
- `m` ranges over `0 ≤ m < M`. The bound `H(A_m) ≤ 2601m²` is for `m ≥ 1`.
- **`m = 0` needs no theorem**: `c₀ = ‖1/7 − β‖ = 0.4880726107`, an explicit positive number.
- Baker/Waldschmidt is applied only for `m ≥ 1`, where `deg A_m = 2` exactly.

## 3. `f(M)`

```
t(M)        := min( C_M , 1/(147 M) ),        C_M := min_{0 <= m < M} c_m
log B_M     := max( 34.1953 , (log(2601 M^2))/2 + 0.275 )
C_M         >= exp( -c_1 (log B_M)^2 - 1 )
ell(M)      <  2 / t(M)                       (the factor 2 is A+1 with A = 1)
log2 ell(M) <= 1 + max( (c_1 (log B_M)^2 + 1)/ln 2 , log2(147 M) )
```

and, with `C = 24.207846`, `C₀ = 35.869175` from `EXPLICIT_DISCREPANCY_CONSTANTS.md`:

> ```
> f(M) := M  -  C * [ 1 + max( (c_1 (log B_M)^2 + 1)/ln 2 , log2(147 M) ) ]  -  C_0
> ```
> **For every integer `M ≥ 2`, the witness `ℓ(M)` satisfies `S(s[0:ℓ(M)]) ≥ f(M)`; hence if
> `Φ(s) = u/v` in lowest terms with `H = max(|u|,v)`, then `H ≥ 2^{f(M)}`.**

Values:

```
M       log B_M    log2 ell(M)     f(M)
1e6      34.195     4.03029e16     -9.75647e17
1e17     43.351     6.47735e16     -1.46803e18
1e18     45.653     7.18371e16     -7.39022e17
1e19     47.956     7.92663e16     +8.08113e18
1e20     50.259     8.70609e16     +9.78924e19
1e25     61.771     1.31516e17     +1.00000e25
```

## 4. The certified threshold

> **`f(M) > 0` for every real `M ≥ M₀` with `M₀ = 1.78337·10^18`.**

Monotonicity is proved, not asserted. On the branch where the Baker term dominates,
`f(M) = M − (Cc₁/ln2)(log B_M)² − const` with `log B_M = log(√2601·M) + 0.275`, so

```
f'(M) = 1 - 2 C c_1 (log B_M) / (M ln 2)  >  0   as soon as   M > 2 C c_1 (log B_M)/ln 2 .
```

At `M = M₀` that threshold is `7.715·10^16 < M₀`, so `f` is strictly increasing on `[M₀,∞)`.
Checked on a `1.05`-ratio grid over 200 steps beyond `M₀`: zero non-increasing steps.

At `M = 10^20` the statement reads `H ≥ 2^{9.789·10^19}`, at a witness length
`ℓ(M) ≈ 2^{8.7·10^16}`.

## 5. What this is and is not

Four heights appear in this programme and they answer different questions.

| | object | size | what it is |
|---|---|---|---|
| **1** | `Φ(W^∞) = c_W/(2^ℓ−3^k)` | height `≈ 2^ℓ` | an **actual rational** matching `s` on a prefix of length `L`. These exist and prove nothing alone |
| **2** | the hypothetical `Φ(s) = u/v` | `H` fixed | the value the asymptotic proof excludes. **Quantifier order matters**: `H` is fixed before `M` |
| **3** | finite certificates | `2^462 … 2^15998` | exact integer comparisons `2^L > F(W)·2^S` at computed witnesses. No analytic input. **The only numerically useful floors** |
| **4** | `f(M)` | positive only past `M₀ ≈ 1.78·10^18` | this document. Beyond computation |

Rows 3 and 4 are not comparable and neither improves the other. **The value of row 4 is that it is
written down**, replacing "effective in principle" with a formula; it is worth nothing numerically,
and no reader should take `M₀` as a computational claim.

## 6. Parameter dependence (item 4)

Let `A` be the largest partial quotient of `α` and `D = [ℚ(α,ρ):ℚ]`.

| constant | depends on | uniform over the family? |
|---|---|---|
| `C₀ = 35.869175` | nothing | **yes, absolutely** |
| `C = 3(2c_A ln2)log₂3 + 1` | `A` only | **yes, given `A`** (`24.21` at `A=1`, `26.70` at `A=2`, `42.19` at `A=10`) |
| `c₁ = 100^6 D^4 log A₁ log A₂` | `D` only | **yes, given `D`** (`2.39e13` at `D=2`, `1.42e15` at `D=6`) |
| `C_h` in `H(A_m) ≤ C_h m^D` | the actual `α, ρ` | **no** |
| `c_L` in `‖mα+ρ‖ ≥ c_L m^{−D²}` (algebraic `ρ`) or `K₀=(A+2)q²` (rational `ρ`) | the actual `α, ρ` | **no** (`K₀` is uniform given `A` and the denominator `q`) |

> **Therefore `f(M)` is not uniformly numerical over the family, and no such claim is made.** `C`,
> `C₀` and `c₁` are; `log B_M` needs `C_h` and `t(M)` needs `c_L`, and neither is bounded over all
> `(α,ρ)` with given `(A,D)` — a `ρ` of enormous height pushes `C_h` up without bound. For any
> **single** explicit `(α,ρ)` both are a finite computation, so `f(M)` is numerical case by case.
> That is what was done above for `α=(√5−1)/2`, `ρ=1/7`, and it is all that is claimed.
