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

## Phase 4 — closes the quadratic CS Rote rung, corrects a wrong working hypothesis

| Result | Status | File |
|---|---|---|
| Phase 3's "all-even tail" classification was incomplete — mixed-parity tails can also lock bad, given the right preperiod | CORRECTED (verified against the automaton directly) | `theorems/phase4/EVEN_TAIL_PROBLEM.md` |
| Silver-ratio extremality (`ice≥2+√2` for lock-sustaining tails) | **FALSE — COUNTEREXAMPLE found** (`\overline{6,2}` with preperiod `(1,4,1,5,1)`, `ice≈3.1547<2+√2`) | `theorems/phase4/SILVER_EXTREMALITY.md` |
| `2+√2` classified: numerical artifact / irrelevant after sharper analysis | AUDITED | `theorems/phase4/SILVER_CONSTANT_AUDIT.md` |
| **Real required threshold is `r_u>2`, not `r_u>2log₂3≈3.17`** — because the odd-weight route's doubled root `R=V\bar V` has density **exactly `1/2`**, always, unconditionally | PROVED (two-line structural fact) | `theorems/phase4/REQUIRED_EXPONENT.md` |
| `ice(u)>2+1/(A+1)` uniformly, any bounded-partial-quotient slope (max partial quotient `A`), via Berthé–Holton–Zamboni's exact formula | PROVED (cited formula + elementary bound, exactly verified) | `theorems/phase4/INITIAL_EXPONENT_FORMULA.md` |
| **`Φ(v)∉ℚ` for every complementary symmetric Rote sequence associated with every quadratic-irrational slope** (intercept-0 representative, both seeds, every shift) | **PROVED — precise subclass** (other intercepts of the same slope not covered) | `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` |
| Exhaustive stress test, 11 configurations (all-even + mixed lock-sustaining tails) | PASS, 11/11, exact surplus positive in every case | `theorems/phase4/COMPUTATIONAL_STRESS_TEST.md` |

## Headline result of the repository

> For **every** complementary symmetric Rote sequence `v` whose associated Sturmian sequence is the intercept-`0` mechanical word of **any** quadratic-irrational slope, `Φ(v)∉ℚ` — **proved** (Phase 4, `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md`). This supersedes Phase 2's five-slope result and Phase 3's odd-tail-only result.

## Open, precisely stated

1. CS Rote sequences at **other intercepts** of the same quadratic-irrational slope (not a shift of the intercept-0 representative) — `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md`'s own stated gap.
2. Extend beyond quadratic irrationals to general bounded-partial-quotient slopes (Target B, `theorems/phase2/THEOREM_TARGET.md`).
3. The rotation-coding repetition-existence gap (`theorems/phase2/ROTATION_EXAMPLE_THEOREM.md`) — no analogue of Theorem 10.2 for mismatched two-interval codings is proved or cited anywhere.
4. The "next frontier" beyond `p(n)=2n` (`LADDER.md`) — deliberately not started.
