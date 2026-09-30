**THE WHOLE OF THEOREM 12, SORTED BY WHO PROVED IT**

# CLAIM_AND_DEPENDENCY_LEDGER.md

Phase 12 / item 4. Five columns of provenance, kept strictly apart. Every row is a link in
`QUADRATIC_RATIONAL_INTERCEPT_THEOREM.md`. Nothing here claims novelty; §6 states what is and is not
settled.

## 1. Dependency diagram

```
                     THEOREM 12:  Phi(s) not in Q
                 s_n = 1 <=> {n a + r} in [0, beta),  a quadratic, r rational
 |
        +-----------------------------+-----------------------------+
 | | |
   COMBINATORIAL                 ANALYTIC                     ARITHMETIC
 | | |
  (P4) mismatch set            (P6) arc at 0                (P11) 2^L <= H F(W)
   M(d) = 2 arcs ||n a|| > 1/((A+2)n)          [S1] isometry
   [M1] no-wrap |d| <= .369     [S3] bounded p.q. (a quad)   [S2] periodic formula
   [M2] signed rule 0 in M |                        [A4] criterion, all
 |                      (P7) arc at beta                  subtleties resolved
  (P5) relaxation | |
   [M3] two-sided                 c_m >= exp(-c1 (log m)^k)  (P10) drift/discrepancy
   [M2] one-sided (r=0) |                         [S5] Kuipers-Niederreiter
 |                     [S4] BAKER III Thm 2                Ch.2 Thm 3.4
  (P1)(P2)(P3)                [M4] A_m > beta - 1/2 > 0       [A3] uniform in rho
   [S6] Rote/Berstel-Vuillon  [M5] H(A_m) = O(m^2), d = 2 |
   (complexity 2n; coverage    (P8) witnesses |
    claim only)                [M6] log ell(M) = O((log M)^k) |
                               [M7] ell(M) > q^2 M -> infinity |
 | |
                                     +------> (P9) L - ell >= M <--+
```

`[S*]` = established source result. `[A*]` = this repository's adaptation of one. `[M*]` = mechanism
result proved here. Quantitative outputs and the qualitative conclusion are §4 and §5.

## 2. Established source results — cited, not proved here

