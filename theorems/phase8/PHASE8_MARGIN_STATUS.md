**MARGIN STATUS — FOUR TIERS; THE SHARP VALUE IS A THEOREM ONLY AT RESTRICTED SCOPE**

# PHASE8_MARGIN_STATUS.md

What is actually proved about the general-intercept margin, at what scope, and which tier
Theorem 2 depends on. `scripts/phase8/phase8_margin_optimality.py`,
`data/phase8/margin_optimality_output.txt`.

## 0. Definitions, fixed once

- `γ = [0; A_1, A_2, A_3, …]` irrational; `A := sup_k A_k < ∞` (bounded type).
- `q_k`: convergent denominators of `γ`; `q_0 = 1`, `q_1 = A_1`, `q_k = A_k q_{k-1} + q_{k-2}`.
- BHZ digits: `a_1 = A_1 − 1`, `a_k = A_k` for `k ≥ 2`; `A_b := sup_k a_k`. Always `A_b ≤ A`.
  Every bound below is sharpest in terms of `A_b`; substituting `A ≥ A_b` weakens it but keeps
  it true.
- **`β_A`** := the unique root `> 1` of `β² = Aβ + 1`, i.e. `β_A = (A + √(A²+4))/2`. Equivalently
  `β_A = lim_k q_k/q_{k-1}` for any slope whose partial quotients are eventually `≡ A`, and
  `1/β_A = lim_k λ_k` with `λ_k := q_{k-1}/q_k`. (`β_1 = θ` the golden mean, `β_2 = 1+√2`.)
- `δ*(γ) := inf{ ice(ω) − 2 : ω ∈ X_γ }`, the sharp margin at the slope `γ`.

## 1. The four tiers

| tier | statement | status | scope |
|---|---|---|---|
| **T1** | `ice(ω) ≥ 2 + 1/(2(A_b+1)² + 1)` for every `ω ∈ X_γ` | **PROVED, PUBLISHED 2006** — BHZ Prop. 5.1 (some `(a_k,a_{k+1}) = (s,t)`, `s>1`, infinitely often) + Prop. 5.2 (`(1,1,t)` infinitely often); bounded type falls into one by pigeonhole | every bounded-type `γ`, every intercept, both conventions |
| **T2** | `ice(ω) ≥ 2 + 1/(2(A_b+1)²)`, **with an attained witness of exponent `≥ 2 + δ` and root length `≥ q_{k-4}` for every `k ≥ 7`** | **PROVED** — `PHASE8_PROOF_OR_OBSTRUCTION.md` Theorem 1 | same |
| **T3** | `ice(ω) = 2 + 1/(A β_A)` **exactly** at the keep-one intercept `c_k = a_k − 1` | **PROVED** (closed-form fixed point; verified to 12 decimals, `A = 1..8`) | slopes whose BHZ digits are eventually `≡ A`; gives `δ*(γ) ≤ 1/(Aβ_A)` there |
| **T3b** | that keep-one is **optimal**: `δ*(γ) = 1/(Aβ_A)`, attained exactly on the keep-one tails | **PROVED** for `A ≥ 2`; for `A = 1` the Fibonacci slope `[0;\overline1]` is settled by **BHZ Prop. 4.3** instead | slopes with eventually-constant BHZ digits, `A ≥ 2` (plus Fibonacci) |
| **T4** | keep-one is optimal on slopes whose BHZ digit tail is **not** eventually constant | **NUMERICAL EVIDENCE ONLY — not a theorem** | 8 mixed-digit slopes, exhaustive periodic scan; matches keep-one in all 8 |

```
T1  <  T2  <=  T3      at every A_b (asserted and checked, A_b = 1..10)
```

**Theorem 2 depends on T1/T2 only.** T3, T3b and T4 are not load-bearing anywhere: the bridge
needs *some* fixed `δ > 0`, and even T1 alone suffices (at half the margin, via the
supremum-versus-attained reduction of `PHASE8_CHAIN_AUDIT.md` §2). Nothing downstream would
change if T3b were withdrawn entirely.

## 2. T3, the closed form

For a slope with BHZ digits eventually `≡ A` and `d_k := a_k − c_k ≡ 1`, the recurrences of
`PHASE8_PROOF_OR_OBSTRUCTION.md` Lemma 1 give `λ_k → λ = 1/β_A` and `m_k → m* = β/(β−1)`
(the fixed point of `m ↦ λm + 1`). Then, using `β² − 1 = Aβ`,

