**THE COMPLETE CHAIN, SORTED BY PROVENANCE AND BY STRENGTH OF CONCLUSION**

# CONSOLIDATED_THEOREM_AND_DEPENDENCIES.md

Phase 13 / item 1. The established theorem is the **rational-intercept** case (Phase 12); Phase 13
extends it to algebraic intercepts (`ALGEBRAIC_INTERCEPT_THEOREM.md`). This file consolidates the
chain for the established case and states which links the extension changes.

## 1. The consolidated statement

> **THEOREM (consolidated).** Let `α ∈ (0,1)` be a quadratic irrational, `ρ ∈ ℚ`, `β = ln2/ln3`,
> `χ = 1_{[0,β)}`, `s_n = χ({nα+ρ})`. Then `s` is aperiodic, has ones-density exactly `β`, has
> `p_s(n) = 2n`, and `Φ(s) ∉ ℚ`.
>
> **Extension (Phase 13):** the same holds for every **real algebraic** `ρ`, and — via the arc
> identity `1_{[u,u+β)}(x) = 1_{[0,β)}(\{x−u\})` — for the interval `[u,u+β)` whenever `ρ−u` is
> algebraic, `ρ` and `u` themselves being unrestricted.

## 2. Chain diagram

```
   COMBINATORIAL                   ANALYTIC                        ARITHMETIC
   -------------                   --------                        ----------
 [S6] Rote / Berstel-Vuillon    [S3] Lagrange, Perron:          [S1] Bernstein-Lagarias:
      p(n) = 2n  (coverage           quadratic a  =>  a_i <= A        v2(Phi(a)-Phi(b)) = lcp
      claim only)                    q_{k+1} <= (A+1) q_k            Phi . S = T . Phi
 |                            1/(q_{k+1}+q_k) < ||q_k a||   [S2] Phi(W^inf) = c_W/(2^l-3^k)
 [M1] M(d) = two arcs                               < 1/q_{k+1} |
      needs |d| <= min(b,1-b) |                        [A1] S(W) = lcp - log2 F(W)
 [M2] signed rule: 0 in M(d)     ARC AT 0                        [A2] limsup S = +inf => Phi not in Q
      iff d < 0                  [M9] rational r: ||ma+r||       [A4] fine print: delta_W odd,
 [M3] two-ball relaxation              > 1/((A+2)q^2 m)                M_n != 0, cancellation,
      (unconditional)            [M13] algebraic r: Liouville          no ceilings
 [M8] L(l) - l = m*(l) ||ma+r|| >= c m^{-D^2}     [A3] discrepancy uniform in r
      (mechanism = [S8])         [M14] exact hits classified      [S5] Kuipers-Niederreiter
 |                              (unique index m0)               Ch.2 Thm 3.4
 |                        ARC AT BETA                      [A5] beta log2(3) = 1  =>  (H)
 |                        [S7] Gelfond-Schneider:               S >= (L-l) - C log2 l - C0
 |                              beta transcendental |
 |                        [M4] A_m > beta - 1/2 > 0 |
 |                        [M5] deg A_m <= D, H = O(m^D) |
 |                        [S4] BAKER (III Thm 2, or I Thm 1.1) |
 |                        [S9] Waldschmidt Thm 10.1 (explicit) |
 | | |
        +---------> [M6] log l(M) = O((log M)^k),  [M7] l(M) -> inf <-----+
 |
                    [M12/M15] L(l(M)) - l(M) >= M   =>   S -> +inf   =>   Phi(s) not in Q
```

## 3. Published source theorems — cited, not proved here

| id | statement | source | new in 13? |
|---|---|---|---|
| **S1** | `v₂(Φ(a)−Φ(b)) = lcp(a,b)`; `Φ` a homeomorphism with `Φ∘S = T∘Φ` | Bernstein & Lagarias, *The 3x+1 conjugacy map*, **Canad. J. Math. 48 (1996) 1154–1169**; foundation Prop. 2.2 | — |
| **S2** | `Φ(W^∞) = c_W/(2^ℓ−3^k)`, `c_W = Σ_{i<ℓ,W_i=1}3^{k−k_{i+1}}2^i` | foundation Prop. 4.1 (re-derived and checked mod `2^60` in Phase 12) | — |
| **S3** | quadratic ⟹ eventually periodic CF ⟹ bounded partial quotients; the two-sided convergent estimate | Lagrange; Perron, classical | — |
| **S4** | `|β₁logα₁+⋯+βₙlogαₙ| > C e^{−(log B)^κ}`, algebraic `β_j`, `C` effective | **Baker, Mathematika 14 (1967), Part III, Thm 2** (= MR0220680 Thm 3.2); or **Part I, Thm 1.1** (`κ>n+1`, uniform over degree `≤ d`) | Part I now preferred for `D > 2` |
| **S5** | `N·D_N ≤ c₁'Σ_{i≤k+1}a_i + c₂'` | Kuipers & Niederreiter, *Uniform Distribution of Sequences*, Ch. 2 Thm 3.4 | — |
| **S6** | two-interval rotation coding has `p(n)=2n` iff the endpoint `∉ ℤα+ℤ` | Rote, **J. Number Th. 46 (1994) 196–213**; Berstel & Vuillon, arXiv:math/0106217 | — |
| **S7** | `log₃2` transcendental | Gelfond–Schneider | — |
| **S8** | the **hitting-time mechanism** | **foundation paper §12 open problem (1)** — the author's own proposal | — |
| **S9** | explicit algebraic-coefficient measure, `exp(−(50m)^{3m}D^{m+2}(log B)²∏log A_i)` | **Waldschmidt**, *Linear independence of logarithms of algebraic numbers*, **Thm 10.1**; book: *Diophantine Approximation on Linear Algebraic Groups*, Grundlehren 326 (2000) | **new in 13** |
| **S10** | Liouville's inequality: `θ ≠ 0` algebraic of degree `≤ D`, height `H` ⟹ `|θ| ≥ (1+H)^{−D}` | classical | **new in 13** |

