**COVERAGE LEDGER — QUALITATIVE CONCLUSIONS COVERED, QUANTITATIVE CONTENT NOT (AND NOT NEW AS A METHOD)**

# PRIOR_RESULT_COVERAGE.md

> **WORDING CLARIFICATION (documentation pass).** Where this file describes **López & Stoll**,
> *The 3x+1 periodicity conjecture in ℝ*, arXiv:2101.12747 (2021), Theorem 1, the current-facing
> statement of this repository is the neutral one: *López–Stoll propose an upper-density exclusion. We
> do not rely on that result; the conclusions developed here follow from the independent arguments
> stated in this repository.* We have **neither established nor disproved** their theorem and take no
> position on it. The sharper language retained below is the **audit record** — it preserves a
> technical observation raised by a third party (`innerlightr-wq/eoc-divergence` issue #30, open at the
> time of writing) together with its source reference and its verification status, namely **not
> verified by us and not a result of this repository**. It is kept, not rewritten, because research
> history should not be edited after the fact; it should not be quoted as a claim. No conclusion in
> this repository depends on López–Stoll in either direction. Canonical wording:
> [`docs/DEPENDENCE_ON_PRIOR_RESULTS.md`](../../docs/DEPENDENCE_ON_PRIOR_RESULTS.md).