| id | result | exact source | used for |
|---|---|---|---|
| **S1** | `v₂(Φ(a)−Φ(b)) = lcp(a,b)`; `Φ` a homeomorphism `{0,1}^ℕ → ℤ₂` with `Φ∘S = T∘Φ` | Bernstein–Lagarias; foundation paper Prop. 2.2 | the valuation step |
| **S2** | `Φ(W^∞) = c_W/(2^ℓ−3^k)`, `c_W = Σ_{i<ℓ,W_i=1}3^{k−k_{i+1}}2^i` | foundation paper Prop. 4.1 | the approximants (re-derived in Phase 12 §6 of the audit, and checked mod `2^60`) |
| **S3** | a quadratic irrational has an eventually periodic continued fraction, hence bounded partial quotients `a_i ≤ A`; and `1/(q_{k+1}+q_k) < ‖q_kα‖ < 1/q_{k+1}` | classical (Lagrange; Perron) | `‖nα‖ > 1/((A+2)n)`, `q_{k+1} ≤ (A+1)q_k`, witness sizing |
| **S4** | `|β₁logα₁+⋯+βₙlogαₙ| > C e^{−(log B)^κ}`, `κ > n`, `C = C(n,α₁,…,αₙ,κ,d)` effective, **either** family `ℚ`-independent, all `α_i, β_j` non-zero | **Baker, *Linear forms in the logarithms of algebraic numbers III*, Mathematika 14 (1967), Theorem 2** (= MR's Thm 3.2). Fallbacks: Part I Thm 1.1 (`κ>n+1`), Part II Thm 2.2 (`κ>2n+1`) | the lower bound on `c_m` |
| **S5** | `N·D_N ≤ c₁'Σ_{i≤k+1}a_i + c₂'` for `q_k ≤ N` | Kuipers–Niederreiter, *Uniform Distribution of Sequences*, Ch. 2 Thm 3.4 | drift and discrepancy |
| **S6** | two-interval coding of an irrational rotation has `p(n) = 2n` iff the endpoint `∉ ℤα+ℤ` | Rote, J. Number Th. **46** (1994) 196–213; Berstel–Vuillon, arXiv:math/0106217 | the complexity value — **coverage claim only** |
| **S7** | `log₃2` is transcendental | Gelfond–Schneider | `β ∉ ℤα+ℤ`; the `β`-boundary is never hit; `Λ_m ≠ 0` |
| **S8** | the **hitting-time mechanism**: "the first entry time of the orbit `{jγ+ρ}` into an interval of length `jD_n` at the partition endpoint" | **foundation paper, §12 open problem (1)** — the author's own proposal | the shape of (P4)/(P9) |

**S8 must stay in this column.** The idea that the agreement excess is a first entry time is the
foundation paper's, stated there as the route to a general-intercept depth law. Phase 11 executed it
in a different setting; it did not invent it.

## 3. This repository's adaptations of source results

| id | adaptation | of | where |
|---|---|---|---|
| **A1** | the surplus invariant `S(W) = lcp(s,W^∞) − log₂F(W)`, `F(W) = |2^ℓ−3^k| + c_W` (the proof-native packaging, never worse than `max(2^ℓ,3^k)+c_W`) | S1 + S2 | `theorems/phase1/`, `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` |
| **A2** | the criterion in Sturmian-free form: `limsup S = +∞ ⟹ Φ(s) ∉ ℚ`, with `limsup` shown to be exactly the right hypothesis | A1 | `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` |
| **A3** | the discrepancy bound made **uniform in the intercept** (shifting the orbit = shifting the interval; the *extreme* discrepancy bounds every interval at once; a shift costs a factor 2) | S5 | Phase 10 Lemma D; re-verified Phase 12 (G) |
| **A4** | the criterion's fine print discharged: zero denominators, oddness of `δ_W`, `M_n ≠ 0`, cancellation irrelevance, no ceilings in the proof | A2 | `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` |
| **A5** | `β·log₂3 = 1` used to turn the drift into the `(H)` inequality `S ≥ (L−ℓ) − C log₂ℓ − C₀` | A1 + A3 | Phase 11 `EXACT_HEIGHT_AND_SURPLUS.md`, corrected Phase 11B |

## 4. Mechanism results proved here

| id | statement | status | first proved | audited |
|---|---|---|---|---|
| **M1** | `M(δ)` equals the two explicit arcs **iff** `|δ| ≤ min(β,1−β) = 0.3690702464`; outside that it is wrong | **PROVED**; hypothesis was unstated in Phase 11 | Phase 11B | Phase 12, independent code: 0 / 39 disagreements inside / outside |
| **M2** | signed rule: under M1, `0 ∈ M(δ) ⟺ δ < 0`; and for `δ > 0`, `M(δ) = [β−δ,β) ∪ [1−δ,1)` | **PROVED** | **Phase 12** | 0 violations, 50 shifts |
| **M3** | `M(δ) ⊆ B(0,|δ|) ∪ B(β,|δ|)`, **unconditional** (survives the wrap) | **PROVED** | Phase 11 (R2) | Phase 11B + 12, 0 violations incl. `q=1` |
| **M4** | `A_m > β − 1/2 > 0` for every `m ≥ 0`, every quadratic `α`, every rational `ρ` — one line, no case analysis | **PROVED** | **Phase 12** | 25 `(α,ρ)` × `m ≤ 3000` |
| **M5** | `A_m = (a_m+b_m√D)/(wq)` with `|a_m|,|b_m| = O(m)`; `d = 2` for `m ≥ 1`; `H(A_m) = O(m²)` | **PROVED** | Phase 11B (`ρ=1/7`) | Phase 12 generalizes and verifies |
| **M6** | `log ℓ(M) = O((log(M+2))^κ)` from the stretched-exponential bound | **PROVED** | Phase 11B | Phase 12 |
| **M7** | `ℓ(M) > q²M → ∞`, so the witnesses grow | **PROVED** | Phase 11B (`49M`) | Phase 12 generalizes |
| **M8** | `L(ℓ) − ℓ = m*(ℓ)` (agreement excess = first hitting time) | **PROVED**; the *idea* is S8 | Phase 11 (R1) | Phase 12, three independent routes |
| **M9** | `‖mα+p/q‖ > 1/((A+2)q²m)`; the rationality of `ρ` is essential | **PROVED** | Phase 11 (R3, `K=147`) | Phase 12 generalizes to `K=(A+2)q²`, 25 cases |
| **M10** | `ρ = 0` needs no finite shift and no separate argument — only M2 plus the `δ>0` convergents | **PROVED** | **Phase 12** | 5 slopes |
| **M11** | `Φ(s) ∉ ℚ` for the named word | **PROVED** | Phase 11 | Phase 12 rebuilt from definitions |
| **M12** | `Φ(s) ∉ ℚ` for every quadratic `α`, every rational `ρ` | **PROVED** | **Phase 12** | 50 end-to-end rows |

**Withdrawn, and to stay withdrawn:** `c_m ≥ C₂m^{−κ}` (Phase 11 R4) — the source gives no polynomial
bound; `ℓ(M) = O(M^κ)` (Phase 11 R5); and the *asymptotic* use of the measured constants `0.41`,
`2.02`.

## 5. Quantitative applications, separated from the qualitative conclusion

**Quantitative — Baker-free, exactly supplied.** Height floors `H ≥ 2^S` from the integer comparison
`2^L > F(W)·2^S`, for any rational `u/v = Φ(s)` with `H = max(|u|,v)`:

```
named word:  H >= 2^462, 2^838, 2^872, 2^2469, 2^15998   (ell = 377, 610, 1597, 2584, 6765)
family:      H >= 2^140 ... 2^8069                       (10 (alpha,rho) pairs, ell <= 3927)
```

**Novelty of the quantitative content — the Phase 10 finding, unchanged.** These floors are not
covered by T1/T2, which are contradiction arguments and bound nothing. But producing effective height
floors by this bridge is **the foundation paper's own claimed contribution** (its Cor. 6.2, Cor. 8.7,
and the credit paragraph: "what Theorem 8.5 adds there is the effective height bound of Corollary 8.7,
which a density argument does not give"). So the floors above are a **new instance of an existing
method**, not a new method. Do not present them as a new kind of result.

**Qualitative — potentially new.** The conclusion `Φ(s) ∉ ℚ` for an aperiodic `s` of lower ones-density
exactly `β` and factor complexity `2n`. `CRITICAL_ROTATION_PRIOR_RESULTS.md` places this as
**(d) an application not located in the searched literature**, with the standing caveat that a
negative search is not a proof of absence.

## 6. What is settled and what is not

| question | answer |
|---|---|
| Is Theorem 12 proved? | **Yes**, modulo S1–S8, all published |
| Is it effective? | Effective **in principle** (Baker's `C` and KN's `c₁',c₂'` are computable); **not numerically explicit**. The finite floors of §5 are explicit and Baker-free |
| Is it new? | **Unresolved**, and deliberately left so. Nothing located covers it; that is not proof |
| Does it bear on the Periodicity Conjecture? | It proves the conjecture **for this family only**. The family is a two-parameter set of measure zero in `{0,1}^ℕ` |
| Does it bear on the Collatz conjecture, or on divergent orbits of positive integers? | **No.** Nothing here concerns integer seeds |
| Does it answer the foundation paper's open problem (4)? | **No.** Problem (4) quantifies over all `s` with `p_s(L) ≤ 2L`; this is one two-parameter family within that class |