**Self-citation notice.** S2, S6-as-used, S8 and the `Cor. 9.3 / Thm 10.1` coverage results come from
the foundation paper, which is by the author of this programme and is a **preprint, not refereed**.
Every use is so flagged.

## 4. Adaptations proved here

| id | adaptation | of |
|---|---|---|
| **A1** | the surplus invariant `S(W) = lcp(s,W^∞) − log₂F(W)`, `F(W) = |2^ℓ−3^k| + c_W` (proof-native packaging) | S1+S2 |
| **A2** | the criterion in Sturmian-free form, with `limsup` shown to be exactly the right hypothesis | A1 |
| **A3** | the discrepancy bound made **uniform in the intercept** (shift the orbit = shift the interval; extreme discrepancy bounds every interval at once; a shift costs a factor 2) — *this is what lets `ρ` be arbitrary* | S5 |
| **A4** | the criterion's fine print discharged: `δ_W ≠ 0` and odd, `M_n ≠ 0`, cancellation irrelevant, no ceilings in the proof | A2 |
| **A5** | `β·log₂3 = 1` turned into `(H)`: `S ≥ (L−ℓ) − C log₂ℓ − C₀` with `C, C₀` depending on `α` alone | A1+A3 |

## 5. Mechanism results proved in this programme

| id | statement | status | origin |
|---|---|---|---|
| **M1** | `M(δ)` = the two explicit arcs **iff** `|δ| ≤ min(β,1−β)` | PROVED; hypothesis was unstated before 11B | 11B |
| **M2** | signed rule `0 ∈ M(δ) ⟺ δ < 0` under M1 | PROVED | 12 |
| **M3** | `M(δ) ⊆ B(0,|δ|) ∪ B(β,|δ|)`, unconditional | PROVED | 11 |
| **M4** | `A_m > β − 1/2 > 0` always — one line, every `α`, every `ρ`, every `m` | PROVED | 12 |
| **M5** | `deg A_m ≤ D`, `H(A_m) = O(m^D)`, `D = [ℚ(α,ρ):ℚ]` | PROVED | 11B (`D=2`), generalised 13 |
| **M6** | `log ℓ(M) = O((log(M+2))^κ)` | PROVED | 11B |
| **M7** | `ℓ(M) → ∞` | PROVED | 11B |
| **M8** | `L(ℓ) − ℓ = m*(ℓ)` | PROVED; *idea* is S8 | 11 |
| **M9** | `‖mα+p/q‖ > 1/((A+2)q²m)` — rationality of `ρ` essential | PROVED | 11 (`K=147`), generalised 12 |
| **M10** | `ρ = 0` needs no shift, only the signed relaxation and `δ>0` convergents | PROVED | 12 |
| **M11** | `Φ(s) ∉ ℚ` for the named word | PROVED | 11, rebuilt 12 |
| **M12** | `Φ(s) ∉ ℚ`, every quadratic `α`, every rational `ρ` | PROVED | 12 |
| **M13** | `‖mα+ρ‖ ≥ c_L m^{−D²}` for algebraic `ρ` — **Liouville, no transcendence input** | PROVED | **13** |
| **M14** | exact `0`-hits: `ρ ∈ ℤα+ℤ`, unique index `m₀`, any value; two independent treatments | PROVED | **13** |
| **M15** | `Φ(s) ∉ ℚ`, every quadratic `α`, every **algebraic** `ρ`; and `[u,u+β)` whenever `ρ−u` is algebraic | PROVED | **13** |