> **CORRECTION (Phase 12).** T2 below is recorded as "preprint". That caveat is too weak: an open, uncontested third-party issue (`innerlightr-wq/eoc-divergence` #30) identifies the step carrying López–Stoll Theorem 1 — from "`Φ_ℝ(v)` irrational" to "`Φ(v)` aperiodic", via an alleged 2-adic expansion of a real irrational — and argues it does not follow. **The securely covered density region is therefore `liminf < β` (Monks–Yazinski 2004, refereed), not `liminf ≠ β`**, and "only density exactly `β` is uncovered" should read "only density at or above `β` is securely uncovered". No verdict about the Phase 11/12 words changes. See [`theorems/phase12/CRITICAL_ROTATION_PRIOR_RESULTS.md`](../phase12/CRITICAL_ROTATION_PRIOR_RESULTS.md) §3.


Supersedes and absorbs `PRIOR_RESULT_SUBSUMPTION.md` (retained unchanged as the historical record of
the first pass). New in this document: the **qualitative / quantitative split** of item 2, which the
first pass did not perform.

## 1. The four prior results, read first-hand

| | source | exact hypothesis | conclusion | status |
|---|---|---|---|---|
| **T1** | Monks–Yazinski, *The autoconjugacy of the 3x+1 function*, **Discrete Math. 275 (2004) 219–236**, Thm 2.7(b) | `x ∈ ℚ_odd`, orbit **divergent** | `ln2/ln3 ≤ liminf_n κ_n(x)/n` | **refereed** |
| **T2** | López–Stoll, *The 3x+1 periodicity conjecture in ℝ*, **arXiv:2101.12747 (2021)**, Thm 1 | `ζ ∈ ℚ_odd`, trajectory divergent | `lim h/ℓ = ln2/ln3`; the usable half is: `v` aperiodic with lower ones-density `> β` `⟹` `Φ(v) ∉ ℚ` | **preprint** |
| **T3** | Dubickas, *Glasgow Math. J.* **51** (2009) Thm 5, **transported** in foundation paper Cor. 9.3 (Lemma 9.1: `T` preserves a fixed odd denominator) | `s` not eventually periodic, `liminf_L p_s(L)/L < 1/log₂(3/2) = 1.70951129…` | `Φ(s) ∉ ℚ` | Dubickas refereed; the transport is a **proved adaptation** in an unpublished ms. |
| **T4** | Foundation paper Thm 10.1 | `γ` irrational, `ρ ∈ [0,1)`, `s` **either** mechanical word of slope `γ`, intercept `ρ` | `Φ(s) ∉ ℚ`, **with** the explicit inequality `c(γ)ℓ ≤ log₂H + log₂(2+3ℓ) + log₂3` | unpublished ms. |

`ℚ ∩ ℤ₂ = ℚ_odd`; `v` eventually periodic `⟺` the orbit of `Φ(v)` is eventually cyclic; for
`x ∈ ℚ_odd` the orbit is eventually cyclic **or** divergent, so T1's dichotomy is exhaustive. Hence
the usable form of T1 is: **`v` aperiodic with `liminf k_n(v)/n < β` `⟹` `Φ(v) ∉ ℚ`**, and this
deduction is written out verbatim in the foundation paper §8.

## 2. The qualitative / quantitative split — the new finding

**T1 and T2 are purely qualitative. Neither yields any bound on the height of a hypothetical
rational value.** Established by reading both proofs:

- **T1.** Their §4.1 fixes `m ∈ ℕ⁺`, invokes Lemma 3.2 ("only finitely many orbit elements lie
  below `m`") to pass to a tail, applies Lemma 4.2's bound `ln2/(ln3 + 1/m) ≤ liminf κ_n/n`, and
  then lets `m → ∞`. The number of discarded terms depends on the unknown `x`. Given an aperiodic
  `v` of density `< β` one obtains a **contradiction**, not a lower bound on `H`.
- **T2.** The above-`β` half concludes "the orbit of `Φ_ℝ(v)` has accumulation points by Lemma 26,
  which implies `Φ_ℝ(v) ∉ ℚ_odd`" — a compactness argument. Again a contradiction, no bound.

**The bridge is quantitative.** `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` derives, for
every candidate root and any hypothetical `Φ(s) = u/v` with `H = max(|u|,v)`,

```
2^{L_n}  <=  H * F(W_n) ,      hence     H  >=  2^{S_n},   S_n = L_n - log2 F(W_n) .
```

Explicit, computable, unbounded. For Thue–Morse (`scripts/phase10b/quantitative_gap.py`):

```
ell      L       S_n      height floor          decimal digits of the floor
 24      40      14.73    H >= 2^14.7                    4
 96     160      62.68    H >= 2^62.7                   19
384     640     254.68    H >= 2^254.7                  77
768    1280     510.67    H >= 2^510.7                 154
```

certified by the integer comparison `2^L > F`. T1 gives nothing of this kind for Thue–Morse.

**But the method is not new either.** The foundation paper's own abstract claims as new "the exact
depth law; **the height floors**; and the independent **effective** Liouville proof" — for Sturmian
words. So the quantitative content of Phases 2–9 is **new instances of an already-claimed method**,
not a new method and not a new irrationality result. That is a real but modest contribution, and it
must be stated in exactly those terms.

## 3. The ledger

**(A)** covered conclusion · **(B)** independent proof of a covered conclusion · **(Q)** quantitative
content not supplied by T1/T2, via the foundation paper's already-claimed method · **(C)** refinement
of the mechanism · **(D)** genuinely uncovered

| result | `(density, complexity)` | cat. | covered by |
|---|---|---|---|
| Phase 1/2 abstract criterion, height and repetition bounds, transfer identity, density-`1/2` fact | — | **C** | — |
| Phase 2 Rote irrationality, 5 quadratic slopes | `(1/2, 2)` | **B** + **Q** | T1 |
| Phase 4 quadratic CS Rote | `(1/2, 2)` | **B** + **Q** | T1 |
| Phase 6 bounded-type CS Rote | `(1/2, 2)` | **B** + **Q** | T1 |
| Phase 8 Thm 2, every intercept | `(1/2, 2)` | **B** + **Q** | T1 |
| Phase 9 Thm 3, unbounded type | `(1/2, 2)` | **B** + **Q** | T1 |
| Phase 9 Cor. 4.1, Thue–Morse | `(1/2, 10/3)` | **B** + **Q** | T1 |
| Phase 9 Cor. 4.2, 21 substitution fixed points | rational densities | **B** + **Q** | T1 (15), T2 (4) |
| Phase 9 Thm 4, `g(γ)` threshold | — | **C** | — |
| Phase 1/2 rotation coding, interval `1/3` | `(1/3, 2)` | **B**; its `O(log N)` discrepancy is **C** | T1 |
| Phase 8 driver identity, attainment routing; Phase 9 weight law; Phases 8/9/9B corrections | — | **C** | — |
| Foundation Thms 6.1/8.5/10.1 at `γ ≠ β` | `(γ, 1)` | **B** + **Q** | T1/T2 |
| Foundation Thms 6.1/8.5/10.1 at `γ = β` | `(β, 1)` | **D** | nothing |
| **Phase 10 target `C(α,ρ)`** | **`(β, 2)`** | **D** | **nothing** |

## 4. Coverage check done by implication, not by name

No searched paper names CS Rote sequences, Thue–Morse or two-interval rotation codings in
connection with `Φ`. Coverage was established by **implication**: computing each class's lower
ones-density and applying T1/T2, which read nothing else. That is why the repository's three
prior-art passes — all of which searched for the *mechanism* — missed it.

**Standing gate.** Before claiming novelty for any class: compute its lower ones-density and compare
with `β = 0.6309297535714574`. If it is not exactly `β`, the qualitative conclusion is already
available whatever the complexity; only the quantitative content can be new, and then only as a new
instance of the foundation paper's method.