```
y(k) -> 1 + m*/(lam + 1) = 1 + beta^2/((beta-1)(beta+1)) = 1 + (A beta + 1)/(A beta) = 2 + 1/(A beta)
x'(k) -> m* = beta/(beta-1) ,
```

and `β/(β−1) ≤ 2 + 1/(Aβ)` for all `A ≥ 1`, with equality exactly at `A = 1`. So
`ice(keep-one) = 2 + 1/(Aβ_A)`. Verified exactly at `k = 60`, `A = 1..8`, agreement to `10^-10`.
`1/(Aβ_A) = Θ(A^{-2})`, so **no margin uniform in `A` exists** and the `A`-dependence in the
original Conjecture 12.1 statement is necessary, not a convenience.

## 3. T3b, the optimality argument and exactly where it stops

Let the BHZ digits be `≡ A` for `k ≥ K`, so `λ_k → 1/β_A`. For any admissible `(c_k)`, exactly
one of three cases holds.

1. `d_k = 1` for all large `k` → `limsup = 2 + 1/(Aβ_A)` by T3.
2. `d_k = 0` for infinitely many `k` → at each such `k`, admissibility forces `c_{k-1} = 0`, so
   `d_{k-1} = a_{k-1} = A` and `y(k) = 1 + m_{k-1} = 1 + a_{k-1} + t_{k-2} ≥ 1 + A`.
3. otherwise `d_j ≥ 1` for all large `j` and `d_k ≥ 2` for infinitely many `k` → at each such
   `k`, `x'(k−1) = m_k = t_{k-1} + d_k ≥ 2 + λ_{k-1}m_{k-1} ≥ 2 + λ_{k-1} → 2 + 1/β_A`.

For `A ≥ 2` both `1 + A` and `2 + 1/β_A` **strictly exceed** `2 + 1/(Aβ_A)` (checked `A = 2..10`;
`min` is `2 + 1/β_A`, and `1/β_A > 1/(Aβ_A)` for `A ≥ 2`). Hence the infimum is `2 + 1/(Aβ_A)`,
attained exactly on the keep-one tails. ∎

Both case inequalities are **pointwise**, and are checked as such: 4 000 random admissible
sequences per `A`, `A = 2..7`, exact arithmetic —

```
  A   case-2 indices   min y(k)      1+A      case-3 indices   min m_k      2+1/beta_A
  2         19531      3.35294118      3            48600      2.56097561    2.414214
  4          6714      5.22471910      5            91732      2.28912467    2.236068
  7          2344      8.14072291      8           112500      2.15968948    2.140055
```

no exception at any index.

**Where it stops.** Case 3 needs `λ_{k-1} → 1/β_A`, i.e. a *convergent* `λ`; and cases 2/3 are
compared against the single number `2 + 1/(Aβ_A)`. When the digit tail is not eventually constant
neither holds: `λ_k` oscillates and the case-1 value is itself a `limsup` over a varying
quantity. The argument therefore does **not** extend, and T4 is recorded as evidence only. An
earlier Phase 8 draft stated the sharp value without this scope restriction; that overstatement
is withdrawn here.

## 4. Numerical record, clearly labelled as such

`data/phase8/margin_search_output.txt` (exhaustive admissible periodic cycles to period 7 for
constant slopes `A = 1..10`; exhaustive branch-and-bound over **all** admissible digit strings of
length 18 for `A ≤ 3`; a greedy minimising adversary on non-eventually-periodic bounded-type
slopes to `A = 6`) finds the observed infimum equal to `1/(Aβ_A)` to eight decimals in every
case, and every configuration clears the T2 floor. `data/phase8/margin_optimality_output.txt`
adds eight mixed-digit slopes, where the exhaustive periodic minimum again coincides with
keep-one.

This is a search for counterexamples that failed. It is **not** promoted to an optimality
theorem outside the T3b scope.

## 5. One indexing caution for anyone reading the tables

The `A` in `data/phase8/margin_search_output.txt` is `A_b = max_k a_k`, the **BHZ digit** bound,
because those scans are driven by digit lists `a`. A slope with BHZ digits `≡ A` is
`γ = [0; A+1, A, A, …]`, whose `sup` partial quotient is `A+1`, not `A`; equivalently the same
`ice` values arise at `γ = [0; \overline{A}]`, where `A_b = A = sup` partial quotient, because
`ice` depends only on tails. The T2 floor tested in those scans is `1/(2(A_b+1)²)`, which is
`≥ 1/(2(A+1)²)` — so the scans test a **stronger** floor than Theorem 1 claims.