**Withdrawn and staying withdrawn:** `c_m ≥ C₂m^{−κ}` (Phase 11 R4); `ℓ(M) = O(M^κ)` (Phase 11 R5);
the *asymptotic* use of the measured constants `0.41`, `2.02`; Phase 12's hope that fixed degree might
yield a polynomial logarithmic-form bound (see `EXPLICIT_CONSTANTS_STATUS.md` §4); Phase 12's one-line
dismissal of the Ridout route (see `FAMILY_THEOREM_PRIOR_COVERAGE.md` §5).

## 6. Qualitative conclusions, separated

| conclusion | strength | status |
|---|---|---|
| `Φ(s) ∉ ℚ` for the family | qualitative | **PROVED** |
| `Φ(s)` irrational **and** transcendental | strictly stronger | **OPEN.** Would follow from Ridout if `m*(ℓ)/ℓ > 1+ε` infinitely often; measured at 7/20 convergents, not proved |
| an irrationality **measure** for `Φ(s)` | strictly stronger | **OPEN** — foundation problem (2); our witnesses bound only the approximants `Φ(W_n^∞)`, not every rational |
| the Periodicity Conjecture for all `p(L) ≤ 2L` | strictly stronger | **OPEN** — foundation problem (4); ours is a two-parameter family inside it |
| the Periodicity Conjecture | strictly stronger | untouched |
| the Collatz conjecture | unrelated | untouched |

## 7. Quantitative height bounds, separated from the qualitative conclusion

For any rational `u/v = Φ(s)` in lowest terms with `H = max(|u|,v)`, the chain gives
`2^{L} ≤ H·F(W)`, i.e. `H ≥ 2^{S}` at each witness. Two regimes, and they must not be conflated:

- **finite certificates** — exact integer comparisons, **no analytic input at all**;
- **the asymptotic floor** `S ≥ M − O((log M)^κ) − C₀` — Baker-dependent.

**Novelty of the quantitative content.** Not covered by T1/T2 (contradiction arguments bound
nothing). But producing effective height floors by this bridge is **the foundation paper's own
claimed contribution** (Cor. 6.2, Cor. 8.7, and its credit paragraph: "what Theorem 8.5 adds there is
the effective height bound of Corollary 8.7, which a density argument does not give"). So these are
**new instances of an existing method**, not a new kind of result.

## 8. Finite certificates — the numbers

Named word (Phase 11, reproduced independently in Phase 12):

```
ell = 377   L = 846     H >= 2^462
ell = 610   L = 1456    H >= 2^838
ell = 1597  L = 2478    H >= 2^872
ell = 2584  L = 5062    H >= 2^2469
ell = 6765  L = 22773   H >= 2^15998        (a 4816-digit lower bound)
```

Rational-intercept family (Phase 12, `M = 32`): `2^140 … 2^8069` over 10 `(α,ρ)` pairs.
Algebraic-intercept family (Phase 13, `M = 32`): `2^67 … 2^598` over 7 cases, `D = 2,4,6`.

## 9. Effectively computable versus numerically supplied — the ledger

| constant | role | effective in principle | numerically supplied |
|---|---|---|---|
| the finite certificates above | height floors at the computed witnesses | — (no constant) | **yes, exactly** |
| `K = (A+2)q²` (arc at `0`, rational `ρ`) | `t₀ > 1/(K|δ|)` | yes | **yes** (`147` for the named word) |
| `c_L, D` (arc at `0`, algebraic `ρ`) | `‖mα+ρ‖ ≥ c_L m^{−D²}` | yes | **yes in principle, computable from `α, ρ` by Liouville**; computed per case in the data files |
| `c₁` (arc at `β`) | `c_m ≥ exp(−c₁(log(m+2))^κ)` | yes | **yes — new in Phase 13**, `c₁ ≈ 2.39·10^13` at `D = 2` via Waldschmidt Thm 10.1. See `EXPLICIT_CONSTANTS_STATUS.md` |
| `C, C₀` (drift/discrepancy) | `S ≥ (L−ℓ) − C log₂ℓ − C₀` | yes | **no** — requires the Kuipers–Niederreiter constants `c₁', c₂'`, not evaluated |

> **So the honest statement is: the analytic side is now numerically explicit; the arithmetic side is
> not.** One constant (`C, C₀`) stands between Theorem 12 and a fully numerical `H ≥ 2^{f(M)}` at
> every `M`. Phases 11–12 said "effective" without this line; Phase 12 introduced the *in
> principle / supplied* distinction; Phase 13 discharges the harder half of it.

## 10. What Phase 13's extension changes in the chain

Only three links: **M9 → M13** (Liouville replaces the `‖qx‖/q` trick), **M10 → M14** (the exact hit
may sit at any index, not only `m = 0`), and **M5** acquires the dependence `H(A_m) = O(m^{D})`,
`D = [ℚ(α,ρ):ℚ]`, with `S4` taken in the Part I form so that one constant serves all degrees `≤ D`.
Everything else — the combinatorial layer, the arithmetic layer, the discrepancy layer — is
**untouched and intercept-free**, which is why the extension costs so little.
