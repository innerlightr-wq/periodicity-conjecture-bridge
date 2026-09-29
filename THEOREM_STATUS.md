# THEOREM_STATUS.md — consolidated status map

One line per load-bearing result, phase of origin, and status. Full statements and proofs are in `theorems/phaseN/`.

## Foundational (source paper, cited not re-derived)

| Result | Status | File |
|---|---|---|
| `Φ` is a 2-adic isometry (`v₂(Φ(a)−Φ(b))=lcp(a,b)`) | KNOWN (source paper, Prop. 2.2) | `reference/` |
| Periodic-value formula `Φ(W^∞)=c_W/(2^ℓ−3^k)` | KNOWN (source paper, Prop. 4.1) | `reference/` |
| Sturmian words have arbitrarily long initial squares | KNOWN (source paper, Thm 10.2, cites ADQZ 2001) | `reference/` |
| Sturmian, `p(n)=n+1` ⟹ `Φ∉ℚ` | KNOWN (source paper, Thm 10.1) | `reference/` |
| `p(n)<1.70951...n`, not eventually periodic ⟹ `Φ∉ℚ` | KNOWN (source paper, Cor. 9.3, Dubickas 2009 transported) | `reference/` |

## Phase 1 — abstraction and first non-Sturmian evidence

| Result | Status | File |
|---|---|---|
| Abstract periodic-approximation criterion (surplus `→+∞` ⟹ `Φ∉ℚ`), Sturmian-free | PROVED | `theorems/phase1/ABSTRACT_BRIDGE_THEOREM.md` |
| `c_W ≤ ℓ·3^⌈D⌉·max(2^ℓ,3^k)`, discrepancy-height bound | PROVED, exhaustively verified `ℓ≤16` | `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md` |
| Squares (`r=2`) suffice unconditionally, no discrepancy hypothesis | PROVED | `theorems/phase1/REPETITION_HEIGHT_CRITERION.md` |
| CS Rote sequences (3 tested slopes) certify | COMPUTATIONAL EVIDENCE | `theorems/phase1/ROTE_COMPUTATIONAL_AUDIT.md` |
| One non-Sturmian two-interval rotation coding certifies | COMPUTATIONAL EVIDENCE | `theorems/phase1/ROTATION_CODING_AUDIT.md` |

## Phase 2 — theorem conversion

| Result | Status | File |
|---|---|---|
| Abstract criterion, every subtlety (reducedness, cancellation, ceilings) resolved | PROVED | `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` |
| Rote–Sturmian transfer: depth preserved exactly, `L+1` | PROVED (was 3-example check in Phase 1) | `theorems/phase2/ROTE_TRANSFER_THEOREM.md` |
| Rote root discrepancy `D(V_n)=O(log ℓ_n)`, bounded-partial-quotient slopes | PROVED (reduction to classical 3-distance/Koksma bound) | `theorems/phase2/ROTE_ROOT_DISCREPANCY.md` |
| Weight-parity eventual periodicity (mechanism) | PROVED | `theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md` |
| `Φ(v)∉ℚ` for CS Rote sequences, 5 explicit quadratic-irrational slopes | **PROVED** | `theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md` |
| Non-Sturmian rotation coding: discrepancy proved generally; repetition-existence still open | PARTIALLY PROVED | `theorems/phase2/ROTATION_EXAMPLE_THEOREM.md` |

## Phase 3 — closing the weight-parity gap

| Result | Status | File |
|---|---|---|
| Finite 8-node automaton: exactly one bad (all-odd-weight) cycle exists, `(A,0)↔(C,1)` | PROVED (exhaustive search) | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| Counterexample found: `γ=[0;1,1,1,\overline2]` has all-odd weight-parity forever | PROVED (explicit, verified) | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| Odd-tail CF ⟹ bad cycle cannot sustain ⟹ infinitely many even-weight witnesses | PROVED | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| All-even-tail CF ⟹ odd-weight witnesses still certify (`r_u→≥2+√2>2log₂3`) | STRONGLY EVIDENCED (4 tails tested), **not proved for a fully general all-even tail** | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| Net: every tested quadratic irrational (9 slopes total, Phase 2+3) certifies; no genuine failure found | EMPIRICAL, consistent with a full theorem | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |

## Headline result of the repository

> For every complementary symmetric Rote sequence `v` whose associated Sturmian sequence has a quadratic-irrational slope with an **odd** partial quotient somewhere in its continued-fraction tail, `Φ(v)∉ℚ` — **proved**. For all-even-tail slopes, the same conclusion holds on every case tested, resting on one classical bound (silver-ratio-type critical exponent `≥2+√2`) not re-derived in full generality here.

## Open, precisely stated

1. Prove `r_u\to\ge2+\sqrt2` (or find a counterexample) for a **general** all-even-partial-quotient continued fraction tail, closing Target C (all quadratic irrationals) completely.
2. Extend beyond quadratic irrationals to general bounded-partial-quotient slopes (Target B).
3. The rotation-coding repetition-existence gap (`theorems/phase2/ROTATION_EXAMPLE_THEOREM.md`) — no analogue of Theorem 10.2 for mismatched two-interval codings is proved or cited anywhere.
4. The "next frontier" beyond `p(n)=2n` (`LADDER.md`) — deliberately not started.
