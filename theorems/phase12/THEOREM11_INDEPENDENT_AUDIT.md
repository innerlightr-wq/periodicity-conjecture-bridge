**THEOREM 11 RECONSTRUCTED FROM DEFINITIONS — IT HOLDS; THREE CORRECTIONS TO THE RECORD**

# THEOREM11_INDEPENDENT_AUDIT.md

Phase 12 / item 1. Every quantity below was recomputed from its definition by
`scripts/phase12/qfield.py` + `scripts/phase12/independent_audit.py`; `scripts/phase11` is not
imported anywhere. Output: `data/phase12/independent_audit_output.txt`.

The reconstruction reproduces the Phase 11 word (`s[0:40] = 1010110110101101101011010110110101101111`),
the hitting-time table, the drift table, and **all five height certificates including `2^15998`**,
from independent code. Theorem 11 is confirmed.

## 1. The statement re-derived

> `α = (√5−1)/2`, `ρ = 1/7`, `β = ln2/ln3`, `χ = 1_{[0,β)}`, `s_n = χ({nα+ρ})`. Then **`Φ(s) ∉ ℚ`**.

## 2. Dependency-by-dependency verdict

| # | dependency | verdict | how checked here |
|---|---|---|---|
| 1 | aperiodicity | **PROVED** | a period `p` makes the proper arc `[0,β)` invariant under rotation by `pα ≢ 0`; impossible. No `p ≤ 400` is a period of `s[0:12000]` |
| 2 | ones-density exactly `β` | **PROVED** | Weyl for irrational `α`; the *limit* exists, so `liminf = limsup = β`. `k_N/N − β = −1.3·10⁻⁵` at `N = 12000` |
| 3 | mismatch set, translation sign, endpoints | **PROVED**, with a hypothesis | `{x+ℓα} = {x+δ}`, `δ = ℓα − round(ℓα)`; four-interval case analysis per sign. See §3 |
| 4 | first mismatch = agreement excess | **PROVED** | `L(ℓ) − ℓ = m*(ℓ)` by literal prefix scan vs. hitting time, agreeing at 13 convergents `3 ≤ q ≤ 987` |
| 5 | both boundary arcs avoided, `m = 0` included | **PROVED** | `‖1/7‖ = 1/7`, `c₀ = 0.4880726107`, both `≫ |δ| < 1/294` |
| 6 | Baker's algebraic-coefficient theorem | **CONFIRMED against two independent sources** | §4 |
| 7 | uniform coefficient degree and height | **PROVED**, and improved | `d = 2` for every `m ≥ 1`; `H(A_m) ≤ 55m²` on `m ≤ 10⁴`. See §5 |
| 8 | growing convergent witnesses | **PROVED** | `ℓ(M) > 49M → ∞`; `log ℓ(M) ≤ c₁(log(M+2))^κ` |
| 9 | proved drift/discrepancy | **PROVED** | KN Ch.2 Thm 3.4 with all `a_i = 1`; `|e_ℓ|/log₂ℓ ≤ 0.04` on the range, but the *proof* is the citation |
| 10 | unbounded surplus | **PROVED** | `S ≥ M − (Cc₁/ln2)(log(M+2))^κ − C₀ → +∞` |
| 11 | the rationality contradiction | **PROVED**, re-derived | §6 |

## 3. The mismatch set — and the hypothesis Phase 11B found, re-confirmed

Independently re-derived case analysis (`δ > 0`; `e := −δ` for `δ < 0`):

```
delta > 0 :  M(delta) = [beta-delta, beta) u [1-delta, 1)
delta < 0 :  M(-e)    = [0, e)             u [beta, beta+e)
```

The half-open side of each arc matches the half-open side of `[0,β)`; an endpoint slip would move
`m*` by one. **The closed form needs `|δ| ≤ min(β,1−β) = 0.3690702464`.** Testing the closed form
(pure arc membership: order comparisons of `x` against `0, |δ|, 1−|δ|, β, β+|δ|` only — *not* the
`χ`-pair definition, so the test is not circular) against the definition over 14 shifts × 3000 orbit
points: **0 disagreements where the hypothesis holds, 39 where it fails, all at `q = 1`**
(`|δ| = 0.3819660113`). Phase 11B's finding is reproduced exactly by independent code.

**New in Phase 12: a signed refinement of the relaxation.** Beyond the two-sided containment
`M(δ) ⊆ B(0,|δ|) ∪ B(β,|δ|)` (unconditional; 0 violations over all 14 shifts including `q=1`), the
one-sided form gives the rule

> **`0 ∈ M(δ) ⟺ δ < 0`**, valid whenever `|δ| ≤ min(β,1−β)`.

