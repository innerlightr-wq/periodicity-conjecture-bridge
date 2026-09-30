**THE LADDER, REBUILT ON THE RIGHT COORDINATES: (LOWER ONES-DENSITY, COMPLEXITY)**

# DENSITY_COMPLEXITY_LADDER.md

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

## 1. The four load-bearing results, with exact hypotheses

Notation: `v ∈ {0,1}^ℕ` a parity word; `k_n(v) = |v[0:n]|_1`; `p_v(L)` the factor complexity;
`β := ln2/ln3 = log₃2 = 1/log₂3 = 0.6309297535714574…`, **transcendental** (Gelfond–Schneider:
`3^β = 2` is algebraic, so `β` cannot be algebraic irrational, and it is not rational since
`3^p = 2^q` is impossible). `Φ` is the Bernstein–Lagarias conjugacy map, parity word `↦` 2-adic
integer. Note `β·log₂3 = 1` exactly — that identity is what "critical" means.

| # | result | exact hypothesis | conclusion | status |
|---|---|---|---|---|
| **T1** | **Monks–Yazinski**, *The autoconjugacy of the 3x+1 function*, **Discrete Math. 275 (2004) 219–236, Thm 2.7(b)** | `x ∈ ℚ_odd` with **divergent** orbit | `ln2/ln3 ≤ liminf_n κ_n(x)/n` | **refereed** |
| | *contrapositive used here* | `v` aperiodic, `liminf k_n(v)/n < β` | `Φ(v) ∉ ℚ` | — |
| **T2** | **López–Stoll**, *The 3x+1 periodicity conjecture in ℝ*, **arXiv:2101.12747 (2021), Thm 1** | `v` aperiodic, lower ones-density **`> β`** | `Φ(v) ∉ ℚ` | **preprint** |
| **T3** | **Dubickas transported** — foundation paper **Cor. 9.3** (after Dubickas, *Glasgow Math. J.* 51 (2009), Thm 5) | `s` not eventually periodic, `liminf_L p_s(L)/L < 1/λ = 1.70951129…` | `Φ(s) ∉ ℚ` | unpublished ms. (Dubickas's own theorem is refereed) |
| **T4** | **Foundation paper, Thm 10.1** | `γ` irrational, `ρ ∈ [0,1)`, `s` **either mechanical word** of slope `γ`, intercept `ρ` (so `p_s(n) = n+1`) | `Φ(s) ∉ ℚ` | unpublished ms. |

`ℚ ∩ ℤ₂ = ℚ_odd`, and `v` is eventually periodic iff the orbit of `Φ(v)` is eventually cyclic — so
T1's dichotomy (eventually cyclic **or** divergent, for `x ∈ ℚ_odd`) is exhaustive.

## 2. The covered region of the plane

Plot a word by `(d, c) :=` (lower ones-density, `liminf p(L)/L`).

```
                 c = liminf p(L)/L
   2n  --|--------------------------------------------------------
         |  T1 covers      |  ###############  |  T2 covers
         |  (refereed)     |  ## UNCOVERED ##  |  (preprint)
1.70951--|-----------------|-------------------|------------------
         |  T3 covers everything below this line, at every density
         |  (and T4 covers the whole line c = 1, i.e. all Sturmian words)
      1  --|-------------|-----------------|--------------------
            0          d < beta        d = beta        d > beta      1
```

Two facts make the picture sharp:

- **Horizontally**, T1 ∪ T2 cover every density except exactly `β`. A single point — but `β` is
  where `2^ℓ = 3^k` and the arithmetic height degenerates, so it is the only place the density
  argument can fail and the only place a genuinely different mechanism is needed.
- **Vertically**, T3 covers everything below `1.70951…`, and T4 covers the whole complexity-`(n+1)`
  line including at `d = β`.

**The uncovered region is therefore a single vertical ray: `d = β` exactly, `c ≥ 1.70951…`.**

## 3. Every existing rung, classified

Categories as required: **(A)** already-covered conclusion, **(B)** independent proof of a covered
conclusion, **(C)** quantitative refinement of the mechanism, **(D)** genuinely uncovered extension.

| rung / result | `(d, c)` | category | covered by |
|---|---|---|---|
| Foundation Thm 6.1 / 8.5 (`1c_γ`, all irrational `γ`) | `(γ, 1)` | **B** for `γ ≠ β`; **D** for `γ = β` | T1/T2 off `β`; nothing at `β` |
| Foundation Thm 10.1 (all Sturmian, every intercept) | `(γ, 1)` | **B** for `γ ≠ β`; **D** for `γ = β` | same |
| Foundation Cor. 9.3 (counting) | any `d`, `c < 1.70951` | **C** — a different *mechanism* covering a region T1/T2 also cover | T1/T2 |
| Phase 1–2 abstract bridge / surplus criterion | — | **C** (a mechanism, not a class) | — |
| Phase 2 Rote irrationality, 5 quadratic slopes | `(1/2, 2)` | **A/B** | T1 |
| Phase 4 quadratic CS Rote | `(1/2, 2)` | **A/B** | T1 |
| Phase 6 bounded-type CS Rote, intercept `0` | `(1/2, 2)` | **A/B** | T1 |
| Phase 8 Thm 2, CS Rote every intercept | `(1/2, 2)` | **A/B** | T1 |
| Phase 9 Thm 3, CS Rote unbounded type | `(1/2, 2)` | **A/B** | T1 |
| Phase 9 Cor. 4.1, Thue–Morse | `(1/2, 10/3)` | **A/B** | T1 |
| Phase 9 Cor. 4.2, 21 substitution fixed points | rational `d`, various `c` | **A/B** (15 via T1, 4 via T2) | T1/T2 |
| Phase 9 Thm 4, the `g(γ)` threshold | — | **C** (refines Phase 1's *unconditional* theorem) | — |
| Phase 1–2 rotation coding at interval length `1/3` | `(1/3, 2)` | **A/B** | T1 |
| Phase 8 driver identity, attainment routing; Phase 9 weight law | — | **C** (exact structure of the mechanism) | — |
| **Phase 10 target (§ `CRITICAL_DENSITY_TARGET.md`)** | **`(β, 2)`** | **D — genuinely uncovered** | **nothing** |

Every **(A/B)** row is a *correct proof* of a conclusion already available. Nothing is discarded:
the proofs, the computational records and the (C) structural results stand, and the (C) results are
the part of this programme that is about the mechanism rather than the class.

## 3b. A third axis: qualitative versus quantitative

Coverage above is about the **qualitative** conclusion `Φ(v) ∉ ℚ`. T1 and T2 supply only that: both
proofs are contradiction arguments (T1 a limiting argument over `m → ∞`, T2 an accumulation-point
argument) and neither bounds the height of a hypothetical rational value. The bridge additionally
supplies an **effective height floor** `H ≥ 2^{S_n}`, explicit and unbounded. So each **(B)** row of
`PRIOR_RESULT_COVERAGE.md` is simultaneously a **(Q)** row: covered qualitatively, not covered
quantitatively. The caveat that keeps this honest: the foundation paper already claims "the height
floors" and "the independent effective Liouville proof" as its own novelty, so the **(Q)** content of
Phases 2–9 is *new instances of an already-claimed method*, not a new method.

## 4. Why the complexity axis was the wrong coordinate

The programme's framing — "crossing the counting frontier at `p(n) = 2n`" — compares only against
**T3**. But T3 is not the binding constraint: T1/T2 cover *every* complexity at *every* density
except `β`. Moving from `p(n) = n+1` to `p(n) = 2n` at a fixed density `1/2` therefore buys nothing,
which is exactly what `PRIOR_RESULT_SUBSUMPTION.md` documents. **The only direction that leaves the
covered region is horizontal: move the density to `β`.** Complexity then matters only to stay above
T3's line and off T4's line.
