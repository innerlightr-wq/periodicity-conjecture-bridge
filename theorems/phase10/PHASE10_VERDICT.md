**ONE UNCOVERED TARGET, WITH ONE PROOF OBLIGATION**

# PHASE10_VERDICT.md

Branch `phase9-unbounded-type`, worked from HEAD `1c365b4`. Nothing pushed, nothing published,
no release rebuilt; `note_rev2.pdf` `8daf1979…` and both `~/Downloads` copies byte-identical.

## 1. The ladder, on the right coordinates

Plotting words by `(lower ones-density, liminf p(L)/L)`, the four known results cover:
**T1** Monks–Yazinski 2004 Thm 2.7(b) [refereed] — density `< β`; **T2** López–Stoll 2021 Thm 1
[preprint] — density `> β`; **T3** Dubickas transported (foundation Cor. 9.3) — complexity
`< 1.70951129…`; **T4** foundation Thm 10.1 — the complexity-`(n+1)` line. Their union leaves
exactly one region:

> **density exactly `β = log₃2`, complexity at or above `1.70951…`.**

Every rung of this repository except the foundation paper's own `γ = β` theorem sits at density
`1/2` or another value `≠ β`, hence inside T1. Full ledger: `DENSITY_COMPLEXITY_LADDER.md`,
`PRIOR_RESULT_SUBSUMPTION.md`.

## 2. The target

> **`C(α, ρ)`**: `β := log₃2`; `α` a **quadratic irrational**; `ρ ∉ ℤα + ℤ`;
> ```
> s_n = 1   <=>   { n*alpha + rho }  in  [0, beta) .
> ```

| requirement | status |
|---|---|
| aperiodic | **PROVED** (a proper arc is not invariant under a non-trivial rotation) |
| lower ones-density **exactly `β`** | **PROVED** (Weyl; the limit exists and equals `β`) |
| complexity outside T3 | `p(n) = 2n` — **cited** (Rote 1994; Berstel–Vuillon 2001) and **verified exactly** at `n = 6, 12, 20` on 15 `(α,ρ)` pairs |
| not covered by T4 | `p(20) = 40 ≠ 21` |
| not covered by T1, T2 | density is `= β`, neither `<` nor `>` |
| discrepancy controlled | **PROVED already in this repository** (`theorems/phase2/ROTATION_EXAMPLE_THEOREM.md`: `O(log N)` for **any** fixed interval and **any** bounded-partial-quotient rotation) |

It is the repository's **own** class with one parameter moved: `CS Rote = ` coding against an
interval of length `1/2`; the target is the same coding at length `β`. Same complexity, minimal
change, and it crosses from covered to uncovered because the density is the only thing T1/T2 read.

## 3. The exact bridge requirement, and why criticality changes its shape

Because `β·log₂3 = 1`, the usual leading term `ℓ·[r − max(1, γlog₂3)]` degenerates to `ℓ(r−1)` and
the requirement collapses onto the **overshoot**:

```
S  >=  (L - ell)  -  ( ceil(D(W)) + max(0, e_ell) ) * log2 3  -  log2 ell ,
       e_ell := k_ell - ell*beta   (the FINITE-root density deviation)
```

Limiting density contributes nothing; `e_ℓ` enters linearly and un-damped. Both corrections are
`O_α(log ℓ)` here — measured `max|e_ℓ| = 1.136`, `max D(W) = 3.51` over `ℓ ≤ 3927`, and the
`O(log N)` bound is already proved in the repository.

## 4. The proof obligation

> **(L2)** For `s = s(α,ρ)` there are infinitely many `ℓ` with `lcp(s, (s[0:ℓ])^∞) − ℓ ≫ log ℓ`.

**(L2) ⟹ `Φ(s) ∉ ℚ`**, with no transfer, no weight parity and no Ostrowski machinery — the
criterion applies to `s` directly. Geometrically (L2) asks that the first entry time of
`({mα+ρ})` into a union of two arcs of length `‖q_kα‖` exceed `log q_k` infinitely often; generic
behaviour is `≈ q_{k+1}/2`, polynomially larger.

**Adversarially tested before attempting a proof.** Over 5 slopes × 3 intercepts, `ℓ` at convergent
denominators up to 3927: with `ρ ∉ ℤα+ℤ` the ratio `(L−ℓ)/log₂ℓ` reached `5 267` (min over scales
`0.46`–`11.7`, and `> 1` at 15/17, 9/9, 7/7, 5/5, 11/12, 17/17 of scales). Exact integer surplus
positive at 45/62 tested triples; **every** failure is a `ρ = 0` row with `L − ℓ = 0`, which is why
`ρ ∉ ℤα+ℤ` is part of the definition. The derived inequality of §3 was asserted on every row.

## 5. Evidence classification

| status | items |
|---|---|
| **PROVED** | aperiodicity and density `= β` of `C(α,ρ)`; the exact requirement of §3; `(L2) ⟹ Φ(s) ∉ ℚ`; `β` transcendental; the ladder's coverage geometry |
| **PROVED ELSEWHERE, CITED** | T1 (refereed), T2 (preprint), T3, T4; `p(n) = 2n` for mismatched two-interval codings (Rote 1994) |
| **PROVED EARLIER IN THIS REPOSITORY** | `O(log N)` interval discrepancy for bounded-type rotations, any fixed interval |
| **CERTIFIED FINITE CHECK** | `p(n) = 2n` at `n ≤ 20`; `e_ℓ`, `D(W)` magnitudes; 62 exact-integer surplus evaluations; the §3 inequality on every row |
| **NUMERICAL EVIDENCE ONLY** | (L2) itself |
| **OPEN** | (L2) |

## 6. Next action

Prove **(L2)**. It is a pure inhomogeneous-Diophantine statement about `α`, `ρ` and `β` jointly —
three-distance combinatorics, no arithmetic input — and it is the single step between the existing
machinery and a theorem in the one region no published result reaches. Two concrete sub-steps, in
order:

1. **Fix `ρ` and let `k` vary.** Show the first entry time into `(−θ_k,0) ∪ (β−θ_k,β)` cannot be
   `O(log q_k)` for *every* `k` unless `ρ` is simultaneously extremely well approximated by the
   orbits of `0` and of `β` — a measure-zero, explicitly describable condition. Then exclude it for
   an explicit `ρ` (e.g. `ρ = 1/7`), which already gives a single named word.
2. **Only then** aim for all `ρ ∉ ℤα+ℤ`.

Do **not** return to `(L1)` or the odd-branch discrepancy estimate: both serve density-`1/2`
classes that T1 already covers.

## 7. Standing gate

Before claiming novelty for any future class, compute its lower ones-density and compare with `β`.
If it is not exactly `β`, the conclusion is already available — whatever the complexity.