Verified: 0 violations over the 13 shifts satisfying the hypothesis; the single exception is `q = 1`,
where `β+|δ| > 1`, the arc at `β` wraps past `0` and swallows the arc at `0`. This rule is not needed
for Theorem 11 (which has `ρ ≠ 0`) but it is exactly what carries `ρ = 0` in the generalization —
see `QUADRATIC_RATIONAL_INTERCEPT_THEOREM.md`.

## 4. Baker, checked first-hand against two independent sources

The audit was asked not to rely on the previous transcription. Two independent sources were read:

**(a) Mathematical Reviews, MR0220680 (36 #3732), review by G. J. Rieger** — reprinted in
*Selections Reprinted from Mathematical Reviews*, Bull. Amer. Math. Soc. **43** (2006), pp. 405–406,
covering Baker I, II, III together. Verbatim, for Part III:

> "In Part III an inhomogeneous analogue is considered. **Theorem 3.1**: Let `α₁,…,αₙ, β₀,β₁,…,βₙ`
> denote non-zero algebraic numbers; suppose `k > n+1`, and let `d` [`H`] denote the maximum of the
> degrees [heights] of `β₀,…,βₙ`; then `|β₀+β₁logα₁+⋯+βₙlogα|>Ce^{−(log H)^k}` for some effectively
> computable number `C = C(n,α₁,…,αₙ,k,d) > 0`. The method of proof can be adapted to `β₀ = 0` and
> yields **Theorem 3.2**: Let `α₁,…,αₙ,β₁,…,βₙ` denote non-zero algebraic numbers; suppose that
> **either** `log α₁,…,log αₙ` **or** `β₁,…,βₙ` are linearly independent over `ℚ`; suppose that
> `k > n` and let `d` [`H`] denote the maximum of the degrees [heights] of `β₁,…,βₙ`; then (∗) holds
> for some effectively computable number `C = C(n,α₁,…,αₙ,k,d) > 0`."

and the height convention, stated at the head of the same review:

> "Define the height of an algebraic number to be the maximum of the absolute values of the
> **relatively prime** integer coefficients in its minimal defining polynomial."

**(b) K. C. Chim, MPhil thesis, TU Graz, *Linear Forms in Logarithms and …*, Theorem 1.3**, attributed
to "Baker [3], Theorem 2" with `[3] = A. Baker, Linear forms in the logarithms of algebraic numbers
III, Mathematika 14 (1967)`, quoted verbatim, identical hypotheses and conclusion, and the remark
"the height is referred to as the classical height".

**Conclusion.** Phase 11B's citation is **correct and its transcription is accurate**. The internal
numbering of paper III is Theorem 1 (inhomogeneous) / Theorem 2 (homogeneous); MR renumbers them
3.1 / 3.2 to disambiguate across the four parts. Phase 11B's "Theorem 2" = MR's Theorem 3.2. ✓

**The "either … or" condition, checked as the task asks.** It is a disjunction and only one branch is
needed. We use the **first** branch: `n = 2`, `α₁ = 3`, `α₂ = 2`, and `log 3, log 2` are linearly
independent over `ℚ` (a relation `a log2 + b log3 = 0` with `(a,b) ≠ 0` gives `2^a = 3^{−b}`,
contradicting unique factorisation). The second branch (`β₁ = A_m`, `β₂ = −1` linearly independent
over `ℚ`, i.e. `A_m ∉ ℚ`) also holds for `m ≥ 1` but **fails at `m = 0`** where `A_0 = 1/7` is
rational — so the first branch is the one that must be, and is, used.

**Two independent fallbacks, recorded for robustness.** Part I Theorem 1.1 gives the same bound under
"`log α₁,…,log αₙ` **and `2πi`** linearly independent over `ℚ`" with `k > n+1 = 3` (our `log2, log3,
2πi` are independent: take imaginary parts). Part II Theorem 2.2 drops `2πi` at the cost of
`k > 2n+1 = 5`. Both apply here, and both ask only "not all `β_j` zero" rather than each non-zero.
So the analytic input survives the loss of any one of the three citations; only the numerical value
of `κ` changes, and nothing downstream depends on it.

**The three notions, kept apart.**

| notion | status |
|---|---|
| **nonvanishing** of `Λ_m = A_m log3 − log2` | available *without* Baker: `Λ_m = 0` makes `log₃2 = A_m` algebraic, contra Gelfond–Schneider |
| **effective lower bound** | **yes** — `C` effectively computable, and *independent of `H`*, which is what makes the bound uniform in `m` |
| **polynomial lower bound** | **no** — `C e^{−(log B)^κ}` is a stretched exponential in `log B`; Phase 11's `c_m ≥ C₂m^{−κ}` stays withdrawn |

## 5. Coefficient degree and height — and a simplification of the nonvanishing argument

`A_m := mα + 1/7 − j_m`, `j_m` the nearest integer to `mα + 1/7 − β`. Then
`A_m = (a_m + 7m√5)/14` with `a_m = −7m + 2 − 14j_m`, `|a_m| ≤ 21m + 30`, primitive minimal
polynomial dividing `196x² − 28a_mx + (a_m²−245m²)`, so `d = 2` exactly for `m ≥ 1` and
`H(A_m) = O(m²)` — measured `≤ 55m²` for `m ≤ 10⁴`. Since `C` depends on `d` and not on `H`, a
**single** constant `C(2,3,2,κ,2)` serves every `m ≥ 1`. `m = 0` has `d = 1`, hence formally a
different constant; it needs none, `c₀ = 0.4880726107` being an explicit number.

**Simplification found here.** Phase 11B proved `A_m ≠ 0` case-by-case (`α ∉ ℚ` for `m ≥ 1`;
`1/7 ∉ ℤ` for `m = 0`). One line covers every case at once, for every slope and intercept:

> `j_m` is the **nearest** integer to `mα+ρ−β`, so `|A_m − β| ≤ 1/2`; and `β = 0.6309… > 1/2`.
> Hence **`A_m > β − 1/2 = 0.1309297536 > 0`** always.

Verified over 25 `(α,ρ)` pairs × `m ≤ 3000`: the minimum observed `A_m` is `0.13094…`, never below
`β − 1/2`. This removes the only place where `m = 0` looked exceptional for Baker's hypotheses.

## 6. The arithmetic side, re-derived rather than quoted

`Φ(v) = −Σ_{i: v_i=1} 3^{−k_{i+1}(v)}2^i`. Summing the geometric series 2-adically,

```
Phi(W^inf) = sum_{i<ell, W_i=1} 3^{k-k_{i+1}(W)} 2^i / (2^ell - 3^k) = c_W / (2^ell - 3^k).
```

Checked numerically as stated, not assumed: the truncated series reduced mod `2^60` equals
`c_W·(2^ℓ−3^k)^{−1} mod 2^60` at three test words. With `M := uδ_W − vc_W ≠ 0`, `v₂(M) = L`, and
`|M| ≤ H·F(W)`, `F(W) := |2^ℓ−3^k| + c_W`:

> `2^L ≤ H·F(W)`, hence `H ≥ 2^{L − log₂F(W)}`, and `limsup S = +∞ ⟹ Φ(s) ∉ ℚ`.

## 7. Finite certificates, asymptotic proof, effectivity — the three separated

**(i) Finite certificates — Baker-free, and explicitly supplied.** Recomputed here by exact integer
comparison `2^L > F(W)·2^S`:

```
ell = 377    L =   846    H >= 2^462
ell = 610    L =  1456    H >= 2^838
ell = 1597   L =  2478    H >= 2^872
ell = 2584   L =  5062    H >= 2^2469
ell = 6765   L = 22773    H >= 2^15998        (a 4816-digit lower bound)
```

No analytic input whatever; these are integer facts about the word.

**(ii) The asymptotic proof — Baker-dependent.** That the witness family continues for *every* `M`
rests on Baker. Its constants are **effectively computable in principle, and are not supplied here**:
`c₁` comes from Baker's `C(2,3,2,κ,2)`, which the source guarantees is computable from the proof but
does not evaluate, and `C, C₀` come from the Kuipers–Niederreiter constants `c₁', c₂'`, likewise
computable and not evaluated. So the honest description is:

| constant | effective in principle | explicitly supplied |
|---|---|---|
| the five height floors above | — (no constant involved) | **yes**, exactly |
| `K = 147` in `t₀ > 1/(147|δ|)` | yes | **yes** |
| `c₁` (Baker) | yes | **no** |
| `C, C₀` (drift/discrepancy) | yes | **no** |

An unconditional, fully explicit statement is therefore available only in the finite regime; the
`S → ∞` conclusion is effective but not yet numerically explicit. Phase 11 said "effective"
throughout without drawing this line, which overstates what is on the page.

## 8. Corrections to the record produced by this audit

1. **`A_m ≠ 0` has a one-line uniform proof** (`A_m > β − 1/2`), superseding Phase 11B's two-case
   argument, and it holds for every quadratic `α` and rational `ρ`.
2. **The `m = 0` term is outside the *second* branch of Baker's disjunction** (`A_0 = 1/7 ∈ ℚ`), so
   the first branch (`log 2, log 3` independent) is load-bearing. Phase 11B recorded the branch used
   but not that the other one fails at `m = 0`.
3. **"Effective" needs splitting** into *effective in principle* and *explicitly supplied*: §7.

None of the three affects the truth of Theorem 11; all three affect how it should be stated.
