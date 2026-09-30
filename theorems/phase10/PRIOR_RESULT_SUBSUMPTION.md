**SUBSUMPTION LEDGER — WHAT IS COVERED, WHAT IS AN INDEPENDENT PROOF, WHAT IS A REFINEMENT, WHAT IS NEW**

# PRIOR_RESULT_SUBSUMPTION.md

Companion to `DENSITY_COMPLEXITY_LADDER.md`. Nothing here withdraws a proof or deletes a record.

## 1. The ledger

**(A)** already-covered conclusion · **(B)** independent proof of a covered conclusion ·
**(C)** quantitative refinement of the mechanism · **(D)** genuinely uncovered extension

| result | class, `(density, complexity)` | cat. | covering result |
|---|---|---|---|
| `theorems/phase1/ABSTRACT_BRIDGE_THEOREM.md`, `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` | the criterion itself | **C** | — |
| `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`, `REPETITION_HEIGHT_CRITERION.md` | height/repetition bounds | **C** | — |
| `theorems/phase2/ROTE_TRANSFER_THEOREM.md` (`L_v = L_u + 1`) | transfer identity | **C** | — |
| `theorems/phase4/REQUIRED_EXPONENT.md` (odd-branch density `1/2`) | structural fact | **C** | — |
| `theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md` | CS Rote, 5 quadratic slopes, `(1/2, 2)` | **B** | T1 |
| `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` | CS Rote, quadratic slopes, `(1/2, 2)` | **B** | T1 |
| `theorems/phase6/BOUNDED_TYPE_THEOREM.md` | CS Rote, bounded type, `(1/2, 2)` | **B** | T1 |
| Phase 8 Theorem 2 | CS Rote, every intercept, `(1/2, 2)` | **B** | T1 |
| Phase 9 Theorem 3 | CS Rote, unbounded type, `(1/2, 2)` | **B** | T1 |
| Phase 9 Corollary 4.1 (Thue–Morse) | `(1/2, 10/3)` | **B** | T1 |
| Phase 9 Corollary 4.2 (21 substitutions) | rational densities | **B** | T1 (15), T2 (4) |
| Phase 9 Theorem 4 (`g(γ)` threshold) | unconditional criterion | **C** | — |
| `theorems/phase1/ROTATION_CODING_AUDIT.md`, `theorems/phase2/ROTATION_EXAMPLE_THEOREM.md` | rotation coding, interval `1/3`, `(1/3, 2)` | **B** for the class; **C** for its proved `O(log N)` discrepancy | T1 |
| Phase 8 driver identity, attainment routing; Phase 9 weight law (W-y)/(W-x) | exact structure | **C** | — |
| Phase 8 BHZ §5 priority; `q_1` convention; exceptional-orbit refutation; Thue–Morse ceiling refutation | corrections to the record | **C** | — |
| **Phase 10 target `C(α,ρ)`** | **`(β, 2)`** | **D** | **none** |

## 2. Corrections to the novelty framing

These replace framing, not mathematics. Every proof and every computational record stands.

### 2.1 CS Rote (Phases 2, 4, 6, 8, 9)

**Withdraw:** that the bounded-type / general-intercept / unbounded-type CS Rote theorems establish
irrationality for a class not previously reached.

**Replace with:** every complementary symmetric Rote sequence has ones-density **exactly `1/2`**
(`v_n = v_0 ⊕ (k_n(u) mod 2)`; Weyl on `γ/2`), and `1/2 < β`, so `Φ(v) ∉ ℚ` follows from
**Monks–Yazinski (2004) Thm 2.7(b)** for *every* CS Rote sequence — every slope, every intercept,
no bounded-type hypothesis. What Phases 2–9 supply is an **independent second proof by a different
(2-adic depth-versus-height) mechanism**, which uses no density input at all, together with the
exact structural results about that mechanism listed as **(C)** above.

The programme's framing compared only against the **counting** route (T3), which indeed fails at
complexity `2n`. The **density** route does not read complexity.

### 2.2 Thue–Morse (Phase 9 Cor. 4.1)

**Withdraw:** novelty, and the attribution to the `g(γ)` threshold.

**Replace with:** Thue–Morse is aperiodic with ones-density `1/2 < β`, so `Φ(TM) ∉ ℚ` is an
instance of Monks–Yazinski (2004) Thm 2.7(b) — a deduction written out verbatim in this
programme's own foundation paper, §8. Independently, the Phase 9B reconstruction shows the proof
needs only Phase 1's **exact** inequality at threshold `max(1, (log₂3)/2) = 1` against a prefix power
of `5/3` with bounded discrepancy `D = 1/2`; `g(γ) = 1.396` is not required. Both the proof and the
Thue–Morse **scope correction** (absence of initial *squares* does not block a repetition-based
method) stand and remain worth recording.

### 2.3 The `p(n) = 2n` "frontier"

**Withdraw:** that `p(n) = 2n` is a frontier.

**Replace with:** the frontier is the **density** `β`, not a complexity value. T1/T2 cover every
complexity at every density except `β`; T3 covers every density below complexity `1.70951…`; T4
covers the complexity-`(n+1)` line. Complexity matters only insofar as a target must stay above
T3's line and off T4's line — which `2n` does, and which is why the Phase 10 target keeps it.

## 3. What is preserved

- All proofs, all scripts, all `data/` records across Phases 1–9B — unchanged and still valid.
- All **(C)** results: the criterion, the height and repetition bounds, the transfer identity, the
  density-`1/2` structural fact, the `g(γ)` refinement, the BHZ driver identity and attainment
  routing, the weight law, and the four corrections to the record made in Phases 8, 9 and 9B.
- The foundation paper's own theorem at `γ = β`, which is **(D)** and was correctly claimed as such
  by the paper itself.

## 4. The standing gate, carried forward

Before claiming novelty for any class: compute its **lower ones-density** and compare with
`β = 0.6309297535714574`. If the density is not exactly `β`, the conclusion is already available
(T1 below, T2 above) whatever the complexity. This gate is what the repository's three prior-art
passes lacked — they searched for the *mechanism* and never asked whether the *conclusion* was
already covered.
